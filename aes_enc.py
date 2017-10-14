from Crypto.Cipher import AES
from Crypto import Random
import binascii

fk = open('k.txt')
key = fk.read()
fk.close()
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CBC, iv)


def AES_File(fs):

    print 'if fs is a multiple of 16...'
    #if fs is a multiple of 16
    x = len(fs) % 16
    print x
    if x != 0:
        fs_pad = fs + '0'*(16 - x) #It shoud be 16-x not
        print 'fs_pad is : ', fs_pad
        print len(fs_pad)
        print len(fs_pad)%16
    msg = iv + cipher.encrypt(fs_pad)
    print 'File after AES is like...', binascii.b2a_hex(msg[:10])
    msg = msg
    return msg

def main():
    fs = open('n.txt')
    fs_msg = fs.read()
    fs.close()

    fc = open('fc.txt', 'wb')
    fc_msg = AES_File(fs_msg)
    fc.writelines(fc_msg)
    fc.close()

if __name__ == "__main__":
    main()
