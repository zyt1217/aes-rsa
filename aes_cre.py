from Crypto.Cipher import AES
from Crypto import Random
import binascii
from Crypto.Hash import MD5

from datetime import datetime

def randomkey():
    timenow = datetime.now()
    h = MD5.new()
    h.update(str(timenow))
    key = h.hexdigest()
    key =key[:16]
    return key

key = randomkey() #16-bytes password

fk = open('k.txt', 'a')
fk.writelines(key)
fk.close()

print key
