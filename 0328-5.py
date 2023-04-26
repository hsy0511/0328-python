try:
    a = [1,2]
    b = a[3]
    print(b)
except IndexError:
    pass

# IndexError가 발생해야하는 문장을 회피한다.