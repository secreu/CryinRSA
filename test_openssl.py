import rsa
import base64
import time

from cryinrsa import read_data, write_data
 
from OpenSSL.crypto import PKey
from OpenSSL.crypto import TYPE_RSA, FILETYPE_PEM, FILETYPE_ASN1
from OpenSSL.crypto import dump_privatekey, dump_publickey
 
 
pk = PKey()
pk.generate_key(TYPE_RSA, 512)
pub = dump_publickey(FILETYPE_PEM, pk)
pri = dump_privatekey(FILETYPE_ASN1, pk)
 
pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(pub)
prikey = rsa.PrivateKey.load_pkcs1(pri, 'DER')

plaintxt = read_data("1mb.txt")
ciphertxt = bytes()
length = len(plaintxt)
esum = 0
dsum = 0

step = 54
for i in range(10):
    begin = time.time()
    for i in range(0, length, step):
        j = (i + step) if  (i + step < length) else length
        ciphertxt += rsa.encrypt(plaintxt[i:j], pubkey)
    end = time.time()
    esum += end - begin
print("encoding cost: %.6f"%(esum / 10))

# ciphertxt = base64.b64encode(ciphertxt)

# for i in range(100):
#     begin = time.time()   
#     plaintxt = rsa.decrypt(base64.b64decode(ciphertxt), prikey)
#     end = time.time()
#     dsum += end - begin
# print("encoding cost: %.6f"%(dsum / 100))

