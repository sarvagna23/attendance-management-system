from Crypto.Cipher import DES
from base64 import *

ciphertext = b64decode('e1d5e1fcaae4aba0b735c8fb2ae8797728b073a34b14c57be236c819e6d5f4bbd94f5748ff9d1e008fcad8d403e23d02811f20f5e3fcb394f28ac4aeb4993fb2ab4f3d8a93beb6bf7158c05975339849')

KEY=b'\x00\x00\x00\x00\x00\x00\x00\x00'
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b'\x1E\x1E\x1E\x1E\x0F\x0F\x0F\x0F'
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b"\xE1\xE1\xE1\xE1\xF0\xF0\xF0\xF0"
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)
