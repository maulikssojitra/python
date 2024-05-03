import random
from hangman_word import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
print(f"The solution is {chosen_word}.")

display = []
for i in range(len(chosen_word)):
    display.append("_")

lives = 6
isFalse = False
while not isFalse:
    guess = input("guess the latter : ").lower()
    
    if guess in display:
        print(f"You've alredy guessed {guess}")
    
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in word. You lose a life.")
        lives -= 1
        if lives == 0:
            isFalse = True
            print("You lose")
        
    print(display)
    
    if "_" not in display:
        isFalse = True
        print("You win")
    
    print(stages[lives])
    