#Yong Da Li
#Tuesday, February 12, 2019
#Professor Nebu Mathai
#CSC190

#assignment A - chess player
#test file

from chessPlayer import*

#sandbox mode, pieces can be moved anywhere
#for testing legal moves and under threat
def debug_mode():
    board = Board()
    choice = 1
    while(choice != 0):
        board.print()
        print("\n")

        print("0. quit")
        print("1. move")
        print("2. legal moves")
        print("3. under threat")
        choice = int(input("\nEnter choice: "))

        if choice == 0:
            break
        elif choice == 1:
            user_move(board)
        elif choice == 2:
            print_legal_moves(board)
        elif choice == 3:
            print_is_pos_under_threat(board)

        print("*" * 41)


#user specifies all moves
#all moves are legal
#user can see what moves are legal in any position
def manual_test():
    board = Board()

    while(1):
        board.print()
        user_move(board)
        board.print()
        print_legal_moves(board)
        print_is_pos_under_threat(board)
        print("*" * 41)


#user moves first, all moves are legal
#computer moves randomly, only legal moves
def random_ai_test():
    board = Board()
    while(1):
        board.print()
        user_move(board)
        board.print()
        random_computer_move(board)
        print("*" * 41)


#user moves first, all moves are legal for user
#computer moves randomly
def ai_test():
    board = Board()
    while(1):
        board.print()
        print("\nHuman")
        legal_user_move(board)
        display_status(board, 10)

        board.print()
        print("Computer\n")
        computer_move(board)
        #display_status(board, 20)
        print("*" * 41)


#test for correct return format, in lab spec
def format_test():
    board = Board()
    board_list = board.get_list()
    player = 20

    r = chessPlayer(board_list, player)
    print("return:", r)


def main():
    #debug_mode()
    #manual_test()
    ai_test()
    #format_test()

main()