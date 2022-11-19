def CRCencode(k, r, g):
    """  15 = 3 + 4 + 8
        参数  
            k : list 待编码信息 8
            r : int  校验位数   4
            g : list 生成多项式
        约束关系
            k + r <= 2 ^ r - 1
            g.len = r + 1
        返回值
            k : 根据CRC编码规则和已有信息生成的CRC编码
    """
    k_new = []
    for i in k:
        k_new.append(i)
    for i in range(r):
        k_new.append(0)
    tmp = Module2Divide(k_new, g)
    for i in tmp:
        k.append(i)
    return k

def Module2Divide(k, g):
    len_of_g = len(g)
    while len(k) >= len_of_g:
        if k[0] == 1:  # 部分余数首位为1
            for i in range(len_of_g):
                k[i] ^= g[i]
        k.pop(0)   
    return k

def CRCcheck(n, g):
    """
        参数
            n : list 通过不确定链路后接收到的校验码
            g : list 生成多项式
        返回值
            1 代表n大概率正确 
            0 代表传输中校验码改变了
    """
    check = Module2Divide(n, g) 
    for i in check:
        if i == 1:
            return 0
    return 1

k = [1, 1, 0, 1, 0, 1, 1, 0, 1, 1]
g = [1, 0, 0, 1, 1]
r = len(g) - 1