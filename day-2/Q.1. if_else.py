print("check you profile")
he=int(input("enter your height in cm"))
if he>= 120:
    print ("you can ride")
    age=int(input("enter your age"))
    if age<=18:
         print("price is 20 rupee")
    elif age<=20:
         print("price is 30 rupee")
    else:
         print("price is 50 rupee")
else:
    print("you cant ride")
