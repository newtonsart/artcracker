# artcracker
Small python program that cracks passwords hashed with different algorithms

## Usage:
1) Using wordlists
'''
python3 artcracker --wordlist <WORDLIST_NAME> <PASSWORD_HASHED> <HASH_TYPE>
'''
2) Using combinations to crack the password
'''
python3 artcracker --bruteforce <MIN_CHARACTERS> <MAX_CHARACTERS> <PASSWORD_HASHED> <HASH_TYPE>
'''

## Hashing algorithms available:
'''
-md5
-sha1
-sha224
-sha256
-sha384
-sha512
'''
