import json
import os
from pathlib import Path

ROOT = Path.cwd()
ANCHORS = ["run", "bench", "lab", "show", "pulse"]

def repo_stats(name: str):
    repo = ROOT / name
    files = []
    for p in repo.rglob("*"):
        if "/.git/" in p.as_posix() or p.name == ".git":
            continue
        if p.is_file():
            files.append(p)
    readme = (repo / "README.md").exists()
    latest = any(p.name == "latest.txt" for p in files)
    exec_count = 0
    for p in files:
        try:
            if os.access(p, os.X_OK):
                exec_count += 1
        except OSError:
            pass
    score = len(files) + exec_count * 3 + (2 if readme else 0) + (1 if latest else 0)
    return {
        "repo": name,
        "files": len(files),
        "executables": exec_count,
        "readme": readme,
        "latest": latest,
        "signal_score": score,
    }

def table(rows):
    headers = ["repo", "files", "executables", "readme", "latest", "signal_score"]
    widths = {h: max(len(h), *(len(str(r[h])) for r in rows)) for h in headers}
    line = " | ".join(h.ljust(widths[h]) for h in headers)
    sep = "-+-".join("-" * widths[h] for h in headers)
    body = [" | ".join(str(r[h]).ljust(widths[h]) for h in headers) for r in rows]
    return "\n".join([line, sep, *body])

rows = [repo_stats(name) for name in ANCHORS]
payload = {
    "root": str(ROOT),
    "anchors": rows,
}

print(table(rows))
print()
print(json.dumps(payload, indent=2))
