#Step 1 
import random
import hangman_word
import hangman_art

word = random.choice(hangman_word.word_list)

empty=[]
l = len(word)

for w in word:
  empty.append("_")

print(hangman_art.logo,"\n")
print(f"{' '.join(empty)}\n")

end_of_game = False
lives = 6

while not end_of_game:

  guess = input("Guess a letter: ").lower()
  
  for x in range(0, l):
    letter = word[x] 
    if letter == guess:
      empty[x] = letter 
  
  print(f"{' '.join(empty)}","\n")
  
  if guess not in empty: 
    lives -=1
    print(hangman_art.stages[lives])
  
    if lives ==0:
      end_of_game =True
      
      print(hangman_art.lose)
  else:
    print(hangman_art.stages[lives])
        
  if "_" not in empty:
    end_of_game = True
    print(hangman_art.win)    