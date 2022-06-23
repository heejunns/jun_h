#  오류 일부러 발생시키기 
# raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다. 
class bird:
    def fly(self):
        raise NotImplementedError 

class eagle(bird):
    def fly(self):
        print("날아올라요.")
a = eagle()
print(a.fly()) # 에러 발생 후 상속 클래스에 다시 fly 메서드를 작성하면 에러가 발생하지 않음.