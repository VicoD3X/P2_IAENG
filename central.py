

def calculer_et_afficher_perimetre():
    """
    Cette fonction demande à l'utilisateur de saisir les longueurs des trois côtés
    d'un triangle et affiche le périmètre du triangle.
    """
    cote1 = float(input("Entrez la longueur du côté 1 : "))
    cote2 = float(input("Entrez la longueur du côté 2 : "))
    cote3 = float(input("Entrez la longueur du côté 3 : "))

    perimetre = cote1 + cote2 + cote3
    print(f"Le périmètre du triangle est : {perimetre}")

calculer_et_afficher_perimetre()