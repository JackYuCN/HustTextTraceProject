import xpinyin as xpy
import jieba
from dic import myDic
import copy
from checkCode import check

class DecodeModule:
    def __init__(self):
        None

    def Load(self, dic_index, txt_path, dics_path, serial_len=12, debug_log_path="../logs/DecodeList.log"):
        self.serial_len = serial_len
        self.dic_index = dic_index
        self.dics = []
        for dic_path in dics_path:
            self.dics.append(myDic(dic_path))
        self.txt = list(jieba.cut(open(txt_path, mode="r", encoding="utf-8").read())) # 分词，按行隔开
        self.debug_log_path = debug_log_path

    def Check(self): 
        ans = []   
        code, num_zeros = [], 0
        decode_list = []
        py = xpy.Pinyin()
        cnt = 0
        if self.debug_log_path != None:
            f = open(self.debug_log_path, mode='w', encoding="utf-8")
        for i in range(len(self.txt)):
            word = self.txt[i]
            if self.is_chinese(word): # 检查word是否为汉字
                first = py.get_initial(word[0])
                idx = self.dic_index[first]
                dic = self.dics[idx]
                res = dic.find_col(word)
                if res != None:
                    cnt += 1
                    decode_list.append((word, res))
                    i += 1
                    code.append(res)
                    if res == 0:
                        num_zeros += 1
                        if num_zeros == 3:
                            ans.append(copy.deepcopy(code[:-3]))
                            if self.debug_log_path != None:
                                f.write(f"{decode_list[:-3]}\n")
                                f.write(f"{decode_list[-3:]}\n")
                            decode_list = []
                            code, num_zeros = [], 0
                            continue
                    else:
                        num_zeros = 0

        return ans
    
    def ConvertIntoNumber(self, arr):
        res = []
        for code in arr:
            flag = check(code, self.serial_len)
            if flag == True:
                num = 0
                num_binary = code[0:10]
                for j in num_binary:
                    if j == 1:
                        num = num * 2 + 1
                    else:
                        num = num * 2
                res.append(num)
        return res

    def Evaluate(self, res): 
        convert = self.ConvertIntoNumber(res)
        single = set(convert)
        res_dic = {}
        for i in single:
            arr = [1 if i == j else 0 for j in convert]
            res_dic[i] = sum(arr)
        max = 0
        max_serial = None
        # print("The result of decode:\n")
        for i in res_dic.keys():
            # print(f"\t{i} : {res_dic[i]}\n")
            if res_dic[i] > max:
                max = res_dic[i]
                max_serial = i
        # print(f"The most likely serial num is {max_serial}\n")
    
    def is_chinese(self, word):
        return word >= u'\u4e00' and word <= u'\u9fa5'