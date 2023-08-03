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


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 12300))
######### step1: receive P1 and send public key #########
data, addr=s.recvfrom(1024)
data = data.decode()
index1 = data.index(',')
P1 = (int(data[:index1]), int(data[index1 + 1:]))
d2, public_key_P = step1(P1)
data = str(public_key_P[0]) + ',' + str(public_key_P[1])
s.sendto(data.encode(), addr)

######### receive T1 and send T2 #########
data, addr=s.recvfrom(1024)
data = data.decode()
index1 = data.index(',')
T1 = (int(data[:index1]), int(data[index1 + 1:]))
tmp = pSM2.inv(d2, pSM2.N)
T2 = pSM2.EC_multi(tmp, T1)
data = str(T2[0]) + ',' + str(T2[1])
s.sendto(data.encode(), addr)


s.close()
print("---------connect closed---------")
