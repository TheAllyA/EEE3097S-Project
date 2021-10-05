import os





f = raw_input("\n Hello, user. "
    "\n \n Please type in the path to your file and press 'Enter': ")
file = open(f, 'r')


os.system("mv " + f + " original")
os.system("tar xzf " + f)
os.system("mv rawData.csv decompressed")
string = os.system("cmp original decompressed")

if string == 0 :
        print("No difference between files")
