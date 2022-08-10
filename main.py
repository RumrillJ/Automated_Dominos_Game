

import random as random
import array as array


class Domino:
    # Constructor for Value and Defining values of domino object
    def __init__(self, val1, val2):

        if val1 < 0 or val1 > 6:
            print("the value of val1 must be between 1 and 6. " + str(val1) + "is not a valid value.")
            return

        if val2 < 0 or val2 > 6:
            print("the value of val2 must be between 1 and 6. " + str(val2) + "is not a valid value.")
            return

        self.val1 = val1
        self.val2 = val2
        self.isUpsideDown = False

    # Function of Domino side
    def flip(self):
        self.isUpsideDown = not self.isUpsideDown

    # Creating a Print to create the domino
    def printDomino(self):
        val1 = self.val2 if self.isUpsideDown else self.val1
        val2 = self.val1 if self.isUpsideDown else self.val2

        print("+=*=*=+")
        self.printHalfDomino(val1)
        print("+=*=*=+")
        self.printHalfDomino(val2)
        print("+=*=*=+")

    # Print lines to create the value of the domino objkect
    def printHalfDomino(self, val):
        value = "|" + ("." if val > 1 else " ") + (" ." if val == 6 else "  ") + (" ." if val > 3 else "  ") + "|"
        print(value)
        value = "| " + (" ." if val % 2 == 1 else "  ") + "  |"
        print(value)
        value = "|" + ("." if val > 3 else " ") + (" ." if val == 6 else "  ") + (" ." if val > 1 else "  ") + "|"
        print(value)

    # Returns to get available values of both sides
    def getAvailableValue(self):
        return self.val1 if self.isUpsideDown else self.val2

    def getAvailableValueIfFirst(self):
        return self.val2 if self.isUpsideDown else self.val1

    # Function to get length of dominos and to play the domino to match either side
    def playIfCan(self, dominos):

        if (len(dominos) == 0):
            dominos.append(self)
            return True

        last = dominos[len(dominos) - 1]
        first = dominos[0]

        if (last.getAvailableValue() == self.val1):
            dominos.append(self)
            return True

        if (last.getAvailableValue() == self.val2):
            self.flip()
            dominos.append(self)
            return True

        if (first.getAvailableValueIfFirst() == self.val2):
            dominos.insert(0, self)
            return True

        if (first.getAvailableValueIfFirst() == self.val1):
            self.flip()
            dominos.insert(0, self)
            return True

        return False


# Create class game to play the game
class Game:
    # Create a constructor for board, deck, playerturn , player1/2 win and player1/2 hand.
    def __init__(self):

        self.board = []
        self.deck = []
        for i in range(7):
            for j in range(i + 1):
                self.deck.append(Domino(i, j))
        # Set up shuffle deck function
        random.shuffle(self.deck)
        self.isPlayer1Turn = True
        self.player1Win = False
        self.player2Win = False
        self.hand1 = self.createStartingHand()
        self.hand2 = self.createStartingHand()
        # Set up random number for which player goes first
        RandomNumb = random.randint(1, 2)
        if (RandomNumb == 1):
            self.isPlayer1Turn = True
            print("Player 1 was elected to go first")
            print("-------------------------------")
            print("----------Good Luck------------")
        else:
            self.isPlayer1Turn = False
            print("Player 2 was elected to go first")
            print("-------------------------------")
            print("----------Good Luck------------")

    # Create Function Play to make sure player 1 and player 2 has played
    def play(self):
        played1 = True
        played2 = True
        while (not self.player1Win and not self.player2Win):
            hasPlayed = self.takeTurn()

            if (self.isPlayer1Turn):
                played1 = hasPlayed
            else:
                played2 = hasPlayed

            if not played1 and not played2:
                print("Neither player can play a domino after turn was passed, game is a draw.")
                return

            self.isPlayer1Turn = not self.isPlayer1Turn

            for domino in self.board:
                domino.printDomino()

        print("player " + ("1" if self.player1Win else "2") + " has won")
        print("The Player who lost had this many Dominos left:")
        print(len(self.hand1) + len(self.hand2))
        print("The Amount of Dominos Left in the Unused Pile was:")
        print(len(self.deck))
        # Print Remainder Domino pieces of domino for Loser
        print("The Player who lost had these pieces: ")
        for domino in self.hand1:
            domino.printDomino()
        for domino in self.hand2:
            domino.printDomino()
        # Print remainder Domino pieces of the deck
        print("The pieces left in the pile are: ")
        for domino in self.deck:
            domino.printDomino()

    def createStartingHand(self):
        hand = []
        for i in range(10):
            hand.append(self.deck.pop())

        return hand

    # Function take turns, when player 1/2 play the other player plays.
    def takeTurn(self):
        print("Player " + ("1" if self.isPlayer1Turn else "2") + "'s turn.")
        hand = self.hand1 if self.isPlayer1Turn else self.hand2

        while (True):

            hasPlayed = False

            for domino in hand:
                if domino.playIfCan(self.board):
                    print("domino has been played.")
                    print("-----------------------")
                    hand.remove(domino)
                    hasPlayed = True
                    break
            # After play, check if hand is < 1 and if it does, player wins.
            if hasPlayed:
                self.checkForWin()
                return True

            elif len(self.deck) > 0:
                print("Player had no possible play, player grabs a domino from the unused pile")
                hand.append(self.deck.pop())

            else:
                print("no domino can be played.")
                return False

    # Function to check for win
    def checkForWin(self):
        if len(self.hand1) == 0:
            self.player1Win = True

        if len(self.hand2) == 0:
            self.player2Win = True


# Main Program to intiate game and to play game
game = Game()
# call from constuctor play
game.play()

# Create a print line to say Good Game and officially end the game(program)
print("---------- Good Game, Game has Ended! ----------")