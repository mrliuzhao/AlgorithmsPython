def solveNQueens(n):
    '''
    解决N皇后问题的方法

    :param n: 在n*n的棋盘上放置N个皇后
    :return: 返回N个皇后所有可能的位置
    '''
    res = []

    def walk(sub):
        if len(sub) == n:
            subres = []
            for k in sub:
                subtemp = ['.' for _ in range(n)]
                subtemp[k] = 'Q'
                subres.append(''.join(subtemp))
            res.append(subres)
        else:
            col_inavailable = set()
            for i in range(len(sub)):
                col_inavailable.add(sub[i])
                if sub[i] + (len(sub) - i) >= 0:
                    col_inavailable.add((sub[i] + (len(sub) - i)))
                if sub[i] - (len(sub) - i) >= 0:
                    col_inavailable.add((sub[i] - (len(sub) - i)))
            temp = set(range(n))
            col_available = temp - col_inavailable
            if len(col_available) > 0:
                for c in col_available:
                    subtemp = sub.copy()
                    subtemp.append(c)
                    walk(subtemp)
    for j in range(n):
        walk([j])
    return res