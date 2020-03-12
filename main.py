import time
import random

count= 0    ##count the number of times you have guessed

n = random.randint(1, 100)         ##random number too guess

guess = int(input("Enter an integer from 1 to 100: "))      ##you're guess

while n != "guess":
    print
    if guess < n:
        print ("you're guess is too low")
        guess = int(input("Enter an integer from 1 to 100: "))
        count = count + 1
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 100: "))
        count= count+ 1
    else:
        print ("Correct!")
        print("\nProcesing all you're data, wait a little bit.")
        print("\n <----------------------------------------->")
        time.sleep(1.5)
        print("\nYou guessed " +str(count)+ " times/time")
        
        if count == 1:
            print("Omg you're a master mind subscribe and comment in my latest video and then you will get awarded if you id it without cheating (Coded armor)")
        if count == 2 or count == 3:
            print("You are a freaking legend")
        if count == 4 or count == 5:
            print ("you're pretty good")
        if count == 6 :
            print("you're good")
        if count >= 7:
            print("you're super bad")
        break
    print
