import xpinyin as xpy
import jieba
from dic import myDic
from checkCode import encrypt

class EncodeModule:
    def __init__(self):
        None

    def Load(self, txt_path, dics_path, debug_log_path, num, serial_length=10):
        """
        param:
            txt_path:        文本路径
            dics_path:       词典路径
            num:             待嵌入水印
            serial_length:   嵌入水印位数,缺省值为10
        """
        self.dic_index = {'B':0, 'C':0, 'D':0, 'T':0, 'E':0, 'F':0,
                          'P':1, 'G':1, 'N':1, 'W':1, 'S':1, 'O':1,
                          'R':2, 'M':2, 'X':2, 'J':2, 'A':2, 'Y':2, 'I':2,
                          'K':3, 'Q':3, 'H':3, 'L':3, 'Z':3, 'U':3, 'V':3}
        self.serial_length = serial_length
        self.serialNum = self.ConvertIntoBinary(num)
        self.dics = []
        for dic_path in dics_path:
            self.dics.append(myDic(dic_path))
        self.txt = jieba.lcut(open(txt_path, mode="r", encoding="utf-8").read()) # 分词，按行隔开
        self.debug_log_path = debug_log_path

    def Insert(self):
        py_module = xpy.Pinyin()
        len_code = len(self.serialNum)
        complete_flag, position, num_zeros= True, 0, 0
        with open(self.debug_log_path, mode='w', encoding='utf-8') as f:
            end_tag_list = []
            encode_list = []
            for i in range(1, len(self.txt)-1):
                word = self.txt[i]                               
                if self.is_chinese(word): # word为汉字
                    first = py_module.get_initial(word[0]) # word的首字母
                    dic = self.dics[self.dic_index[first]] # word所在词典
                    if complete_flag == False: # 处于插入状态
                        bit_value = self.serialNum[position] # 待嵌入的比特值
                        xchg = dic.find_word(word, bit_value) 
                        if xchg is not None: # 在字典中找到要替换（或保留）的词
                            self.txt[i] = xchg # 替换操作
                            if xchg == word or self.cut_check(i, xchg):
                                encode_list.append((xchg, bit_value))
                                position += 1
                                if position == len_code:
                                    f.write(f"{encode_list}\n")
                                    encode_list = []
                                    complete_flag = True
                    else: # 已经插满
                        xchg = dic.find_word(word, 0) 
                        if xchg is not None: # 在字典中找到要替换（或保留）的词
                            self.txt[i] = xchg
                            if xchg == word or self.cut_check(i, xchg):
                                num_zeros += 1
                                end_tag_list.append((xchg, 0))
                                if num_zeros == 3:
                                    f.write(f"{end_tag_list}\n")
                                    end_tag_list = []
                                    complete_flag, position, num_zeros = False, 0, 0

    def ConvertIntoBinary(self, num):
        """
        把待嵌入的水印num转化为奇偶校验加密后的10位二进制数. 存放在self.serialNum列表中
        """
        binary = []
        while num:
            if num % 2 == 0:
                binary.insert(0, 0)
            else:
                binary.insert(0, 1)
            num = num // 2
        while len(binary) != self.serial_length:
            binary.insert(0, 0)
        return encrypt(binary)

    def InsertWatermark(self, out_path):
        self.Insert()
        fout = open(out_path, mode="w", encoding="utf-8")
        for i in self.txt:
            fout.write(i)
        fout.close()
               
    def cut_check(self, idx, word):
        """检查所替换的词和下一个词能否被jieba正确地分开"""
        check = jieba.lcut(self.txt[idx-1]+word+self.txt[idx+1])
        if len(check) != 3 or check[0] != self.txt[idx-1] or check[1] != word:
            return False
        return True
    
    def is_chinese(self, word):
        return word >= u'\u4e00' and word <= u'\u9fa5'