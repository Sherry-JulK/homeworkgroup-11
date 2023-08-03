import secrets
from SM2 import *
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
import binascii

class SM4:
    """
    国密sm4加解密
    """

    def __init__(self):
        self.crypt_sm4 = CryptSM4()

    def str_to_hexStr(self, hex_str):
        """
        字符串转hex
        :param hex_str: 字符串
        :return: hex
        """
        hex_data = hex_str.encode('utf-8')
        str_bin = binascii.unhexlify(hex_data)
        return str_bin.decode('utf-8')

    def encrypt(self, encrypt_key, value):
        """
        国密sm4加密
        :param encrypt_key: sm4加密key
        :param value: 待加密的字符串
        :return: sm4加密后的hex值
        """
        crypt_sm4 = self.crypt_sm4
        crypt_sm4.set_key(encrypt_key.encode(), SM4_ENCRYPT)
        encrypt_value = crypt_sm4.crypt_ecb(value.encode())
        return encrypt_value.hex()

    def decrypt(self, decrypt_key, encrypt_value):
        """
        国密sm4解密
        :param decrypt_key:sm4加密key
        :param encrypt_value: 待解密的hex值
        :return: 原字符串
        """
        crypt_sm4 = self.crypt_sm4
        crypt_sm4.set_key(decrypt_key.encode(), SM4_DECRYPT)
        decrypt_value = crypt_sm4.crypt_ecb(bytes.fromhex(encrypt_value))
        return self.str_to_hexStr(decrypt_value.hex())





Bsk, Bpk = key_gen()

sessionkey = secrets.token_hex(8) 
message = "SM2 PGP"
print("A want to send massage:{}".format(message))

SM4 = SM4()
Aoutput1 = SM4.encrypt(sessionkey, message)

Aoutput2 = SM2_enc(sessionkey, Bpk)

sessionkey_of_B = SM2_dec(Aoutput2, Bsk)
message_of_B = SM4.decrypt(sessionkey_of_B, Aoutput1)
print("\nB recover the massage:{}".format(message_of_B))
print("\nPGP is successful." if message_of_B == message else "Failed\n")
