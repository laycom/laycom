
class Generator:
    def __init__(self):
        self.state = 0
        self.length = 0
        self.alphabet = '0123456789qwertyuiopasdfghjklzxcvbnm'
        self.base = len(self.alphabet)

    def next(self):

        password = ''
        temp_state = self.state

        while temp_state > 0:
            ceil = temp_state // self.base
            rest = temp_state % self.base
            password = self.alphabet[rest] + password
            temp_state = ceil

        password = self.alphabet[0] * (self.length - len(password)) + password

        self.state += 1
        if password == self.alphabet[-1] * self.length:
            self.length += 1
            self.state = 0

        return password
