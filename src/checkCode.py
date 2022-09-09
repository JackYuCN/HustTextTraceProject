def encrypt(code):
    """编码，分别对奇数位和偶数位进行奇偶校验"""
    odd, even = 0, 0
    for i in range(len(code)):
        if i % 2 == 0:
            even ^= code[i]
        else:
            odd ^= code[i]
    code.append(odd)
    code.append(even)
    return code

def check(code, code_length):
    """检测当前编码是否正确"""
    if len(code) != code_length:
        print(code)
        return False
    odd, even = 0, 0
    for i in range(len(code)-2):
        if i % 2 == 0:
            even ^= code[i]
        else:
            odd ^= code[i]
    if even ^ code[-1] == 0 and odd ^ code[-2] == 0:
        return True
    else:
        print(code)
        return False