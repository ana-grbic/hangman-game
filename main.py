import random

words = ["banana", "apple", "pear", "pineapple", "kiwi", "mango", "lemon", "peach", "melon", "apricot"]

def main():
    game_running = True
    chosen_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    print("Welcome to hangman!")
    print("Guess a letter in the word or if you think you know what word it is, guess the word!")
    print("Here is the secret word:")
    
    while game_running:
        print_word(chosen_word, guessed_letters)
        game_running = guess(chosen_word, guessed_letters, wrong_guesses)
        if (is_word_filled(chosen_word, guessed_letters)):
            print("Congratulations! The word was " + chosen_word + ".")
            game_running = False
        
    user_input = input("Would you like to play again? ")
    if user_input.lower() == "yes":
        main()
        
def print_word(chosen_word, guessed_letters):
    current_word = []
    i = 0
    for i in range(len(chosen_word)):
        if chosen_word[i] in guessed_letters:
            current_word.append(chosen_word[i])
        else:
            current_word.append("_")
    for l in current_word:
        print(l + " ", end = "")
    print("")
    
def guess(chosen_word, guessed_letters, wrong_guesses):
    guess = input("Guess: ")
    
    if guess in guessed_letters:
        print("You already guessed " + guess + ".")
        return True
    
    if len(guess) == 1:
        in_word_count = chosen_word.count(guess)
            
        if in_word_count > 0:
            print("Correct! The letter " + guess + " is IN the secret word!")
        else:
            print("Wrong! The letter " + guess + " is not in the word. Try again.")
            wrong_guesses += 1
        guessed_letters.append(guess)
            
    else:
        if guess == chosen_word:
            print("Congratulations! The word was " + chosen_word + ".")
            return False
        else:
            print("Wrong! Try again.")
            wrong_guesses += 1
    
    if (continue_game(wrong_guesses)):
        return True
    else:
        return False

def continue_game(wrong_guesses):
    if wrong_guesses >= 8:
        print("You guessed wrong too many times.")
        print("Game Over")
        return False
    else:
        return True
    
def is_word_filled(chosen_word, guessed_letters):
    for i in range(len(chosen_word)):
        if chosen_word[i] not in guessed_letters:
            return False
    return True
        
if __name__ == "__main__":
    main()