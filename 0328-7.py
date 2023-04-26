class myError(Exception):
    pass

def seefood(food):
    if food == '간장게장':
        raise myError()
    print(food)
    
'''seefood('양념게장')
seefood('간장게장')'''

# 파이썬 내장클래스인 Exception를 상속받아 바보가 나올 때 예외를 만듭니다.

try :
    seefood('양념게장')
    seefood('간장게장')
except myError :
    print('간장게장은 다 떨어졌습니다.')