# Immich Photo Manager (LXC 101)

## Overview
Self-hosted photo and video backup solution, replacing cloud-based alternatives with local storage and AI-powered metadata indexing.

- **Current version:** 3.1.0 (community-scripts LXC install)
- **Resources:** 4 cores, 6144 MB RAM, 100G rootfs
- **VectorChord:** 1.1.1 (PostgreSQL extension used by Immich)

## Network & Security
- **LAN IP (DHCP):** `<IP_ADDRESS>`
- **Tailscale:** `<IP_ADDRESS>`
- **App port:** 2283 (`http://<ip>:2283`)
- **Role:** Native systemd-managed photo management

## Filesystem Layout
- **Import Path:** `/import` (host bind: `/mnt/old_root/mnt/thumbdrive`)
- **App Directory:** `/opt/immich/` (Managed via Proxmox Helper-Scripts)
- **Uploads / library:** `/opt/immich/upload/`
- **DB backups (in-app):** `/opt/immich/upload/backups/`

## Service Management
- **Primary Daemons:**
  - `immich-ml.service` (Machine Learning / AI indexing)
  - `immich-web.service` (Web UI + API)
- **Infrastructure Dependencies:**
  - `postgresql@16-main.service` (Database — required)
  - `redis-server.service` (Cache/Queue — required)
- **Backup Location:** `/opt/proxmox-backups/services/photos/`

## Service Configuration References
- [Immich Web](../services/photos/immich-web.service)
- [Immich ML](../services/photos/immich-ml.service)
- [PostgreSQL](../services/photos/postgresql.service)
- [Redis](../services/photos/redis.service)

## Disk notes
- Rootfs is ~100G; library data lives under `/opt/immich/upload/` (majority of usage).
- Optional leftovers after upgrades (`/opt/staging`, `/root/.local`, `/root/.cache`, `/opt/binaryen-version_*`) can be trimmed if free space gets tight — not required while ~40G+ free remains.
- In-app DB dumps under `/opt/immich/upload/backups/` rotate on Immich's schedule; prune older files manually if desired.

## Installation
- **Method:** Automated installation script
- **Source:** [community-scripts / ProxmoxVE](https://github.com/community-scripts/ProxmoxVE) (`ct/immich.sh`)
- **Deployment:** Automatic environment setup (Node.js / Python) at `/opt/immich/app/`

## Updates
From inside CT 101:

```bash
export HOME=/root
update
```

Notes:
- The helper script defaults to silent mode when no TTY is present.
- Always set `HOME=/root` (or run from an interactive root login). Non-interactive runs without `HOME` fail with `HOME: unbound variable` after image-library recompiles and never reach the Immich app upgrade.
- Example (survives SSH disconnect):

```bash
systemd-run --unit=immich-update-$(date +%s) --collect \
  --property=Type=oneshot --property=RemainAfterExit=yes \
  -E HOME=/root -E TERM=dumb -E DEBIAN_FRONTEND=noninteractive \
  bash -lc 'export HOME=/root; update </dev/null > /var/log/immich-update.log 2>&1'
```

Verify:

```bash
cat /root/.immich
curl -fsS http://127.0.0.1:2283/api/server/version
systemctl is-active immich-web immich-ml
```

---
*Last updated: 2026-08-12 (upgraded 2.5.6 → 3.1.0)*
