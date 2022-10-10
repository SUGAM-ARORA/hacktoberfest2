import random
import time
import string

# Initial Steps to invite in the game:
print("\nWelcome to Hangman\n")
name = input("Enter your name: ")
print(f"Hello {name} ! Best of Luck!")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman!")
time.sleep(3)


# The parameters we require to execute the game:
def main():
    global count, display, word, already_guessed, length, play_game, original_word
    words_to_guess = ["january", "border", "image", "film",
                      "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
    original_word = random.choice(words_to_guess)
    word = original_word
    length = len(word)
    count = 0
    display = '_' * length + f' ({length} letters)'
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:


def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game.lower() not in ["y", "n"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

# Initializing all the conditions required for the game:


def hangman():
    global count, display, word, already_guessed, play_game, original_word
    limit = 5
    guess = input("This is the Hangman Word: " +
                  display + " Enter your guess: \n").lower()
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) > 1 or guess not in string.ascii_lowercase:
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in already_guessed:
        print("Try another letter.\n")

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    else:
        already_guessed.extend([guess])
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong guess. {limit - count} guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong guess. {limit - count} guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong guess. {limit - count} guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong guess. {limit - count} last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", original_word)
            print("Your gussies were:", already_guessed)
            play_loop()

    if word == '_' * length:
        print(
            f"Congrats! You have guessed the word ({original_word}) correctly in only {count} guesses!")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()
