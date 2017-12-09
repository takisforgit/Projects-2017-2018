import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

## MD5 example ##
'''
It is important to note the "b" preceding the string literal,
this converts the string to bytes, because the hashing function only takes
a sequence of bytes as a parameter
'''
hash_object =  hashlib.md5(b"Hello World")
print("MD5   :",hash_object.hexdigest())

'''
So, if you need to take some input from the console, and hash this input,
do not forget to encode the string in a sequence of bytes
'''
##mystring = input('Enter String to hash: ')
### Assumes the default UTF-8
##hash_object = hashlib.md5(mystring.encode())
##print(hash_object.hexdigest())

## SHA1 example ##
hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print("SHA1  :",hex_dig)

## SHA224 example ##
hash_object = hashlib.sha224(b'Hello World')
hex_dig = hash_object.hexdigest()
print("SHA224:",hex_dig)

## SHA256 example ##
hash_object = hashlib.sha256(b'Hello World')
hex_dig = hash_object.hexdigest()
print("SHA256:",hex_dig)

## SHA384 example ##
hash_object = hashlib.sha384(b'Hello World')
hex_dig = hash_object.hexdigest()
print("SHA384:",hex_dig)

## SHA512 example ##
hash_object = hashlib.sha512(b'Hello World')
hex_dig = hash_object.hexdigest()
print("SHA512:",hex_dig)


## DSA example ##
hash_object = hashlib.new('DSA')
hash_object.update(b'Hello World')
print("DSA   :",hash_object.hexdigest())


###################################################
''' In the following example we are hashing a password in order to store it in a database.
In this example we are using a salt. A salt is a random sequence added to the password string
before using the hash function. The salt is used in order to prevent dictionary attacks
and rainbow tables attacks. However, if you are making real world applications and working
with users' passwords, make sure to be updated about the latest vulnerabilities in this field.
If you want to find out more about secure passwords please refer to this article
https://crackstation.net/hashing-security.htm
'''

import uuid
import hashlib

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('ATTENTION ! The password does not match')
