# 생성자 : 객체가 생성 될 때 자동으로 호출되는 메서드를 의미.
class Fourcal:
    def __init__(self,first,second): # __init__ 으로 메소드 이름을 정의하게 되면 생성자로 인식하여 객체가 생성되면 자동 호출 된다.
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

a = Fourcal(4,6) # 이런식으로 setdata 메소드 객체변수 first,second 에 해당하는 값을 적었듯이 클래스 다음 괄호 안에 적어준다. 
print(a.add()) # 적어준 객체변수 first,second 값은 생성자 __init__ 메소드로 자동으로 전달 된다. 