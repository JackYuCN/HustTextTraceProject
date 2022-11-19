import numpy as np
import jieba
dic_num = [0]

# 去重+调位
for i in dic_num:
    new_path = f"../datas/dics/dic_util_1/{i}.txt"
    with open(new_path, mode="w", encoding='utf-8') as f:
        path = f"../datas/dics/dic_util_0/{i}.txt"
        content = np.genfromtxt(path, delimiter=',', encoding='utf-8', dtype=np.str_)
        content_len = content.shape[0]
        tag = np.zeros(content_len)
        for i in range(content_len):
            if tag[i] > 1:
                continue
            a0, a1 = content[i][0], content[i][1]
            for j in range(i+1, content_len):
                if tag[j] > 1:
                    continue
                b0, b1 = content[j][0], content[j][1]
                if a0 == b0 or a1 == b1:
                    tag[j] += 1
                elif a0 == b1 or a1 == b0:
                    content[j][0], content[j][1] = b1, b0
                    tag[j] += 1
                if (a0 == b0 and a1 == b1) or (a0 == b1 and a1 == b0):
                    tag[j] += 2
        for i in range(content_len):
            if tag[i] <= 1:
                f.write(f"{content[i][0]},{content[i][1]}\n")

# 去除无法被jieba分开的词
for i in dic_num:
    new_path = f"../datas/dics/dic_util_2/{i}.txt"
    with open(new_path, mode="w", encoding='utf-8') as f:
        path = f"../datas/dics/dic_util_1/{i}.txt"
        content = np.genfromtxt(path, delimiter=',', encoding='utf-8', dtype=np.str_)
        length = content.shape[0]
        for i in range(length):
            tmp = list(jieba.cut(content[i][0]))
            if len(tmp) == 1:
                tmp = list(jieba.cut(content[i][1]))
                if len(tmp) == 1:
                    f.write(f"{content[i][0]},{content[i][1]}\n")

# 去除长度不等的近义词组
for i in dic_num:
    new_path = f"../datas/dics/dic_util_3/{i}.txt"
    with open(new_path, mode="w", encoding='utf-8') as f:
        path = f"../datas/dics/dic_util_2/{i}.txt"
        content = np.genfromtxt(path, delimiter=',', encoding='utf-8', dtype=np.str_)
        for i in content:
            if len(i[0]) == len(i[1]):
                f.write(f"{i[0]},{i[1]}\n")

# 去除所有前缀四字词语
for i in dic_num:
    new_path = f"../datas/dics/dic_util_4/{i}.txt"
    with open(new_path, mode="w", encoding='utf-8') as f:
        path = f"../datas/dics/dic_util_3/{i}.txt"
        content = np.genfromtxt(path, delimiter=',', encoding='utf-8', dtype=np.str_)
        for i in content:
            if len(i[0]) == 4:
                part1 = i[0][0:2]
                part2 = i[1][0:2]
                part3 = i[0][2:4]
                part4 = i[0][2:4]
                tag = False
                for j in content:
                    if j[0] == part1 or j[1] == part2 or j[0] == part2 or j[1] == part1 or j[0] == part3 or j[1] == part4 or j[0] == part4 or j[1] == part3:
                        tag = True
                        break
                if tag == False:
                    f.write(f"{i[0]},{i[1]}\n")
            elif len(i[0]) == 2:
                f.write(f"{i[0]},{i[1]}\n")
