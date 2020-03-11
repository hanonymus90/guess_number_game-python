import time
import random
count= 0
n = random.randint(1, 100)
guess = int(input("Enter an integer from 1 to 100: "))
while n != "guess":
    print
    if guess < n:
        print ("you're guess is too low")
        guess = int(input("Enter an integer from 1 to 100: "))
        count= count+ 1
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 100: "))
        count= count+ 1
    else:
        print ("Correct!")
        print("\nProcesing all you're data, wait a little bit.")
        print("\n <----------------------------------------->")
        time.sleep(2)
        print("\nYou guessed " +str(count)+ " times")
        if count<= 3:
            print("You are a legend")
        if count == 4 or count == 5:
            print ("you're pretty good")
        if count >=6:
            print("you're good")
        break
    print
