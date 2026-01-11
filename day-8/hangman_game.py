import random
word=["apple","banana","grapes","mango","chickoo","strawberry"]
choosen_word=random.choice(word)
print(choosen_word)
guess=input("guess the letter: ").lower()
print(guess)
for letter in choosen_word:
    if letter==guess:
        print("correct")
    else:
        print("incorrect")