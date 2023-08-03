from gmssl import sm2, sm3, func
import random
import math


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


def key_gen(a, p, n, G):

    sk = random.randint(1, n - 2)
    pk = SM2_Mulyipoint(sk, G, a, p)
    return sk, pk


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


if __name__ == '__main__':
    p = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF
    a = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC
    b = 0x28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93
    n = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123
    Gx = 0x32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7
    Gy = 0xBC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0
    G = [Gx, Gy]
    [sk, pk] = key_gen(a, p, n, G)
    print("generate the secret key for SM2 and ECDSA: d = ", sk)
    sk_bytes = hex(sk)[2:].upper()
    pk_bytes = (hex(pk[0])[2:] + hex(pk[1])[2:]).upper()

    '''Reusing k leads to leaking of d'''
    print("sig different message with SM2 by using the same d")
    sm2_crypt = sm2.CryptSM2(public_key=pk_bytes, private_key=sk_bytes)
    random_hex_str = func.random_hex(sm2_crypt.para_len)  
    data = b"111111"
    data_ = b"222222"
    sign = sm2_crypt.sign(data, random_hex_str)
    sign_ = sm2_crypt.sign(data_, random_hex_str)
    assert sm2_crypt.verify(sign, data)
    signvalue = [sign[:64], sign[64:]]
    print("sign1 = ", signvalue)
    assert sm2_crypt.verify(sign_, data_)
    signvalue_ = [sign_[:64], sign_[64:]]
    print("sign2 = ", signvalue_)
    temp = int(signvalue_[1], 16) - int(signvalue[1], 16)
    temp_ = int(signvalue[1], 16) - int(signvalue_[1], 16) + int(signvalue[0], 16) - int(signvalue_[0], 16)
    dA = SM2__Mod_Decimal(temp, temp_, n)
    print("d has been leaked , that is", dA)

    '''Same d and k with ECDSA, leads to leaking of d'''
    print("sig message with SM2 and ECDSA by using the same d")
    k = int(random_hex_str, 16)
    R = SM2_Mulyipoint(k, G, a, p)
    e = int(sm3.sm3_hash(func.bytes_to_list(data)), 16)
    r1 = SM2_Mod(R[0], n)
    s1 = SM2_Mod((e + r1 * sk) * get_inverse(k, n), n)
    r2 = int(signvalue[0], 16)
    s2 = int(signvalue[1], 16)
    temp = SM2_Mod(s1 * s2 - e, n)
    temp_ = SM2_Mod(r1 - s1 * s2 - s1 * r2, n)
    dA = SM2__Mod_Decimal(temp, temp_, n)
    print("d has been leaked again , that is", dA)
