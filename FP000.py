#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:16:12 2023

@author: ???
"""

from random import seed
from random import randint
 
# *****************************************************
def askInfoGame():
    """
    Asks the user for three values that are important for the game

    Returns
    -------
    minL : integer
        The minimum quantity of liquid the bottle must have.
    maxL : integer
        The maximum quantity of liquid the bottle can have (capacity).
    nrPlayers : integer
        The number of players playing the game.

    """


# *****************************************************
def randomFill(min, max, useSeed = 0):
    """
    Generates and returns a random integer, in the interval [min,max].
    
    Parameters
    ----------
    min : integer
        The minimum value of the random value to be generated.
    max : integer
        The minimum value of the random value to be generated.
    useSeed : integer, optional
        The seed for the random generator. The default is 0.

    Returns
    -------
    integer
        A random integer, in the interval [min,max].

    """


# *****************************************************
def initializePlayers(number):
    """
    Creates and returns an adequate data structure (you must choose the
    one that suits better your purposes) that represents players. Remember 
    each player must have a name, a current number of score points (equal to
    the sum of the quantities he has already chosen), and whether it is still 
    playing or has already lost.

    Parameters
    ----------
    number : integer
        The number of players that are going to play.

    Returns
    -------
    result : ??? you choose the type!!
        An adequate data structure that represents the game players at the
        beginning of the game.

    """


# *****************************************************
def showInfoRound(nrR):
    """
    Prints a line in the standard output informing the number of
    the current round.

    Parameters
    ----------
    nrR : integer
        The number of the current round.

    Returns
    -------
    None.

    """

    
# *****************************************************
def showInfoBottle(liquid, maxLiquid, deltaDown, deltaUp):
    """
    Prints several lines in the standard output informing about the
    current state of the game:
        - The first line informs about the interval of percentages within which 
          lies the current bottle content percentage. This interval depends on
          the values of deltaDown and deltaUp. Example:
              - if liquid is 10, and maxLiquid is 50, then the bottle is 
                20% full.
             - if deltaDown is .15 and deltaUp is .21, then the the program 
               tells the user that the bottle is between 17% and 24% full, 
               because .15 of 20% is 3%, and .21 of 20% is 4.2%
        - The next 11 lines give a somewhat visual representation of that
          interval of percentages (each line accounts for 10% ; the last one
          represents the bottom of the bottle).
    The minimum value of the left side of the interval is 0
    The maximum value of the right side of the interval is 100

    Parameters
    ----------
    liquid : integer
        The current content of the bottle.
    maxLiquid : integer
        The capacity of the bottle.
    deltaDown : float
        A value that allows to calculate the left endpoint of the interval.
    deltaUp : float
        A value that allows to calculate the right endpoint of the interval.

    Returns
    -------
    None.

    """
 
    

# *****************************************************
def notLostYet(players, nr):
    """
    Is it the case that the player number nr hasn't yet lost the game?

    Parameters
    ----------
    players : A data structure (your decision)
        A data structure containing the information about players.
    nr : integer
        A number that allows to identify which player we are referring to.

    Returns
    -------
    boolean
        True if the player with number nr has not yet lost the game. 
        False otherwise.

    """


# *****************************************************
def askForQuantity(players, nr):
    """
    Asks the user for the value of the quantity that the player number nr 
    wants to add to the bottle

    Parameters
    ----------
    players : A data structure (your decision)
        A data structure containing the information about players.
    nr : integer
        A number that allows to identify which player we are referring to.

    Returns
    -------
    integer
        The the quantity that the player number nr wants to add to the bottle.

    """


# *****************************************************
def updatePlayerScores(players, nr, qty):
    """
    Updates the accumulated score of player number nr by adding it the value
    of qty

    Parameters
    ----------
    players : A data structure (your decision)
        A data structure containing the information about players.
    nr : integer
        A number that allows to identify which player we are referring to.
    qty : integer
        The quantity that the player number nr decided to add to the bottle.

    Returns
    -------
    None.

    """


# *****************************************************
def updatePlayerLost(players, nr):
    """
    Updates the status of the player number nr to a looser one

    Parameters
    ----------
    players : A data structure (your decision)
        A data structure containing the information about players.
    nr : integer
        A number that allows to identify which player we are referring to.

    Returns
    -------
    None.

    """

    
# *****************************************************
def allLost(players):
    """
    Is it the case that all the players have already lost the game?

    Parameters
    ----------
    players : A data structure (your decision)
        A data structure containing the information about players.

    Returns
    -------
    result : boolean
        True is all players have already lost. False otherwise.

    """


# *****************************************************
def showInfoResult(bottle,maxL,players,nr,nrRounds):
    """
    Shows the information about the outcome of the game (see the examples 
    given in the text of the project)

    Parameters
    ----------
    bottle : integer
        The current content of the bottle.
    maxL : integer
        The capacity of the bottle.
    players : A data structure (your decision)
        A data structure containing the information about players.
    nr : integer
        A number that allows to identify which player has won, if any.
    nrRounds : integer
        The number of rounds played in the game.

    Returns
    -------
    None.

    """
 

#######################################################
##################  MAIN PROGRAM ######################
#######################################################
winBonus = 50         # The bonus to be given to the winner, if any
deltaLeft = 0.2       # Used to inform the user about the state of the bottle
deltaRight = 0.23     # Used to inform the user about the state of the bottle

minLiquid, maxLiquid, nrPlayers = askInfoGame()

liquidInBottle = randomFill(minLiquid, maxLiquid, useSeed = 1)
players = initializePlayers(nrPlayers)

# It can be the case that the bottle is iniatilly full
endGame = liquidInBottle == maxLiquid  

nrRounds = 0
showInfoBottle(liquidInBottle, maxLiquid, deltaLeft, deltaRight)

# Let's play the game
while not endGame:
    nrRounds += 1
    showInfoRound(nrRounds)
    # Let's play the next round
    nr = -1
    while nr < nrPlayers - 1 and not endGame:
        nr += 1
        # Only players that have not yet lost, are allowed to play their turn
        if notLostYet(players, nr):
           qty = askForQuantity(players, nr)
           updatePlayerScores(players, nr, qty) 
           if qty + liquidInBottle > maxLiquid:
              updatePlayerLost(players, nr)
              print("Oops! You tried to overfill the bottle! The game is over for you!\n")
           else: 
              liquidInBottle += qty
              showInfoBottle(liquidInBottle, maxLiquid, deltaLeft, deltaRight)
           # Should the game end after this turn?
           endGame = liquidInBottle == maxLiquid or allLost(players)

showInfoResult(liquidInBottle,maxLiquid,players,nr,nrRounds)







