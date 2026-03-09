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

## Service Configuration & Installation
All service files are backed up in `/opt/proxmox-backups/services/media/`.

### Installation Table
| Service | Port | Installation Command (Run in /tmp) |
| :--- | :--- | :--- |
| **Prowlarr** | 9696 | `curl -L -O "https://github.com/Prowlarr/Prowlarr/releases/download/v1.31.2.4975/Prowlarr.master.1.31.2.4975.linux-core-x64.tar.gz"` |
| **Sonarr** | 8989 | `curl -L -O "https://github.com/Sonarr/Sonarr/releases/download/v4.0.13.2934/Sonarr.v4.0.13.2934.linux-core-x64.tar.gz"` |
| **Radarr** | 7878 | `curl -L -O "https://github.com/Radarr/Radarr/releases/download/v6.0.4.10291/Radarr.master.6.0.4.10291.linux-core-x64.tar.gz"` |
| **qBittorrent** | 8080 | `apt install qbittorrent-nox` |
| **VPN** | N/A | `apt install wireguard` |

### Installation Pattern (Manual Binary)
After downloading, execute the following steps for each binary service:
1. **Extract:** `tar -xvzf [File] -C /opt/`
2. **Permissions:** `chown -R [user]:media /opt/[App]`
3. **Service:** Create a `systemd` service file in `/etc/systemd/system/`.

---

## Data Flow Diagram
```mermaid
graph LR
    Prowlarr --> Sonarr/Radarr
    Sonarr/Radarr --> qBittorrent
    qBittorrent -- "/downloads" --> Sonarr/Radarr
    Sonarr/Radarr -- "/library" --> Jellyfin
