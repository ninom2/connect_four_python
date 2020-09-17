"""
File:    connect_four.py
Author:  Nino Medina
Date:    4/15/2020
Description:
  Makes a connect 4 game
"""
from random import randint


class AdjoinTheSpheres:

    def __init__(self):
        self.win_condition = False
        self.whose_move = 'x'
        self.desired_map = ''
        self.desired_mode = ''
        self.game_map = []
        self.inner_game_map = []
        self.correct_move = False
        self.bot_check = True



    def check_win(self):
        # Start:
        # This checks if x or o can vertically win by adding to i, since game_map[i] consists of the rows
        for i in range(len(self.game_map) - 1):
            if i != 0 and i != 1:
                for j in range(len(self.game_map[i])):
                    j = j - 1
                    if len(self.game_map[i]) >= i:
                        if self.game_map[i][j] == "x" and self.game_map[i + 1][j] == "x" and self.game_map[i + 2][
                            j] == 'x' and \
                                self.game_map[i + 3][j] == 'x':
                            print("x wins!")
                            return True
                        if self.game_map[i][j] == "o" and self.game_map[i + 1][j] == "o" and self.game_map[i + 2][
                            j] == 'o' and \
                                self.game_map[i + 3][j] == 'o':
                            print("o wins!")
                            return True
        # End
        # Start: This checks the horizontal win conditon by adding to j, as one horizontal win is simply in one
        # game_map[i], adding by j moves it to the right in one row
        for i in range(len(self.game_map) - 1):
            if i != 0 and i != 1:
                for j in range(len(self.game_map[i])):
                    if len(self.game_map[i][j]) >= j:
                        if self.game_map[i][j] == "x" and self.game_map[i][j + 1] == "x" and self.game_map[i][
                            j + 2] == 'x' and \
                                self.game_map[i][j + 3] == 'x':
                            print("x wins!")
                            return True
                        if self.game_map[i][j] == "o" and self.game_map[i][j + 1] == "o" and self.game_map[i][
                            j + 2] == 'o' and \
                                self.game_map[i][j + 3] == 'o':
                            print("o wins!")
                            return True
        # Start:

        # Check diagonal win condition by adding to and subtracting from i and j
        for i in range(len(self.game_map) - 1):
            if i != 0 and i != 1: # checks that the lines containing the dimensions and player move are not considered
                for j in range(len(self.game_map[i])):
                    if len(self.game_map[i][j]) >= j:
                        if self.game_map[i][j] == "x" and self.game_map[i + 1][j + 1] == "x" and self.game_map[i + 2][
                            j + 2] == 'x' and \
                                self.game_map[i + 3][j + 3] == 'x':
                            print("x wins!")
                            return True

                        if self.game_map[i][j] == "x" and self.game_map[i + 1][j - 1] == "x" and self.game_map[i + 2][
                            j - 2] == 'x' and \
                                self.game_map[i + 3][j - 3] == 'x':
                            print("x wins!")
                            return True

                        if self.game_map[i][j] == "o" and self.game_map[i + 1][j + 1] == "o" and self.game_map[i + 2][
                            j + 2] == 'o' and \
                                self.game_map[i + 3][j + 3] == 'o':
                            print("o wins!")
                            return True
        # End

    def main_menu(self):
        desired_mode = input("Connect Four Main Menu \n 1) New Game (2 player) \n 2) New Game (1 player vs "
                             "computer) \n 3) Exit Game \n Select Option from the Menu:")
        if desired_mode == '1':  # if the player selects 2 player
            self.run_2player_move()
        elif desired_mode == '2':  # if the player selects vs computer
            self.run_1player_move()
        elif desired_mode == '3':  # if the player exits the game
            return
        else:
            print('That is not a valid input')

        return None

    def load_game(self):
        temp_map = str(input("What file would you like to load"))

        # Start:
        # This set of lines loads the file and organizes it into something that can be used by the two gameplay
        # functions
        with open(temp_map, "r") as load:
            loaded_map = load.readlines()
            for i in range(len(loaded_map) - 1):
                loaded_map[i] = loaded_map[i][:-1]  # Removes the \n from each of the lines
            for row in loaded_map:
                inner_game_map = []
                for character in row:
                    inner_game_map.append(character)
                self.game_map.append(inner_game_map)
        # End

    def save_game(self):
        file = input("What file would you like to save to?")

        # Start:
        # This set of lines identifies the file to be saved and writes the game map to it.
        with open(file, "w") as temp:
            for i in range(len(self.game_map)):
                for j in range(len(self.game_map[i])):
                    temp.write(self.game_map[i][j])
                temp.write('\n')
        # End

    def run_1player_move(self):
        while not self.check_win:  #
            if self.whose_move == 'x':  # If the current move is x, then the human gets to play
                self.correct_move = True

                while self.correct_move:

                    desired_move = input(
                        "Player x What move do you want to make?  Answer as row (vertical) column (horizontal) or "
                        "save game or load game")
                    if desired_move != 'load game' and desired_move != 'save game':
                        move = desired_move.split(' ')
                        row = int(move[0])
                        column = int(move[1])
                        # Start:
                        # This checks if the two numbers the play input is in bounds, if the player doesn't
                        # enter an in bounds move they have to enter again
                        while row < 0 or column - 1 > len(self.game_map) or column < 0 or row - 1 > len(
                                self.game_map[0]):
                            print("That is out of bounds!")
                            desired_move = input("Player x What move do you want to make?  Answer as row (vertical) "
                                                 "column (horizontal) or save game or load game")
                            move = desired_move.split(' ')
                            row = int(move[0])
                            column = int(move[1])
                        # End
                    if desired_move == 'load game':
                        self.load_game()

                    elif desired_move == 'save game':
                        self.save_game()
                        return
                    elif self.game_map[row + 1][column - 1] == ' ':  # Checks if the spot they chose is empty

                        self.game_map[row + 1][column - 1] = self.whose_move
                    else:
                        print("That is not a valid move")
                    if self.whose_move == 'x':  # Changes whose turn it is after the turn is done
                        self.whose_move = 'o'
                    else:
                        self.whose_move = 'x'
                    self.correct_move = False
            else:
                self.correct_move = True

                while self.correct_move:
                    self.bot_check = True

                    move = [randint(0, len(self.game_map) - 1), randint(0, len(self.game_map[0]) - 1)]
                    # Selects a random interval ^
                    row = int(move[0])
                    column = int(move[1])
                    # Start:
                    # Checks if the random interval is in bounds, if not, a new number will be picked
                    while row < 0 or column > len(self.game_map) or column < 0 or row > len(
                            self.game_map[0]):
                        move = [randint(0, len(self.game_map)), randint(0, len(self.game_map[0]))]
                        row = int(move[0])
                        column = int(move[1])
                    # End
                    if self.game_map[row + 1][column - 1] == ' ':

                        self.game_map[row + 1][column - 1] = self.whose_move
                        temp = []
                        for i in range(len(self.game_map[2])):
                            temp.append(str(i + 1))  # Prints the numbers on top of the board

                        temp1 = "|".join(temp)
                        print(" " + temp1)
                        for i in range(len(self.game_map) - 1):
                            if i != 1 and i != 0:
                                print(str(i - 1) + '|'.join(self.game_map[i]))  # Prints the numbers of the side
                    # Start:
                    # This might be confusing, but basically if the bot places an 'o' where there is already a
                    # character, the bot check will be set to false, therefore the turn will NOT change and
                    # self.which_move will stay at 'o', when the while loop runs again it will go back to the bots
                    # move, and it will do this until the bot makes a valid move
                    else:
                        self.bot_check = False
                    if self.bot_check:
                        if self.whose_move == 'x':
                            self.whose_move = 'o'
                        else:
                            self.whose_move = 'x'
                        self.correct_move = False
                    # End

    def run_2player_move(self): # This function is basically the same as the first half(the human half) of the
        # run_1player_move function

        while not self.check_win:  #
            self.correct_move = True

            while self.correct_move:

                desired_move = input("Player x What move do you want to make?  Answer as row (vertical) column ("
                                     "horizontal) or save game or load game")
                if desired_move != 'load game' and desired_move != 'save game':
                    move = desired_move.split(' ')
                    row = int(move[0])
                    column = int(move[1])
                    while row < 0 or column - 1 > len(self.game_map) or column < 0 or row - 1 > len(self.game_map[0]):
                        print("That is out of bounds!")
                        desired_move = input("Player x What move do you want to make?  Answer as row (vertical) "
                                             "column (horizontal) or save game or load game")
                        move = desired_move.split(' ')
                        row = int(move[0])
                        column = int(move[1])
                if desired_move == 'load game':
                    self.load_game()
                    temp = []
                    for i in range(len(self.game_map[2])):
                        temp.append(str(i + 1))

                    temp1 = "|".join(temp)
                    print(" " + temp1)
                    for i in range(len(self.game_map) - 1):
                        if i != 1 and i != 0:
                            print(str(i - 1) + '|'.join(self.game_map[i]))

                elif desired_move == 'save game':
                    self.save_game()
                    return
                elif self.game_map[row + 1][column - 1] == ' ':
                    self.game_map[row + 1][column - 1] = self.whose_move
                    temp = []
                    for i in range(len(self.game_map[2])):
                        temp.append(str(i + 1))

                    temp1 = "|".join(temp)
                    print(" " + temp1)
                    for i in range(len(self.game_map) - 1):
                        if i != 1 and i != 0:
                            print(str(i - 1) + '|'.join(self.game_map[i]))
                else:
                    print("That is not a valid move")
                if self.whose_move == 'x':
                    self.whose_move = 'o'
                else:
                    self.whose_move = 'x'
                self.correct_move = False


if __name__ == "__main__":
    game = AdjoinTheSpheres()
    game.main_menu()
