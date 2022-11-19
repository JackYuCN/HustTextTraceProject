import numpy as np
import xpinyin as xpy

dic = np.genfromtxt("../datas/dics/origin/dic.txt", delimiter=' ', encoding='utf-8', dtype=np.str_)
dic_list = []
dic_list.append(open("../datas/dics/dic_util_0/0.txt", mode="w", encoding="utf-8"))

dic_index = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
    'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
    'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
    'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
}

py = xpy.Pinyin()

for i in range(len(dic)):
    fir = py.get_initial(dic[i][0].strip()[0])
    sec = py.get_initial(dic[i][1].strip()[0])
    if dic_index[fir] == dic_index[sec]:
        dic_list[dic_index[fir]].write(f"{dic[i][0].strip()},{dic[i][1].strip()}\n")



