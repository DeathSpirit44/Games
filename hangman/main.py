#!/usr/bin/env python3

"""Game that replicate the hangman in the terminal
"""

from random import *
from time import *
from os import *


def get_random_word(words, used_words):
    """genere un mort aleatoire depuis la liste de mots en evitant de reprendre un deja
    utilisé

    Args:
        words (list): liste des mots
        used_words (list): liste des mots deja utilisés

    Returns:
        str: mot tiré aléatoirement
    """
    length = len(words)-1
    word = choice(words)
    while word in used_words:
        word = choice(words)
    return word


def letter_input():
    """ return la lettre entrée par l'utilisateur et redemande tant que l'entrée n'est
    pas une lettre

    Returns:
        str: lettre entrée par l'utilisateur
    """
    print("Entrez une lettre:")
    value = input().lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    while len(value) != 1 or value not in letters:
        print("Entrez une lettre valide:")
        value = input()
    return value


def str_list(string):
    """transforme une chaine de caractère en liste dont chaque element est une lettre

    Args:
        string (str): chaine de caractère

    Returns:
        list: liste associée à la chaine de caractère
    """
    liste = []
    liste.extend(string)
    return liste


def list_str(liste):
    """transforme une liste en chaine de caracère

    Args:
        liste (list): liste à convertir en str

    Returns:
        str: chaine associée à la liste
    """
    string = "".join(liste)
    return string


def update_guessed(mot, lettre, secret_word):
    """met à jour qui doit être afficher

    Args:
        mot (list): liste contenant le mot à afficher
        lettre (str): lettre qui est ajouter ou non au mot
        secret_word (str): mot à deviner

    Returns:
        list: liste contenant le mot mis à jour
    """
    good = False
    for index, letter in enumerate(secret_word):
        if lettre == letter:
            mot[index] = lettre
            good = True
    return mot, good


def process_letter(secret_word, missed_letter, hit_letter, current_word, current_nb):
    """_summary_

    Args:
        secret_word (_type_): _description_
        missed_letter (_type_): _description_
        hit_letter (_type_): _description_
        current_word (_type_): _description_
        current_nb (_type_): _description_

    Returns:
        _type_: _description_
    """
    current_letter = letter_input()
    while current_letter in (missed_letter + hit_letter):
        print("Vous avez deja essayer cette lettre, essayez une autre!")
        current_letter = letter_input()
    current_liste = str_list(current_word)
    current_liste, good = update_guessed(
        current_liste, current_letter, secret_word)
    current_word = list_str(current_liste)
    if good:
        hit_letter.append(current_letter)
    else:
        current_nb += 1
        missed_letter.append(current_letter)
    return current_word, current_nb


def get_number():
    """fonction qui récupère un nombre sur l'entree standard et reessaie tant que l'entree
    n'est pas un nombre

    Returns:
        int: nombre valide
    """
    value = input()
    while not value.isnumeric():
        print("Entrez un nombre")
        value = input()
    return int(value)


def start_game(first):
    """fonction qui gere l'affichage et la gestion du debut du jeu

    Returns:
        bool: True pour yes et false pour non
    """
    if first:
        print("WELCOME TO")
        sleep(1)
        print("THE HANGMAN")
        sleep(1)
        print("Play ? (yes or no)")
    else:
        print()
        print("Play again ? (yes or no)")
    entry = input().lower()
    answer = ["yes", "no", "y", "n"]
    while entry not in answer:
        print("Play ? (yes or no), enter a valid input")
        entry = input().lower()
    if entry in ["yes", "y"]:
        system("clear")
        return True
    system("clear")
    print("BYE")
    sleep(2)
    system("clear")
    return False


def display(liste_pendu, word, index, missed_letters):
    """affiche le pendu dans son état actuel

    Args:
        liste_pendu (list): liste contenant tous les affichages du pendu
        word (str): mot en cours
        index (int): index de l'image du pendu à afficher
        missed_letters (list): liste contenant toutes les lettres ayant échouées
    """
    system("clear")
    print(liste_pendu[index])
    print(f"word: {word}")
    print("Missed letters : ", end="")
    for lettre in missed_letters:
        print(lettre, end=" ")
    print()


def set_parameters():
    """fonction qui recupere depuis l'entree standard la difficulte et le set de mot

    Args    Returns:
        tuple(liste, liste): tuple contenant une liste d'image et une liste de mot
    """
    hangman_pic = ['''
        +
        |
        |
        |
       ===''', '''
       -+
        |
        |
        |
       ===''', '''
      --+
        |
        |
        |
       ===''', '''
     ---+
        |
        |
        |
       ===''', '''
    +---+
        |
        |
        |
       ===''', '''
    +---+
   [    |
        |
        |
       ===''', '''
    +---+
   [ ]  |
        |
        |
       ===''', '''
    +---+
   [0]  |
        |
        |
       ===''', '''
    +---+
   [0]  |
    |   |
        |
       ===''', '''
    +---+
   [0]  |
   /|   |
        |
       ===''', '''
    +---+
   [0]  |
   /|\  |
        |
       ===''', '''
    +---+
   [0]  |
   /|\  |
   /    |
       ===''', '''
    +---+
   [0]  |
   /|\  |
   / \  |
       ===''']
    level1_pics = hangman_pic
    level2_pics = hangman_pic[3:]
    level3_pics = hangman_pic[::2]
    difficulty = {1: level1_pics, 2: level2_pics, 3: level3_pics}

    nourriture = """tacos kebab pizza brioche poulet nuggets croissant lasagnes nutella
                boeuf churros patate pates poisson naan burger""".split()
    transports = """avion bateau peniche voiture train velo helicoptere skate trotinette """.split()
    animaux = """chevre vache girafe elephant antilope lion moustique abeille papillon dauphin
                baleine
                lynx """.split()
    divinite = """zeus, odin, athena, poseidon, thor, tyr, mars, kratos, aphrodite, hephaistos,
                baldur, loki
                """.split()
    categories = {1: ("nourriture", nourriture), 2: ("transports", transports),
                  3: ("animaux", animaux), 4: ("divinités", divinite)}

    len_diff = len(difficulty)
    print(f"choose difficulty between 1 and {len_diff}")
    diff = get_number()
    while diff not in range(1, len_diff+1):
        print(f"Entrez une valeur comprise entre 1 et {len_diff}")
        diff = get_number()
    system("clear")
    print("Categories disponibles :")
    for key, value in categories.items():
        print(f"{key} {value[0]}")
    print("Entrez le numéro de la categorie")
    categorie = get_number()
    len_categories = len(categories)
    while categorie not in range(1, len_categories+1):
        print(f"Entrez une valeur comprises entre 1 et {len_categories} ")
        categorie = get_number()
    return difficulty[diff], categories[categorie][1]


def main():
    """MAIN
    """
    used_word = []
    first_run = True
    system("clear")
    while True:
        if not start_game(first_run):
            return
        hangman_pic, words = set_parameters()
        first_run = False
        secret_word = get_random_word(words, used_word)
        used_word.append(secret_word)
        missed_letter = []
        hit_letter = []
        current_word = "_"*len(secret_word)
        current_nb = 0
        while current_nb < len(hangman_pic)-1:
            display(hangman_pic, current_word, current_nb, missed_letter)
            current_word, current_nb = process_letter(secret_word, missed_letter,
                                                      hit_letter, current_word, current_nb)
            if "_" not in current_word:
                system("clear")
                print("YOU WIN")
                sleep(2)
                break
        if "_" in current_word:
            system("clear")
            print(" +---+")
            sleep(0.1)
            print("[0]  |")
            sleep(0.1)
            print("/|\  |")
            sleep(0.1)
            print("/ \  |")
            sleep(0.1)
            print("    ===")
            print("")
            sleep(0.4)
            print("YOU LOSE")
            sleep(0.4)
            print(f"The word was: {secret_word}")
            sleep(1)


if __name__ == "__main__":
    main()
