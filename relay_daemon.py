#!/usr/bin/env python3
"""
DFS Dead Drop Relay Daemon - v1.1
Works on LawMacBook (macOS) and ThinkPad (Linux) - no API key needed
Watches 99_DEAD_DROP_RELAY/01_DROP/ for new files
Usage:
  python3 relay_daemon.py --once          # single scan
  python3 relay_daemon.py --watch         # continuous (polling every 30s)
  python3 relay_daemon.py --cron-install  # installs cron/launchd entry for git pull
"""
import os, sys, time, pathlib, hashlib, json
from datetime import datetime

RELAY_ROOT = pathlib.Path(__file__).parent / "99_DEAD_DROP_RELAY"
DROP = RELAY_ROOT / "01_DROP"
TRIBUNAL = RELAY_ROOT / "02_TRIBUNAL"
SEALED = RELAY_ROOT / "03_SEALED"
STATE_FILE = RELAY_ROOT / ".relay_state.json"

def sha_file(p):
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()[:12]

def scan_once():
    if not DROP.exists():
        print(f"[RELAY] No DROP folder at {DROP}")
        return
    files = [f for f in DROP.iterdir() if f.is_file() and not f.name.startswith(".") and f.name != ".gitkeep"]
    if not files:
        print(f"[RELAY] {datetime.now().isoformat()} - No new drops. CLEAN.")
        return
    state = {}
    if STATE_FILE.exists():
        try:
            state = json.loads(STATE_FILE.read_text())
        except:
            state = {}
    for f in files:
        fid = sha_file(f)
        if fid in state:
            continue
        print(f"[RELAY] NEW INPRESS DETECTED: {f.name} | sha:{fid} | {f.stat().st_size} bytes")
        print(f"  -> Action: git add this, push, then paste contents to Meta AI for TRIBUNAL conversion")
        state[fid] = {"file": f.name, "seen": datetime.now().isoformat(), "size": f.stat().st_size}
    STATE_FILE.write_text(json.dumps(state, indent=2))
    print(f"[RELAY] Tribunal pending: {len(files)} file(s) in 01_DROP/")

def watch_loop():
    print("[RELAY] Watching 01_DROP/ every 30s - Ctrl+C to stop")
    try:
        while True:
            scan_once()
            time.sleep(30)
    except KeyboardInterrupt:
        print("\n[RELAY] Stopped.")

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "--once"
    if arg == "--once":
        scan_once()
    elif arg == "--watch":
        watch_loop()
    elif arg == "--cron-install":
        print("# Add to crontab (crontab -e) on ThinkPad/Linux:")
        print("0 * * * * cd /path/to/DFS_FLOW_ORO && git pull origin main && python3 relay_daemon.py --once >> 99_DEAD_DROP_RELAY/relay.log 2>&1")
        print("# On Mac (LawMacBook) - launchd, or just run --watch in a tmux")
    else:
        scan_once()