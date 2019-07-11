# ######### 1. 生成公钥私钥 #########
import rsa
import base64


length = 1024
rsa_length = int(length / 8)
enable_length = rsa_length - 11

pub_key_obj, priv_key_obj = rsa.newkeys(length)

pub_key_str = pub_key_obj.save_pkcs1()
pub_key_code = base64.standard_b64encode(pub_key_str)

priv_key_str = priv_key_obj.save_pkcs1()
priv_key_code = base64.standard_b64encode(priv_key_str)

print(pub_key_code)
print(priv_key_code)