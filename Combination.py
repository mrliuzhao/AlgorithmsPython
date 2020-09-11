def combine(n, k):
    '''
    从1-n中选取k个数进行排列

    :param n: 1-n的n
    :param k: 选取的个数
    :return: 返回所有排列组合的list
    '''
    orig = list(range(1, n+1))
    res = []

    def walk(remain, subres):
        if len(remain) + len(subres) < k:
            return
        for i in range(len(remain) - k + len(subres) + 1):
            tempre = remain[i:].copy()
            tempsub = subres.copy()
            tempsub.append(tempre.pop(0))
            if len(tempsub) == k:
                res.append(tempsub)
            else:
                walk(tempre, tempsub)

    walk(orig, [])
    return res
