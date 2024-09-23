"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Olivier Hamel (Matricule1), Nom2 (Matricule2)
"""

import csv

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

collection_bibliotheque_csvfile = open('collection_bibliotheque.csv', newline='')
reader_collection_bibliotheque = csv.DictReader(collection_bibliotheque_csvfile)

bibliotheque = {}

for ligne in reader_collection_bibliotheque :
    bibliotheque[ligne['cote_rangement']] = {
            "titre": ligne['titre'],
            "auteur": ligne['auteur'],
            "date_publication": ligne['date_publication']
        }

print(f' \n Bibliotheque initiale : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

nouvelle_collection_csvfile = open('nouvelle_collection.csv', newline='')
reader_nouvelle_collection = csv.DictReader(nouvelle_collection_csvfile)

for ligne in reader_nouvelle_collection : 
    if ligne['cote_rangement'] not in bibliotheque : # On vérifie avec la cote de rangement si le livre est déjà présent dans la bibliothèque
        bibliotheque[ligne['cote_rangement']] = {
            "titre": ligne['titre'],
            "auteur": ligne['auteur'],
            "date_publication": ligne['date_publication']
        }
        print(f"Le livre {ligne['cote_rangement']} ---- {ligne['titre']} par {ligne['auteur']} ---- a été ajouté avec succès")
    else :
        print(f"Le livre {ligne['cote_rangement']} ---- {ligne['titre']} par {ligne['auteur']} ---- est déjà présent dans la bibliothèque")


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

for cote in list(bibliotheque.keys()):
    if cote.startswith('S'):
        bibliotheque['W' + cote] = {
            "titre": bibliotheque[cote]['titre'],
            "auteur": bibliotheque[cote]['auteur'],
            "date_publication": bibliotheque[cote]['date_publication']
        }
        del bibliotheque[cote]

print(f'\nBibliotheque avec modifications de cote : {bibliotheque}\n')

########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






