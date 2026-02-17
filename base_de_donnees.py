import sqlite3

def connect_db():
    conn = sqlite3.connect("entreprise.db")
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Table employés
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        poste TEXT,
        salaire REAL,
        date_embauche TEXT
    )
    """)

    # Table produits
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prix REAL,
        stock INTEGER
    )
    """)

    # Table ventes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produit_id INTEGER,
        quantite INTEGER,
        total REAL,
        date TEXT,
        FOREIGN KEY (produit_id) REFERENCES produits(id)
    )
    """)

    # Table dépenses
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS depenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        montant REAL,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()
