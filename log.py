from base64 import b64decode

from Crypto.Cipher import AES

def AES_ECB_DECRYPT(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)


data = 'd6d028810212d6241e74024e0b1db4a22a593aa717e08580340f3f4b57f36b74'
print(len(data))
ciphertext = b64decode(data)
print(bytes.fromhex(data))
print(ciphertext)
plaintext = AES_ECB_DECRYPT(b'Yellow submarine', ciphertext)

print(plaintext)
