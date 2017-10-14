from Crypto.PublicKey import RSA

new_key = RSA.generate(2048)
public_key = new_key.publickey().exportKey("PEM")
private_key = new_key.exportKey("PEM")

with open("key", "wb") as f:
    f.write(private_key)

with open("key.pub", "wb") as f:
    f.write(public_key)
