import json
import random
from datetime import datetime, timedelta

def generate_user_activity_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    actions = ["login", "file_download", "file_upload", "logout"]

    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "action": random.choice(actions),
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    
    return logs

def generate_large_file_transfer_logs(num_transfers):
    users = [f"user{i}" for i in range(1, 6)]
    destinations = ["cloud_storage", "external_drive", "internal_server"]

    transfers = []
    for _ in range(num_transfers):
        transfer = {
            "user_id": random.choice(users),
            "file_size": random.randint(10**6, 10**8),
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat(),
            "destination": random.choice(destinations)
        }
        transfers.append(transfer)
    
    return transfers

def generate_file_access_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "file_path": f"file_{random.randint(1, 100)}.txt",  # Changed to file_path
            "action": random.choice(["access", "modify", "delete"]),
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    
    return logs

def generate_database_access_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "database_name": f"db_{random.randint(1, 10)}",
            "action": random.choice(["read", "write", "delete"]),
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    
    return logs

def generate_privileged_access_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "access_level": f"privilege_{random.randint(1, 5)}",  # Changed to access_level
            "action": random.choice(["grant", "revoke", "access"]),
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    
    return logs

def generate_legacy_system_access_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "system_name": f"legacy_system_{random.randint(1, 5)}",
            "action": random.choice(["login", "logout", "access"]),
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    
    return logs

def generate_departmental_access_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    departments = ["HR", "Finance", "IT", "Marketing"]

    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "department_name": random.choice(departments),  # Changed to department_name
            "action": "access",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    
    return logs

def generate_access_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    resources = ["sensitive_file.txt", "internal_server", "confidential_db"]

    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "resource": random.choice(resources),
            "action": "access",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    
    return logs

def generate_unauthorized_software_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    software_names = ["malicious_tool.exe", "unauthorized_app.msi", "hack_tool.py"]

    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "software_name": random.choice(software_names),
            "device_id": f"device_{random.randint(1, 3)}",  # Added device_id
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    
    return logs

def generate_hacking_tools_usage_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    tools = ["nmap", "metasploit", "wireshark"]

    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "tool_name": random.choice(tools),
            "device_id": f"device_{random.randint(1, 3)}",  # Added device_id
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)

    return logs

def generate_command_line_access_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    commands = ["cmd.exe", "powershell.exe", "bash"]

    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "command_used": random.choice(commands),  # Changed to command_used
            "device_id": f"device_{random.randint(1, 3)}",  # Added device_id
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)

    return logs

# New features for data deletion or modification
def generate_mass_deletion_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "files_deleted": random.randint(50, 500),
            "target_directory": f"/home/{random.choice(users)}/files/",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    return logs

def generate_security_log_modification_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "log_file": "security.log",
            "modifications": "Removed entries related to unauthorized access",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    return logs

def generate_database_record_modification_logs(num_logs):
    users = [f"user{i}" for i in range(1, 6)]
    logs = []
    for _ in range(num_logs):
        log = {
            "user_id": random.choice(users),
            "database_name": f"db_{random.randint(1, 10)}",
            "record_id": random.randint(1000, 9999),
            "changes": {
                "field": "salary",
                "old_value": random.randint(30000, 100000),
                "new_value": random.randint(30000, 100000)
            },
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        }
        logs.append(log)
    return logs

if __name__ == "__main__":
    # Generate and save logs
    log_generators = {
        "user_activity_logs": generate_user_activity_logs,
        "large_file_transfer_logs": generate_large_file_transfer_logs,
        "file_access_logs": generate_file_access_logs,
        "database_access_logs": generate_database_access_logs,
        "privileged_access_logs": generate_privileged_access_logs,
        "legacy_system_access_logs": generate_legacy_system_access_logs,
        "departmental_access_logs": generate_departmental_access_logs,
        "access_logs": generate_access_logs,
        "unauthorized_software_logs": generate_unauthorized_software_logs,
        "hacking_tools_usage_logs": generate_hacking_tools_usage_logs,
        "command_line_access_logs": generate_command_line_access_logs,
        "mass_deletion_logs": generate_mass_deletion_logs,  # New feature
        "security_log_modification_logs": generate_security_log_modification_logs,  # New feature
        "database_record_modification_logs": generate_database_record_modification_logs,  # New feature
    }

    for log_type, generator in log_generators.items():
        logs = generator(50)  # Generate 50 logs for each type
        with open(f'C:\\Users\\bhara.KBHARATH\\Downloads\\onepro\\insider-threat-env\\data\\{log_type}.json', 'w') as f:
            json.dump(logs, f, indent=4)
        print(f"{log_type.replace('_', ' ').title()} generated successfully!")
