class Card():
        def __init__(self,suit,rank):
                self.suit = suit
                self.rank = rank
                self.value = value[rank]
        def __str__(self):
                return f"{self.rank} of {self.suit}"

class Deck():
        def __init__(self):
                self.wholeDeck = []
                for suit in suits:
                        for rank in ranks:
                                self.wholeDeck.append(Card(suit,rank))
        def shuffle(self):
                random.shuffle(self.wholeDeck)
        def dealOne(self):
                return self.wholeDeck.pop()

class Player():
        def __init__(self,name):
                self.name = name
        def name(self):
                return f"{name}"

class Bank():
        def __init__(self,player,stack):
                self.player = player
                self.stack = stack
                self.amount = amount
        def __str__(self):
                return f"{player.name}, you have {self.stack} to bet."
        def deposit(self,amount):
                self.stack += amount
        def bet(self):
                hasbet = False
                while hasbet == False:
                        self.amount = int(input("Please enter bet: "))
                        if self.amount > self.stack:
                                print(f"I'm sorry. You don't have {self.amount} left in your pot. You may bet up to {self.stack}.")
                                continue
                        else:
                                self.stack -= self.amount
                                hasbet = True
                                return self.amount

def checktotal(hand):
        if hand < 21:
                return None
        if hand == 21:
                print("Twenty one!\n")
                return "winner"
        if hand > 21:
                return "loser"

def acecall():
        acecall = False
        while acecall == False:
                call = input("Would you like aces to be high or low? Enter high/low ")
                if call == "high" or call == "low":
                        acecall = True
                        if call == "high":
                                value["A"] = 11
                                break
                        else:
                                value["A"] = 1
                                break
                else:
                        continue

def checkwin(playerHandValue):
    if checktotal(playerHandValue) == "winner":
        return "a"
    elif checktotal(playerHandValue) == "loser":
        return "b"
    else:
        return "c"

import random
# import IPython

playerHandValue = 0
dealerHandValue = 0
isover = False
acehigh = True
playergame = True
dealergame = True

# Suits are spade, heart, diamond, club
suits = ["\u2660","\u2665","\u2666","\u2663"]
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
value = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

# intro tasks: get name, assign money to bank

player = Player(input("Welcome to blackjack! Please enter your name: "))
playerbank = Bank(player,500)
print('\n'*100,playerbank)
# IPython.display.clear_output()
print("\nLet's play!")

# create the deck

gamedeck = Deck()

# MAIN  GAMEPLAY

while isover == False:

# player makes bet

    playerbank.bet()
    print(f"You have bet {playerbank.amount}.")

    gameon = True          # shuffle deck, deal hand to player and hand to dealer
    gamedeck.shuffle()
    playerhand = [gamedeck.dealOne(), gamedeck.dealOne()]
    dealerhand = [gamedeck.dealOne(), gamedeck.dealOne()]
    print("Your hand is now:\n")
    for x in range(len(playerhand)):
        print([f"{playerhand[x]}"])
    print(f"Dealer is showing\n{dealerhand[0]}.")
    if playerhand[0].rank == "A" or playerhand[1].rank == "A":
        acecall()

# player loop

    playerHandValue = playerhand[0].value + playerhand[1].value
    dealerHandValue = dealerhand[0].value + dealerhand[1].value

    playergame = True
    dealergame = True
    while playergame == True and dealergame == True:      # check if at 21 already
        if playerHandValue == 21:
            print("You've won!\n")
            playerbank.deposit(2 * playerbank.amount)
            playergame = False
            dealergame = False
            break
        counter = 1        # if not, ask if they want another card
        choicemade = False
        while choicemade == False:
            choice = input("Would you like another card? Enter y/n ")
            if choice == 'y' or choice == 'n':
                choicemade = True
                if choice == 'y':
                    counter += 1
                    playerhand.append(gamedeck.dealOne())
                    print("Your hand is now:\n")
                    for x in range(len(playerhand)):
                        print([f"{playerhand[x]}"])
                    if playerhand[counter] == "A":
                        acecheck()
                    playerHandValue += playerhand[-1].value
                    if checkwin(playerHandValue) == "a":
                        print("You've won\n")
                        playerbank.deposit(2 * playerbank.amount)
                        playergame = dealergame = False
                        break
                    elif checkwin(playerHandValue) == "b":
                        print("Bust! You lose!")
                        playergame = dealergame = False
                        break
                    else:
                        pass
                    print(playerHandValue)
                else:
                    print("You have rested. Dealer's turn.")
                    print("Dealer's hand is:\n")
                    for x in range(len(dealerhand)):
                        print([f"{dealerhand[x]}"])
                    input("Press enter to continue")
                    playergame = False
            else:
                print("Not a valid choice!")
                continue

    while playergame == False and dealergame == True:
        if dealerHandValue <= playerHandValue:
            dealerhand.append(gamedeck.dealOne())
            dealerHandValue += dealerhand[-1].value
            print("Dealer's hand is now:\n")
            for x in range(len(dealerhand)):
                print([f"{dealerhand[x]}"])
            input("Press enter to continue")
        else:
            if dealerHandValue < 21:
                print(f"Sorry, {player.name}! Dealer wins!")
                dealergame = False
                break
            else:
                print(f"Dealer busts! {player.name} wins!")
                playerbank.deposit(2 * playerbank.amount)
                dealergame = False
                break

    nextgame = False
    while nextgame == False:
        if playerbank == 0:
            isover = True
            nextgame = True
            print("Out of money. You lose. Remember: the house always wins.")
            break
        choosenext = input("Would you like to play again? Enter y/n ")
        if choosenext == 'y':
            gameon = True
            nextgame = True
            print(f"You have {playerbank.stack} left to bet with.")
            break
        elif choosenext == 'n':
            isover = True
            nextgame = True
            break
        else:
            continue
