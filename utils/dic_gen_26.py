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
dic_list.append(open("../datas/dics/dic_util_0/8.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/9.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/10.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/11.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/12.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/13.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/14.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/15.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/16.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/17.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/18.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/19.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/20.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/21.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/22.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/23.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/24.txt", mode="w", encoding="utf-8"))
dic_list.append(open("../datas/dics/dic_util_0/25.txt", mode="w", encoding="utf-8"))

dic_index = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
    'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
    'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
    'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

py = xpy.Pinyin()

for i in range(len(dic)):
    fir = py.get_initial(dic[i][0].strip()[0])
    sec = py.get_initial(dic[i][1].strip()[0])
    if dic_index[fir] == dic_index[sec]:
        dic_list[dic_index[fir]].write(f"{dic[i][0].strip()},{dic[i][1].strip()}\n")



