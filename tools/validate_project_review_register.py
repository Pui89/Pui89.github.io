#!/usr/bin/env python3
"""Validate the evidence-backed PUI89 project review register using Python stdlib only."""
import datetime as dt
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
REGISTER=ROOT/"assets"/"data"/"project-review-register.json"
EXPECTED={"coconut","flood-rescue","sentinel","ai-home","ai-nomad","ai-robot-car","ai-robot-motorcycle"}
def fail(message):
    print("ERROR: "+message,file=sys.stderr)
    raise SystemExit(1)
try:
    data=json.loads(REGISTER.read_text(encoding="utf-8"))
except (OSError,json.JSONDecodeError) as exc:
    fail("cannot read valid JSON register: "+str(exc))
if data.get("schema_version")!=1: fail("schema_version must be 1")
projects=data.get("projects")
if not isinstance(projects,list): fail("projects must be a list")
ids=[p.get("id") for p in projects if isinstance(p,dict)]
if set(ids)!=EXPECTED or len(ids)!=len(EXPECTED): fail("project IDs must match the seven PUI89 projects exactly, with no duplicates")
total=0
for p in projects:
    records=p.get("review_records")
    if not isinstance(records,list): fail(p["id"]+": review_records must be a list")
    seen=set()
    for r in records:
        if not isinstance(r,dict): fail(p["id"]+": each review record must be an object")
        required=("review_id","reviewed_on","scope","reviewer_role","outcome","status","evidence")
        if any(not r.get(k) for k in required): fail(p["id"]+": every record needs "+", ".join(required))
        if r["review_id"] in seen: fail(p["id"]+": duplicate review_id "+r["review_id"])
        seen.add(r["review_id"])
        try: dt.date.fromisoformat(r["reviewed_on"])
        except (TypeError,ValueError): fail(p["id"]+"/"+r["review_id"]+": reviewed_on must be YYYY-MM-DD")
        if r["status"] not in ("draft","completed"): fail(p["id"]+"/"+r["review_id"]+": status must be draft or completed")
        if not isinstance(r["evidence"],list) or any(not isinstance(x,str) or not x.strip() for x in r["evidence"]): fail(p["id"]+"/"+r["review_id"]+": evidence must be a list of non-empty references")
        if r["status"]=="completed":
            if not r["evidence"]: fail(p["id"]+"/"+r["review_id"]+": completed reviews require evidence")
            total+=1
print("Validated "+str(len(projects))+" projects; "+str(total)+" completed evidence-backed reviews.")
