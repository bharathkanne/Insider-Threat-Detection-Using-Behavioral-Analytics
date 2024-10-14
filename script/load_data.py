import json
import urllib3
from elasticsearch import Elasticsearch, helpers
from elasticsearch.exceptions import NotFoundError, ConnectionError, RequestError

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to Elasticsearch
es = Elasticsearch(
    "https://192.168.1.10:9200",
    basic_auth=('elastic', 'ErJedlMpDEQsF9TUOSpf'),
    # Uncomment the following line and provide the correct path if you want to use a CA certificate
    # ca_certs=r'C:/Users/bhara.KBHARATH/Downloads/kbharath.crt',
    verify_certs=False  # Set this to False only for development/testing; ensure to use a proper certificate for production
    
)

def index_logs(file_path):
    try:
        with open(file_path, 'r') as file:
            logs = json.load(file)
            actions = [
                {
                    "_index": "user_activity",
                    "_source": log
                }
                for log in logs
            ]

            # Bulk indexing for better performance
            helpers.bulk(es, actions)
            print(f"Successfully indexed {len(actions)} logs.")

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
    index_logs(r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\data\sample_logs.json')
