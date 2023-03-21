import time
 
import oracledb
import sample_env

if not sample_env.get_is_thin():
 oracledb.init_oracle_client(lib_dir=sample_env.get_oracle_client())
print('1')

connection = oracledb.connect(user=sample_env.get_main_user(),
 password=sample_env.get_main_password(),
 dsn=sample_env.get_connect_string())

sprint('True')

print('test git')