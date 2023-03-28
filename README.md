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
## try, else
```python
try:
    4/2
except:
    print('오류가 발생합니다.')
else:
    print('오류가 없습니다.')
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228098532-64d459f3-aec0-4d9e-8f87-a5ba2ec47c9b.png)

try문에서 오류가 있으면 except가 실행되고, 오류가 없을 때 else문이 실행됩니다.
# 오류회피하기
## pass
```python
try:
    a = [1,2]
    b = a[3]
    print(b)
except IndexError:
    pass
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228099434-ddca7cb3-8bc2-4e33-acf3-95595020c0e2.png)

IndexError가 발생해야하는 문장을 회피한다.
# 오류 일부러 발생시키기
## raise 명령어
```python
class a:
    def b(self):
        raise NotImplementedError
    
class s(a):
    pass

ss = s()
ss.b()
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228101386-06b986fb-1196-44e4-9319-435199893984.png)

raise 명령어로 강제 오류를 발생시킨 클래스를 상속 받아 오류가 발생한다.
## raise 명령어에서 강제 오류 벗어나는 방법
```python
class a:
    def b(self):
        raise NotImplementedError
        
class s(a):
    def b(slef):
        print('hello')

ss = s()
ss.b()
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228101663-77466816-5628-4231-8335-2d44255ec474.png)

raise 명령어로 강제 오류를 발생시킨 클래스를 오버라이딩하여 매서드를 재구현해서 오류가 발생하지 않게 한다.
# 예외 만들기
## 내장클래스 Exception
```python
class myError(Exception):
    pass

def seefood(food):
    if food == '간장게장':
        raise myError()
    print(food)
    
seefood('양념게장')
seefood('간장게장')
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228103930-d3005a92-9ab3-4152-a55a-df460b2e89b9.png)

파이썬 내장클래스인 Exception를 상속받아 바보가 나올 때 예외를 만듭니다.
## 만든 예외를 예외 처리 하는 방법
```python
class myError(Exception):
    pass

def seefood(food):
    if food == '간장게장':
        raise myError()
    print(food)
    
try :
    seefood('양념게장')
    seefood('간장게장')
except myError:
    print('간장게장은 다 떨어졌습니다.')
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228104697-c2a251fe-02ac-4374-b1d9-e63a50bdaf8b.png)

try, except문을 사용하여 예외처리를 한다.
# Python 내장함수
## abs
```python
print(abs(-3))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228110062-998d5f57-b134-409c-be01-48d182d7ad1d.png)
abs 함수는 절대값을 나타낸다.
## all
```python
print(all([1,2,0]))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111314-d5969ecf-721b-45b3-abb6-6e13f97e3537.png)

all 함수는 반복가능한 데이터 x값에서 다 참이면 true 하나라도 거짓이 있으면 false를 나타냄
## any
```python
print(any([1,2,0]))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111344-ca3d7189-5f90-4a0a-b21c-266aca849814.png)

any 함수는 반복능한 데이터 x값에서 모두가 거짓이어야만 false 하나라도 참이면 true를 나타냄
## chr
```python
print(chr(97))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111368-1893a829-704d-4b8c-9deb-302f1ee798fd.png)

chr 함수는 유니코드 숫자값을 받아 그 코드에 해당하는 문자를 나타냄
## dir
```python
print(dir([1]))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111416-c16c7910-e4c8-4184-870f-3cdb4fed4ae2.png)

dir 함수는 객체가 지닌 변수나 함수를 보여줌
## divmod
```python
print(divmod(7, 3))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111449-b844854b-90fb-4e9d-a500-37bb0c8768bf.png)

divmod 함수는 2개의 숫자를 입력 받아 2개의 숫자의 나눈 몫과 나머지를 튜플로 나타냄
## enumerate
```python
for i, name in enumerate(['body', 'foo', 'bar']):
     print(i, name)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111478-7bb8f3c4-683f-4dc1-b93e-e8f4d8820c74.png)

enumerate 함수는 순서가 있는 데이터를 입력받아 인덱스 값을 포함하는 객체를 나타냄
## eval
```python
print(eval('1+2'))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111500-2743267a-f692-400b-a07b-abb81f75381a.png)

eval 함수는 문자열로 구현된 표현식을 입력받아 실행한 결과값을 나타냄
## filter
```python
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111535-299993dd-09fc-4c2a-a8a2-fa07448d2777.png)

filter 함수는 함수의 첫번째 인수를 함수에 차례로 들어갈 반복 가능한 데이터를 받고, 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때 반환값이 참인 것만 나타낸다.
## hex
```python
print(hex(3))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111550-e67a25fe-ad3f-4f7b-862e-c731976c332c.png)

hex 함수는 정수를 입력받아 16진수 물자열로 변환하여 나타냄
## id
```python
print(id(3))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111571-e575df54-e41f-41a3-9b45-aa915d067e74.png)

id 함수는 객체의 고유 주소값을 나타냄
## input
```python
print(a = input('입력하세요: '))
```

input 함수는 사용자 입력을 받는다.
## int
```python
print(int(3.4))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228111623-06df2055-0ee5-4ca0-ad14-4e4a7e498042.png)

int 함수는 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 나타냄
## isinstance
```python
class Person: pass

a = Person()
print(isinstance(a, Person))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112355-9bd53bc4-d125-44cd-ad22-4fedb11c627d.png)

isinstance 함수는 첫번째 인수로 객체 두번째로 인수로 클래스를 받고 받은 객체가 받은 클래스의 인스턴스인지 참,거짓으로 판단해 True,False 값을 나타냄
## len
```python
print(len("python"))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112399-cb8fa0ba-ab91-48f2-ba9f-eae014807ac5.png)

len 함수는 입력값의 길이를 나타냄
## list
```python
print(list("python"))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112438-9483de98-28a7-4aca-8754-2256f15fe25f.png)

list 함수는 반복 가능한 데이터를 입력받아 리스트로 만들어 나타냄
## map
```python
def two_times(x): 
    return x*2
print(list(map(two_times, [1, 2, 3, 4])))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228113063-5071220e-4cfd-4d79-9405-7ff78d62acda.png)

map 함수는 반복 가능한 데이터를 입력받고 입력받은 데이터의 각 요소에 함수를 적용한 결과 값을 나타냄
## max
```python
print(max([1, 2, 3]))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112497-cc301c76-34c8-45d4-a07b-0d3f114c7b48.png)

max 함수는 인수로 반복 가능한 데이터를 입력받아 그 최대값을 나타냄
## min
```python
print(min([1, 2, 3]))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112515-74cce933-ea85-4945-b53c-41e94afb2e22.png)

min 함수는 인수로 반복 가능한 데이터를 입력받아 그 최솟값을 나타냄
## oct
```python
print(oct(34))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112522-c79976bd-5993-4716-bbc3-4b5966c14040.png)

oct 함수는 정수를 8진수 바꾸어 문자열로 나타냄
## open
```python
print(f = open("foo.txt", "r"))
```

open 함수는 파일을 지정한 모드로 나타냄
## ord
```python
print(ord('a'))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112557-4b5a407b-f52a-4e16-bfab-db7401b4ce73.png)

ord 함수는 문자의 유니코드 숫자값을 나타냄
## pow
```python
print(pow(2, 4))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112580-59033f8c-b421-4776-8e55-7b86b6b53193.png)

pow 함수는 숫자의 제곱을 나타냄
## range
```python
print(list(range(5)))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112608-87f8d8ad-7302-42b7-86fa-eab5ad765632.png)

range 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 나타냄
## round
```python
print(round(4.6))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112680-86616e03-0a37-45b8-86f5-97412526aa89.png)

round 함수는 숫자를 반올림하여 나타냄
## sorted
```python
print(sorted([3, 1, 2]))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112646-baeb0d67-8f52-488d-8596-255d32343d85.png)

sorted 함수는 입력 데이터를 오름차순으로 정렬해 나타냄
## str
```python
print(str(3))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112726-0b3ba1fb-2642-46f8-87e3-21b40502b2e5.png)

str 함수는 문자열 형태로 객체를 변환하여 나타냄
## sum
```python
print(sum([1,2,3]))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112744-a8a786a9-bfb1-4f01-b239-22a6290f4b54.png)

sum 함수는 입력데이터의 합을 나타냄
## tuple
```python
print(tuple("abc"))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112773-edd457cd-8714-4087-b91c-0fe93d956fc4.png)

tuple 함수는 반복 가능한 데이터를 튜플로 바꾸어 나타냄
## type
```python
print(type("abc"))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112804-711abb59-3530-42d6-9ce8-f9719e462a98.png)

type 함수는 입력값의 자료형이 무엇인지 나타냄
## zip
```python
print(list(zip([1, 2, 3], [4, 5, 6])))
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/228112835-6ceef8f3-6e09-49de-91c6-234ca126f28b.png)

zip 함수는 동일한 인덱스로 이루어진 데이터들을 묶어서 나타냄
# 표준 라이브러리
## datetime.date
```python
import datetime
day = datetime.date(2005,5,11)
print(day)
```
datetime.date는 년, 월, 일로 날짜를 표현할 때 사용하는 함수이다.
## time
```python
import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('출력할 형식 포맷 코드'))
for i in range(10):
    print(i)
    time.sleep(0.01)
```
time.time()은 현재 시간을 1970년 기준으로 지난 시간을 초 단위로 돌려준다.

time.localtime은 time.time()이 받은 실수 값을 사용해서 년, 월, 일, 시, 분, 초의 형태로 바꾸어 주는 함수이다.

time.localtime에 받은 값을 튜플로 보기 쉬운 형태로 나타낸다.

time.ctime은 현재 시간을 나타낸다.

strftime은 시간 함수의 포멧코드를 제공한다.

time.sleep은 일정한 시간 간격을 두고 루프를 실해한다.
## math.gcd
```python
import math
print(math.gcd(60,80,100))
```
math.gcd 함수를 이용하면 최대공약수를 구하기 쉽다.
## math.lcm
```python
import math
print(math.lcm(15, 25))
```
math.lcm 함수를 이용하면 최소공배수를 구하기 쉽다
## random
```python
import random
print(random.random())
print(random.randint(1, 10)) 
a = [1,2,3,4,5]
print(random.choice(a))
print(random.sample(a,3))
```
random은 난수를 발생시킨다.

random.random()은 0.0부터 1.0 사이의 실수 중에서 난수 값을 나타낸다.

random.randint는 정수 중에서 난수 값을 나타낸다.

random.choice는 입력받은 리스트에서 무작위로 하나의 값을 나타낸다

random.sample은 입력받은 리스트에서 무작위로 정한 개수만큼에 값 나타낸다

## itertools.zip_longest
```python
import itertools
a = ['사과','배','복숭아','자두']
b = ['s','b','b']
c = itertools.zip_longest(a,b,fillvalue='j')
print(list(c))
```
itertools.zip_longest는 같은 개수 자료형을 묶고, 전달한 반복 가능 객체의 길이가 다르면 긴 것을 기준으로 빠진 값은 fillvalue로 채울 수 있다.
## itertools.permutation
```python
import itertools
print(list(itertools.permutations(['1', '2', '3'],2)))
```
itertools.permutations는 반복 가능 객체 중에서 선택한 순열을 이터레이터로 나타낸다.
###### ※ 이터레이서는 자바의 컬렉션(Collection)에 저장되어 있는 요소들을 순회하는 인터페이스
## itertools.combination
```python
import itertools
print(len(list(itertools.combinations(range(1, 46), 6))))
```
itertools.combinations는 반복 가능 객체 중에서 선택한 조합을 이터레이터로 나타낸다.
## functools.reduce
```python
import functools
data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)
```
functools.reduce는 함수를 반복 가능한 객체의 요소에 차례대로 누적 적용하여 객체를 하나의 값으로 줄인다.
## operator.itemgetter
```python
from operator import itemgetter
a = [
    ('a',1),
    ('b',2),
    ('c',3),
]
result = sorted(a,key=itemgetter(1))
print(result)
```
operator.itemgetter는 주로 sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬하는 할 수 있도록 도와준다.
## shutil
```python
import shutil
shutil.copy("c:/test/파일.txt", "c:/doit/새파일.txt")
shutil.move("c:/test/파일.txt", "c:/doit/새파일.txt")
```
shutil은 파일을 복사 하거나 이동할 때 사용한다.
## glob
```python
import glob
print(glob.glob("c:/doit/s*"))
```
glob은 디렉터리에 있는 파일을 리스트로 만든다
## pickle
```python
import pickle
f = open("파일.text",'wb')
data = {1 :'python',2:'you need'}
pickle.dump(data.f)
f.close

f = open("파일.txt", 'rb')
data = pickle.load(f)
print(data)
```
pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 한다.

pickle.dump는 딕셔너리 객체를 그대로 차일에 저장한다.

pickle.load는 원래있던 딕셔너리 객체 상태 그대로 불러온다.
## os
```python
import os
os.environ['PATH']
os.chdir("C:\WINDOWS")
os.getcwd()
os.system("dir")
os.popen("dir")
```
os는 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해준다.

내 시스템의 환경 변수값을 알고 싶을 때 - os.environ

디렉터리 위치 변경하기 - os.chdir

디렉터리 위치 돌려받기 - os.getcwd

시스템 명령어 호출하기 - os.system

실행한 시스템 명령어의 결과값 돌려받기 - os.popen
## zipfile
```python
import zipfile
with zipfile.ZipFile('mytext.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')
    
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extractall()
    
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extract('a.txt')
```
zipfile은 여러 개의 파일을 zip 형식으로 합치거나 이를 해제할 때 사용한다.

myzip.write는 파일을 합친다.

myzip.extractall는 모든 파일을 해체한다.

myzip.extract는 특정 파일을 해체한다.

파일을 묶을 때는 compression, compresslevel을 사용한다.

compression에는 4가지 종류가 있다.

ZIP_STORED - 압축하지 않고 파일을 Zip으로만 묶는다. 속도가 빠르다.

ZIP_DEFLATED - 일반적인 ZIP 압축으로 속도가 빠르고 압축률은 낮다.

ZIP_BZIP2 - bzip2 압축으로 압축률이 높고 속도가 느리다.

ZIP_LZMA - lzma 압축으로 압축률이 높고 속도가 느리다.

compressionlevel은 압축 수준을 의미하는 숫자값으로 1 ~ 9를 사용한다.

1은 속도가 가장 빠르고 압축률이 낮고, 9는 속도는 가장 느리지만 최대 압축을 한다.
## threading
threading.Thread를 사용하여 만든 스레드 객체가 동시 작업을 가능하게 한다.
## tempfile
tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 나타냄

tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 나타냄

## traceback
traceback은 프로그램 실행 중 발생한 오류를 추적할 때 사용함

## json
json.load(파일객체)는 파일을 읽을 때 사용함

json.dump(딕셔너리, 파일 객체)는 파일을 생성할 때 사용함

## urllib
urllib은 URL을 읽고 분석할 때 사용함

## webbrowser
webbrowser는 파이썬 프로그램에서 시스템 브라우저를 호출할 때 사용함
# 외부 라이브러리
## pip
pip은 파이썬 모듈이나 패키지를 쉽게 설치할 수 있도록 도와주는 도구이다.
### pip install
```
pip install SomePackage 
```
SomePackage는 설치받을 수 있는 특정 패키지다.
### pip uninstall
```
pip uninstall SomePackage
```
설치한 패키지를 삭제한다.
### 특정 버전으로 설치하기
```
pip install SomePackage==1.0.4
pip install SomePackage 
```
1.0.4버전의 SomePackage를 설치한다.
### 최신 버전으로 업그레이드하기
```
pip install --upgrade SomePackage 
```
--upgrade를 사용하여 최신버전으로 업그레이드 할 수 있다.
```
### 설치된 패키지 확인하기
```
pip list
```
설치한 패키지 목록을 출력한다.
## faker
faker는 테스트용 가짜 데이터를 생성할 때 사용한다.
### faker 사용해보기
```
from faker import Faker
fake = Faker('ko-KR')
fake.name()
```
한글이름을 출력하기 위해 한국을 의미하는 ko-KR을 전달하여 faker를 사용한다.
### faker 활용
![image](https://user-images.githubusercontent.com/104752580/228147995-572a7141-7d16-4e7a-8ff0-23d9f1690b0e.png)
## sympy
sympy는 방정식 기호를 사용하게 해주는 외부 라이브러리이다.
### sympy 사용해보기
```
from fractions import Fraction
import sympy

x = sympy.symbols("x")

f = sympy.Eq(x*Fraction('2/4'),100)

result = sympy.solve(f)
print(result)
# 200
```
x의 2/4가 100이면 100*2의 값이 x의 값이 된다.
###### ※ Fraction은 유리수를 표현할 때 사용
### sympy 활용
#### x ** 2 = 1 식의 해 구하기
```
import sympy
x = sympy.symbols("x")
f = sympy.Eq(x**2, 1)
sympy.solve(f)
```
x의 값의 2제곱이 1이면 x는 -1,1이 나온다. 
