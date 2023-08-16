import subprocess
import datetime
import psycopg2
import schedule
import time

# Database connection parameters
db_params = {
    'host': '146.190.26.15',
    'port': '5432',
    'database': 'postgresdb',
    'user': 'biighunter',
    'password': '1122'
}

# Backup settings
backup_dir = '/root/DateBase-demo/backup/'

# Create a backup
def create_backup():
    try:
        # Generate backup filename with timestamp
        backup_filename = f"backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.sql"

        # Connect to the database
        conn = psycopg2.connect(**db_params)
        conn.autocommit = True
        cursor = conn.cursor()

        # Generate backup command
        backup_command = [
            'pg_dump',
            f"--host={db_params['host']}",
            f"--port={db_params['port']}",
            f"--username={db_params['user']}",
            f"--dbname={db_params['database']}",
            f"--file={backup_dir}/{backup_filename}"
        ]

        # Execute the pg_dump command
        subprocess.run(backup_command, check=True)

        print("Backup created successfully:", backup_filename)

    except Exception as e:
        print("Error creating backup:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

# Schedule the backup to run daily at 6:00 PM
schedule.every().day.at("18:00").do(create_backup)

while True:
    schedule.run_pending()
    time.sleep(1)