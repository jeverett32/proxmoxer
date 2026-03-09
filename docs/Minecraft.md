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
- [Server Properties](../services/minecraft/server.properties)
- [Spigot Configuration](../services/minecraft/spigot.yml)
- [Purpur Configuration](../services/minecraft/purpur.yml)
- [Bukkit Configuration](../services/minecraft/bukkit.yml)
- [Startup Script](../services/minecraft/start.sh)

## Why are these backed up?
These files represent the "brain" of your server. Backing them up ensures that if you ever need to rebuild the VM, you don't lose:
- **Server Identity:** Your server's unique settings and world generation rules (`server.properties`).
- **Performance Tuning:** Custom optimizations for the server engine (`spigot.yml`, `purpur.yml`, `bukkit.yml`).
- **Execution Logic:** The exact commands and memory flags used to boot your server (`start.sh`).

## Playit.gg Configuration
The server relies on the `playit` agent to bypass NAT. 
- **Startup:** Because automated authentication fails, this must be started manually.
- **Command:** `./playit` (Must be run from the playit directory)
- **Persistence:** Currently running in an interactive session; if the VM reboots, this must be re-launched manually to restore tunnel connectivity.

## Backup Strategy
- **World Data:** Managed via Proxmox VM snapshots.
- **Server Config:** Config files are versioned in this repository for easy restoration.
- **Playit Credentials:** Ensure your `~/.playit` configuration directory is included in your VM snapshots.

## Navigation
- [Return to Hardware Specs](./Hardware.md)
