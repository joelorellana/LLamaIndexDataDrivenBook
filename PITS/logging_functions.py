from datetime import datetime
from global_settings import LOG_FILE
import os

def log_action(action, action_type):
    """
    Logs a user action to a file.

    The format of the log entry is:
    timestamp: action_type: action

    Args:
        action (str): The action to be logged.
        action_type (str): The type of the action to be logged.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp}: {action_type} : {action}\n"
    with open(LOG_FILE, 'a') as file:
        # Write the log entry to the file
        file.write(log_entry)


def reset_log():
    """
    Resets the log file to an empty string.
    """
    with open(LOG_FILE, 'w') as file:
        file.truncate(0) # this truncates the file to 0 bytes