#!/usr/bin/env python
"""This module contains the Battleship game, in which only one player is involved, as the enemy will be the PC. 
The player has 10 ships that he places on his own size selected board. Whoever destroys all the opponent's ships will win. 
The player has the first turn. The D represents a ship that has been destroyed, while an X represents a missed shot.
"""


import random


def creation_list_pj(n):
    """This function builds the list of lists where the "O" of the player's base board is stored,
    taking into account the size of the board entered. 
    Args:
        n (int): Is the size of the board.

    Returns:
        list[list[str]]: A list in which there are saved the list with "O" needed according to size. 
    """
    pj = []
    list_supportPj = []
    for i in range(n):
        for j in range(n):
            list_supportPj.append("O")
        pj.append(list_supportPj)
        list_supportPj = []
    return pj


def creation_list_pc(n):
    """This function builds the list of lists where the "O" of the PC base board is stored,
    taking into account the size of the board entered. 

    Args:
        n (int): Is the size of the board.

    Returns:
        list[list[str]]: A list in which there are saved the list with "O" needed according to size.
    """
    pc = []
    list_supportPc = []
    for i in range(n):
        for j in range(n):
            list_supportPc.append("O")
        pc.append(list_supportPc)
        list_supportPc = []
    return pc


def showBoard(pj, pc, name):
    """This function organizes and prints the player and PC board, taking into account the list of lists of each. 
    It also prints the player's name on its corresponding board if it was stated in the beginning.

    Args:
        pj (list[list[str]]): A list that stores the lists that compose the player's board.
        pc (list[list[str]]): A list that stores the lists that compose the PC board.
        name (str): The name entered by the player.
    """
    print("========PC========")
    for i in range(len(pc)):
        for j in range(len(pc)):
            print(pc[i][j], end=" ")
        print()

    if name == "":
        print("========PJ========")
    else:
        print("=====", name, "======")
    for i in range(len(pj)):
        for j in range(len(pj)):
            print(pj[i][j], end=" ")
        print()


def locationShipsPC(pc):
    """This function uses random to generate the coordinates of the PC ships and stores them in a list until they are 10 pairs,
    without repeats. 

    Args:
        pc (list[list[str]]): A list that stores the lists that compose the PC board.

    Returns:
        list[list[str]]: A list that stores the ten coordinates of the ten ships of the PC. 
    """
    list_location = []
    support_list = []
    while len(list_location) <= 10:
        row = random.randint(0, len(pc) - 1)
        support_list.append(row)
        column = random.randint(0, len(pc) - 1)
        support_list.append(column)
        if not support_list in list_location:
            list_location.append(support_list)
        support_list = []
    return list_location


def shootingShips(pj_shot, pc_shot, name):
    """This function controls PC shooting using random and requests the player's shooting coordinates while checking that they are valid. 
    It also displays on-screen warnings if the shot failed and impacted, and ends the game when all 10 player or PC ships have sunk. 

    Args:
        pj_shot (list[list[str]]): A list that stores the lists that compose the player's board
        pc_shot (list[list[str]]): A list that stores the lists that compose the PC board.
        name (str): The name entered by the player.
    """
    shotShipsPj = 0
    shotShipsPc = 0
    # Coordinares_pc refers to the list that contains ships location in the function locationshipsPc
    coordinates_pc = locationShipsPC(pc_shot)
    support_list_coordinates = []
    shot_register = []
    # The cicle finishes when any of the players losses all 10 ships.
    while shotShipsPc <= 10 and shotShipsPj <= 10:
        i = True
        while i == True:
            try:
                row = int(input("Please enter the row of the shot: "))
                if row > len(pj_shot) or row < 0:
                    print("Invalid shot!")
                else:
                    i = False
                    support_list_coordinates.append(row)
            except ValueError:
                print("Invalid shot!")
        j = True
        while j == True:
            try:
                column = int(
                    input("Please enter the column of the shot: "))
                if column > len(pj_shot) or column < 0:
                    print("Invalid shot!")
                else:
                    j = False
                    support_list_coordinates.append(column)
            except ValueError:
                print("Invalid shot!")
        # Player's shootings
        if support_list_coordinates in shot_register:
            print("The coordinate has already been selected")
        elif support_list_coordinates in coordinates_pc:
            pc_shot[row][column] = "D"
            shotShipsPc += 1
            print()
            print("Hit!")
            print("The enemy has: ", 10 - shotShipsPc, " ships left")
            shot_register.append(support_list_coordinates)
        elif not support_list_coordinates in coordinates_pc:
            pc_shot[row][column] = "X"
            shot_register.append(support_list_coordinates)
            print()
            print("Missed shot!")
        support_list_coordinates = []
        # PC shootings
        list_coordinates_pc = []
        shot_register_pc = []
        shot_row = random.randint(0, len(pj_shot) - 1)
        list_coordinates_pc.append(shot_row)
        shot_column = random.randint(0, len(pj_shot) - 1)
        list_coordinates_pc.append(shot_column)
        if not list_coordinates_pc in shot_register_pc:
            shot_register_pc.append(list_coordinates_pc)
            if pj_shot[shot_row][shot_column] == "O":
                pj_shot[shot_row][shot_column] = "X"
                print()
                print("Failed enemy shot!")
            elif pj_shot[shot_row][shot_column] == "B":
                pj_shot[shot_row][shot_column] = "D"
                shotShipsPj += 1
                print()
                print("Enemy hit!")
                print("You have:", 10 - shotShipsPj, "ships left")
        shot_register_pc = []
        showBoard(pj_shot, pc_shot, name)
    # End of the game
    if shotShipsPc == 10:
        print("Game Over")
        print("You Won")
    else:
        print("Game Over")
        print("You Lose")
    input("Press enter to continue")


def locationShipsPJ(name):
    """This feature gives the player the option to choose the board size.
    In addition, it is the function charged with locating the player's ships on their board, 
    asking them for coordinates and checking this available, if they are not, it will give a warning. 

    Args:
        name (str):The name entered by the player.
    """
    i = True
    while i == True:
        size = int(input("Choose the size of the board: "))
        if size < 5 or size > 15:
            print("(Error: Invalid size)")
        else:
            i = False
    list_pjBoard = creation_list_pj(size)
    list_pcBoard = creation_list_pc(size)
    num_ships = 10
    while num_ships > 0:
        row = int(input("Please enter the row: "))
        column = int(input("Please enter the column: "))
        print()
        if list_pjBoard[row][column] == "O":
            list_pjBoard[row][column] = "B"
            num_ships -= 1
            print("Missing ships to locate: ", num_ships)
        else:
            print("Invalid coordinate")
    shootingShips(list_pjBoard, list_pcBoard, name)


def main_menu():
    """This function controls the main menu of the program by displaying the options that the player has.
    It also shows the general information of the game.
    """

    option_menu = 0
    player = ""
    while option_menu != 3:
        print("""Coffee Time
Battleship
Main Menu:
1. Enter player name 
2. Start Game
3. Close the program """)
        option_menu = int(input("Please choose an option: "))
        if (option_menu == 1):
            player = input("Please enter your first name: ")
            print("Hello", player)
            print()
        elif (option_menu == 2):
            locationShipsPJ(player)
        elif (option_menu == 3):
            print("End of the program")
        else:
            print("Error:Invalid selection")


main_menu()
