class Generator:
    def __init__(self):
        self.password_list = ['0', '123', '12345']
        self.index = 0

    def next(self):
        if self.index < len(self.password_list):
            result = self.password_list[self.index]
            self.index += 1
        else:
            result = None

        return result
