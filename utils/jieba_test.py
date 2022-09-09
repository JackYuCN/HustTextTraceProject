import jieba

with open('../datas/jieba_test.txt', mode="w", encoding="utf-8") as f:
    before = list(jieba.cut(open("../datas/before.txt", mode="r", encoding="utf-8").read())) 
    after = list(jieba.cut(open("../datas/after.txt", mode="r", encoding="utf-8").read()))
    for i, j in zip(before, after):
        if i != j:
            f.write(f"{i}  {j}\n")

