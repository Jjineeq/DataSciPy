
class calculator:
    def __init__(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result

    def num(self,num):
        self.result *= num
        return self.result