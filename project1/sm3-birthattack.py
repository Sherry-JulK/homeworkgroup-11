import random
import time
from gmssl import sm3, func

cip_text = str(random.random())
cip_len = len(cip_text)
cip_hash = sm3.sm3_hash(func.bytes_to_list(bytes(cip_text, encoding='utf-8')))

def Birthday_attack(test_len):
    num = int(2 ** (test_len / 2))
    ans = [-1] * 2**test_len
    for i in range(num):
        temp = int(cip_hash[0:int(test_len / 4)], 16)
        if ans[temp] == -1:
            ans[temp] = i
        else:
            return hex(temp)

if __name__ == '__main__':
    test_len = 8
    start = time.time()
    res = Birthday_attack(test_len)
    end = time.time()
    print("前",test_len,"位碰撞为{}".format(res))
    print(end- start,'seconds\n')
