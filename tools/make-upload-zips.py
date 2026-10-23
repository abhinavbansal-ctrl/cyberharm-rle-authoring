#!/usr/bin/env python3
"""Build one clean upload zip per family (rles/ + jobs/ only) and verify nothing forbidden is inside.

Usage:
    python3 make-upload-zips.py <submission-dir> [<submission-dir> ...]
Each <submission-dir> (e.g. .../submission-notifyd) must contain rles/ and jobs/. The zip is written
beside it as <basename>-final.zip, containing only <basename>/rles/** and <basename>/jobs/**, with
caches/stage/secrets excluded. Ship ONE zip per family; never merge families.
"""
import os, sys, zipfile

FORBIDDEN = (".env", "/.stage/", "target_shim", "api keys", "bb_checker", "bb_sync",
             "/.venv/", "runbook")  # substrings that must NOT appear in any shipped path (lowercased)

def skip(path):
    low = path.lower()
    return ("/__pycache__/" in path or path.endswith((".pyc", ".DS_Store")))

def build(sub):
    sub = os.path.abspath(sub.rstrip("/"))
    base = os.path.basename(sub)
    out = os.path.join(os.path.dirname(sub), base + "-final.zip")
    n = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for part in ("rles", "jobs"):
            root = os.path.join(sub, part)
            if not os.path.isdir(root):
                print(f"  !! {base}: missing {part}/"); continue
            for dp, dirs, files in os.walk(root):
                dirs[:] = [d for d in dirs if d != "__pycache__"]
                for f in files:
                    fp = os.path.join(dp, f)
                    if skip(fp):
                        continue
                    z.write(fp, os.path.join(base, os.path.relpath(fp, sub)))
                    n += 1
    # verify
    bad = [nm for nm in zipfile.ZipFile(out).namelist()
           if any(b in nm.lower() for b in FORBIDDEN)]
    tops = sorted({"/".join(nm.split("/")[:2]) for nm in zipfile.ZipFile(out).namelist()})
    print(f"{out}: {n} files, {os.path.getsize(out)//1024} KB; top={tops}")
    if bad:
        print("  !! FORBIDDEN content:", *bad[:10], sep="\n     ")
    else:
        print("  clean (no forbidden paths)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for s in sys.argv[1:]:
        build(s)
