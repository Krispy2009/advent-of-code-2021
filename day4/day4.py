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
    print(marked_boards)
    return marked_boards


def mark_board(number, boards, marked_boards):
    print(f"CALLING {number}")
    for i, board in enumerate(boards):
        for j, line in enumerate(board):
            for k, num in enumerate(line):
                if num == number:
                    print(f"match! board: {i}, line: {j}, idx: {k}")
                    marked_boards[i][j][k] = 1
    print(marked_boards)
    return marked_boards


def check_boards_for_win(marked_boards):
    for b, board in enumerate(marked_boards):
        for col_idx in range(5):
            col_sum = 0
            for l, line in enumerate(board):
                if sum(line) == 5:
                    print("BINGO!")
                    return b, board
                else:
                    col_sum += line[col_idx]
                    if col_sum == 5:
                        print("BINGO!")
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


def part2(marked_boards):
    for idx, number in enumerate(numbers):
        print(f"{len(boards)}, {len(marked_boards)}")

        marked_boards = mark_board(number, boards, marked_boards)
        if idx > 5:
            w, _ = check_boards_for_win(marked_boards)
            if w is not None:
                score = calculate_score(boards[w], marked_boards[w])
                print(f"ANS: {score*number}")
                boards.pop(w)
                marked_boards.pop(w)
                print("pop pop poppin")


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

