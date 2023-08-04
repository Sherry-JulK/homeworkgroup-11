import random
import math
from gmssl import sm3, func


def SM2_Mulyipoint(k, P, a, p):  
    k_b = bin(k).replace('0b', '')  
    i = len(k_b) - 1
    R = P
    if i > 0:
        k = k - 2 ** i
        while i > 0:
            R = SM2_Pluspoint(R, R, a, p)
            i -= 1
        if k > 0:
            R = SM2_Pluspoint(R, SM2_Mulyipoint(k, P, a, p), a, p)
    return R


def SM2_Pluspoint(P, Q, a, p): 
    if (math.isinf(P[0]) or math.isinf(P[1])) and (~math.isinf(Q[0]) and ~math.isinf(Q[1])):  
        R = Q
    elif (~math.isinf(P[0]) and ~math.isinf(P[1])) and (math.isinf(Q[0]) or math.isinf(Q[1])): 
        R = P
    elif (math.isinf(P[0]) or math.isinf(P[1])) and (math.isinf(Q[0]) or math.isinf(Q[1])):  
        R = [float('inf'), float('inf')]
    else:
        if P != Q:
            l = SM2__Mod_Decimal(Q[1] - P[1], Q[0] - P[0], p)
        else:
            l = SM2__Mod_Decimal(3 * P[0] ** 2 + a, 2 * P[1], p)
        x = SM2_Mod(l ** 2 - P[0] - Q[0], p)
        y = SM2_Mod(l * (P[0] - x) - P[1], p)
        R = [x, y]
    return R


def SM2_Mod(a, b): 
    if math.isinf(a):
        return float('inf')
    else:
        return a % b


def SM2__Mod_Decimal(n, d, b):  
    if d == 0:
        x = float('inf')
    elif n == 0:
        x = 0
    else:
        a = bin(b - 2).replace('0b', '')
        y = 1
        i = 0
        while i < len(a):  
            y = (y ** 2) % b  
            if a[i] == '1':
                y = (y * d) % b
            i += 1
        x = (y * n) % b
    return x


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def get_(a, b):
    if b == 0:
        return 1, 0
    x1, y1 = get_(b, a % b)
    x, y = y1, x1 - a // b * y1
    return x, y


def get_inverse(a, p):
    if gcd(a, p) == 1:
        x, y = get_(a, p)
        return x % p
    return 1


def Verify(_r, _s, _e):
    print("待验证的签名值", [_r, _s], "由消息的哈希", _e, "和公钥", d, "生成")
    w = get_inverse(_s, n)
    [r1, r2] = SM2_Pluspoint(SM2_Mulyipoint(_e * w, G, a, p), SM2_Mulyipoint(_r * w, P, a, p), a, p)
    assert r1 == _r
    print("签名合法")


if __name__ == '__main__':
    p = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF
    a = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC
    b = 0x28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93
    n = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123
    Gx = 0x32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7
    Gy = 0xBC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0
    G = [Gx, Gy]
    '''generate a valid signature by "Satoshi"'''
    print('generate a valid signature by "Satoshi"')
    d = random.randint(1, n - 2) 
    P = SM2_Mulyipoint(d, G, a, p) 
    k = random.randint(1, n - 2)
    R = SM2_Mulyipoint(k, G, a, p)
    r = SM2_Mod(R[0], n)
    m = b"Satoshi"
    e = int(sm3.sm3_hash(func.bytes_to_list(m)), 16)
    s = SM2_Mod(get_inverse(k, n) * (e + d * r), n)
    Verify(r, s, e)  

    ''' forge a signature'''
    print("start forging a signature")
    u = random.randint(1, n - 2)
    v = random.randint(1, n - 2)
    [x_, y_] = SM2_Pluspoint(SM2_Mulyipoint(u, G, a, p), SM2_Mulyipoint(v, P, a, p), a, p)
    r_ = SM2_Mod(x_, n)

    e_ = SM2_Mod(r_ * u * get_inverse(v, n), n)
    s_ = SM2_Mod(r_ * get_inverse(v, n), n)
    Verify(r_, s_, e_)
