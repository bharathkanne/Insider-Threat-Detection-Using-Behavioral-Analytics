from elasticsearch import Elasticsearch

# Create an Elasticsearch client with authentication (if needed)
es = Elasticsearch(
    "https://192.168.1.10:9200",
    http_auth=('elastic', 'ErJedlMpDEQsF9TUOSpf'),  # Replace with your credentials if needed
    verify_certs=False  # Bypass SSL verification for self-signed certificates
)

# Verify the connection
try:
    if es.ping():
        print("Connected to Elasticsearch")
    else:
        print("Could not connect to Elasticsearch")
except Exception as e:
    print(f"Error connecting to Elasticsearch: {e}")
