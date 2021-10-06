'''
Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, 
a column, or a diagonal with either three x's 
or three o's drawn in the spaces of a grid of nine squares.
'''
# This is created By Taylor Paxman



print("Welcome to Tic-Tac-Toe")

board = ["1","2","3","4","5","6","7","8","9"]
        


def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def player_move(input,symbol):
    if int(input) == 1:
        board[0] = symbol
    elif int(input) == 2:
        board[1] = symbol
    elif int(input) == 3:
        board[2] = symbol
    elif int(input) == 4:
        board[3] = symbol
    elif int(input) == 5:
        board[4] = symbol
    elif int(input) == 6:
        board[5] = symbol
    elif int(input) == 7:
        board[6] = symbol
    elif int(input) == 8:
        board[7] = symbol
    elif int(input) == 9:
        board[8] = symbol
    
    

def main():
    display_board(board)

x = 1
display_board(board)
while x < 9:
    player_1_sym = "x"
    player_2_sym = "o"
    

    if (x % 2) != 0:
        player_1 = input("x, pick a Number 1-9:")
        if board[int(player_1) - 1] in (player_1_sym, player_2_sym):
            print("That spot's taken, Pick another number")
            player_1 = input("x, pick a Number 1-9:")
      
        
        player_move(player_1,player_1_sym)
    else:
        player_2 = input("o, pick a Number 1-9:")
        if board[int(player_2) - 1] in (player_2_sym, player_1_sym):
            print("That spot's taken, Pick another number")
            player_2 = input("o, pick a Number 1-9:")
        
        player_move(player_2,player_2_sym)

    display_board(board)

    if (board[0] == board[1] == board[2]):
        print("Congrats, you Win")
        break
    elif board[3] == board[4] == board[5]:
        print("Congrats, you Win")
        break
    elif board[6] == board[7] == board[8]:
        print("Congrats, you Win")
        break
    elif board[0] == board[4] == board[8]:
        print("Congrats, you Win")
        break
    elif board[2] == board[4] == board[6]:
        print("Congrats, you Win")
        break
    elif board[0] == board[3] == board[6]:
        print("Congrats, you Win")
        break
    elif board[1] == board[4] == board[7]:
        print("Congrats, you Win")
        break
    elif board[2] == board[5] == board[8]:
        print("Congrats, you Win")
        break



    x += 1
    




    #display_board(board)


if __name__ == "__main__":
    main()