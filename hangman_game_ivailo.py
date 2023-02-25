import random
import string
import sys, time


def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    return ""


def typewriter2(message2):
    for char in message2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    return ""


def main_menu():
    print()
    print()
    print("**************************************")
    print(typewriter2("*  1.➼ Easy [max.4 letters words]    *"))
    print(typewriter2("*  2.➼ Medium [6 letters words]      *"))
    print(typewriter2("*  3.➼ Hard  [8 letters words]       *"))
    print(typewriter2("*  4.➼ Expert [12 letters words]     *"))
    print(typewriter2("*  5.➼ Rules                         *"))
    print(typewriter2("*  6.➼ Exit                          *"))
    print("***************************************")
    return


def hangman_lifes(index_life):
    if index_life == 14:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|\  | ')
        print('        / \  | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 13:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|\  | ')
        print('        /    | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 12:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|\  | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 11:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|   | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 10:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('         |   | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 9:
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 8:
        print('         _____ ')
        print('         |   | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 7:
        print('         _____ ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 6:
        print('               ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 5:
        print('               ')
        print('               ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 4:
        print('               ')
        print('               ')
        print('               ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 3:
        print('               ')
        print('               ')
        print('               ')
        print('               ')
        print('             | ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 2:
        print('               ')
        print('               ')
        print('               ')
        print('               ')
        print('               ')
        print('             | ')
        print('     ________|_')
        return
    if index_life == 1:
        print('               ')
        print('               ')
        print('               ')
        print('               ')
        print('               ')
        print('               ')
        print('     ________|_')
        return


def easy_level():
    # 4 letters words
    easy_level_words = ["book", "pen", "car", "dice", "face", "mask", "cost", "palm", "aloe", "game", "barn", "bake",
                        "base", "cafe", "joke", "lady", "mass", "olio", "onyx", "open"]

    randomized_easy_word = random.choice(easy_level_words)

    return randomized_easy_word


def medium_level():
    # 6 letters words
    medium_level_words = ["doctor", "friend", "banker", "police", "market", "school", "policy", "office", "person",
                          "course", "system", "petrol", "raffle", "vacuum"]
    randomized_medium_level = random.choice(medium_level_words)

    return randomized_medium_level


def hard_level():
    # 8 letters words
    hard_level_words = ["interest", "position", "industry", "research", "minister", "evidence", "question", "language",
                        "business", "magazine", "elephant", "notebook"]

    randomized_hard_words = random.choice(hard_level_words)

    return randomized_hard_words


def expert_level():
    # 12 letters words
    expert_level_words = ["unemployment", "organisation", "conversation", "relationship", "introduction",
                          "contribution", "organization", "distribution", "construction", "grandmother", "magnetomotor"]
    randomized_expert_words = random.choice(expert_level_words)

    return randomized_expert_words


def hangman(rndmized_word):
    word = rndmized_word
    word_letter = set(rndmized_word)
    used_letters = set()
    legit_symbols = set(string.ascii_lowercase)
    lifes = 0
    remaining_lifes = 14

    while len(word_letter) > 0:
        if lifes == 14:
            print("*** Game Over ***")
            print("** You died ! **")
            print(f" The word was: | {word.upper()} |")

            print()

            break

        # input letter
        player_letters_input = input("Guess the word: ").lower()

        if player_letters_input in used_letters:
            print("-----------------------------------------------")
            print(f'Already used letter.Dont use used letters ! :)')
            print("Try again !")
            print("-----------------------------------------------")
            continue

        if player_letters_input in legit_symbols:
            used_letters.add(player_letters_input)
            lifes += 1
            remaining_lifes -= 1

            if player_letters_input in word_letter:
                word_letter.remove(player_letters_input)
                lifes -= 1
                remaining_lifes += 1
            hangman_lifes(lifes)

        if len(player_letters_input) > 1:
            print('-------------------------------------')
            print("Please input letter by letter only ! ")

            print("-------------------------------------")

        elif player_letters_input not in legit_symbols:
            print("--------------------------------")
            print("Invalid character.Try again ! :)")
            print("Input letter from alphabet !")
            print("--------------------------------")

        if len(word_letter) == 0:
            print("----------------------------------")
            print("   Congratulations !   ")
            print(f'The word is : | {(word).upper()} |')
            print("Perfect ! You guessed the word. :)")
            print(f"Number of tries : {lifes}")
            print("----------------------------------")

            break
        # current word is[-a-s] example
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print()
        print(f'➡ Current word: {" ".join(word_list)} ')

        # Used letters print
        print()
        print(f"➡ Already used letters: | {', '.join(used_letters)} | ")
        print()
        print(f"➡ Remaining lives: {remaining_lifes}")
        print("--------------------------------")


print('      ____________________')
print(typewriter('      |      Hangman     |'))
print(typewriter('      |  by Ivailo Ivanov |'))
print('      ____________________')
print()
print("**************************************")
print(typewriter(" *    Game content only nouns       *"))
print("**************************************")
print(typewriter("*  1.➼ Easy [max.4 letters words]    *"))
print(typewriter("*  2.➼ Medium [6 letters words]      *"))
print(typewriter("*  3.➼ Hard  [8 letters words]       *"))
print(typewriter("*  4.➼ Expert [12 letters words]     *"))
print(typewriter("*  5.➼ Rules                         *"))
print(typewriter("*  6.➼ Exit                          *"))
print("***************************************")

while True:

    print()
    print("•••••••••••••••••••••")
    command = input("‣‣‣ Choose command:  ")
    print("•••••••••••••••••••••")

    if command == "1":
        print()
        print("* You choosed - | Easy level | *")
        print()

        print(f"_ " * len(easy_level()), end="")
        print("  --> 4 letters word !")
        print()

        hangman(easy_level())

        input("Press Enter for [ Main Menu ]")
        main_menu()


    elif command == "2":
        print()
        print("* You choosed - | Medium Level | *")
        print()

        print(f"_ " * len(medium_level()), end="")
        print("  --> 6 letters word !")
        print()

        hangman(medium_level())

        input("Press Enter for [ Main Menu ]")
        main_menu()


    elif command == "3":
        print()
        print("* You choosed - | Hard level | *")
        print()

        print(f"_ " * len(hard_level()), end="")
        print("  --> 8 letters word !")
        print()

        hangman(hard_level())

        input("Press Enter for [ Main Menu ]")
        main_menu()


    elif command == "4":
        print()
        print("* You choosed - | Expert level | *")
        print()

        print(f"_ " * len(expert_level()), end="")
        print("  --> 12 letters word !")
        print()

        hangman(expert_level())

        input("Press Enter for [ Main Menu ]")
        main_menu()


    elif command == "5":
        print()
        print("* You choosed - | Rules | *")
        print()
        print("    ---Rules---   ")
        print("1.You have 14 lives (in my hangman game).\n"
              "2.You have to guess the word ,letter by letter !\n"
              "3.If your man die,you loose ! \n"
              "4.You have to input only valid characters (letters from alphabet only).\n")

        input("Press Enter for [ Main Menu ]")
        main_menu()
        continue

    elif command == "6":

        print("Thanks . This is my Hangman game made by - Ivailo Ivanov")
        exit()

    else:
        print()
        print("Please insert valid command ! :)")
        print()
        print("Commands are from 1 - 6 !")

        main_menu()
        continue
