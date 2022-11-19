import numpy as np
import xpinyin as xpy

dic = np.genfromtxt("../datas/dics/origin/dic.txt", delimiter=' ', encoding='utf-8', dtype=np.str_)
dic_list = []
dic_list.append(open("../datas/dics/dic_util_0/0.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/1.txt", mode="w", encoding="utf-8"))

dic_index = {
    'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 1, 'F': 0, 'G': 0,
    'H': 1, 'I': 0, 'J': 1, 'K': 0, 'L': 0, 'M': 1, 'N': 1,
    'O': 1, 'P': 1, 'Q': 1, 'R': 0, 'S': 1, 'T': 1, 'U': 0,
    'V': 0, 'W': 1, 'X': 0, 'Y': 0, 'Z': 0
}

py = xpy.Pinyin()

for i in range(len(dic)):
    fir = py.get_initial(dic[i][0].strip()[0])
    sec = py.get_initial(dic[i][1].strip()[0])
    if dic_index[fir] == dic_index[sec]:
        dic_list[dic_index[fir]].write(f"{dic[i][0].strip()},{dic[i][1].strip()}\n")



