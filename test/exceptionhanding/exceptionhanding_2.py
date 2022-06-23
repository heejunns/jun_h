# 예외처림 except,else
try:
    age = int(input("나이를 입력하세요"))
except:
    print("입력이 정확하지 않아요.")
else:
    if age >= 20:
        print("성인 이네요.")
    else:
        print("미성년자네요.")