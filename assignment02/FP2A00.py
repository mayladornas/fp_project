#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 08:58:15 2023

@author:
GROUP FP13
Bernardo Costa - Nº 49212
Mayla Dornas - Nº 62933

"""

import random

#######################################################
####################  FUNCTIONS  ######################
#######################################################

def showInstructionsOfGame():
    """
       Shows the initial instructions of the game
       """

    print("=== Welcome to the Bottle Filling Game ===\n")
    print("Objective:")
    print(
        "Your mission is to fill bottles with the same liquid symbol. You'll transfer liquid between bottles step by step, following some specific rules.\n")
    print("Rules:")
    print("1. The game will start with ten bottles partially filled with different symbols.")
    print("2. You'll move the symbols from bottle to bottle but you can only add liquid to a bottle if its top symbol matches the liquid you're transferring.")
    print("3. The goal is to have each bottle filled with a single symbol or empty by the end of the game.\n")
    print("How to Play:")
    print("1. You will be asked to choose your expertise level (from less expert (5) to max expert (1)).")
    print("2. The number of bottles that must be completely filled by the end will be based on your expertise level.")
    print("3. You'll be shown the bottles and their current state.")
    print("4. Select the source and destination bottles to transfer the liquid, using capital letters.")
    print("5. Continue until the bottles are filled with the same symbol or completely empty.")
    print("6. IMPORTANT: You can only make 3 mistakes during the game.\n")

    print("LET'S START!!! Enjoy the challenge!\n")



def askForExpertise():
    """
    Asks the user what level of expertise he chooses, and returns the integer value (between MAX_EXPERT and LESS_EXPERT).
    Returns
    -------
    expertiseLevel: integer
        The user's chosen expertise level.
    """

    expertiseLevel = int(
        input(
            f"What is your expertise level? Choose between {MAX_EXPERT} to {LESS_EXPERT}, where {MAX_EXPERT} is the max expertise level. "
        )
    )

    if MAX_EXPERT <= expertiseLevel <= LESS_EXPERT:
        return expertiseLevel
    else:
        print("Choose a number between 1 to 5. ")
        return askForExpertise()


# *****************************************************


def buildGameBottles(expertiseLevel):
    """
    Given an integer expertise representing the user’s expertise, builds and returns a structure
    containing the information of each and every bottle in the game – there will exist NR_BOTTLES
    bottles in total, each with a maximum capacity of CAPACITY; these bottles are to be (partially)
    filled with various symbols in SYMBOLS, and each bottle is named a letter from LETTERS.
    Parameters
    ----------
    expertiseLevel : integer
        The user's chosen expertise level.
    Returns
    -------
    list
        A list containing dictionaries representing each bottle in the game.
    """

    array_of_bottles = [[] for _ in range(NR_BOTTLES)]
    symbolsByExpertise = SYMBOLS[0 : (5 + (5 - expertiseLevel))]
    totalCapacity = NR_BOTTLES * CAPACITY - expertiseLevel * CAPACITY

    # Create a list with symbols repeated 8 times
    repeated_symbols = [symbol for symbol in symbolsByExpertise for _ in range(8)]
    random.shuffle(repeated_symbols)

    while totalCapacity > 0:
        # Choose a random bottle from the array of bottles
        random_array_index = random.randint(0, NR_BOTTLES - 1)

        # Check if the array of bottles still has space
        if len(array_of_bottles[random_array_index]) < CAPACITY:
            # Add a symbol to the chosen array
            array_of_bottles[random_array_index].append(repeated_symbols.pop())

            # Decrease the number of total capacity
            totalCapacity -= 1

    bottles = []
    for i in range(NR_BOTTLES):
        bottle = {"name": LETTERS[i], "quantity": array_of_bottles[i]}
        bottles.append(bottle)

    return bottles


def showBottles(bottles, nrErrors):
    """
    Displays the current state of the game bottles and the number of errors.
    Parameters
    ----------
    bottles : list
        A list of dictionaries representing each bottle in the game.
    nrErrors : int
        The number of errors made so far in the game.
    """

    matrix = []
    for i in range(CAPACITY):
        row = []
        for bottle in bottles:
            try:
                row.append((bottle["quantity"][i]))
            except IndexError:
                row.append(" ")
        matrix.append(row)

    # Print names
    for bottle in bottles:
        print(f" {bottle['name']} ", end=" ")
    print()

    matrix.reverse()

    # Print quantities
    for row in matrix:
        for char in row:
            print(f"|{char}| ", end="")
        print()

    print(f"NUMBER OF ERRORS: {nrErrors}")


def askForPlay():
    """
    Asks the user for the source and destination bottles for the next play.
    Returns
    -------
    tuple
        A tuple containing the names of the source and destination bottles.
    """
    global bottles 
    valid_entries = False
    while not valid_entries:
        sourceBottle = str(input("Source bottle? "))
        destinationBottle = str(input("Destination bottle? "))

        if (
            sourceBottle in [bottle["name"] for bottle in bottles]
            and destinationBottle in [bottle["name"] for bottle in bottles]
            and sourceBottle != destinationBottle
        ):
            valid_entries = True
        else:
            print("Invalid entries. Please enter valid source and destination bottles.")

    return sourceBottle, destinationBottle


def moveIsPossible(source, destin, bottles):
    """
    Checks if a move is possible based on the game rules.

    Parameters
    ----------
    source : str
        The name of the source bottle.
    destin : str
        The name of the destination bottle.
    bottles : list
        A list of dictionaries representing each bottle in the game.

    Returns
    -------
    bool
        True if the move is possible, False otherwise.
    """

    sourceQuantity = []
    destinationQuantity = []
    for bottle in bottles:
        if source == bottle["name"]:
            sourceQuantity = bottle["quantity"]

        if destin == bottle["name"]:
            destinationQuantity = bottle["quantity"]

    transfSourceQuantity = []
    if len(sourceQuantity) > 0 and len(destinationQuantity) < CAPACITY:
        transfSourceQuantity.append(sourceQuantity[-1])
        for i in range(-2, -len(sourceQuantity) - 1, -1):
            if transfSourceQuantity[-1] != sourceQuantity[i]:
                break
            else:
                transfSourceQuantity.append(sourceQuantity[i])
        total = len(destinationQuantity) + len(transfSourceQuantity)

        if destinationQuantity and destinationQuantity[-1] != transfSourceQuantity[-1]:
            return False
        if total <= CAPACITY:
            return True
    return False


def doMove(source, destin, bottles):
    """
    Performs the move if it's possible.

    Parameters
    ----------
    source : str
        The name of the source bottle.
    destin : str
        The name of the destination bottle.
    bottles : list
        A list of dictionaries representing each bottle in the game.
    """

    sourceQuantity = []
    destinationQuantity = []
    for bottle in bottles:
        if source == bottle["name"]:
            sourceQuantity = bottle["quantity"]

        if destin == bottle["name"]:
            destinationQuantity = bottle["quantity"]

    transfSourceQuantity = []

    if sourceQuantity:
        transfSourceQuantity.append(sourceQuantity.pop(-1))
        while sourceQuantity and transfSourceQuantity[-1] == sourceQuantity[-1]:
            transfSourceQuantity.append(sourceQuantity.pop(-1))

    destinationQuantity.extend(transfSourceQuantity)


def full(bottle):
    """
    Checks if a bottle is full with the same symbol.

    Parameters
    ----------
    bottle : dict
        A dictionary representing a bottle in the game.

    Returns
    -------
    bool
        True if the bottle is full with the same symbol, False otherwise.
    """
    return len(set(bottle["quantity"])) == 1 and len(bottle["quantity"]) == CAPACITY


def allBottlesFull(fullBottles, expertise):
    """
    Checks if all bottles are full based on the expertise level.

    Parameters
    ----------
    fullBottles : int
        The number of full bottles.
    expertise : int
        The expertise level of the player.

    Returns
    -------
    bool
        True if all bottles are full, False otherwise.
    """
    return fullBottles == NR_BOTTLES - expertise


#######################################################
##################  MAIN PROGRAM ######################
#######################################################
CAPACITY = 8
LETTERS = "ABCDEFGHIJ"
SYMBOLS = "@#%$!+o?§"
NR_BOTTLES = 10
LESS_EXPERT = 5
MAX_EXPERT = 1
showInstructionsOfGame()
expertise = askForExpertise()
bottles = buildGameBottles(expertise)
nrErrors = 0
fullBottles = 0
endGame = False
showBottles(bottles, nrErrors)
# Let's play the game
while not endGame:
    source, destin = askForPlay()
    if moveIsPossible(source, destin, bottles):
        doMove(source, destin, bottles)
        showBottles(bottles, nrErrors)
        for bottle in bottles:
            if destin == bottle["name"]:
                if full(bottle):
                    fullBottles += 1
                    keepGo = input("Bottle filled!!! Congrats!! Keep playing? (Y/N)")
                    if keepGo == "N":
                        endGame = True
    else:
        print("Error!")
        nrErrors += 1
    if not endGame:
        endGame = allBottlesFull(fullBottles, expertise) or nrErrors == 3

print("Full bottles =", fullBottles, "  Errors =", nrErrors)
if nrErrors >= 3:
    print("Better luck next time!")
else:
    print("CONGRATULATIONS!!")
