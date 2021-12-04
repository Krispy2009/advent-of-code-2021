from copy import deepcopy
import pdb


def calculate_score(board, marked_board):
    sum = 0
    for j, line in enumerate(marked_board):
        for k, num in enumerate(line):
            if num == 0:
                sum += board[j][k]

    print(f"SUM: {sum}")
    return sum


def make_marked_boards(boards):
    marked_boards = deepcopy(boards)
    for i, board in enumerate(boards):
        for j, line in enumerate(board):
            for k, num in enumerate(line):

                marked_boards[i][j][k] = 0
    return marked_boards


def mark_board(number, boards, marked_boards):
    print(f"CALLING {number}")
    for i, board in enumerate(boards):
        for j, line in enumerate(board):
            for k, num in enumerate(line):
                if num == number:
                    marked_boards[i][j][k] = 1
    return marked_boards


def check_boards_for_win(marked_boards, already_marked=None):
    if already_marked is None:
        already_marked = []
    for b, board in enumerate(marked_boards):
        if b in already_marked:
            continue
        for col_idx in range(5):
            col_sum = 0
            for l, line in enumerate(board):
                if sum(line) == 5:
                    print(f"ROW BINGO! {board}")
                    return b, board
                else:
                    col_sum += line[col_idx]
                    if col_sum == 5:
                        print(f"COLUMN BINGO! {board}")
                        return b, board
    return (None, None)


def part1(marked_boards):
    for idx, number in enumerate(numbers):
        marked_boards = mark_board(number, boards, marked_boards)
        if idx > 5:
            w, _ = check_boards_for_win(marked_boards)
            if w:
                score = calculate_score(boards[w], marked_boards[w])
                print(f"ANS: {score*number}")
                exit()


def any_more_marked_wins(marked_boards):
    boards_to_pop = []
    for board in marked_boards:
        w, _ = check_boards_for_win(marked_boards, already_marked=boards_to_pop)
        if w is not None:
            print(f"Adding {w} to boards to pop")
            boards_to_pop.append(w)
    return reversed(boards_to_pop)


def part2(marked_boards):
    for idx, number in enumerate(numbers):
        marked_boards = mark_board(number, boards, marked_boards)
        if idx > 5:
            w, _ = check_boards_for_win(marked_boards)
            if w is not None:
                score = calculate_score(boards[w], marked_boards[w])
                print(f"ANS: {score*number}")
                boards.pop(w)
                marked_boards.pop(w)
            boards_to_pop = any_more_marked_wins(marked_boards)
            for b in boards_to_pop:
                print(f"----Will be Poppin  extras-------")
                # score = calculate_score(boards[w], marked_boards[w])
                # print(f"popped ANS: {score*number}")

                boards.pop(b)
                marked_boards.pop(b)


with open("input.txt") as f:
    board, boards = [], []
    for line in f.readlines():
        if len(line) > 15:
            numbers = [int(n) for n in line.split(",")]
        elif len(line) > 1:
            if len(board) < 5:
                board.append([int(n.strip()) for n in line.strip().split(" ") if n != ""])
            else:
                print("APPEND")
                boards.append(board)
                board = []
                board.append([int(n.strip()) for n in line.strip().split(" ") if n != ""])
        if line == "\n" and len(board) == 5:
            print("APPEND")
            boards.append(board)
            board = []

    marked_boards = make_marked_boards(boards)
    # part1(marked_boards)
    part2(marked_boards)

