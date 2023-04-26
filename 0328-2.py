try:
    f = open('foo.txt','w')
    print('hello')
    
finally:
    f.close()

# try문을 수행중에 예외 발생 여부와 상관없이 항상 수행된다.