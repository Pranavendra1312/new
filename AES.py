import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
block_size = AES.block_size
# key=input("Enter a key :")
# print("Block size is :",block_size)
# key = hashlib.sha256(key.encode()).digest()
# print("Key is:",key)
# print("Key length:",len(key))
# print("hello".encode())
# print(type("hello"))
# print(type(b'hello'))
# print(len("hello"))
# print(len(b'hello'))

def encrypt(plain_text,key):
       plain_text = __pad(plain_text)
       iv = Random.new().read(block_size)
       cipher = AES.new(key, AES.MODE_CBC, iv)
       encrypted_text = cipher.encrypt(plain_text.encode())
       return b64encode(iv + encrypted_text).decode("utf-8")
def decrypt(encrypted_text,key):
       encrypted_text = b64decode(encrypted_text)
       iv = encrypted_text[:block_size]
       cipher = AES.new(key, AES.MODE_CBC, iv)
       plain_text = cipher.decrypt(encrypted_text[block_size:]).decode("utf-8")
       return __unpad(plain_text)
def __pad(plain_text):
       number_of_bytes_to_pad = block_size - len(plain_text) % block_size
       ascii_string = chr(number_of_bytes_to_pad)
       padding_str = number_of_bytes_to_pad * ascii_string
       padded_plain_text = plain_text + padding_str
       return padded_plain_text

   
def __unpad(plain_text):
       last_character = plain_text[len(plain_text) - 1:]
       return plain_text[:-ord(last_character)]
# encrypted_text=encrypt(input("Enter plain text:"))
# print(encrypted_text)
# print("decrypted_text is :",decrypt(encrypted_text))


