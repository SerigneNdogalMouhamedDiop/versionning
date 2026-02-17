from base_de_donnees import connect_db
from datetime import datetime

def ajouter_depense():
    type_depense = input("Type de dépense: ")
    montant = float(input("Montant: "))
    date = datetime.now().strftime("%Y-%m-%d")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO depenses (type, montant, date) VALUES (?, ?, ?)",
                   (type_depense, montant, date))
    conn.commit()
    conn.close()
    print("Dépense ajoutée !")
