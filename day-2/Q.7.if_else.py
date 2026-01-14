bill=0

small_pizza=100 
medium_pizza=150
large_pizza=200
peepronie_small=20
peepronie_medium=40
peepronie_large=60
extra_cheese_small=40
extra_cheese_medium=80
extra_cheese_large=100


print("welcome 1sheka pizza")
pizza_size=str(input("what size of pizza do you want? 's' 'm' 'l'"))
if pizza_size=="s":
    bill+=100
elif pizza_size=="m":
    bill+=150
elif pizza_size=="l":
    bill+=200
else:
    print("pelese select your size properly")

peepronie=str(input("do you want pepporoine on your pizza"))
if peepronie=="y":
    if pizza_size=="s":
        bill+=20
    if pizza_size=="m":
        bill+=40
    if pizza_size=="l":
        bill+=60

extra_cheese=str(input("do you want extra cheese on your pizza"))
if extra_cheese=="y":
    if pizza_size=="s":
        bill+=40
    if pizza_size=="m":
        bill+=80
    if pizza_size=="l":
        bill+=100
print("your total bill is",bill)

print("thank you for order at 1sheka pizza")