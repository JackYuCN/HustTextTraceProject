import numpy as np

dic_num = [3]
for i in dic_num:
    new_path = f"../datas/dics/1_{i}_new.txt"
    with open(new_path, mode="w", encoding='utf-8') as f:
        path = f"../datas/dics/1_{i}.txt"
        content = np.genfromtxt(path, delimiter=',', encoding='utf-8', dtype=np.str_)
        len = content.shape[0]
        tag = np.zeros(len)
        for i in range(len):
            for j in range(i+1, len):
                a0, a1 = content[i][0], content[i][1]
                b0, b1 = content[j][0], content[j][1]
                if a0 == b1 or a1 == b0:
                    content[j][0], content[j][1] = b1, b0
                    tag[j] += 1
                if (a0 == b0 and a1 == b1) or (a0 == b1 and a1 == b0):
                    tag[j] += 2
        for i in range(len):
            if tag[i] <= 1:
                f.write(f"{content[i][0]},{content[i][1]}\n")
