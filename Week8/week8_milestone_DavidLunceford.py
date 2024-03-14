secret_word = 'word'

# print("Welcome to the word game. The rules are simple: Start your guess by looking at how many letters the word has, shown by the underscores, and make a guess with the same amount of letters. If your answer is incorrect you will get hints to help you figure it out until you've guessed the right word. If your guess has more letters than the secret word you won't get a hint. Capital letters designate that your guess had the right letter in the right position in the word. Lowercase letters show that you guessed the right letters in your guess but they don't correspond to the right place in the actual secret word. ")

guess_count = 0
guess = ''

print('Your hint is _ _ _ _')

while guess != secret_word:
    guess = input('What is your guess? ').lower()
    print("Your guess is wrong, son! Try again!")
    guess_count = guess_count + 1
    if guess == secret_word:
        print('Congrats! You guessed it!')
        print(f'It took you {guess_count} guesses.')