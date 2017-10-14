# coding:utf-8

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

# 解密，需要私钥
def decrypt_string(text):
    with open("key", "r") as f:
        private_key = f.read()
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)
    chunk_size = 256
    decrypted  = ""
    offset     = 0
    while offset < len(text):
        chunk = rsakey.decrypt(text[offset:offset+chunk_size])
        decrypted += chunk[:-ord(chunk[-1])]
        offset += chunk_size
    return decrypted

c = open('kcipher.txt')
with open('plain.txt', 'w') as d:
     d.write(decrypt_string(c.read()))
print (decrypt_string(c.read()))
c.close()
d.close

