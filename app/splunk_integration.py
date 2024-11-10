import requests

def send_to_splunk(data):
    url = 'https://splunk-instance:8088/services/collector'  # Replace with your Splunk instance URL
    headers = {
        'Authorization': 'fd68ae48-e5b8-405a-bec9-2a1ff31f81b4',  # Replace with your Splunk token
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            print("Data sent to Splunk successfully.")
        else:
            print(f"Failed to send data to Splunk: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending data to Splunk: {e}")
