msg = 'Hello world from Head First Python'
id(msg)

def hello(a:str):
    return msg + a

id(hello)
type(msg)
type(hello)
hello()


#함수를 인수로 받아 함수를 작동시키기. '객체의 모음은 결국 객체이다.'
def apply(func:object, value:object) -> object:       
    return func(value)

apply(hello,'12')


####


def outer():
    def inner():
        print('This is inner.')
    print('This is outer, returning inner.')
    return inner

i = outer()
type(i)
i()


#### 여러 개의 인자를 받는 함수 생성

#1. 리스트 앞에 *가 붙으면 개개의 인자로 전달될 수 있게 확장된다.
def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

myfunc(10)
myfunc()
myfunc(10,20,30,40,50,60,70)

#2. **를 붙여서 딕셔너리의 key값과 value값으로 확장 가능하다.
def myfunc2(**kwargs):
    for k,v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

myfunc2(a=10, b=20)
myfunc2(a=10, b=20, c=30, d=40)
myfunc2()


#3. *와 **를 동시에 써서 해보기
def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k,v in kwargs.items():
            print(k, v, sep='->', end=' ')

myfunc3(1,2,3)
myfunc3()
myfunc3(1,2,3,4, a=10,b=20,c=30)
