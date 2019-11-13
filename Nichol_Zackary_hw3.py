number_of_sticks_left = 20
player_turn = 1
running = True

while running:
    stick_string_art = ""
    stick_art_numbers = ""
    for i in range(0, number_of_sticks_left):
        if i < 9:
            stick_string_art += "|  "
        else:
            stick_string_art += "|   "
        stick_art_numbers += str(i + 1) + "  "

    for j in range(0, 5):
        print(stick_string_art)
    print(stick_art_numbers)

    print("THERE ARE " + str(number_of_sticks_left) + " STICKS LEFT ... ")
    sticks_taken = int(input("Player " + str(player_turn) + ", it is your turn ... How many sticks will you take? (1-3)"))

    if sticks_taken < 1 or sticks_taken > 3:
        print("YOU CANNOT TAKE THAT MANY STICKS. ONLY TAKE 1 STICK, 2 STICKS, OR 3 STICKS")
        continue
    elif (number_of_sticks_left - sticks_taken) < 0:
        print("YOU CANT TAKE THAT MANY STICKS. YOU CANNOT TAKE STICKS THAT DON'T EXIST")
        continue
    else:
        print("PLAYER " + str(player_turn) + " TAKES " + str(sticks_taken) + " STICKS")
        number_of_sticks_left -= sticks_taken

    if number_of_sticks_left == 0:
        print("YOU, PLAYER" + str(player_turn) + ", WIN!")

        play_again = input("Play again? (y/n)")
        if play_again == 'y' or play_again == 'Y':
            number_of_sticks_left = 20
        else:
            running = False

    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1
