import numpy as np

class myDic:

    def __init__(self, dic_path):
        self.content = np.genfromtxt(dic_path, delimiter=',', encoding='utf-8', dtype=np.str_).tolist()

    def find_word(self, word, col):
        for i in self.content:
            if i[col] == word:          
                return word
            elif i[1-col] == word:
                return i[col]
        return None

    def find_col(self, word):
        for i in self.content:
            if i[0] == word:
                return 0
            elif i[1] == word:
                return 1
        return None