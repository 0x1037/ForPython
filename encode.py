# encrypt user password 
import base64
def encrypt_password (password):
    encrypt = base64.b64encode(password.encode())
    print(encrypt)

code = input("Enter your password: ")
encrypt_password(code)