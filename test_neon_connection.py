import psycopg2

try:
    conn = psycopg2.connect(
        "host=ep-autumn-sea-aeyv34za-pooler.c-2.us-east-2.aws.neon.tech "
        "dbname=neondb user=neondb_owner password=npg_0ECLzgxKnsi5 port=5432 "
        "sslmode=verify-full sslrootcert=/etc/ssl/certs/ca-certificates.crt"
    )
    cur = conn.cursor()
    cur.execute('SELECT NOW();')
    print("Connected! Server time:", cur.fetchone()[0])
    cur.close()
    conn.close()
except Exception as e:
    print("Error connecting to NeonDB:", e)
