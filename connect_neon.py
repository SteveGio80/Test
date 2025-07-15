import psycopg2

try:
    conn = psycopg2.connect(
        dbname='neondb',
        user='neondb_owner',
        password='npg_0ECLzgxKnsi5',
        host='ep-frosty-shadow-aexobfx1-pooler.c-2.us-east-2.aws.neon.tech',
        port='5432',
        sslmode='require'
    )
    print("Connection successful!")

    with conn.cursor() as cursor:
        cursor.execute("SELECT current_database();")
        db_name = cursor.fetchone()[0]
        print(f"Connected to database: {db_name}")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'conn' in locals() and conn:
        conn.close()
        print("Connection closed.")
