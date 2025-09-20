import random

class DATA:
    name = 'Денис'
    password = '413121'
    Email = 'denis_balashov_31_197@yandex.ru'
    
    @staticmethod
    def generate_email():
        return 'denis_balashov_31'+ str(random.randint(100,999)) + '@yandex.ru'

    @staticmethod
    def generate_password():
        return str(random.randint(100000,999999))
    @staticmethod
    def generate_name():
        names = ['Вадим', 'Сергей', 'Илья', 'Константин', 'Алексей', 'Равшан', 'Джамшут']
        return random.choice(names)