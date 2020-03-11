# import the hashlib library for performing hashing functions
import hashlib

# create an initial test string
some_string = "ecsc"

# create an MD5 hash object
hash = hashlib.md5(some_string.encode()).hexdigest()


while hash != 'c89aa2ffb9edcc6604005196b5f0e0e4':
    hash = hashlib.md5(hash.encode()).hexdigest()

    print(hash)