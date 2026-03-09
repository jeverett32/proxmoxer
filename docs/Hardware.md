# Hardware Specifications

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
- **Primary Bridge (vmbr0):** 10.1.23.162
- **Physical Port:** nic0 (enp0s25)
- **Tunnel:** Tailscale (100.92.163.44)

---
*Last updated: 2026-03-09*

### Future Improvements
- [ ] Document UPS power thresholds
- [ ] Add BIOS/Firmware configuration details
- [ ] Detail the physical drive bay layout
- [ ] Backup and Recovery Strategy
