# 예외 만들기 
# 프로그래밍 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용. 
class myerror(Exception):
    pass
    def say(self,first):
        if first == "바보":
            raise myerror()
        print(first)
try:
    a = myerror()
    first = input()
    print(a.say(first))
    print(a.say("바보"))
    print(a.say("안녕하세요."))
    print(a.say("반갑습니다."))
    print(a.say("바보"))
    print(a.say("저녁 드세요."))    
except myerror:
    print("허용되지 않는 말이에요! 좋은말 고운말 쓰기!")
