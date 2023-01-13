#for secure connection to transmit data with end to end encryption

from cryptography.fernet import Fernet
key = b'542ZkZPChbIxUSq53Mcjt4OduQGZSWCCYhFQ_TY7-AA='
# using the generated key
fernet = Fernet(key)
def encrypt(data):
    # encrypting the data
    encrypted = fernet.encrypt(data)
    return encrypted
def decrypt(data):
    decrypted = fernet.decrypt(data)
    return decrypted

def encrypt_file(file):
    with open(file, 'rb') as f:
        original = f.read()

    encrypted_file_data = fernet.encrypt(original)
    with open(file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_file_data)
def decrypt_file(file):
    with open(file, 'rb') as f:
        original = f.read()
    decrypted_file_data = fernet.decrypt(original)
    with open(file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_file_data)




