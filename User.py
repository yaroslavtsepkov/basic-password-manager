import pandas as pd
from Utils import *
from Cipher import *
class User:
    """ Базовый класс user """
    
    def __init__(self, username, password):
        """ 
        Инициализация пользователя
        Входные параметры строковые username, password
        Возвращает экземпляр класса User
        """
        self.username: str = username
        self.password: str = password # Мастер ключ
        self.records = pd.DataFrame()
        self.email = None
        self.AES = AESCipher(self.password)

    def setConfig(self, email):
        """ 
        Простая функция конфигурации, принимает Email
        для того чтобы использовать его в будущем по умолчанию 
        """
        self.email = email

    def addRecord(self, record):
        """ 
        Добавление и шифрование записи в таблицу 
        Принимает параметр record - dict
        """
        if self.email is not None:
            record['email'] = self.email
        record['password'] = self.AES.encrypt(genPassword())
        self.records = self.records.append(pd.Series(record), ignore_index=True)
    
    def getRecords(self, password):
        """ 
        Функция возвращает все записи 
        Принимает параметр password строка 
        Если password соответсвует мастер паролю пользователя
        то все пароли будут расшифрованны, иначе выводит
        зашифрованные пароли
        """
        if password == self.password:
            return self.records['password'].map(lambda x: self.AES.decrypt(x))
        else:
            return self.records

    def getRecord(self, account, key):
        """ Поиск записи согласно аккаунту """
        return self.records.query("account == @account")

    def getUsername(self)->str:
        """ Вернуть имя пользователя """
        return self.username
    
    def getPassword(self)->str:
        """ Вернуть мастер пароль """
        return self.password

    def setPassword(self,password):
        """ Изменить мастер пароль """
        self.password = password

    def setUsername(self,username):
        """ Изменить имя пользователя """
        self.username = username

    def dumpFile(self, path, decrypt):
        """ Метод сохранения в файл """
        if decrypt.lower() == "yes":
            self.records['password'] = self.records['password'].map(lambda x: self.AES.decrypt(x))
            self.records.to_csv(path+'-decrypt'+'.csv', index=False)
        else:
            self.records.to_csv(path+'-encrypt'+'.csv', index=False)