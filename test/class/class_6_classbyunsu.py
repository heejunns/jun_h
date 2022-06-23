# 클래스 변수 
class Family:
    lastname = "김" # 클래스 변수 : 클래스 안에 변수를 선언하여 생성. 

print(Family.lastname) # 클래스이름.클래스변수로 사용.
a = Family()
print(a.lastname) # 이런식으로 객체를 만들어 객체를 통해서도 클래스 변수 사용.
Family.lastname = "박"
print(Family.lastname) # 클래스 변수의 값을 변경하면 객체의 lastname 값도 변경된다.
print(a.lastname) # 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다. 
