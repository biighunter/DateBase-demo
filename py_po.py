import subprocess
import datetime
import psycopg2

# Database connection parameters
db_params = {
    'host': '146.190.26.15',
    'port': '5432',
    'database': 'postgresdb',
    'user': 'biighunter',
    'password': '1122'
}

# Backup settings
backup_dir = '/path/to/backup/directory'
backup_filename = f"backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.sql"

# Create a backup
def create_backup():
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        conn.autocommit = True
        cursor = conn.cursor()

        # Run pg_dump command to create a backup
        backup_path = f"{backup_dir}/{backup_filename}"
        dump_command = [
            'pg_dump',
            f"--host={db_params['host']}",
            f"--port={db_params['port']}",
            f"--username={db_params['user']}",
            f"--dbname={db_params['database']}",
            f"--file={backup_path}"
        ]

        subprocess.run(dump_command, check=True)

        print("Backup created successfully:", backup_path)

    except Exception as e:
        print("Error creating backup:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    create_backup()