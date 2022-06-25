[toc]

# 03-02 에러 / 예외처리 (Error / Exception Handling)



## 1. 디버깅







## 2. 에러와 예외

### [1] 문법 에러 (Syntax Error)

+ 문법 에러 발생시 python 프로그램은 실행되지 않음 / ```try except``` 불가능

+ Invalid syntax
+ assign to literal
+ ELO (End of Line)
  + ```'안녕하세``` 
+ EOF (End of File)
  + ```print(```



### [2] 예외 (Exception)

#### (1) 설명

+ 실행 중에 감지되는 에러를 예외 (Exception) 이라고 함
+ 실행 도중 예외 상황이 발생하면, 프로그램 실행 멈춤
  + 문법 에러 없어도 발생
+ 모든 내장 예외는 Exception class 를 상속받아 이루어짐
+ 사용자 정의 예외를 만들 수 있음



#### (2) 예

+ ZeroDivisionError

+ NameError

+ TypeError : type 불일치 / argument 개수 불일치 / argument type 불일치

+ ValueError : type은 올바르지만, 값이 부적절

+ IndexError

+ KeyError

+ ModuleNotFoundError : 존재하지 않는 모듈 import  ```import nflwnaufn!!w```

+ ImportError : 모듈은 존재하지만, 존재하지 않는 요소(클래스/함수) 가져온 경우

  ```from math import ahahahahah```

+ KeyboardInterrupt : 임의로 프로그램 종료시  ```중지누른경우```

+ IndentationError

+ 





## 3. 예외 처리

### [1] ```try / except```

#### (1) 기본 구조

```python
try:
    code block
except 예외 :
    code block
```



#### (2) 순서도

1. 정상 종료

```try -> end```



2. 예외처리 한 경우

```try -> except -> end```



3. 예외처리 못한 경우

``` try -> end -> 오류```



### [2] ```try / except / else / finally```

+ ```finally``` 는 무조건 실행



#### (1) 기본구조

```python
try:       # 코드 실행
   	code block1
except:    # try 에서 예외 발생시 실행
    code block2
else:      # try 에서 예외 발생하지 않으면 실행 
    code block3
finally:   # 예외 발생 여부와 관계없이 항상 실행
    code block4
```



#### (2) 순서도

1. 정상 종료

```try -> else -> finally -> end```



2. 예외처리 한 경우

```try -> except -> finally -> end```



3.  예외처리 못한 경우

``` try -> finally -> end -> 오류메세지```



### [3] ```try / except1 / except2 / else / finally```





### [4] Except / Exception

+ ```except```에 들어가는 예외들은 상/하 구조가 있음 / 그래서 작은 범위의 예외부터 먼저 적어줘야 함

+ ```except (Error1, Error2) : ``` 로 복수의 에러 적어줄 수 있음 / 이 경우 범위 큰 에러가 반환됨

+ ```except Exception : ``` 모든 에러를 처리

+ 에러를 print 가능

  ```python
  try:
      code block1
  except 예외 as e:
      print(e)
  ```





## 4. 예외 발생 시키기

### [1] raise

+ 강제로 예외 발생
+ 실제 프로덕션 코드에서 활용

#### (1) 기본구조

```python
# Example 1
if <표현식> :        # 조건에 따라
    raise SomeError # 에러를 발생
    
# Example 2
if <표현식>:
    raise SomeError("에러와 함께 출력될 말")
    
    
# Example 3
raise SomeError("에러와 함께 출력될 말")
```







### [2] assert

+ ```assert <조건>, <메세지>```

+ 조건이 거짓이면 발생 / 참이면 그냥 넘어감

+ 상태를 검증하는데 사용되고, 무조건 ```AssertionError``` 발생
+ 일반적으로 디버깅(내부적인 코드 / 테스트 코드) 용도

+ ```-O``` 옵션의 경우... (찾아보기)



#### (1) 기본구조

```python
# Example 1
assert <조건>, <메세지>

assert len([1, 2]) == 1, '길이가 1이 아닙니다'
>>> AssertionError: 길이가 1이 아닙니다

# Example 2
assert len([1]) == 1, '길이가 1이 아닙니다'
print("assert 그냥 넘어감")
>>> assert 그냥 넘어감
```

