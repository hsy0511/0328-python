import datetime
day = datetime.date(2005,5,11)
print(day)

import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('출력할 형식 포맷 코드'))
for i in range(10):
    print(i)
    time.sleep(0.01)
    
import math
print(math.gcd(60,80,100))
print(math.lcm(15, 25))

import random
print(random.random())
print(random.randint(1, 10)) 
a = [1,2,3,4,5]
print(random.choice(a))
print(random.sample(a,3))   

import itertools
a = ['사과','배','복숭아','자두']
b = ['s','b','b']
c = itertools.zip_longest(a,b,fillvalue='j')
print(list(c))
print(list(itertools.permutations(['1', '2', '3'],2)))
print(len(list(itertools.combinations(range(1, 46), 6))))

import functools
data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)

from operator import itemgetter

a = [
    ('a',1),
    ('b',2),
    ('c',3),
]

result = sorted(a,key=itemgetter(1))
print(result)

import shutil
shutil.copy("c:/test/파일.txt", "c:/doit/새파일.txt")
shutil.move("c:/test/파일.txt", "c:/doit/새파일.txt")

import glob
print(glob.glob("c:/doit/s*"))

import pickle
f = open("파일.text",'wb')
data = {1 :'python',2:'you need'}
pickle.dump(data.f)
f.close

f = open("파일.txt", 'rb')
data = pickle.load(f)
print(data)

import os
os.environ['PATH']
os.chdir("C:\WINDOWS")
os.getcwd()
os.system("dir")
os.popen("dir")

import zipfile
with zipfile.ZipFile('mytext.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')
    
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extractall()
    
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extract('a.txt')
    
'''
만약 파일을 압축하여 묶고 싶은 경우에는 compression, compresslevel 옵션을 사용할 수 있다.
compression에는 4가지 종류가 있다.
ZIP_STORED - 압축하지 않고 파일을 Zip으로만 묶는다. 속도가 빠르다.
ZIP_DEFLATED - 일반적인 ZIP 압축으로 속도가 빠르고 압축률은 낮다. (호환성이 좋다.)
ZIP_BZIP2 - bzip2 압축으로 압축률이 높고 속도가 느리다.
ZIP_LZMA - lzma 압축으로 압축률이 높고 속도가 느리다. (7zip과 동일한 알고리즘으로 알려져 있다.)
compressionlevel은 압축 수준을 의미하는 숫자값으로 1 ~ 9를 사용한다.
1은 속도가 가장 빠르고 압축률이 낮고, 9는 속도는 가장 느리지만 최대 압축을 한다.
'''
import threading 
# threading.Thread를 사용하여 만든 스레드 객체가 동시 작업을 가능하게 함

# tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 나타냄
# tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 나타냄
# traceback은 프로그램 실행 중 발생한 오류를 추적할 때 사용함
# json.load(파일객체)는 파일을 읽을 때 사용함
# json.dump(딕셔너리, 파일 객체)는 파일을 생성할 때 사용함
# urllib은 URL을 읽고 분석할 때 사용함
# webbrowser는 파이썬 프로그램에서 시스템 브라우저를 호출할 때 사용함