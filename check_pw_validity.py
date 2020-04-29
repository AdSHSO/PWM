import admin
import configparser

config = configparser.ConfigParser()
config.read('project_config.ini')
RULE_FILE_PATH = config['DEV']['GLOBAL_RULES']

def check(password):
    config_data = admin.read_config(RULE_FILE_PATH)
    minimal_length = config_data["mandatory_complexity"]["minimal_length"]
    if len(password) > minimal_length:
        return True
    else:
        return False
