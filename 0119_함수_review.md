# 02-01. 함수

## 1. Intro

* 함수는 decomposition & abstraction 이 중요한 과정
* abstraction
  * 복잡한 내용을 모르더라도 사용할 수 있도록



## 2. 함수 기초

#

## 3. 함수의 결과값 (output)

+ output (return)은 반드시 하나의 객체를 반환함 : ```None``` or ```something```

###  [1] void funtcion

### [2] value returning function

+ 함수 실행 후, return 문을 통해 값을 반환하고, 함수가 바로 종료됨

### [3] return vs. print

+ return 은 항상 하나의 객체를 반환

  ```return x, y``` 는 사실 ```return (x, y)``` 임

+ ```print```를 할당하면, ```None```으로 할당됨 

    ``` python
    a = print('good')
    b = 100
    c = print('bye')
    print(a,b,c)
    >>> good
        bye
        None 100 None

+ REPL(read - eval - print - loop) 환경 (예 : 주피터) 에서는 마지막 작성 코드의 reutrn 값 보여줌



## 4. 함수의 입력 (input)

### [1] argument

+ argument 란 함수 호출 시에 함수의 parameter를 통해 전달되는 값

+ parameter (매개변수)란 함수 실행 시, 함수 내부에서 사용되는 식별자 / 함수 안의 명령어들을 실행하는 데 필요한 data로, 입력을 받아 함수 내부에서 활용할 변수

  

#### (1) positional argument

+ 함수를 호출할 때, 위치에 따라 받는 것

+ **가변 인자 리스트(arbitrary argument list)**  ```*arg``` 를 이용하여 개수가 정해지지 않은 argument를 ```tuple```로 **packing** 하여 받을 수 있음

  ```python
  def add(a, b, *args):
  	result = a + b
      for arg in args:
  		result += arg
      return result
  add(1,2,3,4,5)
  >>> 15


+ ```function(*args, a, b)```와 같이 정의되면, ```a, b``` 파라미터들은 호출될 시에 ```a = n, b= m```를 입력해야 함

+ 가변 인자 리스트 ```*args```를 이용한 함수의 예로는 ```print()```가 있음

  

#### (2) keyword argument

+ 함수를 호출할 때, ```keyword```를 이용하는 것

+ **가변 (키워드) 인자(arbitrary keyword arguments)**  ```**kwargs```를 이용하여 개수가 정해지지 않은 키워드 인자를 ```dict```로 **packing** 하여 받을 수 있음

  + 가변 (키워드) 인자 ```**kwargs```는 ```dict``` 형태로 처리가 되고,  ```(keyword = value)```  형태로 입력함

+ ```keyword``` 는 식별자로 쓰이게 되므로, 식별자로 사용할 수 있는 ```type```만 입력 가능 (00.파이썬 기초 참고)

  + ```keyword```로 숫자(식별자와 같은 규칙) 불가 : 이용하려면 ```dict( ((1:2), (100,200)) )```과 같이 이용

  ```python
  def name_score(grade : int, room : int, **kwargs):
      # kwargs의 type이 dict임을 확인
      print(type(kwargs))
      # for문을 이용해 함수 활용
      result = str(grade) + '학년 ' + str(room) + '반 '
      for key, value in kwargs.items():
          result += f"{key}는 {value}점 입니다. "
      return result.rstrip(' ')
  
  name_score(1, 2, 김민수 = 100, 안민수 = 90, 이민수 = 70)
  >>>  <class 'dict'>
       '1학년 2반 김민수는 100점 입니다. 안민수는 90점 입니다. 이민수는 70점 입니다.' 


+ 가변 키워드 인자 ```**kwargs```를 이용한 함수의 예로는 ```dict()```가 있음 [공식문서링크](https://docs.python.org/ko/3.10/library/functions.html)

  ```python
  make_dict = dict(홍시 = '주황 과일', 바나나 = '노란 과일')
  print(make_dict)
  >>> {'홍시': '주황 과일', '바나나': '노란 과일'}




#### (3) 규칙 & 유의사항

+ keyword argument 뒤에 positional argument가 올 수 없음



  + ​	**올바른** 예시 : positional argument / keyword argument 
  
    ```python
    def selfintro(name, fruit = '사과'):
        print(f"{name}는 {fruit}를 좋아합니다.")
    selfintro('김민수','바나나')
    selfintro(name='김민수')
    >>> 김민수는 바나나를 좋아합니다.
        김민수는 사과를 좋아합니다.
    ```
  
  + **틀린** 예시
  
    ```python
    # Example 1
    def selfintro(name, fruit = '사과'):
        print(f"{name}는 {fruit}를 좋아합니다.")
    selfintro(name = '김민수', '파인애플')
    >>>   File "<ipython-input-57-5005437eeb02>", line 1
            selfintro(name = '김민수', '파인애플')
                                      ^
        SyntaxError: positional argument follows keyword argument
    
    # Example 2
    def add(a,b,c):
        return a + b + c
    
    add(a = 1, 2 ,3)
    >>> File "<ipython-input-236-b20fb45d086d>", line 4
        add(a = 1, 2 ,3)
                        ^
        SyntaxError: positional argument follows keyword argument```
    ```
  
    


+  ```*```  & ``` **```  와 다른 파라미터가 같이 정의된 경우, 다른 파라미터는 keyword로 입력해 줘야 함

+ 

+ (수정하기)
  
  ```python
  # 식별자는 숫자만으로는 이루어질 수가 없다는 것에 주의
  # 키워드인자로 넘기면 함수 안에서 식별자(변수이름)로 쓰이기 때문입니다.
  # 즉 키워드인자는 함수 안에서 파라미터의 argument로 쓰
  '''식별자의 이름은 영문 알파벳, 언더스코어, 숫자
  첫글자에 숫자 x
  길이 제한 없고, 대소문자 구별
  red_apple 꼴로 적기로 하자.(CamelCase, snake_case)
  내장함수나 모듈 등의 이름으로도 만들면 안됨'''
  
  
  dict(1=1, 2=2)  # SyntaxError #변수명과 똑같은 규칙으로 작성해야 함
  
  dict(((1,2), (100,200))) # 이거는 가능


+ 

​	



## 5. 함수(변수)의 범위 (scope)

+ **scope**란 해당 객체(변수)가 유효한 범위
+ **global scope** 와 **local scope**로 나뉨

### [1] scope

#### (1) global scope

+ 어디에서든 참조할 수 있는 공간

#### (2) local scope

+ 함수가 만든 scope로 함수 내부에서만 참조가능 함



### [2] variable (변수)

#### (1) global variable

+ global scope에 정의된 변수

#### (2) local variable

+ local scope에 정의된 변수



### [3] 변수의 수명

#### (1) built-in scope

+ 파이썬 실행 후부터 계속 유지

#### (2) global scope

+ 모듈이 호출된 시점 이후 / 인터프리터가 끝날 때까지 유지

#### (3) local scope

+ 함수 호출 시 생성, 함수가 종료될 때까지 유지

+ 함수에서 선언된 변수가 저장되고, 함수 종료될 때까지 유지

  

#### (4) 참고

[python tutor](https://pythontutor.com/visualize.html#mode=edit)에서 참고하기



### [4] 이름 검색 규칙(name resolution)

+ 파이썬에서 사용되는 식별자(이름)들은 namespace(이름공간)에 저장되어 있음

#### (1) 아래의 순서로 이름을 찾아나감 (LEGB rule)

1. Local scope : 함수
2. Enclosed scope : 특정 함수의 상위 함수 (함수 A 내의 또 다른 함수 B 정의 시, B에서 변수 찾을 때 상위 함수 A에서 변수를 찾음)
3. Global scope : 함수 밖의 변수, import 모듈
4. Built-in scope : 파이썬의 내장 함수나 속성

#### (2) global & nonlocal 명령어

+ 이를 이용하면 하위 scope에서 상위 scope의 변수를 수정가능
+ 변수가 처음 선언될 때 앞에 붙여서 사용
+ ```nonlocal```의 경우 local scope 대신 enclosed scope에서 찾게 되는 것 같음

#### (3) ```globals()``` & ```locals()```

+ namespace(global, local, builtin)을 dict로 정리해서 보여줌

+ ```locals()``` : 해당 코드가 실행되어지는 함수 내의 local namespace를 보여줌 (찾아보기)

+ ```globals()``` : global, local, builtin 모두 보여줌

  ```python
  def selfintro(name, fruit = '사과'):
      print(locals())
      
  selfintro('김민수','바나나')
  selfintro(name='이민수')
  >>> {'name': '김민수', 'fruit': '바나나'}
      {'name': '이민수', 'fruit': '사과'}
  ```

  

#### (찾아보기) 함수내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것(클로저* 제외)



## 6. 함수의 문서화 (doc-string)

+ 함수나 클래스를 설명하는 글
+ 함수와 parameter의 이름을 잘 짓는 법
  + 상수의 이름은 영문 전체를 대문자로 
    + ex : ```PI = 3.14```
  + ```list``` 안에 여러 객체 담기면 ```s``` 붙이기
  + 함수의 이름만으로 어떤 역할을 하는 함수인지 파악 가능하도록



## 7. 함수응용 

#### (1) map(function, iterable)

+ ```map(function, iterable)```로 map object를 return 함

+ iterable에 function을 적용

+ object를 return 하는 이유는, iterable의 길이가 길 때, 한 번에 맵 결과를 저장하려면 공간을 많이 차지하여, liked something인 object로 저장하여, 다음 것이 무엇인지 알 수 있도록 저장함

  

#### (2) filter(function, iterable)

+ ```filter(function, iterable)``` 로 filter object를 return 함
+ iterable에 function을 적용하여, 결과가 ```True```인 것들을 filter object로 return
+ 

#### (3) zip(*iterables)

+ 여러개의 iterable을 모아 tuple을 원소로하는 zip object를 return 함

+ 여러개의 iterable을 동시에 순회할 때 이용

  ```python
  # Exampl 1
  a = (1,2)
  b = (100,200)
  for i,j in zip(a,b):
      print(i,j)
  >>> 1 100
      2 200
  ```



#### (4) lambda()

+ 표현식을 계산한 결과를 반환하는 함수

+ return 문을 가질 수 없음

+ 장점

  + 함수 정의하는 것보다 간결
  + ```def```를 사용할 수 없는 곳에서도 사용가능(표현식 내부밖에 없음)

+ ```map()```, ```filter```에 활용가능

  ```python
  list(map(lambda x : x**2, range(5)))
  >>> [0, 1, 4, 9, 16]
  ```

  

#### (5) recursive function (재귀 함수)



