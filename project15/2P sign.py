from gmssl import sm3, func
import ECMH
import random


def to_int(byte):
    return int.from_bytes(byte, byteorder='big')



def to_byte(x, size=None):
    if isinstance(x, int):
        if size is None:
            size = 0
            tmp = x >> 64
            while tmp:
                size += 8
                tmp >>= 64
            tmp = x >> (size << 3)
            while tmp:
                size += 1
                tmp >>= 8
        elif x >> (size << 3):
            x &= (1 << (size << 3)) - 1
        return x.to_bytes(size, byteorder='big')
    elif isinstance(x, str):
        x = x.encode()
        if size != None and len(x) > size:
            x = x[:size]
        return x
    elif isinstance(x, bytes):
        if size != None and len(x) > size:
            x = x[:size]
        return x
    elif isinstance(x, tuple) and len(x) == 2 and type(x[0]) == type(x[1]) == int:
        return to_byte(x[0], size) + to_byte(x[1], size)
    return bytes(x)


def join_bytes(data_list):
    return b''.join([to_byte(i) for i in data_list])


def get_bit_num(x):
    if isinstance(x, int):
        num = 0
        tmp = x >> 64
        while tmp:
            num += 64
            tmp >>= 64
        tmp = x >> num >> 8
        while tmp:
            num += 8
            tmp >>= 8
        x >>= num
        while x:
            num += 1
            x >>= 1
        return num
    elif isinstance(x, str):
        return len(x.encode()) << 3
    elif isinstance(x, bytes):
        return len(x) << 3


def get_Z(ID):
    entlen = get_bit_num(ID)
    ENTL = to_byte(entlen, 2)
    mes = join_bytes([ENTL, ID, a, b, Gx, Gy, pk[0], pk[1]])
    Z = sm3.sm3_hash(func.bytes_to_list(mes))
    return Z


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
    [sk, pk] = ECMH.key_gen(a, p, n, G)

    '''step1:send P1'''
    d1 = random.randint(1, n - 1)
    P1 = ECMH.SM2_Mulyipoint(get_inverse(d1, n), G, a, p)
    print("P1=", P1)

    '''step2:send Public Key P'''
    d2 = random.randint(1, n - 1)
    temp = ECMH.SM2_Mulyipoint(get_inverse(d2, n), P1, a, p)
    _G = [Gx, -Gy]
    P = ECMH.SM2_Pluspoint(temp, _G, a, p)
    print("P=", P)

    '''step3:send Q1,e'''
    IDA = "Alice"
    ZA = get_Z(IDA)
    M = b'123'
    M_ = join_bytes([ZA, M])
    e = to_int(to_byte(sm3.sm3_hash(func.bytes_to_list(M_))))
    k1 = random.randint(1, n - 1)
    Q1 = ECMH.SM2_Mulyipoint(k1, G, a, p)
    print("e=", e)
    print("Q1=", Q1)

    '''step4:Generate partial signature r'''
    k2 = random.randint(1, n - 1)
    Q2 = ECMH.SM2_Mulyipoint(k2, G, a, p)
    k3 = random.randint(1, n - 1)
    temp2 = ECMH.SM2_Mulyipoint(k3, G, a, p)
    temp3 = ECMH.SM2_Pluspoint(temp2, Q2, a, p)
    r = ECMH.SM2_Mod(temp[1] + e, n)
    print("r=", r)
    s2 = ECMH.SM2_Mod(d2 * k3, n)
    s3 = ECMH.SM2_Mod(d2 * (r + k2), n)
    print("s2=", s2)
    print("s3=", s3)

    '''step5: Generate signature sigma=(r,s)'''
    s = ECMH.SM2_Mod(d1 * k1 * s2 + d1 * s3 - r, n)
    if s != 0 and s != n - r:
        print("s=", s)
