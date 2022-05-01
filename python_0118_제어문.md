[toc]

# 제어문

## 1. input()

+ ```input()```은 ```string type```을 받음

+ 예시

  ```python
  # map 활용
  s = '1 2 3 4 5 6 7' #input()
  list(map(int,s.split()))
  >>> [1, 2, 3, 4, 5, 6, 7]
  
  s = '1, 2, 3, 4, 5, 6, 7' #input()
  list(map(int,s.split(',')))
  >>> [1, 2, 3, 4, 5, 6, 7]
  ```

+ map 함수는 map(function, iterable) 꼴로 iterable에 function을 적용하여 줌

  + ```map(int, s.split())```처럼 객체 자체를 호출 시, 객체의 정보가 출력됨

  + list 와 tuple 등은 객체를 호출했을 때, [1, 2, 3] 과 같이 값이 출력되도록 구현한 것

    ```python
    n = '1 2 3 4'
    a = map(int,n.split())
    print(a)
    >>> <map object at 0x0000018AB49242B0> #map 객체 a의 주소(16진법)
    
    print(id(a))
    >>> 1695246598832 # map 객체 a의 주소(10진법)
    
    id(a) == int('0x0000018AB49242B0',16) # 함수로 16진수를 10진수로 변환
    >>> True
    ```
    
    
    
    

## 2. 반복문

### 1. for

+ 반복 수가 정해져 있음

+ ```dictionary```에 적용시 ```key```를 순회
+  

### 2. while

+ 조건이 ```True```인 경우에 실행

  

### 3. enumerate

+ ```(index, value)```와 같이 튜플로 ```return``` 함

+ 예시

  ```python
  names = ['김','이','박']
  for index, value in enumerate(names):
      print(index, value)
  >>> 0 김
  >>> 1 이
  >>> 2 박
      
  #원하는 index 부터 반환 가능
  for index, value in enumerate(names, start=100):
      print(index, value)
  >>> 100 김
  >>> 101 이
  >>> 102 박
  ```

  

### 4. list comprehension (리스트 표현식 / 지능형 리스트)

+ [ <변수의 표현> for <변수> in \<iterable>]  꼴

```python
# Example 1
[i**2 for i in range(10)]
>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 2 
[[0]*5 for _ in range(5)]
>>>[[0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

# 참고
[ [0]*5 ] *5  # 이렇게 하면 안됨

# Example 3
[num**2 for num in range(10) if num % 2 == 0]
>>> [0, 4, 16, 36, 64]
```



### 5. dictionary comprehension

```python
# Example 1
{idx : val for idx, val in enumerate(['가','나','다'])}
>>> {0: '가', 1: '나', 2: '다'}

# Example 2
{num : num*2 for num in range(5)}
>>> {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
```



### 6. set comprehension





## 3. 반복문 제어

### 1. break

+ 가장 근접한 반복문을 종료함

  ```python
  # Example 1
  for i in range(10):
      if i == 6:
          break
      print(i, end=' ')
  >>> 0 1 2 3 4 5 
  
  # Example 2 : 이중 for 문
  for i in range(3):
      for j in range(10):
          # j == 4가 되면 안쪽 for문을 break
          if j == 4:
              break
          print(j, end=' ')
      print()
  >>> 0 1 2 3 
  	0 1 2 3 
  	0 1 2 3 
  ```

  

### 2. continue

+ 이후의 코드를 실행하지 않고, 반복문으로 돌아감

  ```python
  # Example 1
  for i in range(5):
      # i == 3 인 경우, continue -> for 문으로 직행 / print(i) 실행 x
      if i == 3:
          continue
      print(i, end = ' ')
  >>> 0 1 2 4
  ```

  

### 3. pass

+ 코드블럭이 있어야하는 곳에 자리 채우는 용이고, 아무런 의미가 없음





### 4. for-else

+ for 문을 끝까지 수행 후에 else를 실행하게 됨

+ for 문에서 break가 되면 else를 실행하지 않음

  ```python
  # Example 1 : break가 안되는 경우
  for i in range(3):
      if i == 4:
          print("4가 있습니다.")
          break
  # for에서 break가 되지 않아, else 실행
  else:
      print("4가 없습니다.")
  >>> 4가 없습니다.
  
  # Example 2 : break가 되는 경우
  for i in range(6):
      # break가 되고, for-else 문이 끝남
      if i == 4:
          print("4가 있습니다.")
          break
  else:
      print("4가 없습니다.")
  >>> 4가 있습니다.
  ```

  

## 4. 그 외

+ 

