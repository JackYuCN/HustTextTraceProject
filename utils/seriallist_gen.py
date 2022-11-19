import sys
sys.path.append("../src")
from checkCode import encrypt

def convert_encrypt(i):
    """将i转化成10位二进制形式. 附加2位奇偶校验信息"""
    res = []
    while i:
        if i % 2 == 0:
            res.insert(0, 0)
        else:
            res.insert(0, 1)
        i = i // 2
    while len(res) != 10:
        res.insert(0, 0)
    return encrypt(res)

def check_ones(np_list, num=3):
    cnt = 0
    if np_list[0] == 0 or np_list[-1] == 0:
        return False
    for i in np_list:
        if i == 0:
            cnt += 1
            if cnt == num:
                return False
        else:
            cnt = 0
    return True

# assert os.path.exists("../datas/files/demo/seriallist.csv") == False, "the seriallist is already exist"
with open("../datas/files/demo/seriallist.csv", mode="w") as fw:
    fw.write(f"serial,valid,username\n")
    for num in range(1024):
        array = convert_encrypt(num)
        check = check_ones(array)
        if check == True:
            fw.write(f"{num},{False},Nobody\n")
        else:
            print(array)
