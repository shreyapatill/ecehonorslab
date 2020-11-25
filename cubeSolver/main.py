from tkinter import *
from solve import *

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
        valid = Label(root,text="Valid input").grid(row=5, columnspan=12)


# make a button to check whether the input is valid
check = Button(root, text="Check Input", command=check_tiles).grid(row=3, columnspan=12)

# calls solve function
check = write_solution(str(colors))

# solve function returns "R L R' L'" for both invalid inputs & solved inputs, so we need to check:
if check == "R L R' L'":
    if colors != ["U", "U", "U",
                  "U", "U", "U",
                  "U", "U", "U",
                  "L", "L", "L", "F", "F", "F", "R", "R", "R", "B", "B", "B",
                  "L", "L", "L", "F", "F", "F", "R", "R", "R", "B", "B", "B",
                  "L", "L", "L", "F", "F", "F", "R", "R", "R", "B", "B", "B",
                  "D", "D", "D",
                  "D", "D", "D",
                  "D", "D", "D"]:
        invalid = Label(root, text="Invalid input", bg='red').grid(row=5, columnspan=12)
    else:
        valid = Label(root,text="Already Solved", bg='green').grid(row=5, columnspan=12)

root.mainloop()
