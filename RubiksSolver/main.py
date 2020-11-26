from tkinter import *
import solver as sv
import motorOutput

root = Tk()

# creating a Label widget (directions)
directions = Label(root,
                   text="Click on tile to change color. Be sure to match your inputs exactly to the pattern on your Rubik's Cube.").grid(
    row=0, columnspan=12)

# initial color input
# U=blue, L=orange, F=white, R=red, B=yellow, D=green
colors = ["U", "U", "U",
          "U", "U", "U",
          "U", "U", "U",
          "L", "L", "L", "F", "F", "F", "R", "R", "R", "B", "B", "B",
          "L", "L", "L", "F", "F", "F", "R", "R", "R", "B", "B", "B",
          "L", "L", "L", "F", "F", "F", "R", "R", "R", "B", "B", "B",
          "D", "D", "D",
          "D", "D", "D",
          "D", "D", "D"]
# array of buttons to represent tiles
tiles = []

# changes color of tiles on click
def color_change(i, bt):
    if colors[i] == "U":
        bt.configure(bg="yellow")
        colors[i] = "B"
    elif colors[i] == "B":
        bt.configure(bg="white")
        colors[i] = "F"
    elif colors[i] == "F":
        bt.configure(bg="orange")
        colors[i] = "L"
    elif colors[i] == "L":
        bt.configure(bg="green")
        colors[i] = "D"
    elif colors[i] == "D":
        bt.configure(bg="red")
        colors[i] = "R"
    elif colors[i] == "R":
        bt.configure(bg="blue")
        colors[i] = "U"

# creates top face
for tile_number in range(0, 9):
    temp_button = Button(root, text=str(tile_number), height=3, width=6, bg="blue")

    if tile_number != 4:  # all but center tile can change color
        temp_button.configure(command=lambda i=tile_number, j=temp_button: color_change(i, j))

    col = tile_number % 3 + 3
    ro = int(tile_number / 3) + 6
    temp_button.grid(row=ro, column=col)
    tiles.append(temp_button)

# creates middle faces
for tile_number in range(9, 45):
    temp_button = Button(root, text=str(tile_number), height=3, width=6)

    if colors[tile_number] == "L":
        temp_button.configure(bg="orange")
    elif colors[tile_number] == "F":
        temp_button.configure(bg="white")
    elif colors[tile_number] == "R":
        temp_button.configure(bg="red")
    else:
        temp_button.configure(bg="yellow")

    if tile_number != 22 and tile_number != 25 and tile_number != 28 and tile_number != 31:
        temp_button.configure(command=lambda i=tile_number, j=temp_button: color_change(i, j))

    col = (tile_number + 3) % 12
    ro = int((tile_number + 3) / 12) + 8
    temp_button.grid(row=ro, column=col)
    tiles.append(temp_button)

# creates bottom face
for tile_number in range(45, 54):
    temp_button = Button(root, text=str(tile_number), height=3, width=6, bg="green")

    if tile_number != 49:  # all but center tile can change color
        temp_button.configure(command=lambda i=tile_number, j=temp_button: color_change(i, j))

    col = tile_number % 3 + 3
    ro = int(tile_number / 3) + 12
    temp_button.grid(row=ro, column=col)
    tiles.append(temp_button)


# method to print the tile colors
def print_colors():
    color_input = Label(root, text=colors).grid(row=2, columnspan=12)
    return colors

# submit button that returns the array of colors
color_button = Button(root, text="Print colors", command=print_colors).grid(row=1, columnspan=12)


# method to check number of tiles for each color
def check_tiles():
    count_dict = {i: colors.count(i) for i in colors}
    count_print = Label(root, text=count_dict).grid(row=4, columnspan=12)
    for key in count_dict:
        if (count_dict[key] > 9):
            invalid = Label(root, text="Invalid input", bg='red').grid(row=5, columnspan=12)
            break
    else:
        valid = Label(root,text="   Valid input   ").grid(row=5, columnspan=12) #extra whitespace so red from invalid doesn't show up


#cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'  # cube definition string of cube we want to solve
# See module enums.py for the format of the cube definition string

#Orignal cubestring, must convert
#               ----------------
#               | 0  | 1  | 2  |
#               ----------------
#               | 3  | 4  | 5  |
#               ----------------
#               | 6  | 7  | 8  |
#               ----------------
#-------------------------------------------------------------
#| 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
#-------------------------------------------------------------
#| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 |
#-------------------------------------------------------------
#| 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 |
#-------------------------------------------------------------
#               ----------------
#               | 45 | 46 | 47 |
#               ----------------
#               | 48 | 49 | 50 |
#               ----------------
#               | 51 | 52 | 53 |
#

def converter(cubeArray):
    #input: an array with cube letters in above format
    #output: a string with cube letters in below format
    toReturn = ""
    for i in range(9): #U face
        toReturn += cubeArray[i]
    toReturn += cubeArray[15] + cubeArray[16] + cubeArray[17] #R face
    toReturn += cubeArray[27] + cubeArray[28] + cubeArray[29]
    toReturn += cubeArray[39] + cubeArray[40] + cubeArray[41]
    toReturn += cubeArray[12] + cubeArray[13] + cubeArray[14] #F face
    toReturn += cubeArray[24] + cubeArray[25] + cubeArray[26]
    toReturn += cubeArray[36] + cubeArray[37] + cubeArray[38]
    for i in range(45, 54): #D face
        toReturn += cubeArray[i]
    toReturn += cubeArray[9]  + cubeArray[10] + cubeArray[11] #L face
    toReturn += cubeArray[21] + cubeArray[22] + cubeArray[23]
    toReturn += cubeArray[33] + cubeArray[34] + cubeArray[35]
    toReturn += cubeArray[18] + cubeArray[19] + cubeArray[20] #B face
    toReturn += cubeArray[30] + cubeArray[31] + cubeArray[32]
    toReturn += cubeArray[42] + cubeArray[43] + cubeArray[44]
    return toReturn

"""""
    The names of the facelet positions of the cube
                  |************|
                  |*U1**U2**U3*|
                  |************|
                  |*U4**U5**U6*|
                  |************|
                  |*U7**U8**U9*|
                  |************|
     |************|************|************|************|
     |*L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*|
     |************|************|************|************|
     |*L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*|
     |************|************|************|************|
     |*L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*|
     |************|************|************|************|
                  |************|
                  |*D1**D2**D3*|
                  |************|
                  |*D4**D5**D6*|
                  |************|
                  |*D7**D8**D9*|
                  |************|
    A cube definition string "UBL..." means for example: In position U1 we have the U-color, in position U2 we have the
    B-color, in position U3 we have the L color etc. according to the order U1, U2, U3, U4, U5, U6, U7, U8, U9, R1, R2,
    R3, R4, R5, R6, R7, R8, R9, F1, F2, F3, F4, F5, F6, F7, F8, F9, D1, D2, D3, D4, D5, D6, D7, D8, D9, L1, L2, L3, L4,
    L5, L6, L7, L8, L9, B1, B2, B3, B4, B5, B6, B7, B8, B9 of the enum constants.
    """

# make a button to check whether the input is valid
check = Button(root, text="Check Input", command=check_tiles).grid(row=3, columnspan=12)

#root.mainloop()

LOOP_ACTIVE = True
while LOOP_ACTIVE:
    try:
        root.update()
    except TclError:
        # calls solve function
        #print(colors)
        cubestring = converter(colors)
        #print(cubestring)
        moves = sv.solve(cubestring, 25, 2)
        print(moves)
        
        motorOutput.motorSolve(moves)

        #write the solution into a file so C++ can use it
        #with open('solutionMoves.txt', 'w') as filehandle:
        #    for listitem in moves.split():
        #        filehandle.write('%s\n' % listitem)

        LOOP_ACTIVE = False