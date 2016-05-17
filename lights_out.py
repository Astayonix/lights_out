from random import choice

def setUp():
    """Allows the user to set up a randomized game board for Lights Out"""
    random_selector_list = ['X','O'] #X represents a tile that is off; O represents a tile that is on
    lightsout_board = []
    print "Welcome to Lights Out: A classic puzzle game!"
    print "The goal of Lights Out is to turn all of O's (lights that are on) into X's (lights that are off)."
    print "The game is won when your game board contains only X's and no O's.  At that point it's lights out!"
    print "Before we get started, I need to know how you want your board set up."

    column_choice = raw_input("How many columns should there be on the board? Please enter a number: >>> ")
    col_choice_valid_input = False
    while col_choice_valid_input == False:
        try:
            if int(column_choice) >= 1:
                column_choice = int(column_choice)
                col_choice_valid_input = True
            else:
                column_choice = raw_input("Invalid input. Please enter the number of columns you want: >>> ")
        except ValueError:
            column_choice = raw_input("Invalid input. Please enter the number of columns you want: >>> ")
    
    row_choice = raw_input("How many rows should there be on the board? Please enter a number: >>> ")
    row_choice_valid_input = False
    while row_choice_valid_input == False:
        try:
            if int(row_choice) >= 1:
                row_choice = int(row_choice)
                row_choice_valid_input = True
            else:
                row_choice = raw_input("Invalid input.  Please enter the number of rows you want: >>> ")
        except ValueError:
            row_choice = raw_input("Invalid input.  Please enter the number of rows you want: >>> ")
    
    col_range = range(column_choice)
    row_range = range(row_choice)
    
    for r in row_range:
        lightsout_board.append([])
        for c in col_range:
            cell = choice(random_selector_list)
            lightsout_board[r].append(cell)
    return lightsout_board

def lightsOut():
    """Allows the user to play a game of lights out"""
    lightsout_board = setUp()
    playing = True
    print "Good luck!"

    while playing:
        print "This is what the board currently looks like."
        for row in lightsout_board:
            print row
        
        num_rows = range(1, len(lightsout_board)+1)
        num_cols = range(1, len(lightsout_board[0])+1)

        column_selection = raw_input("There are %s cols on the board.  The cols are numbered 1-%s from left to right.  Please enter a col number 1-%s: >>> " % (len(num_cols), len(num_cols), len(num_cols)))
        col_valid_input = False
        while col_valid_input == False:
            try:
                if int(column_selection) in num_cols:
                    column_selection = int(column_selection)
                    col_valid_input = True
                else:
                    column_selection = raw_input("Invalid input.  Please enter a col number 1-%s: >>> " % (len(num_cols)))
            except ValueError:
                column_selection = raw_input("Invalid input.  Please enter a col number 1-%s: >>> " % (len(num_rows)))
        
        row_selection = raw_input("There are %s rows on the board.  The rows are numbered 1-%s from top to bottom.  Please enter a row number 1-%s: >>> " % (len(num_rows), len(num_rows), len(num_rows)))
        row_valid_input = False
        while row_valid_input == False:
            try:
                if int(row_selection) in num_rows:
                    row_selection = int(row_selection)
                    row_valid_input = True
                else:
                    row_selection = raw_input("Invalid input.  Please enter a row number 1-5: >>> ")
            except ValueError:
                row_selection = raw_input("Invalid input.  Please enter a row number 1-5: >>> ")
        
        user_selection = [column_selection, row_selection] # all coordinate pairs are represented as [x, y] where x is col and y is row
        focal_coords = [user_selection[0]-1, user_selection[1]-1]
        left_coords = [focal_coords[0]-1, focal_coords[1]]
        right_coords = [focal_coords[0]+1, focal_coords[1]]
        bottom_coords = [focal_coords[0], focal_coords[1]+1]
        top_coords = [focal_coords[0], focal_coords[1]-1]
        
        if lightsout_board[focal_coords[1]][focal_coords[0]] == "X":
            lightsout_board[focal_coords[1]][focal_coords[0]] = "O"
        else:
            lightsout_board[focal_coords[1]][focal_coords[0]] = "X"
        
        if left_coords[0] in range(len(lightsout_board[0])):
            if lightsout_board[left_coords[1]][left_coords[0]] == "X":
                lightsout_board[left_coords[1]][left_coords[0]] = "O"
            else:
                lightsout_board[left_coords[1]][left_coords[0]] = "X"
        
        if right_coords[0] in range(len(lightsout_board[0])):
            if lightsout_board[right_coords[1]][right_coords[0]] == "X":
                lightsout_board[right_coords[1]][right_coords[0]] = "O"
            else:
                lightsout_board[right_coords[1]][right_coords[0]] = "X"
                
        if bottom_coords[1] in range(len(lightsout_board)):
            if lightsout_board[bottom_coords[1]][bottom_coords[0]] == "X":
                lightsout_board[bottom_coords[1]][bottom_coords[0]] = "O"
            else:
                lightsout_board[bottom_coords[1]][bottom_coords[0]] = "X"
        
        if top_coords[1] in range(len(lightsout_board)):
            if lightsout_board[top_coords[1]][top_coords[0]] == "X":
                lightsout_board[top_coords[1]][top_coords[0]] = "O"
            else:
                lightsout_board[top_coords[1]][top_coords[0]] = "X"
        
        victory_checker = [item for each_row in lightsout_board for item in each_row]
        victory_checker = [item for item in victory_checker if item != "X"]
        
        if len(victory_checker) == 0:
            print "This is what the board currently looks like."
            for row in lightsout_board:
                print row 
            print "XX ~ ALL THE LIGHTS ARE OUT!  CONGRATULATIONS!  YOU WIN! ~ XX"
            playing = False
    return victory_checker
    
lightsOut()