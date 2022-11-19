import xpinyin as xpy
import jieba
from dic import myDic
from checkCode import encrypt
import time

class EncodeModule:
    def __init__(self):
        None

    def Load(self, dic_index, txt_path, dics_path, num, serial_length=10, debug_log_path="../logs/EncodeList.log"):
        """
        param:
            dic_index:       汉语拼音首字母对应其在字典中的位置
            txt_path:        文本路径
            dics_path:       词典路径
            num:             待嵌入水印
            serial_length:   嵌入水印位数,缺省值为10
            debug_log_path:  输出debug_log的路径,默认为"../logs/EncodeList.log"
        """
        self.dic_index = dic_index
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

        timecnt = 0
        cnt = 0

        codecnt = 0

        if (self.debug_log_path != None):
            f = open(self.debug_log_path, mode="w", encoding="utf-8")

        with open("C:\\Users\\24561\\Desktop\\VScodeFolder\\Python\\dachuang\\datas\\testfile\\res\\len-time-2.csv", mode="a") as flt:
            end_tag_list = []
            encode_list = []
            for i in range(0, len(self.txt)-1):
                word = self.txt[i]                               
                if self.is_chinese(word): # word为汉字
                    first = py_module.get_initial(word[0]) # word的首字母
                    try:
                        dic = self.dics[self.dic_index[first]] # word所在词典
                    except:
                        dic = self.dics[0]
                    if complete_flag == False: # 处于插入状态
                        bit_value = self.serialNum[position] # 待嵌入的比特值

                        before = time.time()
                        xchg = dic.find_word(word, bit_value) 
                        timecnt += time.time() - before
                        cnt += 1
                        
                        if xchg is not None: # 在字典中找到要替换（或保留）的词
                            self.txt[i] = xchg # 替换操作
                            i += 1 # 连续两个词不能同时参与编码
                            if xchg == word or self.cut_check(i-1, xchg):
                                encode_list.append((xchg, bit_value))
                                position += 1
                                if position == len_code:
                                    if self.debug_log_path != None:
                                        f.write(f"{encode_list}\n")
                                    encode_list = []
                                    complete_flag = True
                    else: # 已经插满

                        before = time.time()
                        xchg = dic.find_word(word, 0) 
                        timecnt += time.time() - before
                        cnt += 1

                        if xchg is not None: # 在字典中找到要替换（或保留）的词
                            self.txt[i] = xchg
                            i += 1
                            if xchg == word or self.cut_check(i-1, xchg):
                                num_zeros += 1
                                end_tag_list.append((xchg, 0))
                                if num_zeros == 3:
                                    codecnt += 1
                                    if self.debug_log_path != None:
                                        f.write(f"{end_tag_list}\n")
                                    end_tag_list = []
                                    complete_flag, position, num_zeros = False, 0, 0
                
            flt.write(f"{timecnt / cnt}, {len(self.txt) / codecnt}\n")

        if self.debug_log_path != None:
            f.close()



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
        check = jieba.lcut(word+self.txt[idx+1])
        if len(check) != 2 or check[0] != word:
            return False
        return True
    
    def is_chinese(self, word):
        return word >= u'\u4e00' and word <= u'\u9fa5'