# 사칙연산 클래스 만들기 
from cgi import print_form

class Fourcal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        add_result = self.first + self.second
        return add_result
    def mul(self):
        mul_result = self.first * self.second
        return mul_result
    def sub(self):
        sub_result = self.first - self.second
        return sub_result
    def div(self):
        div_result = self.first / self.second
        return div_result    
a = Fourcal()
b = Fourcal()
a.setdata(3,4)
b.setdata(10,7)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())





'''
print(a.first) 
print(a.second)
print(b.first) 
print(b.second)
print(id(a.first)) # 아래와 주소는 서로 다르다.각각 다른곳에 값이 저장된다. 
print(id(b.first)) 
# a 객체의 first,second 값은 b 객체의 first,second에 영향을 주지 않는다.
'''