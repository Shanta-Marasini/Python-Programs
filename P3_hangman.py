import random

def hangman():
    wordList = ['hello', 'heist','homework','anchorite']
    word = random.choice(wordList)
    guessmade = ''
    turns = 10

    while len(word) > 0:
        main = ''

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + '_' + ' '       #main is formed here _____

        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:", main)
        guess = input()

        while True:
            if guess in guessmade:
                print('you already guessed this one')
                guess = input('enter next letter:')
            else:
                break

        while True:
            if guess.isalpha():
                guessmade += guess
                break
            else:
                print("Enter a valid character")
                guess = input()


        if guess not in word:
            turns = turns - 1
            print('wrong guess')

            if turns == 9:
                print('you have 9 attempts left')

            if turns == 8:
                print('You have 8 attempts left')
                print('      0      ')

            if turns == 7:
                print('You have 7 attempts left')
                print('      0      ')
                print('      |      ')

            if turns == 6:
                print('You have 6 attempts left')
                print('      0      ')
                print('      |      ')
                print('     /        ')

            if turns == 5:
                print('You have 5 attempts left')
                print('      0      ')
                print('      |      ')
                print('     / \\    ')

            if turns == 4:
                print('You have 4 attempts left')
                print('    \\ 0      ')
                print('      |      ')
                print('     / \\    ')

            if turns == 3:
                print('You have 3 attempts left')
                print('    \\ 0 /    ')
                print('      |      ')
                print('     / \\    ')

            if turns == 2:
                print('You have 2 attempts left')
                print('    \\ 0 /  | ')
                print('      |      ')
                print('     / \\    ')

            if turns == 1:
                print('You have 1 attempts left')
                print('    \\ 0 /_|  ')
                print('      |      ')
                print('     / \\    ')

            if turns == 0:
                print(f'You could not guess the word {word},made innocent die.')
                print('      0 _|   ')
                print('    / | \\   ')
                print('     / \\    ')
                break




    else:
        print('You could not make the correct guess')




name = input('Enter your name: ')
print(f'Hi {name}')
print('--------------')
print('Try to guess in less than 10 times')
hangman()





