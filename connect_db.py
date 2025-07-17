import psycopg2

conn = psycopg2.connect(
    host="pg.neon.tech",
    port=5432,
    dbname="neondb",
    user="neondb_owner",
    password="npg_0ECLzgxKnsi5",
    sslmode="verify-full",
    sslrootcert="/etc/ssl/certs/ca-certificates.crt"
)

print("Connected successfully!")
conn.close()
