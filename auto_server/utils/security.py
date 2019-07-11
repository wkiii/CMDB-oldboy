from auto_server import settings
import hashlib
import rsa
import base64


def gen_key(time):
    s = '{}|{}'.format(settings.KEY, time)
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()


def decrypt(value):
    key_str = base64.standard_b64decode(settings.PRIV_KEY)
    pk = rsa.PrivateKey.load_pkcs1(key_str)

    val_list = []
    for i in range(0, len(value), settings.RSA_LENGTH):
        v = value[i:i + settings.RSA_LENGTH]
        val = rsa.decrypt(v, pk)
        val_list.append(val)

    return b''.join(val_list)
