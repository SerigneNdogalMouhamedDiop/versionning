from base_de_donnees import connect_db
from datetime import datetime

def ajouter_employe():
    nom = input("Nom: ")
    poste = input("Poste: ")
    salaire = float(input("Salaire: "))
    date = datetime.now().strftime("%Y-%m-%d")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employes (nom, poste, salaire, date_embauche) VALUES (?, ?, ?, ?)",
                   (nom, poste, salaire, date))
    conn.commit()
    conn.close()
    print("Employé ajouté avec succès !")

def afficher_employes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employes")
    employes = cursor.fetchall()
    conn.close()

    for emp in employes:
        print(emp)
