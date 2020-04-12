# artcracker
Small python program that cracks passwords hashed with different algorithms.
Please don't use this for illegal purposes.

## Usage:
### 1) Using wordlists
```
python3 artcracker --wordlist <WORDLIST_NAME> <HASH> <HASH_TYPE>
```
### 2) Using combinations to crack the password
```
python3 artcracker --bruteforce <MIN_CHARACTERS> <MAX_CHARACTERS> <PASSWORD_HASHED> <HASH_TYPE>
```
You can use custom characters by adding --characters <CUSTOM_CHARACTERS> at the end of the --bruteforce argument

### Examples
#### With a wordlist
```
python3 artcracker --wordlist wordlist.txt d8578edf8458ce06fbc5bb76a58c5ca4 md5
```
#### With bruteforce
```
python3 artcracker --bruteforce 6 8 d8578edf8458ce06fbc5bb76a58c5ca4 md5
```
#### With bruteforce and custom characters
```
python3 artcracker --bruteforce 6 8 d8578edf8458ce06fbc5bb76a58c5ca4 md5 --characters qwerty
```

## Hashing algorithms available:
```
-md5
-sha1
-sha224
-sha256
-sha384
-sha512
```


## Built with
* [Python 3](https://www.python.org/downloads/) - The language used.
* Python modules used: hashlib, sys, string, itertools.

## Authors
* **[[LolArt](https://github.com/lilart)]**
