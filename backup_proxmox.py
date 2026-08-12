import json
import os
from pathlib import Path

from proxmoxer import ProxmoxAPI

BACKUP_DIR = "/opt/proxmox-backups/configs"
SECRETS_FILE = Path("/etc/proxmox-backups/secrets.env")


def load_secrets(path: Path) -> dict:
    secrets = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        secrets[key.strip()] = value.strip().strip('"').strip("'")
    return secrets


secrets = load_secrets(SECRETS_FILE)
token_id = secrets["PVE_TOKEN_ID"]
token_secret = secrets["PVE_TOKEN_SECRET"]
user, token_name = token_id.split("!", 1)

proxmox = ProxmoxAPI(
    "localhost",
    user=user,
    token_name=token_name,
    token_value=token_secret,
    verify_ssl=False,
)

os.makedirs(f"{BACKUP_DIR}/lxc", exist_ok=True)
os.makedirs(f"{BACKUP_DIR}/vms", exist_ok=True)

for resource in proxmox.cluster.resources.get(type="vm"):
    vmid = resource["vmid"]
    node = resource["node"]
    res_type = resource.get("type")

    if res_type == "lxc":
        conf = proxmox.nodes(node).lxc(vmid).config.get()
        with open(f"{BACKUP_DIR}/lxc/{vmid}.json", "w") as f:
            json.dump(conf, f, indent=4)
    elif res_type == "qemu":
        conf = proxmox.nodes(node).qemu(vmid).config.get()
        with open(f"{BACKUP_DIR}/vms/{vmid}.json", "w") as f:
            json.dump(conf, f, indent=4)

print("Backup complete")
