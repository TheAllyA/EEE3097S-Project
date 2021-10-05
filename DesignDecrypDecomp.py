import os





f = raw_input("\n Hello, user. "
    "\n \n Please type in the path to your file and press 'Enter': ")
file = open(f, 'r')


os.system("tar xzf " + f)
