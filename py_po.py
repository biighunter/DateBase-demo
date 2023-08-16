import subprocess
import psycopg2
from psycopg2 import OperationalError
import datetime

db_config = {
    'dbname': 'hunt',
    'user': 'biighunter',
    'password': '1122',
    'host': '146.190.26.15',
    'port': '5432',
}

backup_path = "/root/DateBase-demo/backup/"
# Construct the backup filename
current_date = datetime.date.today()
backup_filename = f'{current_date}_backup.sql'

def backup_database():
    try:
        # Connect to the remote PostgreSQL database
        connection = psycopg2.connect(**db_config)
        connection.autocommit = True
        print("Connected to the database")

        # Construct the pg_dump command
        pg_dump_command = [
            '/usr/bin/pg_dump',
            f'--dbname=postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["dbname"]}',
            f'--file={backup_path}/{backup_filename}',
        ]

        # Execute the pg_dump command
        subprocess.run(pg_dump_command, check=True)
        print("Backup completed successfully!")

    except OperationalError as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()
            print("Connection closed")

if __name__ == '__main__':
    backup_database()