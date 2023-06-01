from tkinter import *
import random

def minesweeper():
    global root
    root = Tk()

    board = []

    # Creates the board in array form
    for row in range(0, 20):
        board.append([])
        for column in range(0, 24):
            board[row].append([])

    buttonPresed = []
    for row in range(0, 20):
        buttonPresed.append([])
        for column in range(0, 24):
            buttonPresed[row].append("no")

    mineLocations = {}
    # Creates a dictionary of mine locations
    for counter in range(0, 20):
        mineLocations.update({counter: []})

    def populateMines(row, column):
        mineCounter = 99
        while mineCounter != 0:
            mineRow = random.randint(0, 19)
            mineColumn = random.randint(0, 23)

            if mineColumn not in mineLocations[mineRow]:
                # If the mine
                if abs(mineRow - row) <= 1 and abs(mineColumn - column) <= 1:
                    continue
                else:
                    board[mineRow][mineColumn] = "Mine"
                    mineLocations[mineRow].append(mineColumn)
                    mineCounter -= 1


    numberBoard = []

    def calculateAdjacentMines():
        for row in range(0, 20):
            numberBoard.append([])
            for column in range(0, 24):
                numberBoard[row].append([])

        for numberRow in range(0, 20):
            for numberColumn in range(0, 24):
                adjacentMines = 0
                if board[numberRow][numberColumn] == "Mine":
                    numberBoard[numberRow][numberColumn] = "M"
                    continue

                for row_offset in [-1, 0, 1]:
                    for col_offset in [-1, 0, 1]:
                        if row_offset == 0 and col_offset == 0:
                            continue
                        row = numberRow + row_offset
                        col = numberColumn + col_offset
                        if 0 <= row < 20 and 0 <= col < 24:
                            if board[row][col] == "Mine":
                                adjacentMines += 1

                numberBoard[numberRow][numberColumn] = adjacentMines

    initialSetup = {"status": "not set up"}

    def pressAdjacentButtons(replaceRow, replaceColumn):
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                if row_offset == 0 and col_offset == 0:
                    continue
                row = replaceRow + row_offset
                col = replaceColumn + col_offset
                if 0 <= row < 20 and 0 <= col < 24:
                    if buttonPresed[row][col] == "no":
                        buttonArray[row][col].invoke()

    def showMine(button):
        if "pyimage" in button.cget("image"):
            return
        mine = Label(root, text="M")
        replaceRow = int(button.grid_info()['row'])
        replaceColumn = int(button.grid_info()['column'])



        if initialSetup["status"] == "not set up":
            populateMines(replaceRow, replaceColumn)

            calculateAdjacentMines()

            initialSetup["status"] = "has been set up"

        # if replaceColumn in mineLocations[replaceRow]:
        #     mine.grid(row=replaceRow, column=replaceColumn)
        #     window = Toplevel(root)
        #     defeat = Label(window, text = "Oops! You've stepped on a mine. Better luck next time.")
        #     restart = Button(window, text="Restart", command=lambda: refresh())
        #     defeat.grid()
        #     restart.grid()
        if replaceColumn in mineLocations[replaceRow]:
            mine.grid(row=replaceRow, column=replaceColumn)
            window = Toplevel(root)
            defeat = Label(window, text="Oops! You've stepped on a mine. Better luck next time.")
            restart = Button(window, text="Restart", command=lambda: refresh())
            defeat.pack(expand=True)
            restart.pack()

            #The update_idletasks method is called on the root window to make sure that its size and position have been calculated.
            # Then, the winfo_screenwidth, winfo_screenheight, winfo_reqwidth, and winfo_reqheight methods are used to get the width and height
            # of the screen and the required width and height of the root window. These values are used to calculate
            # the coordinates of the top-left corner of the root window such that it is centered on the screen.
            window.update_idletasks()
            x = (window.winfo_screenwidth() - window.winfo_reqwidth()) // 2
            y = (window.winfo_screenheight() - window.winfo_reqheight()) // 2
            window.geometry(f"+{x}+{y}")
        else:
            number = str(numberBoard[replaceRow][replaceColumn])
            colors = {"1": "blue", "2": "green", "3": "red", "4": "purple", "5": "maroon", "6": "cyan", "7": "black",
                      "8": "orange"}

            if number == "0":
                empty = Label(root, padx=7, pady=1, bg="#bdbdbd")
                empty.grid(row=replaceRow, column=replaceColumn)
                numberOfEmpty = 1
                buttonPresed[replaceRow][replaceColumn] = "yes"
                pressAdjacentButtons(replaceRow, replaceColumn)
            else:
                # If no number is found, then #bdbdbd is used as default
                color = colors.get(number, "#bdbdbd")
                numberLabel = Label(root, padx=7, pady=1, text=number, bg="#bdbdbd", fg=color)
                numberLabel.grid(row=replaceRow, column=replaceColumn)


    def left(event):
        # print('clicked left')
        pass


    photo = PhotoImage(file='flag.png')
    # photo = photo.zoom(2)
    photo = photo.subsample(10)


    # Photos can't be created in functions

    def right(event):
        replaceRow = int(event.widget.grid_info()['row'])
        replaceColumn = int(event.widget.grid_info()['column'])
        # flag = Label(root, text="F")
        # flag.grid(row=replaceRow, column=replaceColumn)

        # if event.widget.cget("image") == "pyimage2":
        if "pyimage" in event.widget.cget("image"):
            # The image is called pyimage2 for some reason. Checked with cget
            event.widget.config(image='')
            # print(event.widget.cget("image"))
        else:
            event.widget.config(image=photo)
            # print(event.widget.cget("image"))
            # event.widget.config(state=DISABLED)

    buttons = []
    for i in range(1, 481):
        button = Button(root, text="", padx=7, pady=1)
        button.config(command=lambda b=button: showMine(b))
        buttons.append(button)

    buttonArray = []

    # Creates the board in array form
    for row in range(0, 20):
        buttonArray.append([])
        for column in range(0, 24):
            buttonArray[row].append([])

    loopRow = 0
    loopColumn = 0
    for b in root.children:
        if loopColumn == 24:
            loopColumn = 0
            loopRow += 1
        buttonArray[loopRow][loopColumn] = root.children.get(b)
        root.children.get(b).grid(row=loopRow, column=loopColumn)
        root.children.get(b).bind('<Button-1>', left)
        root.children.get(b).bind('<Button-3>', right)
        loopColumn += 1

    # The update_idletasks method is called on the root window to make sure that its size and position have been calculated.
    # Then, the winfo_screenwidth, winfo_screenheight, winfo_reqwidth, and winfo_reqheight methods are used to get the width and height
    # of the screen and the required width and height of the root window. These values are used to calculate
    # the coordinates of the top-left corner of the root window such that it is centered on the screen.
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) // 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) // 2
    root.geometry(f"+{x}+{y}")
    root.mainloop()

def refresh():
    root.destroy()
    minesweeper()

minesweeper()