import requests

API_URL = "https://official-joke-api.appspot.com/random_joke"


def get_joke():
    """Recupere une blague aleatoire depuis l'API."""

    try:
        response = requests.get(API_URL, timeout=10)

        response.raise_for_status()

        joke = response.json()

        print("\n===== VOTRE BLAGUE =====")
        print("Categorie :", joke["type"])
        print()
        print(joke["setup"])
        print(joke["punchline"])
        print()
        print("ID :", joke["id"])

    except requests.exceptions.RequestException:
        print("\nErreur : impossible de contacter l'API.")
        print("Verifiez votre connexion Internet.")

    except (KeyError, ValueError):
        print("\nErreur : les donnees recues sont invalides.")


def main():
    """Menu principal de l'application."""

    print("==============================")
    print("       RANDOM JOKE APP")
    print("==============================")

    while True:
        print("\n1. Obtenir une blague")
        print("2. Quitter")

        choice = input("\nVotre choix : ")

        if choice == "1":
            get_joke()

        elif choice == "2":
            print("\nMerci d'avoir utilise Random Joke App !")
            print("Au revoir.")
            break

        else:
            print("\nChoix invalide. Veuillez entrer 1 ou 2.")


if __name__ == "__main__":
    main()
