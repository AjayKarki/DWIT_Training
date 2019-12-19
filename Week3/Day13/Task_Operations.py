class Operations:
    def __init__(self, num1: int, num2: int):  # to indicate that num1,num2 should be strictly int
        self.num1 = num1
        self.num2 = num2

    def add(self) -> int:  # to indicate that add strictly returns int
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


c = Operations(5, 2)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())
