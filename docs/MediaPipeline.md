# Media Pipeline Documentation (LXC 105)

## Overview
This container serves as the automated media acquisition hub. It secures all external traffic through a WireGuard VPN tunnel and maintains a structured file pipeline to feed the Jellyfin media server.

## Pipeline Architecture

1. **Prowlarr** searches indexers.
2. **Sonarr/Radarr** manage content logic and queue downloads.
3. **qBittorrent** downloads content via the VPN interface.
4. **Jellyfin** (External) consumes the processed media from the library.

## Network & Security
- **Static IP:** 10.1.23.159
- **VPN:** WireGuard (Mullvad) via `wg-quick@wg0.service`.
- **Tunneling:** `/dev/net/tun` passthrough enabled in container config.
- **Verification:** Run `wg show` inside LXC 105 to confirm tunnel status.

## Filesystem Layout

The Proxmox host HDD (`/mnt/data_pool`) is mounted into the container as follows:

| Host Path | Container Path | Purpose |
| :--- | :--- | :--- |
| `/mnt/data_pool/torrents` | `/downloads` | qBittorrent active downloads |
| `/mnt/data_pool/library` | `/library` | Final media library (Jellyfin source) |

## Service Definitions
All service files are backed up in `/opt/proxmox-backups/services/`.
- **Prowlarr:** `prowlarr.service`
- **Sonarr:** `sonarr.service`
- **Radarr:** `radarr.service`
- **qBittorrent:** `qbittorrent-nox.service`
- **VPN:** `wg-quick@wg0.service`

---

## Data Flow Diagram
```mermaid
graph LR
    Prowlarr --> Sonarr/Radarr
    Sonarr/Radarr --> qBittorrent
    qBittorrent -- "/downloads" --> Sonarr/Radarr
    Sonarr/Radarr -- "/library" --> Jellyfin
