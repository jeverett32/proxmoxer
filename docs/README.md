# Home Lab Infrastructure Documentation

Welcome to the central documentation repository for the Proxmox home lab. This repository maintains the state, configuration, and recovery procedures for all running services and virtual machines.

## Infrastructure Overview

| ID | Name | Role | Status | Documentation |
| :--- | :--- | :--- | :--- | :--- |
| **100** | **Pi-hole** | Network-wide ad-blocking / DNS | running | [View](./Pihole.md) |
| **101** | **Immich** | Photo & video management (v3.1.0) | running | [View](./Immich.md) |
| **102** | **Docker / Portainer** | Container orchestration hub | running | [View](./DockerPortainer.md) |
| **103** | **Minecraft** | Gaming server (VM) | stopped | [View](./Minecraft.md) |
| **104** | **Jellyfin** | Media consumption | stopped | [View](./Jellyfin.md) |
| **105** | **Media Pipeline** | Acquisition & processing | stopped | [View](./MediaPipeline.md) |
| **106** | **mlb-db** | MLB pipeline PostgreSQL | running | [View](./MLBPipeline.md) |
| **107** | **mlb-app** | MLB pipeline app / dashboard | running | [View](./MLBPipeline.md) |
| **109** | **Paseo** | Agent host (VM, 8G RAM / 64G disk) | running | [View](./Paseo.md) |
| **110** | **Actual** | Actual Budget (Docker in LXC) | running | [View](./Actual.md) |

For a technical log of hardware/software upgrades, view [here](./Timeline.md)

## Maintenance & Backup
- **Hardware Specs:** Host/pool mapping in [Hardware.md](./Hardware.md).
- **Service Configurations:** systemd and stack manifests in `services/`.
- **Config snapshots:** LXC/VM JSON under `configs/` (refreshed by `backup_proxmox.py` / `sync.sh`).
- **Backups:** Critical data via Proxmox LXC/VM snapshots; environment configs versioned via Git.

## Emergency Recovery
1. Restore the underlying LXC/VM from the latest Proxmox snapshot.
2. Refer to the specific service page above for manual configuration drift or state restoration.

### Exterior PC
<img width="720" height="960" alt="image" src="https://github.com/user-attachments/assets/6aebe1e2-5287-48f7-8de5-28e123a816af" />

### Interior PC
<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/4ec7107b-4525-4f0f-a180-6994c4c1849e" />

---
*Inventory last updated: 2026-08-12*
