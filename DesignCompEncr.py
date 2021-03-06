import os
from cryptography.fernet import Fernet

fR = input("\n Hello, user. "
    "\n \n Please type in the path to your file and press 'Enter': ")
file = open(fR, 'r')

os.system("mv " + fR + " rawData.csv")
os.system("tar czf rawData.csv.tar.gz rawData.csv")

#print("File size for original file is: ")
os.system("ls -l rawData.csv > originalsize.txt")

#print("File size for compressed file is: ")
os.system("ls -l rawData.csv.tar.gz > compressedsize.txt")



with open('originalsize.txt') as a:
    line = a.readline()  # read up to 8 chars from first line
print("Size of original file is " + line[19:-25] + " Bytes")

with open('compressedsize.txt') as a:
    compressedline = a.readline()  # read up to 8 chars from first line
print("Size of compressed file is " + compressedline[19:-32] + " Bytes")

originalsize = float(line[19:-25])
compressedsize = float(compressedline[19:-32])

reduction = ((originalsize-compressedsize)/originalsize)*100

print("Compression ratio : " + str(reduction) + "%")

os.system("mv rawData.csv " + fR)
#os.system("mv rawData.csv.tar.gz " + f + ".tar.gz")
os.system("rm originalsize.txt compressedsize.txt")

#    def key_create:
e_key = Fernet.generate_key()
#        return e_key

#    def key_write(key, key_name):
with open('mykey.e_key','wb') as mykey:
    mykey.write(e_key)

f = Fernet(e_key)

with open('rawData.csv.tar.gz','rb') as zipped_file:
    zipped = zipped_file.read()

encrypted_file = f.encrypt(zipped)

with open('finalEncrypt.csv.tar.gz','wb') as finalEncrypt:
    finalEncrypt.write(encrypted_file)


with open('finalEncrypt.csv.tar.gz','rb') as e:
    encrypted = e.read()

decrypted_file = f.decrypt(encrypted)

with open('finalDecrypt.csv.tar.gz','wb') as finalDecrypt:
    finalDecrypt.write(decrypted_file)

#f = raw_input("\n Hello, user. "
#    "\n \n Please type in the path to your file and press 'Enter': ")
#file = open(finalDecrypt, 'r')


os.system("mv " + fR + " original")
os.system("tar xzf finalDecrypt.csv.tar.gz")
#os.system("mv finalDecrypt.csv rawData.csv")
string = os.system("cmp original rawData.csv")

if string == 0 :
        print("No difference between files")

