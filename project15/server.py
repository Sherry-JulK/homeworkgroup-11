import secrets
import pSM2

def step1(P1):
    """step 1 of right
    :param P1: received P1
    :return d2:random sub private key
    :return public_key_P: public key should be published
    """
    d2 = secrets.randbelow(pSM2.N)
    tmp = pSM2.inv(d2, pSM2.N)
    tmp = pSM2.EC_multi(tmp, P1)
    public_key_P = pSM2.EC_sub(tmp, pSM2.G)
    return d2, public_key_P

def step2(d2, Q1, e):
    """step 2 of right
    :param d2: generated in step 1
    :param Q1: receivced
    :param e: received
    :return r, s2, s3
    """
    e = int(e, 16)
    k2 = secrets.randbelow(pSM2.N)
    k3 = secrets.randbelow(pSM2.N)
    Q2 = pSM2.EC_multi(k2, pSM2.G)
    tmp = pSM2.EC_multi(k3, Q1)
    tmp = pSM2.EC_add(tmp, Q2)
    x1 = tmp[0]
    r = (x1 + e) % pSM2.N
    if r == 0:return 'error: r == 0'
    s2 = d2 * k3 % pSM2.N
    s3 = d2 * (r + k2) % pSM2.N
    return r, s2, s3




s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 12300))

data, addr=s.recvfrom(1024)
data = data.decode()
index1 = data.index(',')
P1 = (int(data[:index1]), int(data[index1 + 1:]))
d2, public_key_P = step1(P1)


data, addr=s.recvfrom(1024)
data = data.decode()
index1 = data.index(',')
index2 = data.index(';')
Q1 = (int(data[:index1]), int(data[index1 + 1:index2]))
e = data[index2 + 1:]
r, s2, s3 = step2(d2, Q1, e)
data = str(r) + ',' + str(s2) + ';' + str(s3)
s.sendto(data.encode(), addr)
s.close( )

print("connect closed")
