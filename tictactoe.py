
class cell:
    def __init__(self, display):
        self.number = display       # the location of the element in the array
        self.value = display       # default character is _, will become either X or O
        self.claimed = False
    def printNumber(self): return self.number
    def printValue(self): return self.value
    def setValue(self, player): self.value = player
    def printClaimed(self): return self.claimed
    def setClaimedTrue(self): self.claimed = True

board = []      # list of lists that stores the board

# making a 3x3 array of cells
counter = 0
board = []
for x in range(3):
    row = []
    for y in range(3):
        counter += 1
        row.append(cell(counter))
        #print(row[-1].printValue())
    board.append(row)

# Print the board contents
def printBoard():
    print()
    for row in board:
        for element in row:
            print(element.printValue(), " | ", end = '')
        print()
    print()

def editCell(num, player):
    for row in board:

        for element in row:
            if element.printNumber() == num:
                if element.printClaimed() == True:
                    print("That location is already taken. Please try again.")
                    return False
                element.setValue(player)
                element.setClaimedTrue()
                print(element.printNumber(), " ", element.printValue())
                return True

# Returns true if someone won              
def checkIfWinner(player):
    # Check horizontals
    for row in board:
        if row[0].value == player and row[1].value == player and row[2].value == player:
            return True

    # Check Verticals the lazy way
    if board[0][0].value == player and board[1][0].value == player and board[2][0].value == player:
        return True
    if board[0][1].value == player and board[1][1].value == player and board[2][1].value == player:
        return True
    if board[0][2].value == player and board[1][2].value == player and board[2][2].value == player:
        return True

    # Check Diagonals
    if board[0][0].value == player and board[1][1].value == player and board[2][2].value == player:
        return True
    if board[0][2].value == player and board[1][1].value == player and board[2][0].value == player:
        return True

    return False
    
    



def main():
    flag = True
    player = 'X'

    print("\nWelcome to tic tac toe\n")

    while flag == True:
        printBoard()

        print("It is currently player ", player, "'s turn.")

        cellCheck = False
        newVal = 33
        while newVal > 9 or newVal < 1 or cellCheck == False:
            newVal = int(input("Please enter the location you want to claim:\t"))
            print(newVal)

            #edit the chosen cell
            cellCheck = editCell(newVal, player)
           
        if checkIfWinner(player) == True:
            printBoard()
            print("Conglaturation, player ", player, " is winner!\n\n")
            break


        if player == 'X': player = 'O'
        else: player = 'X'



   
    

if __name__ == "__main__":
    main()


