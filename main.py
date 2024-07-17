## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
import sys
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_hand = []
computers_hand = []

def addCard(hand):
  """To shorten codes length for adding cards."""
  hand.append(random.choice(cards))


def decksPrint(hidden):
  """Prints player's deck and computer's hidden or revealed deck depending on situation."""
  
  print(f"You have deck of {players_hand}")
  if hidden:
    print(f"Dealer has deck of [{computers_hand[0]}{', |*|' * (len(computers_hand)-1)}]")
  else:
    print(f"Dealer's deck is {computers_hand}")


def gameStart():
  """Start of the game. Gives two cards to user and computer (dealer). Then checks if there's a blackjack."""
  
  for i in range(2):
    addCard(players_hand)
    addCard(computers_hand)

  if blackjack():
    playAgain()
  else:
    playerDraws()


def blackjack():
  """Checks if user or computer has a blackjack, returns True of False."""
  
  if sum(computers_hand) == 21:
    decksPrint(False)
    print("Dealer has a BLACKJACK, you LOST the game!")
    return True
    
  elif sum(players_hand) == 21:
    decksPrint(False)
    print("You got BLACKJACK, you WON the game!")
    return True
    
  return False


def playAgain():
  """Asks user to play again or exit."""
  
  play_again = input("Type 1 to play again, anything else to exit: ")
  if play_again == "1":
    clear()
    players_hand.clear()
    computers_hand.clear()
    gameStart()
  else:
    sys.exit()


def aceInDeck(hand):
  """Checks if there's ace in deck and value is over 21. If yes, ace gets value of 1 instead of 11."""
  
  while sum(hand) > 21 and 11 in hand:
    x = hand.index(11)
    hand[x] = 1


def playerDraws():
  """Asks user if they want to draw a card. Checks if user's value goes over 21."""
  
  game_on = True
  while game_on:
    aceInDeck(players_hand)
    decksPrint(True)
    
    if sum(players_hand) > 21:
      print("You have cards value over 21, you LOST the game!")
      game_on = False
      playAgain()   
      
    else:
      draw_card = input("To draw a card type 1, anything else to skip: ")     
      if draw_card == "1":
        addCard(players_hand)
      else:
        game_on = False
        computerDraws()


def computerDraws():
  """Computer gets cards until value is over 16. Checks if computer's value goes over 21."""
  
  takes_card = True
  while takes_card:
    aceInDeck(computers_hand)
    
    if sum(computers_hand) > 21:
      decksPrint(False)
      print("Dealer's cards value is over 21, you WON the game!")
      takes_card = False
      playAgain()
      
    elif sum(computers_hand) < 17:
      addCard(computers_hand)
      print("Dealer takes a card from the deck")
    else:
      
      takes_card = False
      compare()


def compare():
  """Compares user's and computer's deck and announces winner. End of the game."""
  
  decksPrint(False)
  
  if sum(players_hand) > sum(computers_hand):
    print("Value of your cards is bigger, you WON the game!")
    
  elif sum(players_hand) == sum(computers_hand):
    print("You and dealer have the same value of cards, it's a DRAW!")
    
  else:
    print("Value of dealers cards is bigger, you LOST the game!")
  playAgain()


gameStart()
  