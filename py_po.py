import os
import time

# Database details
DB_HOST = '146.190.26.15'
DB_USER = 'biighunter'
DB_PASS = '1122'
DB_NAME = 'postgresdb'

# Backup details
BACKUP_PATH = '/root/DateBase-demo/backup/'
TIMESTAMP = time.strftime('%Y-%m-%d-%H-%M-%S')
BACKUP_FILE = DB_NAME + '_' + TIMESTAMP + '.sql'

# Command to take a backup
BACKUP_CMD = "pg_dump -h {0} -U {1} -d {2} > {3}".format(DB_HOST, DB_USER, DB_NAME, os.path.join(BACKUP_PATH, BACKUP_FILE))

# Execute the backup command
os.system(BACKUP_CMD)