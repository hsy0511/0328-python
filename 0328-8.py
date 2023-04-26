print(abs(-3))
print(all([1,2,0]))
print(any([1,2,0]))
print(chr(97))
print(dir([1]))
print(divmod(7, 3))
for i, name in enumerate(['body', 'foo', 'bar']):
     print(i, name)
print(eval('1+2'))
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
print(hex(3))
print(id(3))
# print(a = input('입력하세요: '))
print(int(3.4))
class Person: pass

a = Person()
print(isinstance(a, Person))

print(len("python"))
print(list("python"))
def two_times(x): 
    return x*2
print(list(map(two_times, [1, 2, 3, 4])))

print(max([1, 2, 3]))
print(min([1, 2, 3]))
print(oct(34))
# print(f = open("foo.txt", "r"))
print(ord('a'))
print(pow(2, 4))
print(list(range(5)))
print(round(4.6))
print(sorted([3, 1, 2]))
print(str(3))
print(sum([1,2,3]))
print(tuple("abc"))
print(type("abc"))
print(list(zip([1, 2, 3], [4, 5, 6])))

