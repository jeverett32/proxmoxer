#!/bin/bash
cd /opt/proxmox-backups
python3 backup_proxmox.py
git add .
git commit -m "Auto-backup: $(date)"
git push -u origin main
