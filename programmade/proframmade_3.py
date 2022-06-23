# 게시판 페이징하기 
# 페이징: 게시판의 페이지 수를 보여 주는 것 
import math # 오름차순 써야 할 듯?
x= int(input("게시물의 총 개수는 몇개 입니까?"))
def gettotalpage(x):
    n = 10 
    if x/n > 0:
        totlapage = math.ceil(x/n) 
    return totlapage   # x는 게시물의 총 건수 , n은 한 페이지에 보여줄 게시물 수

print("필요한 게시판의 수는"+str(gettotalpage(x))+"개 입니다.") 