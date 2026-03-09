# Immich Photo Manager (LXC 101)

## Overview
Self-hosted photo and video backup solution, replacing cloud-based alternatives with local storage and AI-powered metadata indexing.

## Network & Security
- **Static IP:** 10.1.23.157
- **Role:** Native systemd-managed photo management.

## Filesystem Layout

- **Import Path:** `/import` (Mapped to `/mnt/old_root/mnt/thumbdrive` on host)
- **App Directory:** `/opt/immich/` (Managed via Proxmox Helper-Scripts)

## Service Management
- **Primary Daemons:** - `immich-ml.service` (Machine Learning/AI indexing)
    - `immich-web.service` (Web UI)
- **Infrastructure Dependencies:**
    - `postgresql@16-main.service` (Database - Required)
    - `redis-server.service` (Cache/Queue - Required)
- **Backup Location:** `/opt/proxmox-backups/services/photos/`

## Service Configuration References
Links to the backed-up service definitions:
- [Immich Web](../services/photos/immich-web.service)
- [Immich ML](../services/photos/immich-ml.service)
- [PostgreSQL](../services/photos/postgresql.service)
- [Redis](../services/photos/redis.service)

## Installation
- **Method:** Automated installation script
- **Source:** [Proxmox VE Helper-Scripts](https://tteck.github.io/Proxmox/)
- **Deployment:** Automatic environment setup (Node.js/Python) at `/opt/immich/app/`
