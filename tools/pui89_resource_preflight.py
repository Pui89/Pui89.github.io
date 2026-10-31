#!/usr/bin/env python3
"""Read-only, standard-library PUI89 resource preflight. Never installs or downloads."""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import platform
import shutil
import sys
from pathlib import Path
from typing import Any

OPTIONAL_PACKAGES = (
    "numpy", "PIL", "cv2", "torch", "torchvision", "ultralytics",
    "onnxruntime", "open3d", "transformers", "smolagents",
)


def available_memory_bytes() -> int | None:
    """Return available physical memory without adding a platform dependency."""
    if os.name == "nt":
        try:
            import ctypes

            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
                ]

            status = MEMORYSTATUSEX()
            status.dwLength = ctypes.sizeof(status)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
                return int(status.ullAvailPhys)
        except (AttributeError, OSError, TypeError):
            return None
    try:
        pages = os.sysconf("SC_AVPHYS_PAGES")
        page_size = os.sysconf("SC_PAGE_SIZE")
        return int(pages * page_size)
    except (AttributeError, OSError, ValueError):
        return None


def classify_resources(memory_gib: float | None, disk_gib: float | None) -> dict[str, str]:
    """Conservative guidance, not a hardware compatibility guarantee."""
    if memory_gib is None:
        memory = "UNKNOWN"
    elif memory_gib < 4:
        memory = "LOW"
    elif memory_gib < 8:
        memory = "LIMITED"
    else:
        memory = "LOCAL_LIGHTWEIGHT_WORKLOADS"
    if disk_gib is None:
        disk = "UNKNOWN"
    elif disk_gib < 5:
        disk = "LOW"
    elif disk_gib < 15:
        disk = "LIMITED"
    else:
        disk = "BASIC_HEADROOM"
    return {"memory_guidance": memory, "disk_guidance": disk}


def collect_report(root: Path | str = ".") -> dict[str, Any]:
    root = Path(root).resolve()
    memory = available_memory_bytes()
    try:
        free_disk = shutil.disk_usage(root).free
    except OSError:
        free_disk = None
    memory_gib = round(memory / (1024 ** 3), 2) if memory is not None else None
    disk_gib = round(free_disk / (1024 ** 3), 2) if free_disk is not None else None
    packages: dict[str, bool] = {}
    for package in OPTIONAL_PACKAGES:
        try:
            packages[package] = importlib.util.find_spec(package) is not None
        except (ImportError, ValueError, ModuleNotFoundError):
            packages[package] = False
    report: dict[str, Any] = {
        "report_type": "pui89_read_only_resource_preflight",
        "python": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "processor": platform.processor() or "UNKNOWN",
        "cpu_logical_count": os.cpu_count(),
        "available_memory_gib": memory_gib,
        "free_disk_gib": disk_gib,
        "optional_packages_installed": packages,
        "guidance": classify_resources(memory_gib, disk_gib),
        "network_access_used": False,
        "packages_installed": False,
        "models_downloaded": False,
        "paid_services_used": False,
        "hardware_actuation_permitted": False,
        "limitations": [
            "Available memory and disk are point-in-time observations.",
            "GPU/VRAM, driver compatibility, model licence and model suitability are not assessed.",
            "Package presence does not prove that a package or model works correctly.",
            "This report does not install, download, benchmark or launch any model.",
        ],
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Directory whose free disk space is checked")
    parser.add_argument("--output", help="Optional JSON output path")
    args = parser.parse_args()
    report = collect_report(args.root)
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
