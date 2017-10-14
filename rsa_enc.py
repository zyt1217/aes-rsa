# coding:utf-8

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

# 加密，需要公钥
def encrypt_string(plaintext):
    with open("key.pub", "r") as f:
        public_key = f.read()
    rsakey = RSA.importKey(public_key)
    rsakey = PKCS1_OAEP.new(rsakey)
    # 使用PKCS1_OAEP有填充字符，所以我们可用块大小为2048/8-2-2*20，即214字节
    chunk_size = 214
    encrypted  = ""
    offset     = 0
    # 将数据分解成指定大小块并进行加密
    while offset < len(plaintext):
        # 使用至少一个字节作为填充字符，解密时可以精确控制文本大小
        chunk = plaintext[offset:offset+chunk_size-1]
        # 计算块数据大小与指定块大小的差距，然后填充字符
        count = chunk_size - len(chunk)
        chunk += count * chr(count)
        # 加密数据
        encrypted += rsakey.encrypt(chunk)
        offset += chunk_size - 1
    return encrypted

f = open('k.txt')
with open('kcipher.txt', 'w') as c:
    c.write(encrypt_string(f.read()))
c.close
f.close()
