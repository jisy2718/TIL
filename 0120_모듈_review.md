# 02-02. 모듈

# 1. 모듈과 패키지

패키지를 모듈로 부르기도 하는 등 전체적으로 용어가 혼용된다.

## 모듈

• 특정 기능을 하는 코드를 파이썬 파일(.py)



## 패키지

+ 여러 모듈의 집합

  

## 모듈과 패키지 불러오기

+ ```import moduleA```    /  ```from moduleA import object(var, function, class)```
  + 해당 공간에서 moduleA 라는 이름을 쓸 수 있게 됨  / 해당 공간에서 import한 요소 쓸 수 있게 됨
+ ```from package.module import object(var, function, class)```
  + 모듈에서 선언되어 있는 모든 요소(객체?)를 가져다 쓸 수 있음/  ```import *``` 하면 전체 요소 쓸 수 있음

+ ```from package import module```

# 2. 파이썬 표준 라이브러리

+ pip ( the python package installer : 파이썬 패키지 관리자)

  + **PyPI (Python Package Index)** 에 저장된 외부 패키지를 설치할 수 있게 해주는 패키지 관리 시스템

+ pip 에서 쓸 수 있는 명령어

  | 명령어    | 설명                             | 예시                                                         |
  | --------- | -------------------------------- | ------------------------------------------------------------ |
  | pip       | pip에 대한 설명                  | ```$ pip```                                                  |
  | install   | 패키지 설치                      | ```$ pip install ‘SomePackage>=1.0.4’``` <br />```$ pip install SomePackage==1.0.4``` |
  | uninstall | 패키지 삭제                      | ```$ pip uninstall SomePackage ```                           |
  | list      | 전체 패키지와 버전 목록          | ```$ pip list```                                             |
  | show      | 1가지 패키지의 상세정보          | ```$ pip show somepackage```                                 |
  | freeze    | 지금 설치된 패키지의 버전을 매핑 | ``` $ pip freeze```<br />``` $ pip freezxe > requirements.txt```<br />txt로 저장 후 다른 사람에게 공유 후, <br />``` pip install -r requirements.txt``` 해주면 패키지 설치 버전을 맞출 수 있음<br />(package의 github에 requirements.txt 공유되어 있음) |
  
  
  
  





# 3. 가상환경

: 라이브러리(패키지)를 활용하기 위한 환경 / 프로젝트 별로 각각 폴더를 만들어 놓고, 패키지가 해당 폴더에 저장되도록 하는 것이 가상환경

+ 한 컴퓨터에는 하나의 패키지 버전만 설치가 가능
+ 2개 이상의 패키지 버전을 이용해야 할 때는, 가상환경을 만들어서 프로젝트별로 독립적인 패키지 관리 가능
+ ```venv```
  + 가상 환경을 만들고 관리하는데 사용되는 모듈 (python 3.5+)
  + 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
    + 특정 폴더에 가상 환경이 (패키지 집합 폴더 등) 있고
    + 실행 환경( 예 - bash )에서 가상환경을 활성화 시켜, 해당 폴더에 있는 패키지를 관리/사용함


## [1] 가상환경의 생성

+ ``` $ python -m venv foldername``` : foldername으로 주로 venv 사용

+ 가상환경을 실행하고, 패키지를 설치하면, 해당 폴더에 설치가 됨

  + 원래 C:/Users/username/appdata/local/prigrams/python/lib 에 설치 됨

+ 가상환경의 실행 ( git-bash 기준 )

  + 가상환경 folder를 가지고 있는 디렉토리에서``` $ source foldername/Scripts/activate```
  + 활성화 되면, git bash에서 코드 실행시 아래에 (foldername) 이 뜸
  + 이 후 패키지 설치하면, 해당 폴더에 설치됨
  + ```deactive``` 입력하면 가상환경 종료
  + 

  





# 4. 사용자 모듈과 패키지

## [1] 모듈 만들기 & 활용

1. ```module.py``` 에 원하는 함수와 변수들을 정의하기

2. 같은 폴더 상의 ```curent.py``` 에서 ```import module```  or ```from module import *``` 하여 쓸 수 있음

   : ```import module``` 의 경우 ```module.function``` 꼴로 써줘야 함

   

## [2] 패키지

+ 패키지는 여러 모듈/하위 패키지로 구조화

+  ```__init__.py```  : 이 파일이 있는 폴더에 있는 파일들은 하나의 패키지로 인식하게 됨

  + python 3.3 부터는 없어도 되지만, 하위 버전 호환 및 프레임워크 등에서의 동작을 위해 파일 생성을 권장

  + 예 :

    my_package/

    ​    \__init__.py

    ​    math/

    ​        \__init__.py

    ​        tools.py

    ​        variable.py

    ​    statistics/

    ​        \__init__.py

    ​        tools.py

    

  + 위의 내용에서 math / statistics 의 tools 에 여러 변수나 함수 존재 가능

    