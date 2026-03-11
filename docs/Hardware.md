# Hardware Specifications

## PC
- **Model:** 2012  Dell Optiplex 7010 Small Form Factor

## CPU
- **Model:** Intel(R) Core(TM) i5-3550 CPU @ 3.30GHz
- **Architecture:** x86_64

## Memory
- **Total Physical RAM:** 32GB (31Gi)
- **Swap Partition:** 8.0GB

## Storage Layout
| Device | Model | Size | Role |
| :--- | :--- | :--- | :--- |
| **sda** | ADATA SU800NS38 | 476.9G | Proxmox OS & Local Storage |
| **sdb** | WDC WD5000AAKS | 465.8G | Media Data Pool |

## Network Interfaces
- **Primary Bridge (vmbr0):** <IP_ADDRESS>
- **Physical Port:** nic0 (enp0s25)
- **Tunnel:** Tailscale <IP_ADDRESS>

---
*Last updated: 2026-03-11*

### Future Improvements
- [ ] Document UPS power thresholds
- [ ] Add BIOS/Firmware configuration details
- [ ] Detail the physical drive bay layout
- [ ] Backup and Recovery Strategy
