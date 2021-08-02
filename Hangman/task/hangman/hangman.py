# Write your code here
import random


def random_word():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    rand_word = random.choice(word_list)
    return rand_word


def word_check(a):
    if a == random_word():
        print("You survived!")
    else:
        print("You lost!")
    return


print("H A N G M A N")
print("The game will be available soon.")
user_guess = input("Guess the word: ")
word_check(user_guess)
