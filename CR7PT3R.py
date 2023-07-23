import hashlib
import os
from colorama import Fore, Style

while(True):
    try:
        os.system('cls')
        logo=("""{}  
   _____ _____  ______ _____ _______ ____  _____  
  / ____|  __ \|____  |  __ \__   __|___ \|  __ \ 
 | |    | |__) |   / /| |__) | | |    __) | |__) |
 | |    |  _  /   / / |  ___/  | |   |__ <|  _  / 
 | |____| | \ \  / /  | |      | |   ___) | | \ \ 
  \_____|_|  \_\/_/   |_|      |_|  |____/|_|  \_\
                                                  
                                                  
                                                                                                               
""".format(Fore.RED))
        print(logo)
        print(Fore.BLUE + "[1]SHA512\n[2]SHA384\n[3]SHA256\n[4]SHA224\n[5]SHA1\n[6]MD5")
        x = int(input("\n::>"))

        if(x == 1):
            os.system('cls')
            print(logo)
            data =input(Fore.BLUE +"~/SHA512:> ")
            sha512crypt = hashlib.sha512(data.encode()).hexdigest()
            print("HASH: "+sha512crypt)
            y = str(input("Return Main Menu [Y/n]: "))

        if(x == 2):
            os.system('cls')
            print(logo)
            data =input(Fore.BLUE +"~/SHA384:> ")
            sha384crypt = hashlib.sha384(data.encode()).hexdigest()
            print("HASH: "+sha384crypt)
            y = str(input("Return Main Menu [Y/n]: "))

        if(x == 3):
            os.system('cls')
            print(logo)
            data =input(Fore.BLUE +"~/SHA256:> ")
            sha256crypt = hashlib.sha256(data.encode()).hexdigest()
            print("HASH: "+sha256crypt)
            y = str(input("Return Main Menu [Y/n]: "))

        if(x == 4):
            os.system('cls')
            print(logo)
            data =input(Fore.BLUE +"~/SHA224:> ")
            sha224crypt = hashlib.sha224(data.encode()).hexdigest()
            print("HASH: "+sha224crypt)
            y = str(input("Return Main Menu [Y/n]: "))

        if(x == 5):
            os.system('cls')
            print(logo)
            data =input(Fore.BLUE +"~/SHA1:> ")
            sha1crypt = hashlib.sha1(data.encode()).hexdigest()
            print("HASH: "+sha1crypt)
            y = str(input("Return Main Menu [Y/n]: "))
            
        if(x == 6):
            os.system('cls')
            print(logo)
            data =input(Fore.BLUE +"~/MD5:> ")
            md5crypt = hashlib.md5(data.encode()).hexdigest()
            print("HASH: "+md5crypt)
            y = str(input("Return Main Menu [Y/n]: "))
        
        if(y=="Y"or y=="y"):
            continue
        elif(y=="n" or y =="N"):
            print(Style.RESET_ALL)
            break
        

    except KeyboardInterrupt:
        print("\n\nBye")
        print(Style.RESET_ALL)
        break
