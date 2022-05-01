[toc]

# OOP

## 1. OOP (객체지향 프로그래밍)

+ 파이썬은 모든 것이 객체(object)

  + 파이썬이 동적타이핑 언어라 조금 더 주의를 기울여야

  

+ 객체는 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것

  + 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미
  + 변수, 자료구조, 함수, 메서드가 될 수 있음



+ 객체지향 프로그래밍은 컴퓨터 프로그래밍의 패러다임 중 하나

  + 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나, 여러 개의 독립된 단위인 객체들의 모임으로 봄

  + 각각의 객체는 메세지를 주고받고, 데이터를 처리할 수 있음

    

+ 객체는 특정 타입의 인스턴스(instance : 사례) 임
  + ```5, 10``` 은 ```int```의 instance





+ 객체(object) = 속성(attribute) + 기능(method)
  + 타입(type) : 어떤 연산자(operator)와 조작(method) 이 가능한가?
  + 속성(attribute) : 어떤 상태(데이터)를 가지는가?
  + 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

---

+ 객체지향 프로그래밍이란?

  + 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그램 방법
  + 객체를 내부적으로 바꿀 수 있음 ( 데이터 자체를 바꿀 수 있음 )
  + 데이터와 기능(메소드) 분리, 추상화된 구조(인터페이스)

  
  
+ 절차지향 프로그래밍이란

  + 조건문, 반복문, 함수들로 이루어진 코드 형식
  + 데이터를 바꾸려면 함수의 output을 계속 저장해서 사용해야 함



+ 절차지향과 객체지향의 차이

  ```python
  # 절차 지향
  a = [1, 2, 3]
  
  a = sorted(a)
  
  a = reversed(a)
  
  def append(l, value):
      return l + [value]
  a = append(a, 4)
  
  # 객체 지향 : 주어 + 동사 느낌
  a = [1, 2, 3]
  a.sort()
  a.reverse()
  a.append(4)
  ```

  ---



+ 객체지향 프로그래밍이 필요한 이유
  + 현실 세계를 프로그램 설계에 반영 (추상화) 한, method, attribute를 쉽게 이용 가능
  
  + 절차 지향에서는 attrribute에 접근하려면, 직접 구체적으로 입력하여 접근해야 하고, method를 이용하려면 함수를 정의해서 input, output을 계속 변수에 저장해 주어야 함.
  
    ```python
    # 절차 지향
    person1 = {'name' : 'J', 'age' : 20}
    #=> name에 접근하기 위해서는 person1['name']으로 구체적으로 입력하여 접근해야 함
    
    # 객체 지향
    person1.name #과 같이 접근 가능
    person1.greeting() # 내부에 정의된 method로 인사하는 함수 실행
    ```
  
  + 소프트웨어의 개발과 보수를 간편하게하고, 보다 직관적인 코드 분석을 가능하게 함
  
    ```python
    l = ['a', 'b', 'c']
    
    l.count('a') # 주어 + 동사 관계로 직관적으로 무엇을 하는 것인지 알 수 있음
    
    # 위 처럼 안하면, 루프로 구해야 함
    ```
  
    





### [1] OOP 기초

#### (1) 기본문법

+ 클래스 정의 

  ```python
  class Myclass:
      pass
  ```

+ 인스턴스 생성 : ```instance = Myclass()```

+ method 호출 : ```instance.method()```
+ 속성 (attribute) :  ```instance.attribute```



#### (2) 클래스 / 인스턴스 / 속성 / method

+ 객체의 틀 (클래스)을 가지고, 객체 (인스턴스)를 생성함
  + 파이썬은 모든 것이 객체이고, 모든 객체는 특정 타입의 인스턴스
+ 클래스 : 객체들의 분류
+ 인스턴스 : 하나하나의 실체 / 예
+ 속성 (attribute) : 특정 데이터 타입과 클래스의 객체들이 가지게 될 상태 (데이터, 정보)

+ method : 특정 데이터 타입과 클래스의 객체에 공통적으로 적용가능한 함수 (행동)



#### (3) 객체 비교

+ ```==```
  + 변수가 참조하는 객체가 내용이 같은 경우 ```True```
  + 동일 대상 가리킨다는 보장 없음
+ ```is```
  + 두 변수가 동일한 객체를 가리키는 경우 ```True```
  + 동일한 (identical)





### [2] 인스턴스

#### (1) 인스턴스 변수(attribute)

+ 인스턴스가 가지고 있는 속성 (attribute)
+ 생성자 method 에서 ```self.attribute```로 정의



#### (2) 인스턴스 method

+ 인스턴스 변수를 사용 or 인스턴스 변수에 값을 설정하는 method

+ 호출 시, **첫번째 인자로 인스턴스 자기자신(self)이 전달**됨

  + 그 이유는 method 호출 시, 해당 인스턴스가 가지고 있는 값들을 조작해야 하는데, 이를 위해서는 method의 인자로 인스턴스를 넘겨줘야하기 때문에, 이를 자동으로 해줌

  

#### (3) self

+ 인스턴스 자기 자신을 의미

+ Instance method / Instance attribute 는 호출 시, 첫번째 인자로 Instance 자기 자신이 전달되도록 설계

  ```python
  class Person:
      
      def check(self):
          return self
  
  p1 = Person()
  p1.test() # (1)과
  Person.check(p1) # (2)는 같음
  # (1)이 내부적으로는 (2)와 같이 실행됨
  ```



#### (4) constructor (생성자) method

+ ```__init__(self)```
  + Instance 객체가 생성될 때, 자동으로 호출되는 method
  + Instance 변수들의 초깃값을 설정

#### (5) destructor (소멸자) method

+ ```__del__(self)```
  + Instance 객체가 소멸되기 직전에 호출되는 method (```del instance``` 경우 호출됨)



#### (6) other magic method ( [공식문서](https://docs.python.org/3/reference/datamodel.html#special-method-names) )

+ Double underscore(```__```) 가 있는 method
+ 특정 상황에 자동으로 불러지는 method 



+ ```__str__(self)``` : Instance ```print()```(출력) 시 ```__str__(self)``` 의 반환값이 출력
  + ```pinrt()``` 호출 시 자동으로 호출됨
+ ```__len__(self)``` : ```len()```호출 시 반환되는 값 설정 (확인 필요)
+ ```__repr__(self)``` : 
+ ```__lt(le)__(self, other)```  : less than(eqaul) ```instance1 >(>=) instance2```
+ ```__gt(ge)__(self, other)```
+ ```__eq(ne)__(self, other)```



+ ```__lt__(self)``` or ```__gt__(self)``` 중 하나 정의하면 나머지 하나가 정의되지는 않지만, 부등호 연산값은 반대로 나오는 듯? (확인 필요)

  

### [3] 클래스

#### (1) 클래스 변수 (attribute)

+ 한 클래스의 모든 인스턴스가 같은 값을 가지고 있는 속성

  ```python
  # Example 1
  class Person:
      species = 'human' # class variable
  ```



#### (2) 클래스 method

+ ```@classmethod``` 데코레이터를 이용하여 정의한, 클래스가 사용하는 method

+ 클래스 자체와 클래스의 속성 (attribute)에 접근할 필요 있는 경우 이용

+ 호출 시, **첫번째 인자로 클래스(cls)**가 전달

  ```python
  # Example 1
  class Person:
      species = 'human' # class variable
      
      @classmethod
      def class_method(cls, *arg):
          pass
      
  ```

  

#### (3) static(정적,스태틱) method

+ ```@staticmethod``` 데코레이터를 이용하여 정의한, 클래스가 사용하는 method

+ 클래스와 클래스 속성 (attribute)에 접근할 필요 없는 경우 이용

+ 호출 시, **어떠한 인자도 전달되지 않음** (클래스 정보에 접근/수정 불가) /  전달 받은 argument만 활용

  ```python
  # Example 1
  import math
  math.pi
  >>> 3.141592653589793
  
  # Example 2
  class Person:
      species = 'human' # class variable
      
      @staticmethod
      def static_method(*arg):
          pass
  ```

  



### [4] method (메서드) 정리

+ 인스턴스는 3가지 method에 접근 가능하지만 instance method에만 접근하기
+ 클래스는 class method와 static method에 접근가능하고, 이 둘에만 접근하기

#### (1) Instance methods

#### (2) Class methods

#### (3) Static methods

```python
# Example
class Person:
    species = 'human' # class variable
    
    #instance method
    def instance_method(self, *arg):
        return self
    
    @classmethod
    def class_method(cls, *arg):
        return cls
    
    @staticmethod
    def static_method(*arg):
        return 3.14

# 1. instance_method는 자기 자신을 첫 인자로 넘김
p1 = Person()
p2 = p1.instance_method()
print(p1 is p2)
>>> True

# 2. class 와 instance는 다른 것
c1 = Person.class_method()
print(p1) # instance
print(c1) # class
>>> <__main__.Person object at 0x000001F026459730>
    <class '__main__.Person'>
    
# 3. class_method는 자기 자신을 첫 인자로 넘김
print( c1 is Person )
>>> True

# 4. 아래는 p3 = Person() 과 같은 것
p3 = c1() 

# 5. static_method & namespace
print(p3.species)  # 원래는 클래스 변수가 들어가 있음
>>> 'human'

p3.species = 'animal'  # 인스턴스 변수로 들어가게 됨
print(p3.speceis)      # 인스턴스 변수에서 species를 먼저 찾음
>>> 'animal'
```



### [5] namespace

+ 인스턴스 &rarr; 클래스 순으로 탐색

  











## 2. 객체지향의 핵심개념

### [1]추상화

+ 세부적인 내용은 감추고 필수적인 부분만 표현하는 것 

+ 여러 클래스가 공통적으로 사용할 속성 및 method를 추출하여, 기본 클래스로 작성하여 활용

  

### [2] 상속

+ 부모 클래스의 모든 속성이 자식 클래스에게 상속될 수 있음
+ 코드 재사용성이 높아짐



#### (1) super()

+ super() 자체가 부모클래스를 의미????(찾아보기)



### [3] 다형성

+ 동일한 method가 class에 따라 다르게 행동

+ method overriding 을 이용

  + method overriding : 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것

  + ```__init__``` 도 method overriding 하는 것임

    

### [4] 캡슐화

+ 객체의 일부 구현 내용에 대해, 외부로부터의 직접적인 엑세스를 차단하는 것

  + 이를 통해, 내부적 동작의 신뢰성을 확보할 수 있음

+ 파이썬은 캡슐화가 암묵적으로 존재하지만, 언어적으로 존재하지 않아, 실제로 접근을 막지는 못함

+ 접근제어자의 종류
  + Public Access Modifier

  + Protected Access Modifier

  + Private Access Modifier

    

#### (1) Public member

+ 언더바 없이 시작하는 메서드와 속성들
+ 어느 곳에서든 호출 가능
+ 하위 클래스에서 method overriding 허용



#### (2) Protected mamber

+ 언더바 1개 ```_```로 시작하는 메서드와 속성들

+ 암묵적으로 부모 클래스 내부와 자식 클래스에서만 호출 가능

  + 실제로는 외부 호출 가능 : ```instance._MethodOrAttribute()``` 가능

  + ```getter, setter``` 를 이용하여 호출하고 변경하는 것을 권장

    

+ 하위 클래스에서 method overriding 허용



#### (3) Private member

+ 언더바 2개 ```__``` 로 시작하는 메서드와 속성들

+ 본 클래스의 내부에서만 사용 가능

+ 하위 클래스 상속 및 외부 호출이 불가

  + ```getter, setter``` 를 이용하여 호출하고 변경해야 함

  + ```.__MethodOrAttribute() = 10``` 과 같이 하면, 해당 변수가 생기는 것이지 기존의 것이 변경되는 것 아님

    ```python
    class Person:
        
        def __init__(self, name, age):
            self.name = name
            self.__age = age
        
        def get_age(self): 
            return self.__age
        
    p1 = Person('나', 30)
    print(p1.get_age())
    p1.__age = 10
    print(p1.get_age())
    print(p1.__age)
    >>> 30
        30
        10
    ```



#### (4) ```getter``` & ```setter```

+ ```getter``` :  변수의 값을 읽는 method (외부에서 내부 데이터를 가져올 때 이용)
  + ```@property``` 데코레이터를 이용

+ ```setter``` : 변수의 값을 설정하는 method (외부에서 내부 데이터를 설정할 때 이용)

  + ```@변수.setter``` 를 이용

  ```python
  class Person:
      
      def __init__(self, age):
          self._age = age 
          
      @property
      def age(self):
          return self._age
      
      @age.setter
      def age(self, new_age):
          if new_age <= 30:
              raise ValueError('Too Young to sleep')
              return
          
          self._age = new_age
          
  p1 = Person(40)
  print(p1._age)
  p1.age = 50
  print(p1.age)
  >>> 40
      50
  ```



#### (5) 다중상속

+ 두개 이상의 클래스를 상속 받는 경우

  + 상속 받은 모든 클래스의 요소 이용 가능

  + 중복된 속성과 method는 상속 순서에 의해 결정

    ```python
    class Person:
        pass
    
    class Dad(Person):
        pass
    
    class Mom(Person):
        pass
    
    class baby(Dad, Mom):
        pass
    ```

    baby 기준으로 Dad와 Mom에 중복되는 속성이나 method 있는 경우, Dad와 똑같이 해당 속성이나 method가 실행.

    

+ 상속관계에서의 이름 공간과 MRO (Method Resolution Order)

  + 인스턴스 &rarr; 자식 클래스 &rarr; 부모 클래스 순으로 찾아봄
  + ```ClassName.__mro__``` or ```ClassName.mro()```

  
  
  
  
  
