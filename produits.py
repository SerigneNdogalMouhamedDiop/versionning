from base_de_donnees import connect_db

def ajouter_produit():
    nom = input("Nom produit: ")
    prix = float(input("Prix: "))
    stock = int(input("Stock: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produits (nom, prix, stock) VALUES (?, ?, ?)",
                   (nom, prix, stock))
    conn.commit()
    conn.close()
    print("Produit ajouté !")

def afficher_produits():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produits")
    produits = cursor.fetchall()
    conn.close()

    for prod in produits:
        print(prod)
print("Ceci est un test")
