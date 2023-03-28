# 0328-python
# 예외처리
# 오류 예외처리 기법
## try, except문
```python
try :
    4/0
except ZeroDivisionError as e:
    print(e)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228095657-0a385848-1b08-478e-9b4b-14a4f30286f6.png)

except문은 발생오류와 오류변수를 통해 오류내용을 알고싶을때 방법이다.
###### ※ [] 기호를 사용하면 [] 안에있는 내용을 생략할 수 있다는 표기법이다.
## try, finally문
```python
try:
    f = open('foo.txt','w')
    print('hello')
    
finally:
    f.close()
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228096460-7e7e9bd1-efb5-495a-a44e-08e932e0c932.png)

try문을 수행중에 예외 발생 여부와 상관없이 항상 수행된다.(파일을 닫을 때 주로 사용됨.)
## 여러개 오류 처리하기
```python
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228097272-af6b527b-93bc-4f89-a8f1-41bf958e23db.png)

2개 이상의 오류를 처리할 때는 () 괄호안에 발생오류를 적은 후 사용한다.
###### ※ 먼저 받은 오류만 출력되고 나머지 오류는 출력하지 않는다.
