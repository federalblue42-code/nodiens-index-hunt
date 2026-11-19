# Nodiens Index Hunt Tracker

import json
import os

NODIENS_CONFIG = {
    "name": "Nodiens Index Hunt",
    "app_url": "https://app.nodiens.com",
    "discord": "https://discord.com/invite/nodiens",
    "reward_pool": "$1,000 in stablecoins",
    "schedule": "Nov 16-28 (Daily clues at 12:00 UTC)",
    "steps": [
        "Join Discord & open #index-hunt",
        "Sign up at app.nodiens.com",
        "Solve daily market clues using app indices & coin pages",
        "Submit answer via pinned form"
    ]
}

def log_nodiens():
    print(f"[*] Initializing Tracker for: {NODIENS_CONFIG['name']}")
    print(f"[*] Reward Pool: {NODIENS_CONFIG['reward_pool']}")
    print(f"[*] Schedule: {NODIENS_CONFIG['schedule']}")
    for step in NODIENS_CONFIG['steps']:
        print(f"    - {step}")
    
    os.makedirs("/data/data/com.termux/files/home/Yura-Hana/wallet", exist_ok=True)
    with open("/data/data/com.termux/files/home/Yura-Hana/wallet/nodiens_status.json", "w") as f:
        json.dump(NODIENS_CONFIG, f, indent=2)
    print("[+] Nodiens Index Hunt logged successfully, oppa! 💜")

if __name__ == "__main__":
    log_nodiens()
