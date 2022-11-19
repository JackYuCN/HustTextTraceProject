# 修改意见：
# 1. 将四个词典混在一起参与encode
# 2. encode逻辑是如果jieba分词不能正确的区分替换后的词，那么就不改变进度且完成替换
# 3. 弃用纠错码，转而使用尾数较少的检错码（2位）
# 4. 使用连续3个0作为结束标志

from Decode import DecodeModule
from Encode import EncodeModule

serial_path = "../datas/files/demo/seriallist.csv"

shared_path = "C:\\Users\\24561\\Desktop\\VScodeFolder\\Python\\dachuang\\datas\\testfile\\violence test\\"
total = 130

dics_path = ["../datas/dics/dic_util_4/0.txt",
             "../datas/dics/dic_util_4/1.txt",]
username = "John"
dic_index = {
    'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 1, 'F': 0, 'G': 0,
    'H': 1, 'I': 0, 'J': 1, 'K': 0, 'L': 0, 'M': 1, 'N': 1,
    'O': 1, 'P': 1, 'Q': 1, 'R': 0, 'S': 1, 'T': 1, 'U': 0,
    'V': 0, 'W': 1, 'X': 0, 'Y': 0, 'Z': 0
}


def main():
    
    for i in range(total):
        
        before_path = shared_path + "before" + str(i) + ".txt"
        after_path = shared_path + "after" + str(i) + ".txt"
        
        module_encode = EncodeModule()
        module_encode.Load(dic_index, before_path, dics_path, 586)
        module_encode.InsertWatermark(after_path)

        # module_decode = DecodeModule()
        # module_decode.Load(dic_index, after_path, dics_path)
        # result = module_decode.Check()
        # module_decode.Evaluate(result)
            

if __name__ == '__main__':
    main() 
