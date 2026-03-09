# Minecraft Server (VM 103)

## Overview
Dedicated Minecraft server instance for persistent world hosting. 

## Configuration
- **Server Path:** /home/john/mc_server/MinecraftServer/
- **World Path:** /home/john/mc_server/MinecraftServer/world/
- **Port:** 25565
- **Tunnel:** playit.gg (Manual)

## Service Management
- [Minecraft Service](../services/misc/minecraft.service)

## Playit.gg Configuration
The server relies on the `playit` agent to bypass NAT. 
- **Startup:** Because automated authentication fails, this must be started manually.
- **Command:** `./playit` (Must be run from the playit directory)
- **Persistence:** Currently running in an interactive session; if the VM reboots, this must be re-launched manually to restore tunnel connectivity.

## Backup Strategy
- **World Data:** Managed via Proxmox VM snapshots.
- **Server Config:** `server.properties` and associated files are part of the VM disk.
- **Playit Credentials:** Ensure your `~/.playit` configuration directory is included in your VM snapshots.

## Navigation
- [Return to Hardware Specs](./Hardware.md)
