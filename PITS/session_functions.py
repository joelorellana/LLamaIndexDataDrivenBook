

from global_settings import SESSION_FILE
import yaml
import os   


def save_session(state):
    """
    Saves the current state of the user to a yaml file.

    The state is a dictionary that contains the information about the user's
    current state in the application. This function takes the state as an
    argument and saves it to a yaml file.

    Args:
        state (dict): The current state of the user.

    Returns:
        None
    """
    # Create a copy of the state to be saved
    state_to_save = {key: value for key, value in state.items()}
    # Save the state to a yaml file
    with open(SESSION_FILE, 'w') as file:
        yaml.dump(state_to_save, file)

def load_session(state):
    """
    Loads the current state of the user from a yaml file.

    If the file does not exist, it returns False. If the file exists but is
    empty or if there is an error while loading the file, it also returns
    False.

    Args:
        state (dict): The current state of the user.

    Returns:
        bool: True if the session was loaded, False otherwise.
    """
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as file:
            try:
                # The yaml file might be empty, so we need to check if it
                # contains any data before loading it.
                loaded_state = yaml.safe_load(file)
                if loaded_state:
                    for key, value in loaded_state.items():
                        state[key] = value
                    return True
                else:
                    return False
            except yaml.YAMLError:
                # If there is an error while loading the file, we return False
                return False
    # If the file does not exist, we return False
    return False


def delete_session(state):
    """
    Deletes the session file and clears the current state of the user.

    This function is used when the user wants to start a new session. It
    deletes the session file and clears the current state of the user.

    Args:
        state (dict): The current state of the user.

    Returns:
        None
    """
    # Check if the session file exists
    if os.path.exists(SESSION_FILE):
        # Delete the session file
        os.remove(SESSION_FILE)
        # Clear the current state of the user
        for key in list(state.keys()):
            del state[key]
