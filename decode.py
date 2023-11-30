# decode the password base64
import base64

def decode_64 (password):
    decode = base64.b64decode(password)
    print(decode)

the_code = input("Enter Your encode password: ")
decode_64(the_code)