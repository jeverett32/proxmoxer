# Docker & Portainer Hub (LXC 102)

## Overview
Centralized management hub for all Docker-based services. Portainer provides the GUI for stack orchestration, while Docker Engine handles container execution.

## Configuration Paths
- Docker Data: /var/lib/docker/
- Compose Manifests: /var/lib/docker/volumes/portainer_data/_data/compose/

## Service Management
- Docker Engine Service: ../services/docker/docker.service

## Backup Strategy
- Volumes: Managed via Proxmox LXC snapshots.
- Stacks: docker-compose.yml manifests are synced from Portainer's internal volume directory.
- Stack References:
    - [Stack 1](../services/docker/stacks/stack_1.yml)
    - [Stack 2](../services/docker/stacks/stack_2.yml)
    - [Stack 3](../services/docker/stacks/stack_3.yml)
    - [Stack 6](../services/docker/stacks/stack_6.yml)

## Installation & Setup
To bootstrap a clean LXC (102) with Docker and Portainer:

### 1. Install Docker Engine
apt update && apt install -y curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
apt update && apt install -y docker-ce docker-ce-cli containerd.io

### 2. Deploy Portainer
docker volume create portainer_data
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest

## Navigation
- Return to Hardware Specs: ./Hardware.md
