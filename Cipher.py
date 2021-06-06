from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from hashlib import md5
import os


class AESCipher:
    def __init__(self, key):
      self.key = md5(key.encode()).digest()[:16]
      self.iv = os.urandom(16)
      self.aes = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), default_backend())
      self.encryptor = self.aes.encryptor()
      self.decryptor = self.aes.decryptor()
    
    def encrypt(self, data):
      self.encryptor = self.aes.encryptor()
      ct = self.encryptor.update(data.encode())+self.encryptor.finalize()
      return ct
    
    def decrypt(self, ct):
      self.decryptor = self.aes.decryptor()
      text = self.decryptor.update(ct)+self.decryptor.finalize()
      return text.decode()