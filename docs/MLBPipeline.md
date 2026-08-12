# MLB Pipeline (LXC 106 / 107)

## Overview
Production MLB intelligence pipeline split across two LXCs. Application code and operational detail live in the `mlb-pipeline` repo; this page is the Proxmox inventory pointer.

| ID | Hostname | Role | Resources |
| :--- | :--- | :--- | :--- |
| **106** | mlb-db | PostgreSQL | 1 core, 1024 MB, 16G |
| **107** | mlb-app | App / dashboard / systemd services | 4 cores, 4096 MB, 20G |

## Network
| Host | LAN | Tailscale |
| :--- | :--- | :--- |
| mlb-db | `<IP_ADDRESS>` | `<IP_ADDRESS>` |
| mlb-app | `<IP_ADDRESS>` | `<IP_ADDRESS>` |

## Ops pointer
- Repo helper: `mlb-pipeline/homelab.py` and `docs/homelab_access.md`
- Prefer direct SSH to the LXCs for service debugging (not `pct exec` from day-to-day workflows)

---
*Last updated: 2026-08-12*
