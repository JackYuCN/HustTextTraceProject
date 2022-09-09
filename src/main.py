# 修改意见：
# 1. 将四个词典混在一起参与encode
# 2. encode逻辑是如果jieba分词不能正确的区分替换后的词，那么就不改变进度且完成替换
# 3. 弃用纠错码，转而使用尾数较少的检错码（2位）
# 4. 使用连续3个0作为结束标志

from Decode import DecodeModule
from Encode import EncodeModule
import pandas as pd

serial_path = "../datas/files/demo/seriallist.csv"
txt_path = "../datas/files/demo/before.txt"
dics_path = ["../datas/dics/dic_util_4/0.txt", 
             "../datas/dics/dic_util_4/1.txt",
             "../datas/dics/dic_util_4/2.txt", 
             "../datas/dics/dic_util_4/3.txt",]
out_path = "../datas/files/demo/after.txt"
debug_path_encode = "../datas/files/demo/EncodeList.txt"
debug_path_decode = "../datas/files/demo/DecodeList.txt"
username = "John"

def main():

    df = pd.read_csv(serial_path)
    tag, num = False, None
    for i in range(len(df)):
        if df['valid'][i] == False:
            tag = True
            num = df['serial'][i]
            df.loc[i, 'valid'], df.loc[i, 'username'] = True, username
            break
    assert tag == True, "the serial list is full!"
     
    module_encode = EncodeModule()
    module_encode.Load(txt_path, dics_path, debug_path_encode, num)
    module_encode.InsertWatermark(out_path)

    df.to_csv(serial_path, index=None)    

    module_decode = DecodeModule()
    module_decode.Load(out_path, dics_path, debug_path_decode)
    result = module_decode.Check()
    module_decode.Evaluate(result)

if __name__ == '__main__':
    main() 
