# 메서드 오버라디잉
# 메서드 div 기능에서 만약 4를 0으로 나눈다면 에러가 발생한다. 오류가 아닌 0을 돌려주도록 만들려면 
# 어떻게 해야할까?
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

# a = Fourcal(5,0)
# print(a.div()) 오류발생
class safeFourcal(Fourcal):
    def div(self):
        if self.second == 0 :
            return 0
        else:
            return self.first/self.second
# safeFourcal 클래스는 Fourcal 클래스의 div 메서드를 동일한 이름으로 다시 작성하였다. 
# 이렇게 상속한 클래스에 있는 메서드를 동일한 이름으로 다시 작성하는 것을 메서드 오버라이딩이라고 한다. 
# 이렇게 되면 div 메서드를 호출하면 상속받은 메서드가 호출되지 않고 새로 작성한 메서드가 호출된다. 
a = safeFourcal(5,0)
print(a.div())
