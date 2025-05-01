import psycopg2

try:
    connection = psycopg2.connect(
        database="my_litellm_db",
        user="litellm_user",
        password="litellm",
        host="localhost",
        port="5432",
    )

    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()

    print("Connected to PostgreSQL DB Version:", version)
except Exception as e:
    print("Connection error:", e)
finally:
    if connection:
        cursor.close()
        connection.close()
