class a:
    def b(self):
        raise NotImplementedError
    
class s(a):
    pass

ss = s()
ss.b()
    # raise 명령어로 강제 오류를 발생시킨 클래스를 상속 받아 오류가 발생함 
class s(a):
    def b(slef):
        print('hello')

ss = s()
ss.b()
    # 강제 오류를 발생시킨 클래스를 오버라이딩하여 매서드를 재구현해서 오류가 발생하지 않음 