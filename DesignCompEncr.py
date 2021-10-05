import os

f = raw_input("\n Hello, user. "
    "\n \n Please type in the path to your file and press 'Enter': ")
file = open(f, 'r')

os.system("mv " + f + " rawData.csv")
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
