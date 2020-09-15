def solveSudoku(board):
    '''
    解数独

    :param board: 一个9 * 9的二维字符数组，表示数独题目，其中'.'代表空格
    :return: 不需要返回值，原位修改题目的二维数组，将其中的'.'号替换为正确的数字
    '''

    def dfs(pos: int):
        nonlocal valid
        if pos == len(spaces):
            valid = True
            return

        i, j = spaces[pos]
        for digit in range(9):
            if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
            if valid:
                return

    line = [[False] * 9 for _ in range(9)]
    column = [[False] * 9 for _ in range(9)]
    block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
    valid = False
    spaces = list()

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                spaces.append((i, j))
            else:
                digit = int(board[i][j]) - 1
                line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

    dfs(0)


b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoku(b)
