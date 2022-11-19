import numpy as np
import xpinyin as xpy

dic = np.genfromtxt("../datas/dics/origin/dic.txt", delimiter=' ', encoding='utf-8', dtype=np.str_)
dic_list = []
dic_list.append(open("../datas/dics/dic_util_0/0.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/1.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/2.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/3.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/4.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/5.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/6.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/7.txt", mode="w", encoding="utf-8"))

dic_index = {
    'A': 5, 'B': 0, 'C': 6, 'D': 1, 'E': 4, 'F': 6, 'G': 0,
    'H': 4, 'I': 0, 'J': 2, 'K': 6, 'L': 0, 'M': 2, 'N': 2,
    'O': 2, 'P': 4, 'Q': 0, 'R': 0, 'S': 3, 'T': 3, 'U': 0,
    'V': 0, 'W': 4, 'X': 6, 'Y': 7, 'Z': 5
}

py = xpy.Pinyin()

for i in range(len(dic)):
    fir = py.get_initial(dic[i][0].strip()[0])
    sec = py.get_initial(dic[i][1].strip()[0])
    if dic_index[fir] == dic_index[sec]:
        dic_list[dic_index[fir]].write(f"{dic[i][0].strip()},{dic[i][1].strip()}\n")



