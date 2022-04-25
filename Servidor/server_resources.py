from psycopg2 import connect

def init_db():
    conn = connect(
        host="postgres",
        dbname="Tarea1",
        password="postgres",
        port=5432,
        user="postgres"
    )
    return conn