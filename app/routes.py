from flask import Blueprint, request, jsonify, Flask, render_template
from elasticsearch import Elasticsearch
import pandas as pd
import numpy as np
import logging
import sys
import os

from app import logger
from splunk_integration import send_to_splunk



from logging.handlers import RotatingFileHandler
app = Flask(__name__)
from .models import (
    train_large_file_transfer_model, detect_anomalies,
    train_file_access_model, detect_file_access_anomalies,
    train_database_access_model, detect_database_access_anomalies,
    train_privileged_access_model, detect_privileged_access_anomalies,
    train_legacy_system_access_model, detect_legacy_system_access_anomalies,
    train_department_access_model, detect_department_access_anomalies,
    train_unauthorized_software_installation_model, detect_unauthorized_software_installation,
    train_hacking_tools_model, detect_hacking_tools,
    train_command_line_access_model, detect_command_line_access,
    train_database_record_alteration_model, train_mass_deletion_model,
    detect_database_record_alteration_anomalies, detect_mass_deletion_anomalies,
    train_security_log_modification_model, detect_security_log_modification_anomalies
)

main = Blueprint('main', __name__)
es = Elasticsearch("https://192.168.1.10:9200", basic_auth=('elastic', 'Jr1O617_hAvHHzE3i1hB'), verify_certs=False)

# Global variables to store trained models
large_file_model = None
file_access_model = None
database_access_model = None
privileged_access_model = None
legacy_system_access_model = None
department_access_model = None
unauthorized_software_model = None
hacking_tools_model = None
command_line_access_model = None
mass_deletion_model = None
log_modification_model = None
database_record_alteration_model = None

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.before_request
def log_request_info():
    # Log the method, URL, and JSON data (if any) of incoming requests
    logger.info(f'Request Method: {request.method}, URL: {request.url}, Data: {request.get_json()}')
    
@main.route('/')
def index():
    return render_template('index.html')


# --- Large File Transfer Endpoints ---
@main.route('/train_large_file_transfer', methods=['POST'])
def train_large_file_transfer():
    global large_file_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        large_file_model = train_large_file_transfer_model(df)
        logger.info("Large file transfer model trained successfully.")
        return jsonify({"message": "Large file transfer model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training large file transfer model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_large_file_transfer', methods=['POST'])
def detect_large_file_transfer():
    global large_file_model
    try:
        if large_file_model is None:
            return jsonify({"error": "Large file transfer model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        anomalies = detect_anomalies(large_file_model, df)
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in large file transfer: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting large file transfer anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500

# --- File Access Endpoints ---
@main.route('/train_file_access', methods=['POST'])
def train_file_access():
    global file_access_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        file_access_model = train_file_access_model(df)
        logger.info("File access model trained successfully.")
        return jsonify({"message": "File access model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training file access model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_file_access', methods=['POST'])
def detect_file_access():
    global file_access_model
    try:
        if file_access_model is None:
            return jsonify({"error": "File access model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        anomalies = detect_file_access_anomalies(file_access_model, df)
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in file access: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting file access anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500

# --- Database Access Endpoints ---
@main.route('/train_database_access', methods=['POST'])
def train_database_access():
    global database_access_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        database_access_model = train_database_access_model(df)
        logger.info("Database access model trained successfully.")
        return jsonify({"message": "Database access model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training database access model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_database_access', methods=['POST'])
def detect_database_access():
    global database_access_model
    try:
        if database_access_model is None:
            return jsonify({"error": "Database access model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        anomalies = detect_database_access_anomalies(database_access_model, df)
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in database access: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting database access anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500

# --- Privileged Access Endpoints ---
@main.route('/train_privileged_access', methods=['POST'])
def train_privileged_access():
    global privileged_access_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        privileged_access_model = train_privileged_access_model(df)
        logger.info("Privileged access model trained successfully.")
        return jsonify({"message": "Privileged access model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training privileged access model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_privileged_access', methods=['POST'])
def detect_privileged_access():
    global privileged_access_model
    try:
        if privileged_access_model is None:
            return jsonify({"error": "Privileged access model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        anomalies = detect_privileged_access_anomalies(privileged_access_model, df)
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in privileged access: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting privileged access anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/train_legacy_system_access', methods=['POST'])
def train_legacy_system_access():
    global legacy_system_access_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        legacy_system_access_model = train_legacy_system_access_model(df)
        logger.info("Legacy system access model trained successfully.")
        return jsonify({"message": "Legacy system access model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training legacy system access model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_legacy_system_access', methods=['POST'])
def detect_legacy_system_access():
    global legacy_system_access_model
    try:
        if legacy_system_access_model is None:
            return jsonify({"error": "Legacy system access model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        anomalies = detect_legacy_system_access_anomalies(legacy_system_access_model, df)
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in legacy system access: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting legacy system access anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500

# --- Cross-Departmental Access Endpoints ---
@main.route('/train_department_access', methods=['POST'])
def train_department_access():
    global department_access_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        department_access_model = train_department_access_model(df)
        logger.info("Cross-departmental access model trained successfully.")
        return jsonify({"message": "Cross-departmental access model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training department access model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_department_access', methods=['POST'])
def detect_department_access():
    global department_access_model
    try:
        if department_access_model is None:
            return jsonify({"error": "Department access model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        anomalies = detect_department_access_anomalies(department_access_model, df)
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in department access: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting department access anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500

# --- Unauthorized Software Installation Endpoints ---
@main.route('/train_unauthorized_software', methods=['POST'])
def train_unauthorized_software():
    global unauthorized_software_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        unauthorized_software_model = train_unauthorized_software_installation_model(df)
        logger.info("Unauthorized software installation model trained successfully.")
        return jsonify({"message": "Unauthorized software installation model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training unauthorized software installation model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_unauthorized_software', methods=['POST'])
def detect_unauthorized_software():
    global unauthorized_software_model
    try:
        if unauthorized_software_model is None:
            return jsonify({"error": "Unauthorized software model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        anomalies = detect_unauthorized_software_installation(unauthorized_software_model, df)
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in unauthorized software installation: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting unauthorized software installation anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500

# --- Hacking Tools Endpoints ---
@main.route('/train_hacking_tools', methods=['POST'])
def train_hacking_tools():
    global hacking_tools_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        hacking_tools_model = train_hacking_tools_model(df)
        logger.info("Hacking tools model trained successfully.")
        return jsonify({"message": "Hacking tools model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training hacking tools model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_hacking_tools', methods=['POST'])
def hacking_tools_detection_endpoint():
    global hacking_tools_model
    try:
        if hacking_tools_model is None:
            return jsonify({"error": "Hacking tools model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        
        # Call the detection function
        anomalies = detect_hacking_tools(hacking_tools_model, df)
        
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in hacking tools usage: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting hacking tools usage anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500


# --- Command Line Access Endpoints ---
@main.route('/train_command_line_access', methods=['POST'])
def train_command_line_access():
    global command_line_access_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        command_line_access_model = train_command_line_access_model(df)
        logger.info("Command line access model trained successfully.")
        return jsonify({"message": "Command line access model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training command line access model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_command_line_access', methods=['POST'])
def command_line_access_detection_endpoint():
    global command_line_access_model
    try:
        if command_line_access_model is None:
            return jsonify({"error": "Command line access model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        
        # Call the detection function
        anomalies = detect_command_line_access(command_line_access_model, df)
        
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in command line access: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting command line access anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500


# --- Mass Deletion Endpoints ---
@main.route('/train_mass_deletion', methods=['POST'])
def train_mass_deletion():
    global mass_deletion_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        mass_deletion_model = train_mass_deletion_model(df)
        logger.info("Mass deletion model trained successfully.")
        return jsonify({"message": "Mass deletion model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training mass deletion model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_mass_deletion', methods=['POST'])
def detect_mass_deletion():
    global mass_deletion_model
    try:
        if mass_deletion_model is None:
            return jsonify({"error": "Mass deletion model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        logger.info(f"Data received for mass deletion detection: {df.head()}")  # Log the received data

        # Convert timestamp to datetime and then to Unix time
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['timestamp'] = df['timestamp'].astype('int64') // 10**9  # Convert to seconds

        anomalies = detect_mass_deletion_anomalies(mass_deletion_model, df)
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in mass deletion: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting mass deletion anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500


# --- Security Log Modification Endpoints ---
@main.route('/train_security_log_modification', methods=['POST'])
def train_security_log_modification():
    global log_modification_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        log_modification_model = train_security_log_modification_model(df)
        logger.info("Security log modification model trained successfully.")
        return jsonify({"message": "Security log modification model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training security log modification model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_security_log_modification', methods=['POST'])
def detect_security_log_modification():
    global log_modification_model
    try:
        if log_modification_model is None:
            return jsonify({"error": "Security log modification model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        anomalies = detect_security_log_modification_anomalies(log_modification_model, df)
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in security log modifications: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting security log modification anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500

# --- Database Record Alteration Endpoints ---
@main.route('/train_database_record_alteration', methods=['POST'])
def train_database_record_alteration():
    global database_record_alteration_model
    try:
        data = request.json
        df = pd.DataFrame(data)
        database_record_alteration_model = train_database_record_alteration_model(df)
        logger.info("Database record alteration model trained successfully.")
        return jsonify({"message": "Database record alteration model trained successfully"}), 200
    except Exception as e:
        logger.error(f'Error training database record alteration model: {str(e)}')
        return jsonify({"error": str(e)}), 500

@main.route('/detect_database_record_alteration', methods=['POST'])
def detect_database_record_alteration():
    global database_record_alteration_model
    try:
        if database_record_alteration_model is None:
            return jsonify({"error": "Database record alteration model is not trained yet"}), 400
        data = request.json
        df = pd.DataFrame(data)
        anomalies = detect_database_record_alteration_anomalies(database_record_alteration_model, df)
        anomalies = anomalies[anomalies['anomaly'] == -1]
        logger.info(f'Detected anomalies in database record alterations: {anomalies.to_dict(orient="records")}')
        return jsonify({"anomalies": anomalies.to_dict(orient='records')}), 200
    except Exception as e:
        logger.error(f'Error detecting database record alteration anomalies: {str(e)}')
        return jsonify({"error": str(e)}), 500

       

# Create the Flask app and register the blueprint

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
