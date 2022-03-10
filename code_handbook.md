# 자주 다시 검색하여 찾게되는 코드들

# 1. Python

+ ```isinstance```

  ```python
  1test = {1:3}
  isinstance(test, dict)
  >>> True
  ```

+ ```isdecimal()```

  ```isdigit()```

  ```isnumeric()```

  

  출처: https://it-neicebee.tistory.com/33 [IT's Portfolio]

+ ```id()``` 함수의 경우 인자로 받은 객체의 메모리에서의 고유 주소를 return 함



+ ```locals()``` : 해당 코드가 실행되어지는 함수 내의 local namespace를 보여줌 (찾아보기)
+ ```globals()``` : global, local, builtin 모두 보여줌

+ ```dir(library)``` 하면 해당 library의 객체들 볼 수 있음
+ ```dir(__builtins__)``` 로 built in function 목록 볼 수 있음

+ keword list 보는 방법

  ```python
  import keyword
  keyword.kwlist
  ```

​		식별자로 사용하면 안되는 keyword를 보여줌





+ ```%timeit```의 활용

  ```python
  def function():
      pass
  %timeit function
  %timeit -n 100 -r 1000 function #각 100번도는 루프를 1000번 실행시킴
  ```



+ 변수명 초기화

  ```python
  # 1 하나 삭제
  del object_name
  
  # 2 전체 namespace가 초기화?
  %reset 
  
  # 3 code(스크립트) 실행 전에 메모리위 모든 변수를 지우기
  from IPython import get_ipython
  get_ipython().magic('reset -sf')
  #my code
  ```

  

+ 예쁘게 출력하기

  ```python
   from pprint import pprint
   pprint("예브게 출력됩니다.")
  ```




+ ```round, math.ceil, math.floor, trunc```

  ```python
  # round(float, 소수점 자리수)는 반올림
  round(3.2252,2)
  >>> 3.23
  
  # math.ceil(x) : 올림 : x 이상의 최소 정수
  math.ceil(3.2223)
  >>> 4
  
  # math.floor(x) : 내림 : x 이하의 최대 정수
  math.floor(3.2223)
  >>> 3
  
  # math.trunc(x) : Truncates the Real x to the nearest Integral toward 0
  math.trunc(-0.3)
  >>> 0
  
  math.trunc(0.2)
  >>> 0
  ```

  

+ ```random``` package 관련 [공식문서](https://docs.python.org/3/library/random.html)
  
  
  + 복원추출
  
  
      + ```random.choices(population, weights=None, *, cum_weights=None, k=1)```
      
        : Return a *k* sized list of elements chosen from the *population* with replacement. If the *population* is empty, raises [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError).
  
  
  
  
  
  
  + 비복원추출
  
    + ```random.sample(population, k, *, counts=None)```
  
      : Return a *k* length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement.
  
    ​		             If the sample size is larger than the population size, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) is raised.
  
    
  
  + 셔플
  
    + ```random.shuffle(x[, random])```
  
      : Shuffle the sequence *x* in place.
  
      To shuffle an immutable sequence and return a new shuffled list, use `sample(x, k=len(x))` instead.
  
    



+ ```dictionary```의 정렬

  + ```sorted(iterable, key=function, reverse = T/F)``` 을 이용 &rarr; ```list```로 반환

    ```python
    target = {'가':100, '라': 29, '다':30, '나':31}
    
    # case 1) key 값 기준으로 정렬
    sorted(target.items(), key = lambda item : item[0])
    >>> [('라', 29), ('다', 30), ('나', 31), ('가', 100)]
    
    # case 2) value 값 기준으로 정렬
    sorted(target.items(), key = lambda item : item[1])
    >>> [('가', 100), ('나', 31), ('다', 30), ('라', 29)]
    ```

    









# 2. 파이썬 알고리즘

## 1. input 관련

```python
import sys
# 아래 대신에
N = int(input())
# 이를 써도 됨
N = int(sys.stdin.readline())
```











# 3. git bash

* ```pip install --upgrade pip```

+ ```pip list``` : 저장된 library 보여줌





# 4. pytesseract (python)

+ 이미지 OCR 프로그램

+ 기본적인 사용법 ([github](https://github.com/madmaze/pytesseract))

  1. 우선 tesseract를 다운받은 후 ( 한국어 이용하고 싶으면, 설치 중 한국어도 추가로 설치해야 함)
  2. 시스템 환경 변수 편집 &rarr; 고급 &rarr; 환경변수 &rarr; Path에 ```C:\Program Files\Tesseract-OCR``` (설치경로) 추가
  3. ```pip install pytesseract```
  4. 아래와 같이 설정 후 사용

  ```python
  import pytesseract
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
  ```

  5. 사용

  ```python
  # lang 설정안하면 english / lang = 'eng'로도 가능
  print(pytesseract.image_to_string('저장위치/0127hw_num2.png', lang = 'kor'))
  ```

  





# 5. vscode

vscode extention : indent-rainbow(파이썬 들여쓰기 가동성 엄청 높아짐)

vscode extention : live Server(웹페이지 새로고침 안해도 vs코드에서 코드 변경될 때마다 웹페이지 갱신됨 웹할때 편함)

꿀팁 ctrl + shift + alt + L을 누르면 한번에 파이썬 글자 형식을 맞출 수 있다.. 깔끔한 코딩을 위한 단축키입니다.. ㅎㅎ
