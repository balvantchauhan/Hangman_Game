import time
import random

# Initial steps to invite user into the game
print('Welcome to the Game of Hangman \n')
player_name = raw_input('Please enter your name : \n')
print('Hello ' + player_name + ' Best of luck!!!')
time.sleep(2)
print('The game is about to start. \nLet\'s play Hangman!!')
time.sleep(2)


def main():
    global word
    global length
    global display
    global already_guessed
    global play_game
    global count
    word_to_guess = [['january',
                      'Name of month'],
                     ['border',
                      'a line separating two countries, administrative divisions'],
                     ['image',
                      'a representation of the external form of a person or thing in art.'],
                     ['film',
                      'a story or event recorded by a camera as a set of moving images'],
                     ['promise',
                      'assure someone that one will definitely do something or that something will happen.'],
                     ['kids',
                      'a child or young person.'],
                     ['lungs',
                      'an open space in a town or city, where people can breathe fresher air.'],
                     ['doll',
                      'a small model of a human figure, typically one of a baby or girl, used as a child\'s toy.'],
                     ['rhyme',
                      'a short poem in which the sound of the word with that at the end of another.'],
                     ['damage',
                      'physical harm that impairs the value, usefulness, or normal function of something.'],
                     ['plants',
                      'a living organism of the kind exemplified by trees']]

    word = random.choice(word_to_guess)
    print('Here is the hint for the hangman word to guess, HINT is :\n' + word[1] + '\n')
    length = len(word[0])
    display = '_' * length
    already_guessed = []
    play_game = ''
    count = 0


def play_loop():
    global play_game
    play_game = raw_input('Do you want to play again? y = yes, n = no \n')
    while play_game not in ['Y', 'N', 'y', 'n']:
        play_game = raw_input('Do you want to play again? y = yes, n = no \n')
    if play_game == 'y':
        main()
        hangman()
    elif play_game == 'n':
        print('Thanks for playing! We expect you back again!')
        exit()


def hangman():
    global word
    global display
    global already_guessed
    global count
    global length
    limit = 5
    guess = raw_input('This is Hangman word :' + display + ' Enter your guess\n')
    guess = guess.strip()

    if len(guess) == 0 or len(guess) >= 2 or guess <= '9':
        print('Invalid input, Try a letter\n')
        hangman()

    elif guess in word[0]:
        already_guessed.extend([guess])
        index = word[0].find(guess)
        word[0] = word[0][:index] + '_' + word[0][index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + '\n')

    elif guess in already_guessed:
        print('Try another letter\n')
    else:
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
            print('Wrong guess.' + str(limit - count) + ' last guess remaining\n')
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess.' + str(limit - count) + ' last guess remaining\n')
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess.' + str(limit - count) + ' last guess remaining\n')
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess.' + str(limit - count) + ' last guess remaining\n')
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\\ \n"
                  "  |    / \\ \n"
                  "__|__\n")
            print('Wrong guess. You are hanged\n')
            print('The word was: ', already_guessed, word[0])
            play_loop()
    if word[0] == '_' * length:
        print('Congrats! You have guessed the word correctly!')
        play_loop()
    elif count != limit:
        hangman()


main()

hangman()
