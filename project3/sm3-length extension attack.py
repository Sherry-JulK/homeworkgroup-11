from gmssl import sm3, func
import random
import osm3
import struct
messageorigin = str(random.randint(0,2**64))
secret_hash = sm3.sm3_hash(func.bytes_to_list(bytes(messageorigin, encoding='utf-8')))
secret_len = len(messageorigin)
append_m = "1901210403"
pad_str = ""
pad = []
def generate_guess_hash(old_hash, secret_len, append_m):
    vectors = []
    message = ""
    for r in range(0, len(old_hash), 8):
        vectors.append(int(old_hash[r:r + 8], 16))
    if secret_len > 64:
        for i in range(0, int(secret_len / 64) * 64):
            message += 'a'
    for i in range(0, secret_len % 64):
        message += 'a'
    message = func.bytes_to_list(bytes(message, encoding='utf-8'))
    message = padding(message)
    message.extend(func.bytes_to_list(bytes(append_m, encoding='utf-8')))
    return osm3.sm3_hash(message, vectors)


def padding(msg):
    mlen = len(msg)
    msg.append(0x80)
    mlen += 1
    tail = mlen % 64
    range_end = 56
    if tail > range_end:
        range_end = range_end + 64
    for i in range(tail, range_end):
        msg.append(0x00)
    bit_len = (mlen - 1) * 8
    msg.extend([int(x) for x in struct.pack('>q', bit_len)])
    for j in range(int((mlen - 1) / 64) * 64 + (mlen - 1) % 64, len(msg)):
        global pad
        pad.append(msg[j])
        global pad_str
        pad_str += str(hex(msg[j]))
    return msg


guess_hash = generate_guess_hash(secret_hash, secret_len, append_m)
new_msg = func.bytes_to_list(bytes(messageorigin, encoding='utf-8'))
new_msg.extend(pad)
new_msg.extend(func.bytes_to_list(bytes(append_m, encoding='utf-8')))
new_msg_str = messageorigin + pad_str + append_m

new_hash = sm3.sm3_hash(new_msg)

print("初始消息: "+messageorigin)
print("初始消息长度:%d" % len(messageorigin))
print("初始消息hash值:" + secret_hash)
print("附加消息:", append_m)
print("构造的消息的hash值:" + guess_hash)
print("相加值: \n" + new_msg_str)
print("相加后hash值:" + new_hash)
if new_hash == guess_hash:
    print("成功!")
else:
    print("失败")
