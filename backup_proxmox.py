import json
import os
from proxmoxer import ProxmoxAPI

# --- Configuration ---
# Use 'localhost' since it's running on the server itself
HOST = 'localhost' 
USER = 'root@pam'
PASSWORD = 'txDn0sw@Id%rGKlemon' 
BACKUP_DIR = '/opt/proxmox-backups/configs'

proxmox = ProxmoxAPI(HOST, user=USER, password=PASSWORD, verify_ssl=False)
os.makedirs(f"{BACKUP_DIR}/lxc", exist_ok=True)
os.makedirs(f"{BACKUP_DIR}/vms", exist_ok=True)

# Export all resources
for resource in proxmox.cluster.resources.get(type='vm'):
    vmid = resource['vmid']
    node = resource['node']
    res_type = resource.get('type')
    
    if res_type == 'lxc':
        conf = proxmox.nodes(node).lxc(vmid).config.get()
        with open(f"{BACKUP_DIR}/lxc/{vmid}.json", 'w') as f:
            json.dump(conf, f, indent=4)
    elif res_type == 'qemu':
        conf = proxmox.nodes(node).qemu(vmid).config.get()
        with open(f"{BACKUP_DIR}/vms/{vmid}.json", 'w') as f:
            json.dump(conf, f, indent=4)
