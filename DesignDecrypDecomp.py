import os
from cryptography.fernet import Fernet

with open('finalEncrypt.csv.tar.gz','rb') as e:  
    encrypted = e.read()

decrypted_file = f.decrypt(encrypted)

with open('finalDecrypt.csv.tar.gz','wb') as finalDecrypt:
    finalDecrypt.write(decrypted_file)

#f = raw_input("\n Hello, user. "
#    "\n \n Please type in the path to your file and press 'Enter': ")
file = open(finalDecrypt, 'r')


os.system("mv " + finalDecrypt + " original")
os.system("tar xzf " + finalDecrypt + ".tar.gz")
os.system("mv rawData.csv decompressed")
string = os.system("cmp original decompressed")

if string == 0 :
        print("No difference between files")
