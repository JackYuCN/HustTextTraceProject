import numpy as np
import xpinyin as xpy

dic = np.genfromtxt("../datas/dics/origin/dic.txt", delimiter=' ', encoding='utf-8', dtype=np.str_)
dic_list = []
dic_list.append(open("../datas/dics/dic_util_0/0.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/1.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/2.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/3.txt", mode="w", encoding="utf-8"))

dic_index = {
    'A': 3, 'B': 0, 'C': 3, 'D': 1, 'E': 2, 'F': 3, 'G': 0,
    'H': 2, 'I': 0, 'J': 1, 'K': 3, 'L': 0, 'M': 1, 'N': 1,
    'O': 0, 'P': 2, 'Q': 2, 'R': 0, 'S': 2, 'T': 2, 'U': 0,
    'V': 0, 'W': 2, 'X': 3, 'Y': 0, 'Z': 3
}

py = xpy.Pinyin()

for i in range(len(dic)):
    fir = py.get_initial(dic[i][0].strip()[0])
    sec = py.get_initial(dic[i][1].strip()[0])
    if dic_index[fir] == dic_index[sec]:
        dic_list[dic_index[fir]].write(f"{dic[i][0].strip()},{dic[i][1].strip()}\n")



