secret_word = 'word'

guess_count = 1
guess = ''

print('Your hint is _ _ _ _')
guess = input('What is your guess? ').lower()
    
while guess != secret_word:
    print('Your hint is _ _ _ _')
    guess = input('What is your guess? ').lower()
    matching_letters = '' 
    
    if len(guess) == len(secret_word):
        for i in range(len(secret_word)):
            if secret_word[i] == guess[i]:
                matching_letters += secret_word[i]
        print(matching_letters)

    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")

    guess_count += 1
    
    if guess == secret_word:
        print('Congrats! You guessed it!')
        print(f'It took you {guess_count} guesses.')