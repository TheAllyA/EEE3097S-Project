






os.system("mv " + f + " original")
os.system("tar xzf " + f + ".tar.gz")
os.system("mv rawData.csv decompressed")
string = os.system("cmp original decompressed")

if string == 0 :
        print("No difference between files")
