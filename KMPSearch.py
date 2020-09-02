def KMPStringSearch(text, tar):
    '''
    使用KMP算法实现字符串检索

    :param text: 检索的文本
    :param tar: 要检索的子字符串
    :return: 返回一个list，为所有在text中检索到的目标子字符串的起点下标
    '''
    res = []
    idx = 0
    while idx <= (len(text) - len(tar)):
        submatch = ''
        for j in range(len(tar)):
            if tar[j] != text[idx+j]:
                mismatch = True
                break
            submatch += tar[j]
        if j == 0:
            idx += 1
        else:
            if len(submatch) == len(tar):
                res.append(idx)
            # 计算部分匹配
            prefix = set()
            suffix = set()
            for i in range(len(submatch) - 1):
                prefix.add(submatch[:-(i + 1)])
                suffix.add(submatch[(i+1):])
            temp = prefix.intersection(suffix)
            sub_mat_len = 0
            for s in temp:
                sub_mat_len = max(len(s), sub_mat_len)
            idx += j - sub_mat_len
    return res


res = KMPStringSearch('BBC ABCDAB ABCDABCDABDE', 'ABCDABD')



