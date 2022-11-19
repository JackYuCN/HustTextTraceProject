import sys
sys.path.append("../src")
from Decode import DecodeModule

dic_index = {
    'D': 0, 'J': 0, 'N': 0, 'M': 0,
    'S': 1, 'H': 1, 'T': 1, 'W': 1, 'Q': 1, 'P': 1, 'E': 1,
    'Z': 2, 'X': 2, 'C': 2, 'F': 2, 'K': 2, 'A': 2,
    'B': 3, 'G': 3, 'I': 3, 'L': 3, 'O': 3, 'R': 3, 'U': 3, 'V': 3, 'Y': 3
}
dics_path = ["../datas/dics/dic_util_4/0.txt",
             "../datas/dics/dic_util_4/1.txt",
             "../datas/dics/dic_util_4/2.txt",
             "../datas/dics/dic_util_4/3.txt"] 

debug_path_encode = "../datas/files/demo/EncodeList.txt"
debug_path_decode = "../datas/files/demo/DecodeList.txt"

lst = ['0.txt', '1.txt', '2.txt', '3.txt', '4.txt', '6.txt', '7.txt', '8.txt', '9.txt']
path = '../datas/files/demo/testcases/'
out_path = '../logs/analyze.log'


module_decode = DecodeModule()
with open(out_path, "w") as f:
    for i in lst:
        f.write(f"{i}:\n")
        filename = path + i
        module_decode.Load(dic_index, filename, dics_path, debug_path_decode)
        result, word_cnt = module_decode.Check()
        module_decode.Evaluate(result, f)
        f.write(f"word_cnt: {word_cnt}\n\n")