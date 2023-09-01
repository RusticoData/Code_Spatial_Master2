# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Initialisation des plateaux de jeu pour les joueurs Nord et Sud
N = [2] * 16
S = [2] * 16

# Fonction pour afficher les plateaux de jeu
def affiche(N, S):
    for i in range(8):
        print(N[i], end=" ")  # Affiche la ligne externe du joueur Nord
    print()
    for i in range(15, 7, -1):
        print(N[i], end=" ")  # Affiche la ligne interne du joueur Nord
    print()
    for i in range(15, 7, -1):
        print(S[i], end=" ")  # Affiche la ligne interne du joueur Sud
    print()
    for i in range(8):
        print(S[i], end=" ")  # Affiche la ligne externe du joueur Sud
    print('\n- - - - - -')

def semer(graines, position, plateau):
    # On initialise i à la position de départ
    i = position
    # On continue tant qu'il reste des graines à semer
    while graines > 0:
        i = (i - 1) % 16  # On calcule la prochaine position (circulaire), 
                                # maintenant dans le sens inverse des aiguilles d'une montre
        plateau[i] += 1   # On sème une graine à la position i
        graines -= 1      # On décrémente le nombre de graines restantes
    return i              # On retourne la position de la dernière graine semée


def jouer(position, N, S, tour_N):
    if tour_N:
        while not 0 <= position <= 7:  # Ajoute une vérification pour le joueur Nord
            position = int(input("Choix invalide. Veuillez choisir une case entre 0 et 7: "))
        graines = N[position]
        N[position] = 0
        derniere_position = semer(graines, position, N)
        # Vérifie si la dernière graine a été semée dans une case vide
        if N[derniere_position] == 1:
            return
        # Sinon, continue à semer
        while N[derniere_position] > 1:
            graines = N[derniere_position]
            N[derniere_position] = 0
            derniere_position = semer(graines, derniere_position, N)
    else:
        while not 0 <= position <= 7:  # Ajoute une vérification pour le joueur Sud
            position = int(input("Choix invalide. Veuillez choisir une case entre 0 et 7: "))
        position = (position + 8) % 16  # Ajuste la position pour le joueur Sud
        graines = S[position]
        S[position] = 0
        derniere_position = semer(graines, position, S)
        # Vérifie si la dernière graine a été semée dans une case vide
        if S[derniere_position] == 1:
            return
        # Sinon, continue à semer
        while S[derniere_position] > 1:
            graines = S[derniere_position]
            S[derniere_position] = 0
            derniere_position = semer(graines, derniere_position, S)

def partie(N, S):
    joueur_N = input("Entrez le prénom du joueur Nord: ")
    joueur_S = input("Entrez le prénom du joueur Sud: ")
    tour_N = True  # Le joueur Nord commence
    while True:
        affiche(N, S)
        if tour_N:
            print(f"C'est le tour de {joueur_N}.")
        else:
            print(f"C'est le tour de {joueur_S}.")
        position = int(input("Entrez la position de la case que vous voulez jouer: "))
        jouer(position, N, S, tour_N)
        # Vérifie si le jeu est terminé
        if sum(N[8:]) == 0:
            print(f"{joueur_S} a gagné!")
            return
        elif sum(S[:8]) == 0:
            print(f"{joueur_N} a gagné!")
            return
        tour_N = not tour_N  # Change le tour

partie(N, S)