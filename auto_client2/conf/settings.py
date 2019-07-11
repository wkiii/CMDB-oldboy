import os
import logging

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENGINE = 'agent'
# ENGINE = 'ssh'
# ENGINE = 'salt'

ENGINE_DICT = {
    'agent': 'src.engine.agent.AgentHandler',
    'ssh': 'src.engine.ssh.SSHHandler',
    'salt': 'src.engine.salt.SaltHandler',
}

PLUGINS_DICT = {
    'basic': 'src.plugins.basic.Basic',
    'disk': 'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'nic': 'src.plugins.nic.NIC',
    'cpu': 'src.plugins.cpu.Cpu',
    'main_board': 'src.plugins.main_board.MainBoard',

}

DEBUG = True
FILE_PATH = os.path.join(BASE_PATH, 'files')

# ################## ssh配置 ##########################

SSH_PRIVATE_KEY = '私钥路径'
SSH_PORT = 22
SSH_USER = '用户名'

ASSET_URL = 'http://127.0.0.1:8000/api/asset/'

# ################## 日志配置 ##########################

LOGGER_PATH = os.path.join(BASE_PATH, 'log', 'cmdb.log')
LOGGER_NAME = 'cmdb'
LOGGER_LEVEL = logging.DEBUG

CERT_PATH = os.path.join(BASE_PATH, 'conf', 'cert')

KEY = 'caorui'

PUB_KEY = b'LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JR0pBb0dCQUpiaHVrZEhsVUNsazJlVHFITzVQMXNndGJLWmlYUEtKZkZPeEhWTlR6UDZ0YnZFVWJBRFZhd08Kdko2T2U5SmJYcFhoZk15U3VkbEcyZXJRYmNsVldTVVNMUzRuV3pwQnllZlRQTlQ4cU9ndkZ5aGxRZ3BYTzYycwo1R0EvMG03T0VsZ3hTb3BnVFU2OEFMWnJHc0hSL3VSVzRLZXdxdkRPZVB4VzJNUU5ZQjloQWdNQkFBRT0KLS0tLS1FTkQgUlNBIFBVQkxJQyBLRVktLS0tLQo='


LENGTH = 1024
RSA_LENGTH = int(LENGTH / 8)
ENABLE_LENGTH = RSA_LENGTH - 11