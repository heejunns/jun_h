# 클래스 상속 
# => 어떤 클래스를 만들 때 다른 클래스의 기능을 물려 받을 수 있다. 
from audioop import add
from distutils.command.build_scripts import first_line_re


class Fourcal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
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
# class 클래스 이름(상속할 클래스 이름)
class MoreFourcal(Fourcal): # 클래스를 상속하기 위해서는 클래스 이름 뒤 괄호 안에 상속하라 클래스 이름을 넣어 주면 된다. 
    def pow(self): # 거듭제곱 메서드 생성 
        result = self.first ** self.second
        return result     
# 상속은 기존 클래스의 기능은 그대로 놔두고 기능을 확장시킬 때 주로 사용한다. 
a = MoreFourcal(2,3)
print(a.add())
print(a.pow())
