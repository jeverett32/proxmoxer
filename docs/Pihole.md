# Pi-hole DNS Documentation (LXC 100)

## Overview
Acts as the central network-wide ad blocker and local DNS resolver.

## Network & Security
- **Static IP:** <IP_ADDRESS>
- **Role:** Primary DNS for the local network.

## Service Management
- **Primary Daemon:** `pihole-FTL.service`
- **Backup Location:** `/opt/proxmox-backups/services/network/pihole-FTL.service`

## Service Configuration References
- [Pi-hole FTL Service](../services/network/pihole-FTL.service)

## Blocklist Configuration
Your current active blocklists are managed through the following sources:
- **StevenBlack:** [https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts)
- **OISD (big):** [https://big.oisd.nl/](https://big.oisd.nl/)
- **Hagezi (DNS-blocklists/pro):** [https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt)
- **Firebog:** [https://v.firebog.net/hosts/lists.php?type=tick](https://v.firebog.net/hosts/lists.php?type=tick)

## Replication & Backup
- **Config Directory:** `/etc/pihole/`
- **Gravity Database:** `/etc/pihole/gravity.db` (Contains your blocklists and whitelist)

## Installation
- **Method:** `curl -sSL https://install.pi-hole.net | bash`
