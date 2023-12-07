import io
import os
from PIL import Image
from cryptography.fernet import Fernet

class ImageEncryption:
    #이미지를 암호화 하는 경우 key_path를 비우고 image_path만 넣어주면 된다.
    #이미지를 복호화 (암호화 해제)하는 경우 key_path에 key.txt 파일의 경로를 넣어주고 image_path에 암호화된 이미지의 경로를 넣어주면 된다.
    def __init__(self, image_path, key_path=None):
        self.image_path = image_path
        if key_path is None:
                self.key = Fernet.generate_key()
                self.image = Image.open(image_path)
        else:
            with open(key_path, 'r') as key_file:
                self.key = key_file.read().encode()
                print(self.key)
        self.cipher_suite = Fernet(self.key)
        print(self.cipher_suite)

    #이미지를 암호화 하는 경우 savePath에 암호화된 이미지를 저장할 경로를 넣어주면 된다. key.txt 파일도 같은 경로에 생성된다.
    def encrypt_image(self, savePath):
        with open(self.image_path, 'rb') as image_file:
            original_image_data = image_file.read()
        encrypted_data = self.cipher_suite.encrypt(original_image_data)
        with open(savePath, 'wb') as encrypted_image_file:
            encrypted_image_file.write(encrypted_data)
            
        # Get the directory of the image file
        directory = os.path.dirname(savePath)
        # Create the path for the key file
        key_path = os.path.join(directory, 'key.txt')
        
        with open(key_path, 'w') as key_file:
            key_file.write(self.key.decode())

    #이미지를 복호화 (암호화 해제)하는 경우 savePath에 복호화된 이미지를 저장할 경로를 넣어주면 된다.
    def decrypt_image(self, savePath):
        with open(self.image_path, 'rb') as encrypted_image_file:
            encrypted_data = encrypted_image_file.read()
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        decrypted_image = Image.open(io.BytesIO(decrypted_data))
        if decrypted_image.mode == 'RGBA':
            decrypted_image = decrypted_image.convert('RGB')
        decrypted_image.save(savePath)
    #to be deleted
    def restore_image(self, savePath):
        with open(savePath, 'rb') as image_file:
            encrypted_data = image_file.read()
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        with open(savePath, 'wb') as image_file:
            image_file.write(decrypted_data)
        Image.open(savePath).show()
    #why do we need this?
    def save_decrypted_data(self, decrypted_data, file_path):
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)