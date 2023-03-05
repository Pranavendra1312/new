import Huffman as hf
import RSA as rsa
import Vig_qw as vig
plain_text=input("Enter plain text : ")
print("")
print("======================== VIGENERE ENCRYPTION ==================================")
print("")
key=input("Enter vig key : ")
key=vig.generateKey(plain_text,key)
Vig_encryp_text=vig.vig_encrypt(plain_text,key)
print("Vigenere Cipher_text is: ",Vig_encryp_text)
# print(vig.vig_decrypt(Vig_encryp_text,key))
print("")
print("======================== RSA ENCRYPTION ==================================")
print("")
p = int(input(" - Enter a prime number (17, 19, 23, etc): "))
q = int(input(" - Enter another prime number (Not one you entered above): "))
public,private=rsa.generate_key_pair(p,q)
print("Public and Private keys are:",public,private)
print("")
rsa_encryp_text=rsa.encrypt(public,Vig_encryp_text)
print("RSA Cipher_text is : ",rsa_encryp_text)

print("")
# print(rsa.decrypt(private,rsa_encryp_text))
b='*'.join([str(elem) for elem in rsa_encryp_text])
print(b)
print("")
print("======================== HUFFMAN ENCODING ==================================")
print("")
hf_enc,hf_tree=hf.HuffmanEncoding(b)
print(type(hf_tree))
print(hf_tree)
print("Cipher text after huffman encoding is :")

print(hf_enc)
##x=hf.HuffmanDecoding(hf_enc,hf_tree)
##print(x)
##p=x.split('*')
##p=[int(elem) for elem in p]
##rsa_decryp_text=rsa.decrypt(private,rsa_encryp_text)
##print(rsa_decryp_text)
##vig_decryp_text=vig.vig_decrypt(rsa_decryp_text,key)
##print(vig_decryp_text)













