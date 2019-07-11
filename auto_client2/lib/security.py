import hashlib
from conf import settings
import rsa
import base64


def gen_key(t):
    s = '{}|{}'.format(settings.KEY, t)
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()


# ##### 加密 #####
def encrypt(value):
    key_str = base64.standard_b64decode(settings.PUB_KEY)
    pk = rsa.PublicKey.load_pkcs1(key_str)

    val_list = []
    for i in range(0, len(value), settings.ENABLE_LENGTH):
        v = value[i:i + settings.ENABLE_LENGTH]
        val = rsa.encrypt(v.encode('utf-8'), pk)
        val_list.append(val)
    return b''.join(val_list)