#create a program that allows a user to play a game of blackjack against a computer dealer.
#The program should allow the user to:
#1. See the value of their cards
#2. See the value of the dealer's cards
#3. Draw a new card(using a random number generator)
#4. Hold their hand
#5. See the value of their hand
#6. See the value of the dealer's hand
#7. Determine if they have won, lost, or tied
#8. Play again
#9. Quit
import random
import time
Gameloop = True
usersHand = 0
dealersHand = 0

while Gameloop:
    print("Welcome to Blackjack!")
    time.sleep(1)
    print("You will be playing against the dealer.")
    time.sleep(1)
    print("The goal of the game is to get as close to 21 as possible without going over.")
    time.sleep(1)
    print("your cards will be dealt first.")
    time.sleep(1)
    print("You will then have the option to draw another card or hold your hand.")
    time.sleep(1)
    usersHand = random.randint(1, 11)
    print("Your first card is a " + str(usersHand))
    time.sleep(1)
    print("are you going to hit or hold?")
    time.sleep(1)
    usersChoice = input("Type hit or hold: ")
    while usersChoice == "hit":
        usersHand = usersHand + random.randint(1, 11)
        print("Your new hand is a " + str(usersHand))
        if usersHand > 21:
            break
        usersChoice = input("Type hit or hold: ")
    dealersHand = random.randint(15, 24)
        
    if usersHand > 21:
        print("You busted!")
    elif dealersHand > 21:
        print("The dealer busted!")
    elif usersHand > dealersHand:
        print("You win!")
            
    elif dealersHand > usersHand:
        print("You lose!")
            
    elif usersHand == dealersHand:
        print("You tied!")
        
    print("would you like to play again?")
    time.sleep(1)
    usersChoice = input("Type yes or no: ")
    if usersChoice == "no":
        Gameloop = False
    
        
    