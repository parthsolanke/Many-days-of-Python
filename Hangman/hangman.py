import random
import stages
import words

lives  = 6
notend = True
print(stages.logo)
chosen_word = random.choice(words.word_list)

hangman_list = []
for i in range(len(chosen_word)):
    hangman_list.append('_')
g = []    
while notend:
    guess = input("Guess a letter: ").lower()
    if guess in g:
      print(f"You've alredy entered {guess}")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            hangman_list[i] = guess
            g.append(guess)
  
    if guess not in chosen_word:
      print(f'The letter {guess} is not in the word, you lose a life')
      lives -= 1
    print(f"{' '.join(hangman_list)}")
         
    if lives == 0:
      print('You lose.')
      notend = False     
    if '_' not in hangman_list:
      print('You won!')
      notend = False
        
    print(stages.stages_lst[lives])   