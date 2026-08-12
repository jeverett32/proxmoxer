# Paseo Agent Host (VM 109)

## Overview
Dedicated QEMU VM for running Paseo agent workloads. Isolated from LXC service containers so agent tooling, worktrees, and disk growth do not contend with Immich / Docker stacks.

## Resources
| Resource | Value |
| :--- | :--- |
| **vCPU** | 4 |
| **Memory** | 8192 MB |
| **Boot disk** | `local-lvm:vm-109-disk-0` **64G** |
| **On boot** | yes (`startup order=5`) |

## Network
- **Tailscale hostname:** `paseo-server`
- **Tailscale IP:** `<IP_ADDRESS>`
- **LAN MAC:** `BC:24:11:D2:90:54` (DHCP on `vmbr0`)
- **Guest agent:** not installed (console / Tailscale SSH for guest ops)

## Disk resize notes
Proxmox only grows the virtual disk. After `qm resize 109 scsi0 <size>`:

1. Confirm host LV size: `lvs | grep 109` / `qm config 109`
2. Reboot or rescan in guest if needed
3. Grow partition + filesystem inside the guest (`growpart` / `resize2fs` or distro equivalent)
4. Verify with `lsblk` and `df -h /`

History:
- Prior resize: 32G → 52G
- 2026-08-12: 52G → 64G (Proxmox task OK; guest reboot performed)

## Operations
- Start/stop from Proxmox host: `qm start 109` / `qm stop 109`
- Config backup path: `configs/vms/109.json`

---
*Last updated: 2026-08-12*
