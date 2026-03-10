### Homelab Technical Log

**September 7, 2025: Initial Acquisition**
* **Hardware:** Dell Optiplex 7010 SFF ($30)
* **Specs:** 10GB RAM / 500GB HDD
* **OS/Services:** Windows 10; Minecraft Server

**February 2, 2026: Remote Management**
* **Tools Added:** Rustdesk (Remote Desktop) and Tailscale (Mesh VPN)
* **Goal:** Off-site troubleshooting and server stability monitoring

**February 13, 2026: The Proxmox Pivot**
* **Infrastructure:** Migrated to Proxmox VE (Hypervisor) via USB install
* **Network Fix:** Replaced faulty Ethernet cable to resolve intermittent crashing
* **Services Deployed:**
    * **Networking:** Tailscale, Pi-hole, Cloudflare Tunnels
    * **Management:** Docker, Portainer, Uptime-Kuma
    * **Media/Storage:** Immich, Minecraft Server (VM)

**February 23, 2026: Storage Upgrade**
* **Hardware:** 512GB ADATA M.2 SATA SSD via [Sabrent 2.5" Adapter](https://www.amazon.com/dp/B01N6PMZLW?ref=ppx_pop_mob_ap_share)
* **Configuration:** * **Boot Drive:** 512GB SSD (Fresh Proxmox install)
    * **Storage Pool:** 500GB HDD (Dedicated to Immich/Jellyfin media)

**February 25, 2026: Memory Expansion**
* **Hardware:** [32GB DDR3L-1600 UDIMM](https://www.amazon.com/dp/B0DDH5KWYY?ref=ppx_pop_mob_ap_share)
* **Allocation:** 12GB dedicated to Minecraft; 20GB for LXC containers and VMs

#### **NEXT STEPS**
* Clean dust from inside desktop
* Reapply thermal paste to CPU
* Remove optical drive mounting and replace with mounting for SSD
* Upgrade 500GB HDD to 2-8TB HDD
* Perform vulnerability scanning and system hardening
* Host personal cloud storage like Google Drive (Not sure if I want to do this one)