import numpy as np

def isvalid(board, i, j, num):
    tst =np.array(board)
    if num in tst[i]:
        return False
    if num in tst[:,j]:
        return False
    il = i//3*3
    ih = i//3*3+3
    jl = j//3*3
    jh = j//3*3+3

    checkarray = tst[il:ih,jl:jh]
    if num in checkarray:
        return False
    return True


def bt(board, n_ele):
    global fi, res
    if n_ele >=79:
        res = board.copy()
        fi =True
        return

    else:
        i = n_ele // 9
        j = n_ele % 9
        if board[i][j] != '.':
            bt(board, n_ele + 1)
        else:
            for number in range(1, 10):
                if not isvalid(board, i, j, str(number)):
                    continue
                board[i][j] = str(number)
                bt(board, n_ele + 1)
                if not fi:
                    board[i][j] = '.'
                else:
                    return



board =[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
lst = np.array(board)
lastele = np.where(lst =='.')[0][-1]*9 + np.where(lst =='.')[1][-1]

res =[]
fi = False
bt(board, 0)
print(res)