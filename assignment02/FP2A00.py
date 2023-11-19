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
    symbolsByExpertise = SYMBOLS[0: (5 + (5 - expertiseLevel))]
    totalCapacity = NR_BOTTLES * CAPACITY - expertiseLevel * CAPACITY

    # Create a list with symbols repeated 8 times
    repeated_symbols = [
        symbol for symbol in symbolsByExpertise for _ in range(8)]
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

    matrix = []
    for i in range(CAPACITY):
        row = []
        for bottle in bottles:
            try:
                row.append((bottle['quantity'][i]))
            except IndexError:
                row.append(' ')
        matrix.append(row)

    # Print names
    for bottle in bottles:
        print(f"{bottle['name']} ", end='')
    print()

    matrix.reverse()

    # Print quantities
    for row in matrix:
        for char in row:
            print(f"|{char}| ", end='')
        print()

    print(f"NUMBER OF ERRORS: {nrErrors}")

def askForPlay():

    sourceBottle = str(
        input(
            "Source bottle? "
        )
    )

    destinationBottle = str(
        input(
            "Destination bottle? "
        )
    )

    return sourceBottle, destinationBottle

def moveIsPossible(source, destin, bottles):

    sourceQuantity = []
    destinationQuantity = []
    for bottle in bottles:
        if source == bottle['name']:
            sourceQuantity = bottle['quantity']

        if destin == bottle['name']:
            destinationQuantity = bottle['quantity']

    transfSourceQuantity = []
    if len(sourceQuantity) > 0 and len(destinationQuantity) <= CAPACITY:
        transfSourceQuantity.append(sourceQuantity[-1])
        for i in range(-2, -len(sourceQuantity) - 1, -1):
            if transfSourceQuantity[-1] != sourceQuantity[i]:
                break
            else:
                transfSourceQuantity.append(sourceQuantity[i])
        total = len(destinationQuantity) + len(transfSourceQuantity)
        if destinationQuantity[-1] == transfSourceQuantity[-1] and total <= CAPACITY:
            return True
        else:
            return False
    else:
        return False

def doMove(source, destin, bottles):

    sourceQuantity = []
    destinationQuantity = []
    for bottle in bottles:
        if source == bottle['name']:
            sourceQuantity = bottle['quantity']

        if destin == bottle['name']:
            destinationQuantity = bottle['quantity']

    transfSourceQuantity = []
    transfSourceQuantity.append(sourceQuantity.pop(-1))
    for i in range(-1, -len(sourceQuantity) - 1, -1):
        if transfSourceQuantity[-1] == sourceQuantity[i]:
            transfSourceQuantity.append(sourceQuantity.pop(i))
        else:
            break
    destinationQuantity.extend(transfSourceQuantity)


#######################################################
##################  MAIN PROGRAM ######################
#######################################################
CAPACITY = 8
LETTERS = "ABCDEFGHIJ"
SYMBOLS = "@#%$!+o?§"
NR_BOTTLES = 10
LESS_EXPERT = 5
MAX_EXPERT = 1
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
        if full(bottles[destin]):
            fullBottles += 1
            keepGo = input("Bottle filled!!! Congrats!! Keep playing? (Y/N)")
            if keepGo == "N":
                endGame = True
    else:
        print("Error!")
        nrErrors += 1
    endGame = allBottlesFull(fullBottles, expertise) or nrErrors == 3

print("Full bottles =", fullBottles, "  Errors =", nrErrors)
if nrErrors >= 3:
    print("Better luck next time!")
else:
    print("CONGRATULATIONS!!")
