# 5장 연습문제 
# 1번 
class calculator:
    def __init__(self):
        self.value = 0 
    def add(self, val):
        self.value += val 

class upgradecalculator(calculator):
    def minus(self, val):
        self.value -= val

a = upgradecalculator()
a.add(10)
a.minus(7)

print(a.value)