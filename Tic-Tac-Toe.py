
def main():

    gameBoard = {
        "1,1": " ", "1,2": " ", "1,3": " ",
        "2,1": " ", "2,2": " ", "2,3": " ",
        "3,1": " ", "3,2": " ", "3,3": " ",
    }

    gamePlayLoop(gameBoard)


def printBoard(board):
    counter = 0
    for key in board:
        counter += 1
        if ",2" in key:
            print("|" + board[key] + "|", end="")
        else:
            print(board[key], end="")
        if counter % 3 == 0 and counter < 7:
            print("\n" + "-" + "+" + "-" + "+" + "-")


def playerOne(gameBoard):
    printBoard(gameBoard)
    movePlaced = False
    while movePlaced == False:
        playerOneMove = input(
            "\nPlayer One (X) where would you like to place an 'X'?")

        if playerOneMove not in gameBoard:
            print(
                "That is not a valid spot, please select a different spot!")
        elif gameBoard[playerOneMove] != " ":
            print(
                "There has already been a move there, please select a different spot!")
        else:
            gameBoard[playerOneMove] = "X"
            movePlaced = True


def playerTwo(gameBoard):
    printBoard(gameBoard)
    movePlaced = False
    while movePlaced == False:
        playerTwoMove = input(
            "\nPlayer Two (O) where would you like to place an 'O'?")

        if playerTwoMove not in gameBoard:
            print(
                "That is not a valid spot, please select a different spot!")
        elif gameBoard[playerTwoMove] != " ":
            print(
                "There has already been a move there, please select a different spot!")
        else:
            gameBoard[playerTwoMove] = "O"
            movePlaced = True


def checkEndState(gameBoard):
    winningCombos = [["1,1", "1,2", "1,3"], ["2,1", "2,2", "2,3"], ["3,1", "3,2", "3,3"], ["1,1", "2,1", "3,1"],
                     ["1,2", "2,2", "3,2"], ["1,3", "2,3", "3,3"], ["1,1", "2,2", "3,3"], ["1,3", "2,2", "3,1"]]

    playerOneSpots = []
    playerTwoSpots = []

    for key in gameBoard:
        if "X" in gameBoard[key]:
            playerOneSpots.append(key)
            for combo in winningCombos:
                if all(elem in playerOneSpots for elem in combo) and len(playerOneSpots) >= 3:
                    print("Player One Wins!")
                    endGamePrompt()

        else:
            if "O" in gameBoard[key]:
                playerTwoSpots.append(key)
                for combo in winningCombos:
                    if all(elem in playerTwoSpots for elem in combo) and len(playerTwoSpots) >= 3:
                        print("Player Two Wins!")
                        endGamePrompt()

    if len(playerOneSpots) == 5 and len(playerTwoSpots) == 4:
        while True:
            answer = input(
                "This game is a draw, would you like to play again? y/n")
            answer = answer.lower()
            if answer == "y":
                main()
            elif answer == "n":
                exit()
            else:
                print("Please enter either 'y' or 'n'")


def endGamePrompt():
    while True:
        answer = input("Would you like to play again? y/n")
        answer = answer.lower()
        if answer == "y":
            main()
        elif answer == "n":
            exit()
        else:
            print("Please enter either 'y' or 'n'")


def gamePlayLoop(gameBoard):
    print("welcome! Here is your board!" + "\n" +
          "Please enter your moves as row,column with no spaces!")
    turnCounter = 0
    while turnCounter <= 10:
        checkEndState(gameBoard)
        playerOne(gameBoard)
        checkEndState(gameBoard)
        turnCounter += 1
        checkEndState(gameBoard)
        playerTwo(gameBoard)
        checkEndState(gameBoard)
        turnCounter += 1


if __name__ == "__main__":
    main()
