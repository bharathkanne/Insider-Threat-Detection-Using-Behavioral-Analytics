from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np
# --- Training for Large File Transfer ---
def train_large_file_transfer_model(data):
    """
    Train an Isolation Forest model on large file transfer data.
    Assumes 'data' is a DataFrame with columns 'file_size', 'user_id', and 'destination'.
    """
    data['user_id_encoded'] = data['user_id'].astype('category').cat.codes
    data['destination_encoded'] = data['destination'].astype('category').cat.codes

    model = IsolationForest(n_estimators=100, contamination=0.1)
    model.fit(data[['file_size', 'user_id_encoded', 'destination_encoded']])
    return model

def detect_anomalies(model, new_data):
    """
    Detect anomalies in new large file transfer data.
    """
    new_data['user_id_encoded'] = new_data['user_id'].astype('category').cat.codes
    new_data['destination_encoded'] = new_data['destination'].astype('category').cat.codes

    predictions = model.predict(new_data[['file_size', 'user_id_encoded', 'destination_encoded']])
    new_data['anomaly'] = predictions
    return new_data

# --- Generic Training Function for Access Models ---
def train_access_model(data, features):
    """
    Train an Isolation Forest model for access data using specified features.
    """
    for feature in features:
        if data[feature].dtype == 'object':
            data[f'{feature}_encoded'] = data[feature].astype('category').cat.codes

    model = IsolationForest(n_estimators=100, contamination=0.1)
    model.fit(data[[f'{feature}_encoded' for feature in features]])
    return model

# --- Functions for Specific Access Types ---
def train_file_access_model(data):
    return train_access_model(data, ['user_id', 'file_path'])

def train_database_access_model(data):
    return train_access_model(data, ['user_id', 'database_name'])

def train_privileged_access_model(data):
    return train_access_model(data, ['user_id', 'access_level'])

def train_legacy_system_access_model(data):
    return train_access_model(data, ['user_id', 'system_name'])

def train_department_access_model(data):
    return train_access_model(data, ['user_id', 'department_name'])

# --- New: Functions for Unusual Software Usage ---
def train_unauthorized_software_installation_model(data):
    return train_access_model(data, ['user_id', 'software_name', 'device_id'])

def train_hacking_tools_model(data):
    return train_access_model(data, ['user_id', 'tool_name', 'device_id'])

def train_command_line_access_model(data):
    return train_access_model(data, ['user_id', 'command_used', 'device_id'])

# --- Functions to Detect Anomalies for Different Access Types ---
def detect_access_anomalies(model, new_data, features):
    for feature in features:
        if new_data[feature].dtype == 'object':
            new_data[f'{feature}_encoded'] = new_data[feature].astype('category').cat.codes
    
    predictions = model.predict(new_data[[f'{feature}_encoded' for feature in features]])
    new_data['anomaly'] = predictions
    return new_data

# --- Functions for Detecting Anomalies for Each Access Type ---
def detect_file_access_anomalies(model, new_data):
    return detect_access_anomalies(model, new_data, ['user_id', 'file_path'])

def detect_database_access_anomalies(model, new_data):
    return detect_access_anomalies(model, new_data, ['user_id', 'database_name'])

def detect_privileged_access_anomalies(model, new_data):
    return detect_access_anomalies(model, new_data, ['user_id', 'access_level'])

def detect_legacy_system_access_anomalies(model, new_data):
    return detect_access_anomalies(model, new_data, ['user_id', 'system_name'])

def detect_department_access_anomalies(model, new_data):
    return detect_access_anomalies(model, new_data, ['user_id', 'department_name'])

# --- New: Functions to Detect Anomalies for Unusual Software Usage ---
def detect_unauthorized_software_installation(model, new_data):
    return detect_access_anomalies(model, new_data, ['user_id', 'software_name', 'device_id'])

def detect_hacking_tools(model, new_data):
    return detect_access_anomalies(model, new_data, ['user_id', 'tool_name', 'device_id'])

def detect_command_line_access(model, new_data):
    return detect_access_anomalies(model, new_data, ['user_id', 'command_used', 'device_id'])

# Mass Deletion of Files
def train_mass_deletion_model(df):
    # Convert timestamp to UNIX timestamp (float)
    df['timestamp'] = pd.to_datetime(df['timestamp']).astype(np.int64) // 10**9  # Convert to seconds

    model = IsolationForest(contamination=0.1)
    model.fit(df[['file_count', 'timestamp']])  # Use numeric features for training
    return model

def detect_mass_deletion_anomalies(model, df):
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Convert to Unix time (seconds)
    df['timestamp'] = df['timestamp'].astype('int64') // 10**9  # Convert to seconds
    
    df['anomaly'] = model.predict(df[['file_count', 'timestamp']])  # Modify based on your features
    return df


# Modification of Security Logs
def train_security_log_modification_model(df):
    df['modification_time'] = pd.to_datetime(df['timestamp']).astype(int) / 10**9  # Convert to seconds
    model = IsolationForest(contamination=0.1)
    model.fit(df[['modification_time']])  # Using modification_time as the feature
    return model

def detect_security_log_modification_anomalies(model, df):
    df['modification_time'] = pd.to_datetime(df['timestamp']).astype(int) / 10**9  # Convert to seconds
    df['anomaly'] = model.predict(df[['modification_time']])  # Using modification_time as the feature
    return df

# Alteration of Database Records
def train_database_record_alteration_model(df):
    # Convert 'alteration_time' to datetime
    df['alteration_time'] = pd.to_datetime(df['alteration_time'])
    # Convert datetime to a numeric format (e.g., Unix timestamp)
    df['alteration_time'] = df['alteration_time'].astype(np.int64) // 10**9  # Convert to seconds

    model = IsolationForest(contamination=0.1)
    model.fit(df[['alteration_time']])  # Fit the model on the numeric timestamp
    return model


def detect_database_record_alteration_anomalies(model, df):
    # Convert 'alteration_time' to datetime
    df['alteration_time'] = pd.to_datetime(df['alteration_time'])
    # Convert datetime to a numeric format (e.g., Unix timestamp)
    df['alteration_time'] = df['alteration_time'].astype(np.int64) // 10**9  # Convert to seconds

    df['anomaly'] = model.predict(df[['alteration_time']])  # Modify based on your features
    return df

