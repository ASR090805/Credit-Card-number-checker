import random

hangman_art = {0:('   ',
                   '   ',
                   '   '),
               1:(' 0 ',
                  '   ',
                  '   '),
               2:(' 0 ',
                  ' | ',
                  '   '),
               3:(' 0 ',
                  '/| ',
                  '   '),
               4:(' 0 ',
                  '/|\\',
                  '   '),
               5:(' 0 ',
                  '/|\\',
                  '/  '),
               6:(' 0 ',
                  '/|\\',
                  '/ \\')}

def hangman(wrong_guess):
    print('******************')
    for line in hangman_art[wrong_guess]:
        print(line)
    print('******************')

def hint_fun(hint):
    print(' '.join(hint))

def display_answer(answer):
    print(' '.join(answer))

words = ['messi', 'ronaldo', 'neymar', 'zidane', 'buffon']
answer_word = random.choice(words)
hint = ['_'] * len(answer_word)
wrong_guess = 0
max_wrong = 6
guessed_letter = set()
is_running = True

while is_running:
    hangman(wrong_guess)
    hint_fun(hint)
    guess = input('enter a letter: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('invalid input')
        continue

    if guess in guessed_letter:
        print(f'already guessed: {guess}')
        continue

    guessed_letter.add(guess)

    if guess in answer_word:
        for i in range(len(answer_word)):
            if guess == answer_word[i]:
                hint[i] = guess
        if '_' not in hint:
            hangman(wrong_guess)
            display_answer(answer_word)
            print('you win')
            is_running = False
    else:
        wrong_guess += 1
        if wrong_guess >= max_wrong:
            hangman(wrong_guess)
            print(f'you lose! the word was: {answer_word}')
            is_running = False