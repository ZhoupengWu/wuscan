from django.db import connections

DB = "default"

def crea_tabella():
    with connections[DB].cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS scanner (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                colpo TEXT
            )
        """)

def aggiungi_nota(text: str, colpo: str):
    with connections[DB].cursor() as cur:
        cur.execute("""
            INSERT INTO scanner (text, colpo)
            VALUES (%s, %s)
        """, [text, colpo])

def leggi_note():
    with connections[DB].cursor() as cur:
        cur.execute("""
            SELECT * FROM scanner
        """)

        return cur.fetchall()

def stato():
    with connections[DB].cursor() as cur:
        cur.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = "table" AND name = %s
        """, ["scanner"])

        is_exist = cur.fetchone() is not None

        rows = 0

        if is_exist:
            cur.execute("SELECT COUNT(*) FROM scanner")
            rows = cur.fetchone()[0]

    return {"tabella": is_exist, "righe": rows}
