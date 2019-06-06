import hashlib, sys, threading, string
from itertools import product

def md5_check(passwrd_hashed, generated):
    result = hashlib.md5(generated.encode())
    if result.hexdigest() == passwrd_hashed:
        print("PASSWORD FOUND!!\nTHE PASSWORD IS: "+generated)
        quit()
    else: return

def sha1_check(passwrd_hashed, generated):
    result = hashlib.sha1(generated.encode())
    if result.hexdigest() == passwrd_hashed:
        print("PASSWORD FOUND!!\nTHE PASSWORD IS: "+generated)
        quit()
    else: return

def sha224_check(passwrd_hashed, generated):
    result = hashlib.sha224(generated.encode())
    if result.hexdigest() == passwrd_hashed:
        print("PASSWORD FOUND!!\nTHE PASSWORD IS: "+generated)
        quit()
    else: return

def sha256_check(passwrd_hashed, generated):
    result = hashlib.sha256(generated.encode())
    if result.hexdigest() == passwrd_hashed:
        print("PASSWORD FOUND!!\nTHE PASSWORD IS: "+generated)
        quit()
    else: return

def sha384_check(passwrd_hashed, generated):
    result = hashlib.sha384(generated.encode())
    if result.hexdigest() == passwrd_hashed:
        print("PASSWORD FOUND!!\nTHE PASSWORD IS: "+generated)
        quit()
    else:return

def sha512_check(passwrd_hashed, generated):
    result = hashlib.sha512(generated.encode())
    if result.hexdigest() == passwrd_hashed:
        print("PASSWORD FOUND!!\nTHE PASSWORD IS: "+generated)
        quit()
    else: return
        
def cracking_pass(passwrd_hashed, hash_type, generated):
    if hash_type == "md5":
        md5_check(passwrd_hashed, generated)
    if hash_type == "sha1":
        sha1_check(passwrd_hashed, generated)
    if hash_type == "sha224":
        sha224_check(passwrd_hashed, generated)
    if hash_type == "sha256":
        sha256_check(passwrd_hashed, generated)
    if hash_type == "sha384":
        sha384_check(passwrd_hashed, generated)
    if hash_type == "sha512":
        sha512_check(passwrd_hashed, generated)
    else:print("Hash type error, we have the following hash types available:\n\tmd5\n\tsha1\n\tsha224\n\tsha256\n\tsha384\n\tsha512")

def wordlist_method(wordlist, passwrd_hashed, hash_type):
    for generated in wordlist.readlines():
        generated.replace("\n","")
        t = threading.Thread(target=cracking_pass, args=(passwrd_hashed, hash_type, generated, ))
        t.start
        x+=1
        print("\rPaswords used: {}, current password: {}".format(x, generated), end="\r")

def bruteforce_method(min_characters, max_characters, passwrd_hashed, hash_type):
    characters = [char for char in string.printable.replace("\t\n\r\x0b\x0c","")]
    print("Characters going to be used: "+characters)
    if max_characters < min_characters:
        print("The max number of characters is smaller than the min number of characters\nUsage: python3 {} <MIN_CHARACTERS> <MAX_CHARACTERS> <OUTPUT FILE>".format(sys.argv[0]))
        quit()
    for lenght in range(min_characters, max_characters):
        for item in product(characters, repeat=lenght):
            generated = "".join(item)
            t = threading.Thread(target=cracking_pass, args=(passwrd_hashed, hash_type, generated, ))
            t.start
            x+=1
            print("\rPaswords used: {}, current password: {}".format(x, generated), end="\r")

if __name__ == '__main__':
    try:
        if sys.argv[1] == "--wordlist":
            try:
                wordlist = open(sys.argv[2], "r")
            except FileNotFoundError:
                print("That file does not exist, please input an already existing file or path.\nIf you dont have a wordlist, you can use the bruteforce method or you can create a wordlist with the tool: https://github.com/lilart/wordlistgenerator")
            passwrd_hashed = sys.argv[3]
            hash_type = sys.argv[4]
            wordlist_method(wordlist, passwrd_hashed, hash_type)
        if sys.argv[1] == "--bruteforce":
            min_characters = int(sys.argv[2])
            max_characters = int(sys.argv[3]) + 1
            passwrd_hashed = sys.argv[4]
            hash_type = sys.argv[5]
            bruteforce_method(min_characters, max_characters, passwrd_hashed, hash_type)
    except:
        print("  Usage: \n\t1) python3 {} --wordlist <WORDLIST_NAME> <PASSWORD_HASHED> <HASH_TYPE>\n\t2) python3 {} --bruteforce <MIN_CHARACTERS> <MAX_CHARACTERS> <PASSWORD_HASHED> <HASH_TYPE>".format(sys.argv[0], sys.argv[0]))
