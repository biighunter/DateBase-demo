import psycopg2

db_host = "146.190.26.15"
db_port = "5432"
db_database = "postgresdb"
db_user = "biighunter"
db_pass = "1122"

conn = psycopg2.connect(dbname=db_database, user=db_user, password=db_pass, host=db_host, port=db_port)

conn.close()