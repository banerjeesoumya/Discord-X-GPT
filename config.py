import configparser

def get_bot_token():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get('Bot', 'bot_token')

def get_API():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get('API', 'api_key')