from Crypto import Random
from Crypto.PublicKey import RSA
from config import RSA_PRIVATE_KEY_PASSPHRASE
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import base64,os


class Rsa(object):

    __current_dir = os.path.dirname(__file__)
    __public_key_file = os.path.join(__current_dir,'public.pem')
    __private_key_file = os.path.join(__current_dir,'private.pem')

    def __init__(self):
        if os.path.exists(self.__public_key_file) and os.path.exists(self.__private_key_file):
            pass
        else:
            self.__make_key()

    def __make_key(self):
        random_generator = Random.new().read
        rsa = RSA.generate(1024,random_generator)

        private_key = rsa.exportKey(passphrase=RSA_PRIVATE_KEY_PASSPHRASE,pkcs=8)
        with open(self.__private_key_file,'wb+') as f:
            f.write(private_key)

        public_key = rsa.publickey().exportKey()
        with open(self.__public_key_file,'wb+') as f:
            f.write(public_key)

    def get_public_key(self):
        with open(self.__public_key_file,'rb') as f:
            key = f.read()
            public_key = RSA.importKey(key)
            return public_key

    def get_private_key(self):
        with open(self.__private_key_file,'rb') as f:
            key = f.read()
            private_key = RSA.importKey(key,passphrase=RSA_PRIVATE_KEY_PASSPHRASE)
            return private_key

    # 公钥加密
    def encrypt(self,data):
        if isinstance(data,str):
            data = data.encode(encoding='utf-8')

        cipher = Cipher_pkcs1_v1_5.new(self.get_public_key())
        encrypt_data = base64.b64encode(cipher.encrypt(data))
        return encrypt_data

    # 秘钥解密
    def decrypt(self,encrypt_data):
        cipher = Cipher_pkcs1_v1_5.new(self.get_private_key())
        data = cipher.decrypt(base64.b64decode(encrypt_data), None)
        return data.decode()

    # 秘钥签字
    def signature(self, data:str):
        if isinstance(data,str):
            data = data.encode(encoding='utf-8')
        signer = Signature_pkcs1_v1_5.new(self.get_private_key())
        digest = SHA.new()
        digest.update(data)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
        return signature.decode()

    # 公钥验证
    def verify(self, data:str, signature):
        if isinstance(data,str):
            data = data.encode(encoding='utf-8')
        verifier = Signature_pkcs1_v1_5.new(self.get_public_key())
        digest = SHA.new()
        digest.update(data)
        is_verify = verifier.verify(digest, base64.b64decode(signature))
        return is_verify

if __name__ == '__main__':
    rsa = Rsa()
    print(rsa.get_public_key())
    message = b'123' or '123' or '中文测试'
    en_message = rsa.encrypt(message)
    print(en_message)
    ret = rsa.decrypt(en_message)
    print(ret)