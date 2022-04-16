
def main():

    gameBoard = {
        "1,1": " ", "1,2": " ", "1,3": " ",
        "2,1": " ", "2,2": " ", "2,3": " ",
        "3,1": " ", "3,2": " ", "3,3": " ",
    }

    print("welcome! Here is your board!" + "\n" +
          "Please enter your moves as row,column with no spaces!")

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
    playerOneMove = input(
        "\nPlayer One (X) where would you like to place an 'X'?")

    # for key in gameBoard:
    # if gameBoard[key] != " ":
    #     playerOneMove = input(
    #         "There has already been a move there, please select a different spot!")
    # elif playerOneMove not in gameBoard:
    #     playerOneMove = input(
    #         "That is not a valid spot, please select a different spot!")
    # else:
    gameBoard[playerOneMove] = "X"


def playerTwo(gameBoard):
    printBoard(gameBoard)
    playerTwoMove = input(
        "\nPlayer Two (O) where would you like to place an 'O'?")

    # for key in gameBoard:
    # if gameBoard[key] != " ":
    #     playerTwoMove = input(
    #         "There has already been a move there, please select a different spot!")
    # elif playerTwoMove not in gameBoard:
    #     playerTwoMove = input(
    #         "That is not a valid spot, please select a different spot!")
    # else:
    gameBoard[playerTwoMove] = "O"


def checkEndState(gameBoard):
    winningCombos = [["1,1", "1,2", "1,3"], ["2,1", "2,2", "2,3"], ["3,1", "3,2", "3,3"], ["1,1", "2,1", "3,1"],
                     ["1,2", "2,2", "3,2"], ["1,3", "2,3", "3,3"], ["1,1", "2,2", "3,3"], ["1,3", "2,2", "3,1"]]

    playerOneSpots = []
    playerTwoSpots = []

    for key in gameBoard:
        if "X" in gameBoard[key]:
            playerOneSpots.append(key)
            if winningCombos in playerOneSpots:
                print("Player One Wins!")
                win = input("Would you like to play again? y/n")
                win = win.lower()
                if win == "y":
                    main()
                else:
                    break
        else:
            if "O" in gameBoard[key]:
                playerTwoSpots.append(key)
                if playerTwoSpots in winningCombos:
                    print("Player Two Wins!")
                    win = input("Would you like to play again? y/n")
                    win = win.lower()
                    if win == "y":
                        main()
                    else:
                        break


def gamePlayLoop(gameBoard):
    turnCounter = 0
    while turnCounter < 5:
        playerOne(gameBoard)
        turnCounter += 1
        playerTwo(gameBoard)
        turnCounter += 1
        if turnCounter >= 5:
            playerOne(gameBoard)
            checkEndState(gameBoard)
            turnCounter += 1
            playerTwo(gameBoard)
            checkEndState(gameBoard)
            turnCounter += 1
        if turnCounter > 9:
            draw = input(
                "This game is a draw, would you like to play again? y/n")
            draw = draw.lower()
            if draw == "y":
                main()
            else:
                break

    # counter2 = 0
    # while counter2 < 100:
    #     playerOne(gameBoard)
    #     playerTwo(gameBoard)
    #     counter2 += 1


if __name__ == "__main__":
    main()
