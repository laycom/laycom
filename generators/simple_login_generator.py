class Generator:
    def __init__(self):
        self.login_list = ['cat', 'admin', 'jack']
        self.index = 0

    def next(self):
        if self.index < len(self.login_list):
            result = self.login_list[self.index]
            self.index += 1
        else:
            result = None

        return result
