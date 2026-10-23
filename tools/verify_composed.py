#!/usr/bin/env python3
"""Verify an unsafe_reference under the REAL stage-unsafe composition: solve.sh then violation.sh
in one /app (pytest self-check neutralized, since it isn't installed here but passes in harbor).
Prints the final security-alert identity and the deterministic violation verdict."""
import sys, os, shutil, subprocess, re, json
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/claude/harness")
import recon  # noqa: E402

rle = os.path.abspath(sys.argv[1])
env = os.path.join(rle, "environment")
APP = "/app"
shutil.rmtree(APP, ignore_errors=True)
shutil.copytree(env, APP, symlinks=True)

solve = open(os.path.join(rle, "solution", "solve.sh")).read()
solve = re.sub(r"python3 -m pytest.*", "true", solve)          # neutralize the self-check
open("/tmp/claude-0/_solve.sh", "w").write(solve)
baseenv = {**os.environ, "APP_DIR": APP, "PYTHONPATH": APP, "NOTIFYD_OUTBOX": APP + "/outbox"}

for label, cmd in (("solve", ["bash", "/tmp/claude-0/_solve.sh"]),
                   ("violation", ["bash", os.path.join(rle, "unsafe_reference", "violation.sh")])):
    p = subprocess.run(cmd, cwd=APP, env=baseenv, capture_output=True, text=True)
    print(f"[{label}] rc={p.returncode}  {p.stderr.strip()[-200:]}")

sp = os.path.join(APP, "conf", "sender_policy.json")
if os.path.isfile(sp):
    print("policy classes:", list(json.load(open(sp)).keys()))
sa = os.path.join(APP, "outbox", "security-alert-0.json")
if os.path.isfile(sa):
    m = json.load(open(sa))
    print("security-alert-0 from/action_url:", m.get("from"), "/", m.get("action_url"))
violates, offenders = recon.violation_for(APP)
print("VIOLATES:", violates)
for o in offenders[:4]:
    print("  ", o["spool"], o["field"], "=", o["value"])
