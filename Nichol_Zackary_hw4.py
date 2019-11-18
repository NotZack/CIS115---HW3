# Name: Zackary Nichol
# Section: 9:30 CIS 115
# Project: Pickup Sticks Game (hw4)
# Description: This pickup sticks game program is an implementation of the simple game of pickup sticks
# There are two players
# At the beginning of a turn a player can pickup 1-3 sticks. Turns go back and forth until the player that takes the
# last stick wins. The game will run until the user does not want to 

number_of_sticks_left = 20
player_turn = 1
running = True

# Runs the game until running is set to false (until the game is over)
while running:

    # Creates the sticks ASCII art for each turn
    stick_string_art = ""
    stick_art_numbers = ""
    for i in range(0, number_of_sticks_left):
        if i < 9:
            stick_string_art += "|  "
        else:
            stick_string_art += "|   "
        stick_art_numbers += str(i + 1) + "  "

    # Prints out the ASCII art for each turn
    for j in range(0, 5):
        print(stick_string_art)
    print(stick_art_numbers)

    print("THERE ARE " + str(number_of_sticks_left) + " STICKS LEFT ... ")

    # Collects how many sticks to take for this player's turn
    sticks_taken = int(input("Player " + str(player_turn) + ", it is your turn ... How many sticks will you take? (1-3)"))

    # Parses to make sure that the input amount of sticks to take is valid input
    if sticks_taken < 1 or sticks_taken > 3:
        print("YOU CANNOT TAKE THAT MANY STICKS. ONLY TAKE 1 STICK, 2 STICKS, OR 3 STICKS")
        continue
    elif (number_of_sticks_left - sticks_taken) < 0:
        print("YOU CANT TAKE THAT MANY STICKS. YOU CANNOT TAKE STICKS THAT DON'T EXIST")
        continue
    else:
        print("PLAYER " + str(player_turn) + " TAKES " + str(sticks_taken) + " STICKS")
        number_of_sticks_left -= sticks_taken

    # Finishes the game if there are no sticks left, then asks if the user wants to play again
    if number_of_sticks_left == 0:
        print("YOU, PLAYER" + str(player_turn) + ", WIN!")

        play_again = input("Play again? (y/n)")
        if play_again == 'y' or play_again == 'Y':
            number_of_sticks_left = 20
        else:
            running = False

    # Switches the turn to the nest player
    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1
