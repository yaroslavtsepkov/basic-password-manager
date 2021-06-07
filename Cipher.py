from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from hashlib import md5
import os


class AESCipher:
  """ Класс шифрования AES """

  def __init__(self, key):
    """ Инициализация объекта """
    self.key = md5(key.encode()).digest()[:16] # в качестве ключа выступает md5 хэш передеанного key
    self.iv = os.urandom(16) # iv генерируется 16 случаный бит 
    self.aes = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), default_backend()) # экземпляр AES 
    self.encryptor = self.aes.encryptor() # функция шифрования по умолчанию
    self.decryptor = self.aes.decryptor() # функция шифрования по умолчанию 
  
  def encrypt(self, data):
    """ 
    Функция шифрования 
    Принимает параметр data строка
    Возвращает шифрованную строку
    """
    self.encryptor = self.aes.encryptor()
    ct = self.encryptor.update(data.encode())+self.encryptor.finalize()
    return ct
  
  def decrypt(self, ct):
    """
    Функция дешифрования
    Принимает параметр шифрованная строка
    Возвращает чистую строку
    """
    self.decryptor = self.aes.decryptor()
    text = self.decryptor.update(ct)+self.decryptor.finalize()
    return text.decode()