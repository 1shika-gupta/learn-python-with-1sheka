import random
word_list=["apple","banana","grapes","mango","chickoo","strawberry"]
choosen_word=random.choice(word_list)
print(choosen_word)
placeholder=""
word_length=len(choosen_word)
for position in range(word_length):
    placeholder +="_"
print(placeholder)
guess=input("guess the letter: ").lower()

display = ""
for letter in choosen_word:
    if letter==guess:
        display += letter
    else:
        display += "_"
print(display)