def dividePipe(n: int, k: int):
    '''
    将整数n分成k个整数

    :param n: n
    :param k: 分成k个整数
    :return: 返回所有分法的数组
    '''
    if k == 1:
        return [[n]]
    # 每个部分可能最大的数
    max_part = n - k + 1
    res = []
    for i in range(1, max_part + 1):
        sub = dividePipe(n - i, k - 1)
        for x in sub:
            temp = [i]
            temp.extend(x.copy())
            res.append(temp)
    return res


f1 = dividePipe(5, 2)
f2 = dividePipe(5, 3)
f3 = dividePipe(5, 4)
f4 = dividePipe(5, 5)


def dividePipeAll(n:int):
    '''
    将长度为n的钢管分成整数长度，总共有多少种分法

    :param n: 钢管长度
    :return: 返回所有切割方式
    '''

    # 遍历将钢管切割成1份 - n份的所有可能
    merge = []
    for k in range(1, n + 1):
        sub = dividePipe(n, k)
        # 不去重
        merge.extend(sub)

        # 去重
        # res_set = set()
        # for x in sub:
        #     res_set.add(tuple(sorted(x)))
        # merge.extend(list(res_set))
    return merge


allfive = dividePipeAll(5)
allfour = dividePipeAll(4)


def findMaxValuedDivide(n:int, prices=[0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]):
    '''
    切割长度为n的钢管，查找使得价格最高的切割方式

    :param n: 钢管长度
    :param prices: 价格表，下标为i的数值即为长度为i的钢管的价格
    :return: 返回最优切割方案（列表）和对应价格
    '''

    max_divide = []
    max_value = 0
    for k in range(1, n + 1):
        sub = dividePipe(n, k)
        # 不去重
        for div in sub:
            div_value = 0
            for l in div:
                if l > len(prices) - 1 or prices[l] is None:
                    div_value = None
                    break
                div_value += prices[l]
            if div_value is not None:
                if div_value > max_value:
                    max_value = div_value
                    max_divide = [div.copy()]
                elif div_value == max_value:
                    max_divide.append(div.copy())
    return max_divide, max_value


divide4, max_value4 = findMaxValuedDivide(4)
divide5, max_value5 = findMaxValuedDivide(5)


def findMaxValuedDivide2(n:int, prices=[0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]) -> int:
    '''
    切割长度为n的钢管，查找使得价格最高的切割方式

    :param n: 钢管长度
    :param prices: 价格表，下标为i的数值即为长度为i的钢管的价格
    :return: 返回最优价格
    '''
    if n == 0:
        return prices[0]
    # 长度为1的钢管只有不切割的可能
    if n == 1:
        return prices[1]

    max_value = 0
    # 长度不切割有价格时先记录不切割的价格
    if n < len(prices) and prices[n] is not None:
        max_value = prices[n]
    # 二分问题，将钢管切割成两部分，查看 k 和 n - k最大值的和
    # for k in range(1, n):
    for k in range(1, int(n / 2) + 1):
        subval1 = findMaxValuedDivide2(k)
        subval2 = findMaxValuedDivide2(n - k)
        if subval1 + subval2 > max_value:
            max_value = subval1 + subval2
    return max_value


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
cache_max = {0:p[0], 1:p[1]}
def findMaxValuedDivide_DP(n:int, prices=[0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]):
    '''
    切割长度为n的钢管，查找使得价格最高的切割方式，动态规划版本，自顶向下

    :param n: 钢管长度
    :param prices: 价格表，下标为i的数值即为长度为i的钢管的价格
    :return: 返回最优对应价格
    '''
    if cache_max.get(n, None) is not None:
        return cache_max[n]

    max_value = 0
    # 长度不切割有价格时先记录不切割的价格
    if n < len(prices) and prices[n] is not None:
        max_value = prices[n]
    # 二分问题，将钢管切割成两部分，查看 k 和 n - k最大值的和
    for k in range(1, int(n / 2) + 1):
        if cache_max.get(k, None) is not None:
            subval1 = cache_max[k]
        else:
            subval1 = findMaxValuedDivide_DP(k)
        if cache_max.get(n - k, None) is not None:
            subval2 = cache_max[n - k]
        else:
            subval2 = findMaxValuedDivide_DP(n - k)
        if subval1 + subval2 > max_value:
            max_value = subval1 + subval2
    cache_max[n] = max_value
    return max_value


def findMaxValuedDivide_DP2(n:int, prices=[0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]):
    '''
    切割长度为n的钢管，查找使得价格最高的切割方式，动态规划版本，非递归版本，自底向上

    :param n: 钢管长度
    :param prices: 价格表，下标为i的数值即为长度为i的钢管的价格
    :return: 返回最优对应价格
    '''
    caches = {0: prices[0], 1: prices[1]}
    if n <= 1:
        return caches[n]

    for j in range(2, n+1):
        max_value = 0
        if j < len(prices) and prices[j] is not None:
            max_value = prices[j]
        for i in range(1, int(j / 2) + 1):
            subval1 = caches[j - i]
            subval2 = caches[i]
            if subval1 + subval2 > max_value:
                max_value = subval1 + subval2
        caches[j] = max_value
    return caches[n]

dp2 = findMaxValuedDivide_DP2(11)

import time
# 比较动态版本和非动态版本的耗时
start = time.time()
findMaxValuedDivide2(25)
end = time.time()
print("Time cost by NonDP: " + str((end - start) * 1000.0) + " ms")

start = time.time()
findMaxValuedDivide_DP(25)
end = time.time()
print("Time cost by DP: " + str((end - start) * 1000.0) + " ms")

