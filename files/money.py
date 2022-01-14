class Money:
    def __init__(self, number):
        self.number = number

    def __iadd__(self, money):
        self.number += money
        print(self.number)