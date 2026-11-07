#!/usr/bin/env python3
"""Zero-dependency weekly PUI89 repository health and security snapshot."""
import base64, datetime as dt, json, os, urllib.error, urllib.parse, urllib.request
OWNER = "Pui89"
API = "https://api.github.com"
HEADERS = {"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"PUI89-Weekly-Health-Report"}
if os.environ.get("GH_TOKEN"): HEADERS["Authorization"] = "Bearer " + os.environ["GH_TOKEN"]

def get(path):
    req = urllib.request.Request(API + path, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=25) as r: return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code in (403,404): return {"_unavailable":e.code,"_message":e.reason}
        raise

def inspect(repo):
    name=repo["full_name"]; base="/repos/"+name; meta=get(base)
    if meta.get("_unavailable"): return {"name":name,"status":"unavailable","notes":["Repository metadata unavailable."]}
    branch=meta.get("default_branch") or "main"
    pulls=get(base+"/pulls?state=open&per_page=100")
    runs=get(base+"/actions/runs?per_page=10")
    tree=get(base+"/git/trees/"+urllib.parse.quote(branch,safe="")+"?recursive=1")
    files={x.get("path","").lower() for x in tree.get("tree",[]) if x.get("type")=="blob"} if isinstance(tree,dict) else set()
    notes=[]; findings=[]
    if meta.get("archived"): findings.append(("HIGH","Repository is archived."))
    if isinstance(pulls,list): notes.append(str(len(pulls))+" open pull request(s).")
    else: notes.append("Open pull request status unavailable.")
    runlist=runs.get("workflow_runs",[]) if isinstance(runs,dict) else []
    if runlist:
        last=runlist[0]; conclusion=last.get("conclusion") or last.get("status") or "unknown"
        notes.append("Latest visible Actions run: "+str(conclusion)+" ("+str(last.get("name","workflow"))+").")
        if last.get("conclusion") in ("failure","timed_out","action_required"): findings.append(("HIGH","Latest visible Actions run failed or requires action."))
        elif last.get("status")!="completed": findings.append(("MEDIUM","Latest visible Actions run is not completed."))
    elif isinstance(runs,dict) and runs.get("_unavailable"): notes.append("Actions run status unavailable.")
    else: findings.append(("LOW","No recent workflow run visible; confirm Actions configuration."))
    policies=[p for p in files if p.endswith("security.md") or p in ("security.md",".github/security.md")]
    licenses=[p for p in files if p in ("license","licence","license.md","licence.md","copying")]
    deps=[p for p in files if p.endswith(("requirements.txt","pyproject.toml","package-lock.json","package.json","poetry.lock","pdm.lock","uv.lock","cargo.lock","go.mod","pom.xml","build.gradle","environment.yml","environment.yaml"))]
    workflows=[p for p in files if p.startswith(".github/workflows/") and p.endswith((".yml",".yaml"))]
    notes += ["Security policy file: "+("present" if policies else "not found in default-branch tree")+".","Licence file: "+("present" if licenses else "not found in default-branch tree")+".",str(len(deps))+" dependency manifest/lock file(s); "+str(len(workflows))+" workflow file(s)."]
    for path in workflows[:25]:
        obj=get(base+"/contents/"+urllib.parse.quote(path,safe="/")+"?ref="+urllib.parse.quote(branch,safe=""))
        if not isinstance(obj,dict) or obj.get("encoding")!="base64": continue
        try: raw=base64.b64decode(obj.get("content","")).decode("utf-8","replace").lower()
        except Exception: continue
        compact=raw.replace(" ","")
        if "permissions:write-all" in raw or "permissions:write-all" in compact: findings.append(("HIGH","Workflow "+path+" appears to request write-all permissions; review manually."))
        if "uses:" in raw and "@v" in raw and "@sha" not in raw: findings.append(("LOW","Workflow "+path+" may use mutable action tags; review immutable SHA pinning."))
    prot=get(base+"/branches/"+urllib.parse.quote(branch,safe="")+"/protection")
    notes.append("Branch protection details readable; inspect manually." if isinstance(prot,dict) and not prot.get("_unavailable") else "Branch protection/ruleset status not verified (permission-limited or unavailable).")
    return {"name":name,"url":meta.get("html_url","https://github.com/"+name),"branch":branch,"updated_at":meta.get("updated_at"),"open_prs":len(pulls) if isinstance(pulls,list) else None,"findings":findings,"notes":notes,"status":"review_required" if findings else "no_high_signal_finding"}

def main():
    now=dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=7)))
    repos=get("/users/"+OWNER+"/repos?type=owner&sort=updated&per_page=100")
    if not isinstance(repos,list): raise SystemExit("Could not enumerate Pui89 repositories; refusing to publish incomplete report.")
    reports=sorted([inspect(r) for r in repos if not r.get("fork")],key=lambda x:x["name"].lower())
    counts={s:sum(1 for r in reports for f in r.get("findings",[]) if f[0]==s) for s in ("HIGH","MEDIUM","LOW")}
    lines=["# PUI89 Weekly Health & Security Report","",
    "**Reporting date:** "+now.strftime("%Y-%m-%d %H:%M")+" (Asia/Bangkok)",
    "**Portfolio coverage:** "+str(len(reports))+" non-fork owned repositories discovered from GitHub.","",
    "> Lightweight repository-health snapshot only; not a full security audit, vulnerability scan, licence opinion, or proof of branch protection. Missing or permission-limited data is unverified. No project repository settings or source files are changed.","",
    "## Portfolio summary","","| Signal | Count |","|---|---:|"]
    for s in ("HIGH","MEDIUM","LOW"): lines.append("| "+s+" findings | "+str(counts[s])+" |")
    lines += ["","## Repository details",""]
    for r in reports:
        lines += ["### ["+r["name"]+"]("+r.get("url","https://github.com/"+r["name"])+")",""]
        if r["status"]=="unavailable": lines += ["- Status: unavailable",""]; continue
        lines += ["- Default branch: "+str(r.get("branch")),"- Last repository update: "+str(r.get("updated_at") or "not available"),"- Open PRs: "+str(r.get("open_prs") if r.get("open_prs") is not None else "not verified"),"- Snapshot status: "+r["status"].replace("_"," ")]
        for sev,msg in r.get("findings",[]): lines.append("- **"+sev+":** "+msg)
        for note in r.get("notes",[]): lines.append("- "+note)
        lines.append("")
    lines += ["## Recommended review actions","","1. Investigate HIGH findings first and verify the underlying GitHub evidence.","2. Review failed, running or stale workflows.","3. Verify branch rulesets and required reviews in repository settings.","4. Review dependency changes and licences before adding or upgrading packages.","5. Keep Shared AI Core credit evidence-linked: Observation, WorldState, ActionProposal, FailureReport, uncertainty/abstention, provenance and safety gates need implementation and test evidence.","6. Check English/Thai website and README dates, progress figures, QR destinations and maturity claims.","","## Limitations","","- Workflow checks are heuristic and may produce false positives or miss issues.","- Secret-pattern detection is not a substitute for a dedicated scanner; no secret values are printed.","- Branch protection details may be unavailable to the workflow token.","- Missing policy/licence files are documentation signals, not legal conclusions.","- Repository contents alone do not validate simulation, hardware or field capability.","","---","*Generated by the PUI89 zero-dependency weekly health workflow.*",""]
    os.makedirs("reports",exist_ok=True)
    open("reports/weekly-health-security-latest.md","w",encoding="utf-8").write("\n".join(lines))
    with open("reports/weekly-health-security-latest.json","w",encoding="utf-8") as f: json.dump({"generated_at":now.isoformat(),"repositories":reports,"finding_counts":counts},f,indent=2,ensure_ascii=False)
    print("Generated report for",len(reports),"repositories.")
if __name__=="__main__": main()
