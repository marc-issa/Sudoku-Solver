def userInput(): #*
    bo = []
    for i in range(9):
        new = list(map(int, input().split()))
        bo.append(new)
        print(bo)

    return bo


def print_sudoku(bo):
    print("\nBoard:\n")
    h = 0
    v = 0
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if len(bo[i]) % 9 == 0:
                print(bo[i][j], end=" ")
                v += 1
                if v % 3 == 0 and v % 9 != 0:
                    print("|", end=" ")
        print("\n")

        h += 1
        if h % 3 == 0 and h % 9 != 0:
            print("----------------------")


def valid(bo, num, pos): #*
    # row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # col
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # square
    x = pos[0] // 3
    y = pos[1] // 3

    for i in range(x * 3, x * 3 + 3):
        for j in range(y * 3, y * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def empty_box(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return i, j  # row and column


def solve(bo):
    find = empty_box(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True

            bo[row][col] = 0

    return False


# board = userInput()
board = [
    [5, 0, 0, 0, 0, 0, 9, 0, 2],
    [0, 7, 2, 1, 0, 0, 0, 0, 8],
    [0, 0, 8, 3, 0, 0, 5, 0, 7],
    [8, 0, 0, 7, 6, 0, 0, 0, 3],
    [4, 0, 0, 0, 0, 0, 0, 9, 1],
    [0, 0, 0, 9, 0, 4, 8, 0, 6],
    [0, 6, 0, 0, 3, 7, 2, 0, 4],
    [0, 8, 0, 0, 1, 0, 0, 0, 5],
    [0, 4, 0, 2, 0, 6, 0, 7, 0],
]
solve(board)
print_sudoku(board)
