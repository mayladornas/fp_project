#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 08:58:15 2023

@author: FP
"""
#######################################################
####################  FUNCTIONS  ######################
#######################################################        

# Insert your functions here

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
        doMove(source, destin,bottles)
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
    