from django.db import connections

DB = "default"

def crea_tabella():
    with connections[DB].cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS scanner (
                id INTEGER not null PRIMARY KEY,
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
