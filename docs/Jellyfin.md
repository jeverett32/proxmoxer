# Jellyfin Media Server (LXC 104)

## Overview
Jellyfin acts as your primary media consumption interface, ingesting the library processed by the Arr stack and providing high-performance streaming.

## Network & Security
- **Static IP:** <IP_ADDRESS>
- **Port:** 8096
- **Tunneling:** `/dev/net/tun` enabled (Allows VPN integration if needed).

## Filesystem Layout
The Proxmox host library (`/mnt/data_pool/library`) is mounted for media ingestion:

| Host Path | Container Path | Purpose |
| :--- | :--- | :--- |
| `/mnt/data_pool/library` | `/media/movies` | Read-only media library for Jellyfin |

## Hardware Acceleration (Transcoding)

- **Configuration:** `lxc.cgroup2.devices.allow: c 10:200 rwm` (Direct access to Intel render node).
- **Backend:** VA-API / Intel QuickSync.

## Service Management
- **Service Name:** `jellyfin.service`
- **Backup Location:** `/opt/proxmox-backups/services/media/jellyfin.service`

## Service Configuration References
- [Jellyfin Service](../services/media/jellyfin.service)
- [Prowlarr Service](../services/media/prowlarr.service)
- [qBittorrent-nox Service](../services/media/qbittorrent-nox.service)
- [Radarr Service](../services/media/radarr.service)
- [Sonarr Service](../services/media/sonarr.service)

## Installation
- **Method:** Official Repository (`apt`)
- **Verification:** `systemctl status jellyfin`

---

## Data Flow Diagram
```mermaid
graph LR
    Sonarr/Radarr -- "/library" --> Jellyfin
    Jellyfin -- "Streaming" --> Client
