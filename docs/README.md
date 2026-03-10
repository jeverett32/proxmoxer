# Home Lab Infrastructure Documentation

Welcome to the central documentation repository for the Proxmox home lab. This repository maintains the state, configuration, and recovery procedures for all running services and virtual machines.

## Infrastructure Overview

| ID | Name | Role | Documentation |
| :--- | :--- | :--- | :--- |
| **100** | **Pi-hole** | Network-wide Ad-blocking | [View](./Pihole.md) |
| **101** | **Immich** | Photo & Video Management | [View](./Immich.md) |
| **102** | **Docker/Portainer** | Service Orchestration | [View](./DockerPortainer.md) |
| **103** | **Minecraft** | Gaming Server | [View](./Minecraft.md) |
| **104** | **Jellyfin** | Media Consumption | [View](./Jellyfin.md) |
| **105** | **Media Pipeline** | Acquisition & Processing | [View](./MediaPipeline.md) |

For a timeline of hardware/software upgrades, view [here](./Timeline.md)

## Maintenance & Backup
- **Hardware Specs:** Detailed host/pool mapping can be found in [Hardware.md](./Hardware.md).
- **Service Configurations:** All `systemd` and stack manifests are stored in the `services/` directory.
- **Backups:** Critical data is maintained via Proxmox LXC/VM snapshots; environment configs are versioned via Git.

## Emergency Recovery
1. Restore the underlying LXC/VM from the latest Proxmox snapshot.
2. Refer to the specific service page above for manual configuration drift or state restoration.

### Exterior PC
<img width="720" height="960" alt="image" src="https://github.com/user-attachments/assets/6aebe1e2-5287-48f7-8de5-28e123a816af" />

### Interior PC
<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/4ec7107b-4525-4f0f-a180-6994c4c1849e" />

