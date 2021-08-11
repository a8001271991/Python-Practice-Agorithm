######################################################
# 1. for loop 從 (0, 0) 開始放
#    1-1. 檢查是否可以放 Queen (檢查前一行的左上，上，右上)
#         1-1-1. 不可，移動到下一個 col
#         1-1-2. 可以，放 Queen，移動到下一個 row
#                1-1-3. 重複步驟 1-1
#    1-2. 如果已經到最後一個 row，代表找到一個可能組合
######################################################

# global variable
boardSize = 0       # 棋盤大小
result = []         # 輸出的答案組合
queen = []      # 目前 Queen 的所在位置
cols = []

def checkAvailable(coor: tuple) -> bool:
    row = coor[0]
    col = coor[1]

    # 檢查是同個 col 中是否有 Queen
    if col in cols:
        print('checkAvailable FALSE, coor = %s, cols = %s' %(coor, cols))
        return False
    
    # 算出左斜角的所有位置
    checkTargetDia = list()
    for i in range(1, row + 1):
        checkTargetDia.append((row - 1 * i, col - 1 * i))

    # 算出右斜角的所有位置
    checkTargetOffDia = list()
    for i in range(1, row + 1):
        checkTargetOffDia.append((row - 1 * i, col + 1 * i))

    checkTarget = list()
    checkTarget = checkTargetDia + checkTargetOffDia

    # 檢查是斜角中是否有 Queen
    for item in queen:
        if item in checkTarget:
            print('checkAvailable FALSE, coor = %s, cols = %s, checkTarget = %s' %(cols, coor, checkTarget))
            return False

    print('checkAvailable FALSE, coor = %s, cols = %s, checkTarget = %s' %(coor, cols, checkTarget))
    return True

def resultFormat() -> list[str]:
    print('resultFormat queen = %s' %(queen))
    board = list()
    for item in queen:
        formatString = "." * item[1] + "Q" + "." * (boardSize - item[1] - 1)
        print('resultFormat formatString = ' + str(formatString))
        board.append(formatString)
    
    print('resultFormat board = %s' + str(board))
    return board

def dfs(row: int):
    if row == boardSize:
        print('dfs find solution!')
        result.append(resultFormat())
    else:
        print('dfs tracing')
        for col_idx in range(boardSize):
            currentCoor = (row, col_idx)
            print('dfs currentCoor = ' + str(currentCoor))
            if checkAvailable(currentCoor):
                queen.append(currentCoor)
                cols.append(col_idx)

                dfs(row + 1)

                queen.remove(currentCoor)
                cols.remove(col_idx)

def solveQueens(row: int):
    dfs(0)

print('Please input boardSize')
input = input()
if input.isdigit():
    boardSize = int(input)
    solveQueens(boardSize)
    print('The are ' + str(len(result)) + ' possible solutions.')
    print('Answers are: ')
    for answers in result:
        print(answers)
else:
    print('Invalid value!')