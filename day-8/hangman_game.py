import random
stages=[r'''
     _______
     |/      |
     |       O
     |      \|/
     |       |
     |      / \
     |
 ____|_____
=============
 ''',
 r'''
     _______
     |/      |
     |       O
     |      \|/
     |       |
     |      / 
     |
 ____|_____
 =============
 ''',
 r'''
    _______
     |/      |
     |       O
     |      \|/
     |       |
     |       
     |
 ____|_____
 =============
 ''',
 r'''
    _______
     |/      |
     |       O
     |      \|
     |       |
     |       
     |
 ____|_____
 =============
 ''',
 r'''
    _______
     |/      |
     |       O
     |       |
     |       |
     |       
     |
 ____|_____
 =============
 ''',
 r'''
    _______
     |/    |
     |          
     |       
     |       
     |       
     |
 ____|_____
 =============
''']

word_list=["apple","banana","grapes","mango","chickoo","strawberry"]

lives=6 

choosen_word=random.choice(word_list)
print(choosen_word)

placeholder=""
word_length= len(choosen_word)
for position in range (word_length):
    placeholder +="_"
print(placeholder)

game_over= False
correct_letter=[]

while not game_over:

    guess=input("guess the letter: ").lower()
    display = ""
    for letter in choosen_word:
        if letter==guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in choosen_word:
        lives-=1
        if lives== 0:
            game_over=True
            print("you loose,Try again")
    if "_" not in display:
        game_over = True
        print("you win")

    print(stages[lives-1])