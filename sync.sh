#!/bin/bash
set -euo pipefail
cd /opt/proxmox-backups
python3 backup_proxmox.py
git add -A
if git diff --cached --quiet; then
  echo "No changes to commit"
  exit 0
fi
git commit -m "Auto-backup: $(date)"
# Push may fail if GitHub key missing — log but don't hide backup success
git push origin main || echo "WARNING: git push failed — local backup commit kept" >&2
