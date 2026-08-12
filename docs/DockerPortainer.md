# Docker & Portainer Hub (LXC 102)

## Overview
Centralized Docker host. Portainer provides a GUI for container management; Compose stacks run Uptime Kuma and Cloudflare Tunnel.

- **Resources:** 2 cores, 2048 MB RAM, 16G rootfs
- **Packages kept:** `docker-ce`, `docker-ce-cli`, `containerd.io`, `docker-compose-plugin`
- **Removed (unused):** Watchtower, Miniflux, n8n, `docker-buildx-plugin`, `docker-model-plugin`, `docker-ce-rootless-extras`

## Active containers

| Name | Image | Role |
| :--- | :--- | :--- |
| **portainer** | `portainer/portainer-ce:latest` | Docker management UI (`:9443` HTTPS, `:8000`) |
| **uptime-kuma** | `louislam/uptime-kuma:latest` | Uptime monitoring (`:3001`) |
| **cloudflared** | `cloudflare/cloudflared:latest` | Cloudflare Tunnel |

## Configuration Paths
- Docker data: `/var/lib/docker/`
- Portainer volume: `portainer_data`
- Uptime Kuma volume: `uptimekuma_uptime-kuma-data`
- Compose manifests (Portainer): `/var/lib/docker/volumes/portainer_data/_data/compose/`
  - Stack `2` → Uptime Kuma
  - Stack `3` → Cloudflared

## Service Management
- Docker Engine: [docker.service](../services/docker/docker.service)

```bash
docker ps
docker compose version
```

## Backup Strategy
- Volumes: Proxmox LXC snapshots
- Stack manifests mirrored in-repo (tokens redacted):
  - [Uptime-Kuma](../services/docker/stacks/stack_2.yml)
  - [Cloudflared](../services/docker/stacks/stack_3.yml)

## Installation & Setup
To bootstrap a clean LXC (102) with Docker and Portainer:

### 1. Install Docker Engine
```bash
apt update && apt install -y curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
apt update && apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

### 2. Deploy Portainer
```bash
docker volume create portainer_data
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data \
  portainer/portainer-ce:latest
```

---
*Last updated: 2026-08-12*
