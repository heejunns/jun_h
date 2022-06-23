# 5장 연습문제 
# 2번 
class calculator:
    def __init__(self):
        self.value = 0
    def add(self,val):
        self.value  += val 

class maxlimitcalculator(calculator):
    def add(self,val):
        self.value += val
        if self.value <= 100:
            return self.value
        else: 
            self.value = 100 
            return self.value
            
        

a = maxlimitcalculator()
a.add(50)
print(a.value)
a.add(49)
print(a.value)
a.add(5)
print(a.value)

