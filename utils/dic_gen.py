import numpy as np
import xpinyin as xpy

dic = np.genfromtxt("../datas/2022.txt", delimiter=' ', encoding='utf-8', dtype=np.str_)
dic_list = []
dic_list.append(open("../datas/dics/1_0.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/1_1.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/1_2.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/1_3.txt", mode="w", encoding="utf-8"))

relation = {'B':0, 'C':0, 'D':0, 'T':0, 'E':0, 'F':0,
            'P':1, 'G':1, 'N':1, 'W':1, 'S':1, 'O':1,
            'R':2, 'M':2, 'X':2, 'J':2, 'A':2, 'Y':2, 'I':2,
            'K':3, 'Q':3, 'H':3, 'L':3, 'Z':3, 'U':3, 'V':3}

py = xpy.Pinyin()

try:
    for i in range(len(dic)):
        fir = py.get_initial(dic[i][0].strip()[0])
        sec = py.get_initial(dic[i][1].strip()[0])
        if relation[fir] == relation[sec]:
            dic_list[relation[fir]].write(f"{dic[i][0].strip()},{dic[i][1].strip()}\n")
except:
    print(i)

