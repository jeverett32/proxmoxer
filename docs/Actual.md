# Actual Budget (LXC 110)

## Overview
Self-hosted [Actual Budget](https://actualbudget.org/) server for personal finance. Runs as a Docker Compose stack inside an Ubuntu LXC with Tailscale for remote access.

## Resources
| Resource | Value |
| :--- | :--- |
| **vCPU** | 2 |
| **Memory** | 2048 MB |
| **Rootfs** | 8G |
| **Tags** | finance |
| **On boot** | yes (`startup order=7`) |

## Network & Access
- **LAN IP (DHCP):** `<IP_ADDRESS>`
- **Tailscale IP:** `<IP_ADDRESS>`
- **Listen:** `127.0.0.1:5006` and Tailscale IP `:5006` (HTTPS via self-signed certs in compose)
- Prefer Tailscale from other hosts (e.g. Cloudflare Tunnel / Uptime Kuma). Use `noTLSVerify` if the edge proxy does not trust the self-signed cert.

## Filesystem Layout
- **Stack:** `/opt/actual/compose.yaml`
- **Data:** `/opt/actual/data`
- **TLS certs:** `/opt/actual/certs` (mounted read-only into the container)

## Service Management

```bash
cd /opt/actual
docker compose ps
docker compose logs -f --tail=100
docker compose up -d
```

Container name: `actual-server`  
Image: `docker.io/actualbudget/actual-server:latest`

## Notes
- Nesting + `/dev/net/tun` enabled for Docker and Tailscale inside the unprivileged LXC.
- Config backup path: `configs/lxc/110.json`

---
*Last updated: 2026-08-12*
