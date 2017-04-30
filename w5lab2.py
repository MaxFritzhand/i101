import random

Total = random.randint(2,12)
dieColors = ["Red", "Yellow", "Black", "Blue"]
print ("              Welcome to 'Guess the Die Numb'!")
print ("    Your job is to guess the sum of the Red Die and Blue Die.")
print ("                      Good luck!")

while True:
	DiceA = input("Toss the Red Die, 1 to 6:")
	DiceB = input("Toss the Blue Die, 1 to 6:")
	DiceAB = int(DiceA) + int(DiceB)
	try:
	    if int(DiceAB) > Total:
	     		print ("Too High")
	    elif int(DiceAB) < Total:
	     		print ("Too Low")
	    else:
	                print("You Guessed Correctly!")
	                print (random.randint(2, 12))
                        dieColors.remove("Yellow", "Black")

	except:
	     	 print("Your Guess is Not a Number!")




#  ~~Practice~~

#name = input("Enter you name: ")

#print ("Hello " + name)

#while True:
#    a = input("please enter a number: ")    
#    b = input ("please enter another number: ")


#    try:
#        print(int(a) + int(b) )
#        break
#    except:
#        print("one of those is not a number")


#counter = 2
#while counter <= 100:
#    print(counter)
#    counter = counter + 2


#number = random.randint(1,100)
#guess = 421384831238246324876346343489
#while guess != number: 
#    guess = input("Enter a number between 1 and 100: ")
#    try:
#        if int(guess) > number:
#                print ("Too high")
#        elif int(guess) < number:
#                print ("Too low")
#        else:
#                print("You guessed it!")
#    except:
#            print("your guess is not a number!")


#print (random.randint(1, 100))



#colorsList = ["black", "brown", "orange", "green", "blue", "purple", "yellow"]

#while colorList:
#   myColor = random.choice(colorsList)
#   print(myColor)
#   colorsList.remove(myColor)
