import json
import urllib3
from elasticsearch import Elasticsearch, helpers
from elasticsearch.exceptions import NotFoundError, ConnectionError, RequestError

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to Elasticsearch
es = Elasticsearch(
    "https://192.168.1.10:9200",
    basic_auth=('elastic', 'Jr1O617_hAvHHzE3i1hB'),
    verify_certs=False  # Set this to False only for development/testing; ensure to use a proper certificate for production
)

def index_logs(file_path, index_name):
    """Index logs from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            logs = json.load(file)
            actions = [
                {
                    "_index": index_name,
                    "_source": log
                }
                for log in logs
            ]

            # Bulk indexing for better performance
            helpers.bulk(es, actions)
            print(f"Successfully indexed {len(actions)} logs into {index_name}.")

    except NotFoundError as nf_err:
        print(f"Index not found: {nf_err}")
    except ConnectionError as conn_err:
        print(f"Connection error: {conn_err}")
    except RequestError as req_err:
        print(f"Request error: {req_err}")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please ensure the log file is properly formatted.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define paths to your log files
    log_files = {
        "user_activity": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\sample_logs.json',
        "large_file_transfers": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\large_file_transfers.json',
        "access_logs": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\access_logs.json',
        "file_access_attempts": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\file_access_logs.json',
        "database_access_attempts": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\database_access_logs.json',
        "privileged_access_attempts": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\privileged_access_logs.json',
        "legacy_system_access_attempts": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\legacy_system_access_logs.json',
        "departmental_access_attempts": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\departmental_access_logs.json',
        "unauthorized_software_installation": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\unauthorized_software_logs.json',
        "hacking_tools_usage": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\hacking_tools_usage_logs.json',
        "command_line_access": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\command_line_access_logs.json',
        "mass_deletion": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\mass_deletion_logs.json',
        "security_log_modification": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\security_log_modification_logs.json',
        "database_record_modification": r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\database_record_modification_logs.json'
    }

    # Index each log file
    for index_name, file_path in log_files.items():
        index_logs(file_path, index_name)
