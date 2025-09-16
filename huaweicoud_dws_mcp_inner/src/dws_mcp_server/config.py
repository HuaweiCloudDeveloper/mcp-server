import os


def get_config():
    config = {
        'host': os.getenv('DB_HOST', 'ip_address'),
        'port': os.getenv('DB_PORT', 'port_no'),
        'database': os.getenv('DB_NAME', 'database'),
        'user': os.getenv('DB_USER', 'username'),
        'password': os.getenv('DB_PWD', 'password')
    }
    return config
