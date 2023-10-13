import random

def deviner_nombre():
    nombre_secret = random.randint(1, 100)
    essais = 0

    print("Bienvenue dans le jeu de devinette de nombre !")
    print("Je pense à un nombre entre 1 et 100. Pouvez-vous deviner quel est ce nombre ?")

    while True:
        essais += 1
        essai = int(input("Entrez votre devinette : "))

        if essai < nombre_secret:
            print("Le nombre est plus grand. Essayez encore.")
        elif essai > nombre_secret:
            print("Le nombre est plus petit. Essayez encore.")
        else:
            print(f"Bravo ! Vous avez deviné le nombre en {essais} essais.")
            break

if __name__ == "__main__":
    deviner_nombre()