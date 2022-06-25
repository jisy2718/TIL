[toc]

# 파이썬 기초

## 1. 변수

### [1] 할당

``` python
# 같은 값을 동시에 할당
x = y = 1

# 다른 값을 동시에 할당 (튜플 대입)
x , y = 1, 2 #이 때 1, 2 는 (1, 2)로 묵시적으로 튜플로 형변환(Typecasting) 됨


```

### [2] 식별자(예약어) (identifier)

+ python의 객체(변수, 상수, 함수, 모듈, 클래스 등)의 이름

+ python에서 사용할 수 없는 식별자

  ```python
  False, None, True, and, break, class, continue, def, del, elif, else, finally, for, from, if, import in, is, lambda, not, or, return, try, while
  as, assert, async, await, except, global, nonlocal, pass, raise, with, yield 
  ```



+ keword list 보는 방법

  ```python
  import keyword
  keyword.kwlist
  ```



+ 사용하면 안되는 식별자를 할당한 경우 초기화 하는 방법

  ```python
  # sol 1 : 해당 식별자만 초기화 : del
  max = min
  print( max(1,2) )
  >>> 1  # max function이 min function이 됨
  del max 
  print( max(1,2) )
  >>> 2
  
  # sol 2 : 할당된 모든 변수들 초기화 : %reset
  %reset
  >>> Once deleted, variables cannot be recovered. Proceed (y/[n])? #y 입력하면 초기화
  
  ```

  [내장함수문서](https://docs.python.org/3.9/library/functions.html) 를 참고

  





## 2. 자료형

### 1. None

### 2. Boolean

```python
# 다음은 모두 False로 반환
0, 0.0, (), [], {}, '', "", None
bool(0)
>>> False

# 그 외의 것은 모두 True로 반환
bool(그 외 아무 것)
>>> True
```



### [3] Integer (Numeric)

+ Python 3부터 long type 없고, 모두 integer type 임

+ 임의 정밀도 산술(arbitrary precision arithmetic)을 통해, 고정된 형태의 메모리가 아닌 가용 메모리들을 활용하여 모든 수를 표현하는 것에 사용하여, 오버플로우가 발생하지 않음

  ```python
  # 표기할 수 있는 최대값 찾기
  import sys
  sys.maxsize
  >>> 9223372036854775807
  ```

  

+ 진수표현

  ```python
  #2진수 ,8진수, 16진수, 10진수
  0b10; 0o10; 0x10; 10
  
  #16진수의 10, 11, 12, 13, 14, 15
  0xa; 0xb; 0xc; 0xd; 0xe; 0xf
  ```

  

### [4] Float (Numeric)

+ 정수가 아닌 실수는 모두 Float type 임

+ 0 과 1로 정수를 표현하기는 쉽지만, 소수를 표현하기는 어려움 &rarr;  Rounding error 고려

  ```python
  0.54 - 0.32
  >>> 0.22000000000000003
  ```

  위와 같이 정확한 계산이 되지 않음. 그 이유는 2진법의 경우 0.1, 0.01, ... 0.0000001 모두 끝이 5로 끝나서 정확한 소수 값을 표현할 수 없음

#### (1) math.isclose()

+ Rounding error를 고려하여 두 수의 크기를 비교하는 방법

  ```python
  # method 1
  abs(0.54 - 0.32) <= 1e-10
  
  # method 2
  import sys
  abs(0.54 - 0.32) <= sys.float_info.epsilon
  
  # method 3
  import math
  math.isclose(0.54, 0.32)
  ```

  

### [5] Complex (Numeric)

+ 3+5j 와 같이 j를 이용하여 허수부 표현

+ 기본적인 함수들

  ```python
  # complex function
  2 + 3j == complex(2, 3)
  >>> True
  
  # real, imag
  a = 2 + 3j
  print(a.real, a.imag)
  >>> 2.0 3.0
  
  # size (크기)
  abs(a)
  >>> 3.605551275463989
  
  # conjugate (켤레복소수)
  a.conjugate()
  >>> (2-3j)
  ```

  

### [6] String

+ 모든 문자는 string type 임

+ 문자열 작성 시 ```''```  or ```""``` 중 하나로 일관되게 이용하기

+ 문자열은 immutable(수정불가) 하고 iterable(반복가능) 함

  ```python
  a = "Hello World!"
  
  #immutable
  a[-1] = ~ #불가능함
  
  #iterable
  for char in a:
      print(char, end = ' ')
  >>> H e l l o   W o r l d !
  ```

  

+ 기본적인 예시코드

  ```python
  a = "Hello World!"
  
  # 문자열 뒤집기
  a[::-1]  #이는 a[-1:-(len(a)+1):-1]과 같음
  >>> '!dlroW olleH'
  
  # 문자열 복사 / a[:] 과 a[::] 은 같음
  a[:] is a[::]
  >>> True
  ```



* 다중 따옴표 (중첩, 삼중) (nested quotes)

  * ```"a'bcd'e "``` 는 ```"a\'bcd\'e"``` 와 같음,  즉 내부의 따옴표는 문자처리 됨
  
  ```python
  # 중첩
  print("안녕하세요. 그는 속으로 생각했다. '행복합니다.'")
  >>> 안녕하세요. 그는 속으로 생각했다. '행복합니다.'
  
  print('안녕하세요. 그는 속으로 생각했다. "행복합니다."')
  >>> 안녕하세요. 그는 속으로 생각했다. "행복합니다."
  
  # 삼중
  print("""삼중 따옴표는 자동으로
  줄바꿈을 해준다.
  무척 편리하지?""")
  >>> 삼중 따옴표는 자동으로
  줄바꿈을 해준다.
  무척 편리하지?
  
  print('''삼중 따옴표 안에 "이렇게도 할 수 있고", '이렇게도 할 수 있다?'
  그리고 마지막에 ''를 써야한다면 '이렇게 할 수 있다?\'''')
  >>> 삼중 따옴표 안에 "이렇게도 할 수 있고", '이렇게도 할 수 있다?'
  그리고 마지막에 ''를 써야한다면 '이렇게 할 수 있다?'
  
  print(''''처음에 이렇게' 쓰는 거는 괜찮다? ''')
  >>> '처음에 이렇게' 쓰는 거는 괜찮다? 
  ```
  
  

+ Escape sequence

  | 명령어          | 설명 | 예시 |
  | --------------- | ---- | ---- |
  | \n              |      |      |
  | \t              |      |      |
  | \r (캐리지리턴) |      |      |
  | \0              |      |      |
  | \\'             |      |      |
  | \\''            |      |      |
  | \b              |      |      |
  |                 |      |      |
  |                 |      |      |

  ```python
  # 참고 : raw string
  print(r'Escape sequence \n 를 무시하고 \\ 싶어요')
  >>> Escape sequence \n 를 \t 무시하고 \\ 싶어요
  ```

  

+ String interpolation

  [공식문서](https://docs.python.org/ko/3/tutorial/inputoutput.html)
  
  ```%-formatting```
  
  * ```%s``` : string type
  
  * ```%d``` : int type
    
  * ```%f``` : float type
    
  * ```%.2f``` : 소수점 2자리까지
  
  
  ```python
  name, age, height = "J", 21, 178.352 
  
  # method 1
  print("안녕? 내 이름은 %s이고, 나이는 %d이고, 키는 %.2f 야."%(name, age, height))
  >>> 안녕? 내 이름은 J이고, 나이는 21이고, 키는 178.35 야.
  
  # method 2
  print("안녕? 내 이름은 {0}이고, 나이는 {1}이고, 키는 {2:.2f} 야.".format(name, age, height))
  >>> 안녕? 내 이름은 J이고, 나이는 21이고, 키는 178.35 야.
  
  # method 3 (python3.6+)
  print(f"안녕? 내 이름은 {name}이고, 나이는 {age}이고, 키는 {height:.2f} 야.")
  >>> 안녕? 내 이름은 J이고, 나이는 21이고, 키는 178.35 야.
  
  # 자리수 표현
  print(f"안녕? 내 이름은 {name}이고, 나이는 {age:10d}이고, 키는 {height:10.2f} 야.")
  >>> 안녕? 내 이름은 J이고, 나이는         21이고, 키는     178.35 야.
  ```

+ 좌, 우측 정렬

  + ```>int``` int만큼의 공간을 확보하고, 우측정렬
  + ```<int``` int만큼의 공간을 확보하고, 좌측정렬

  ```python
  print("안녕 {0:<10}ㅎㅎ".format('천재'))
  print("안녕 {0:>10}ㅎㅎ".format('천재'))
  >>> 안녕 천재        ㅎㅎ
      안녕         천재ㅎㅎ
  ```

  



* string format

  ```python
  import datetime
  now = datetime.....지금쓰는 거
  ```

  



## 3. 컨테이너

### [0] 요약

| 컨테이너   | sequence<br />(ordered/index 접근 o) | iterable | immutable | 연산              | method      |
| ---------- | ------------------------------------ | -------- | --------- | ----------------- | ----------- |
| list       | o                                    | o        | x         | ```+, *```        | append()    |
| tuple      | o                                    | o        | o         | ```+, *```        |             |
| range      | o                                    | o        | o         | ?                 |             |
| string     | o                                    | o        | o         | ```+, *```        | string 반환 |
| binary     | o                                    | ?        | ?         |                   |             |
| set        | x                                    | o        | x         | ``` -, |, &, ^``` | add()       |
| dictionary | x                                    | o        | x         |                   |             |



### [1] list





### [2] tuple

+ 생성 후에 객체 변경이 불가(immutable)하고 순서가 있음(sequence/ordered/index 접근 가능)

+ 튜플 대입

  ```python
  # 우변의 값을 좌변의 변수에 한 번에 할당하는 과정
  a, b = 0, 1  #우선 0, 1 => (0, 1)로 만든 후, a와 b에 unpacking
  print(a, b)
  >>> 0 1
  ```

  

+ packing / unpacking

  + packing : 여러 값들을 하나의 객체인 튜플로 만들어서, 변수에 할당
  
  + unpacking : packing 된 것을 풀고, 각 원소에 하나의 변수를 대응시키는 것
  
    ```python
    a, *b = 1, 2, 3, 4, 5 #packing : 남는 변수 모두 b에 list로 만들어서 할당
    print(a)
    print(b)
    print(*b) #unpacking
    >>> 1
    >>> [2, 3, 4]
    >>> 2 3 4
    ```
  
    ```python
    # unpacking : argument 가 *로 시작하는 경우
    def sum_str(x,y,z):
        return(str(x)+str(y)+str(z))
    
    a = [1,4,'d']
    sum_str(*a)
    >>> '14d'
    ```
  
  
  

### [3] range

+ 생성 후에 객체 변경이 불가(immutable)하고 순서가 있음(sequence o / ordered o /index 접근 o)

  

### [4] set

+ 생성 후에 담고 있는 객체 변경이 가능(mutable)하고 순서가 없음(sequence x /ordered x / index 접근 x)
+ 객체는 hashable type(immutable)만 가능
+ ``` -, +, |, ^ ``` 연산자 가능
+ 





### [5] dictionary

+ ```key```는 hashable type(immutable)만 가능하고, 중복 불가

  + ```dict.keys()``` : a set like object

  + ```key``` 중복 시, 마지막에 입력된 key의 value가 저장됨

    ```python
    my_dict = {1 : 'a', 1  : 'b'}
    print(my_dict[1])
    >>> b
    ```

+ ``` dict.items(), dict.keys(), dict.values() ```

+ ```dict.get(key)``` : dict에서 key에 해당하는 value를 return, 만약 key가 없다면 ```None``` return

+ ordered dictionary

  + key를 입력한 순서가 보존됨

  ```python
  from collections import OrderedDict
  ordered_dic = OrderedDict()
  ordered_dic['A'] = 1
  ordered_dic['가'] = 2
  ordered_dic['C'] = 3
  print(ordered_dic)
  >>> OrderedDict([('A', 1), ('가', 2), ('C', 3)])
  ```

  



## 4. 형 변환 (Typecasting)

### [1] 묵시적(암시적, implicit) 형 변환

+ 파이썬 내부에서 자동적으로 자료형을 변환

+ 데이터의 손실이 발생하지 않는 경우에 발생 (확대 변환)

  ```python
  # Example 1
  a = 1
  b = True
  print(1+True) # 묵시적 변환 : True -> 1
  print("-"*20)
  
  # Example 2
  a = 1
  if a: # 묵시적 변환 : 1 -> True 
      print("hello")
      print("-"*20)
  
  # Example 3 
  a = 1
  b = 1.1
  print(type(a), type(b)) # 프로그래밍 언어에서는 같은 타입만 연산이 가능함
  print( a + b ) # 묵시적 변환 : 1  -> 1.0 (int -> float)
  
  >>> 2
  >>> --------------------
  >>> hello
  >>> --------------------
  >>> <class 'int'> <class 'float'>
  >>> 2.1
  ```

  

### [2] 명시적(Expleicit) 형 변환

+ 사용자가 특정 함수를 이용해 자료형을 변환



#### (1) 자료형의 변환

+ ``` str(), int(), float(), complex() ```를 이용한다.

  + 불가능 예

    ```python
    int('3.5') + 3
    >>> ---------------------------------------------------------------------------
    >>> ValueError                                Traceback (most recent call last)
    >>> <ipython-input-58-b1f090ae38a3> in <module>
    >>> ----> 1 int('3.5') + 3
    >>> 
    >>> ValueError: invalid literal for int() with base 10: '3.5'
    ```

+ 진수의 변환

  ```python
  # 1 : 16 / 8 / 2 진수를 10진수로 변환
  int('0x11',16)  #16진수 0x123을 10진수로 변환
  >>> 17
  
  # 2 :10진수를 16 / 8 / 2 진수로 변환
  "{0: x}".format(11) #10진수 11을 16진수로 변환
  >>> 'b'
  ```

  

  + ```int('0x123',16)```  과 같이 16진수를 10진수로 변환가능
  + ```"{0: x}".format(10)``` 

  ​	

#### (2) 컨테이너의 변환

+ ```string, list, tuple, range, set, dictionary```에 대하여 가능
+ 결과가 ```range, dictionary```로는 바꿀 수 없음
+ ``` str(), list(), tuple(), set()```으로 가능
+ ``` list(dictionary), tuple(dictionary), set(dictionary)```는 ```key``` 값만을 이용





## 5. 연산자

+ ``` q,r = divmod(10,3)```
+ ```**(1/2)``` 로 제곱근(root) or 거듭제곱 표현 가능

### 1. 비교 연산자

+ ``` is, is not ```

+ ``` ==, !=```

  

### 2. 논리 연산자

+ ``` and, or, not ```

+ 단축 평가

  + ``` A and B```와 같은 상황에서 첫 값에 의해 명확히 값 정의되면, 뒤에는 읽지 않음

    + ```and```  : ``` A```가 참이면 ``` B```를 return,  ``` A```가 거짓이면 ``` A```를 return

      ```python
      print('a' and 'z')
      print('z' and 'a')
      print([] and '2')
      >>> z
      >>> a
      >>> []
      
      print( ('a' and 'z' ) in 'abcdefg' )
      print( ('z' and 'a' ) in 'abcdefg' )
      
      >>> False
      >>> True
      ```
    
      
    
    + ```or``` : ```A```가 참이면 ```A```를 return, ```A```가 거짓이면 ```B```를 return
    
      ```python
      print(5 or 3)
      print(3 or 0)
      print(0 or 3)
      print(0 or [])
      print(4 and ([] or 1))
      
      >>> 5
      >>> 3
      >>> 3
      >>> []
      >>> 1
      ```
    
      



### 3. 복합 연산자

| 연산자  | 의미       |
| ------- | ---------- |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |
| a **= b | a = a ** b |



### 4. 멤버십 연산자 (Membership Operator)

+ 요소가 ```string, list, tuple, range, set, dictionary(key)``` 에 있는지 파악
+ ```in, not in```을 이용



### 5. 식별 연산자 (Identity Operator)

+ 동일한 객체인지 파악함

+ ```is, is not```를 이용 / ```None``` 인지 여부를 판별할 때 많이 이용

+ ```id()```와 ```is```의 관계
  + ```id()``` function은 각 객체의 고유한 식별자 / ```is```는 식별자가 같은지 파악

+ ```id()```

  ```python
  a = map(int,input().split()) # input is 1 2 3 4
  print(a)
  >>> 객체의 10진수 주소 출력
  
  a
  >>> (interpreter 상에서만) <해당 object at 16진수 주소>
  ```

  


### 6. Slicing

+ 일부분 슬라이싱

  ```python
  [0,1,2,3,4,5][1:4]
  (0,1,2,3,4,5)[:4]
  range(100)[8:11]
  
  >>> [1, 2, 3]
  >>> (0, 1, 2, 3)
  >>> range(8, 11)
  ```

  

+ 시퀀스의 k 간격 슬라이싱

  ```python
  print([0,1,2,3,4,5][1:4:2])
  print((0,1,2,3,4,5)[:4:2])
  print(range(100)[8:11:2])
  print('0123456789'[1:9:2])
  
  >>> [1, 3]
  >>> (0, 2)
  >>> range(8, 11, 2)
  >>> 1357
  ```

  

+ 역순으로 변환

  ```python
  a = 'abcde'
  a[::-1]  #[::-1] == [-1 : -(len(a)+1) :-1]
  >>> 'edcba'
  
  a = [1,2,3,4,5]
  a[::-1]
  >>> [5, 4, 3, 2, 1]
  
  a = (1,2,3,4)
  a[::-1]
  >>> (4, 3, 2, 1)
  
  a = range(10)
  a[::-1]
  >>> range(9, -1, -1)
  ```

  





## 6. 파이썬 프로그램 구성 단위(수정 필요)

+ 식별자 (identifier) : 이름, 예약어

​			&darr; 

+ 리터럴 (literal) : 읽혀지는 값 자체

​			&darr;

+ 표현식 (expression) : 

​			&darr; 

+ 문장 (statement) 

​			&darr; 

+ 함수(function)

​			&darr; 

+ 모듈 (Module) 

​			&darr; 

+ 패키지 (package) 

​			&darr; 

+ 라이브러리 (library)



