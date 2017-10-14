from Crypto.Cipher import AES
from Crypto import Random
import binascii

fk = open('plain.txt')
key = fk.read()
fk.close()
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CBC, iv)

def dAES_File(fc):
    dmsg = cipher.decrypt(iv+fc)
    return dmsg


def main():
    fd = open('fd.txt', 'wb')
    fc = open('fc.txt')
    fc_msg = fc.read()
    fc.close()
    fd_msg = dAES_File(fc_msg)
    fd.writelines(fd_msg[32:(len(fd_msg)-len(fd_msg)%16)])
    fd.close
    print(fd_msg[32:])

if __name__ == "__main__":
    main()
