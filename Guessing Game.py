from random import randint, random
for x in range(1, 8):
        gass_number=int(input("Enter your number:"))
        ramdom_number=randint(1,100)
        if gass_number==ramdom_number:
              print("You are win")
        else:
              print("you are lost in the game")
              print("the random number is:" ,ramdom_number)


