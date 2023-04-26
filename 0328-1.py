# except문 예외처리

try :
    4/0    
except :
    print()
    
    
try :
    4/0
except ZeroDivisionError:
    print()



try :
    4/0
except ZeroDivisionError as e:
    print(e)
    
# except문은 발생오류와 오류변수를 지정하여 사용한다.