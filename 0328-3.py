try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
    
# 2개 이상의 오류를 처리할 때는 () 괄호안에 발생오류를 적은 후 사용한다.
# 먼저 받은 오류만 출력되고 나머지 오류는 출력하지 않는다.