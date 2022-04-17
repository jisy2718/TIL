[toc]





# Django02 - Django Model



# MODEL

## 1. Model

+ 각각의 model은 하나의 데이터베이스 테이블에 매핑됨

+ 웹 애플리케이션의 **데이터를 구조화하고 조작**하기 위한 도구

  

## 2. DB & 쿼리

### [1] 정의

+   DB
  + 체계화된 데이터들의 모임

+ 쿼리 (Query)
  + 데이터를 조회하기 위한 멸령어
  + DB를 조작

### [2] DB 구조

+ 스키마
  + DB에서 자료의 구조, 표현방법, 관계등을 정희한 구조
  
+ 테이블
  + 열, 필드, 속성
  + 행, 레코드, 튜플
  
+ PK (Primary Key)
  + 각 행의 고유값으로 반드시 설정
  
    

## 3. Migrations

### [1] 의미

+ Django가 model에 생긴 변화를 반영하는 방법



### [2] 명령어

+ makemigrations

  + model을 변경한 것에 기반한 새로운 마이그레이션(설계도) 만들 때

  + ```bash
    $ python manage.py makemigrations
    ```

    

+ migrate

  + 마이그레이션을 DB에 반영

  + Model의 변경사항들과 DB의 스키마가 동기화됨

  + ```bash
    $ python manage.py migrate
    ```

    

+ sqlmigrate

  + 마이그레이션에 대한 SQL 구문 보기위해 사용

  + ```bash
    $ python manage.py sqlmigrate app_name 0001
    ```

  + 

+ showmigrations

  + 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용

  + Migrate 유무 알수 있음

  + ```bash
    $ python manage.py showmigrations
    ```



### [3] migration 3 단계

+ models.py

  + model 변경

+ ```bash
  $ python manage.py makemigrations
  ```

  + migrations 파일 생성

+ ```bash
  $ python manage.py migrate
  ```

  + DB에 반영 (Model과 DB 동기화)

























# ORM

+ Object - Relational - Mapping

## 1. 의미

+ 객체지향 프로그래밍 언어를 사용하여, 호환되지 않는 유형의 시스템 간(Django - SQL)의 데이터를 변환하는 프로그래밍 기술

+ OPP  프로그래밍에서 RDBMS를 연동할 때, DB와 OPP 언어간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

+ DB 를 조작하기 위해 ORM 사용

  

**워크플로우**

+ SQL statement  &harr; ORM &harr; PYTHON object



## 2. 장단점

+ 현대 웹 프레임워크의 요점은 웹 개발 속도 향상(생산성향상)

**장점**

+ SQL 잘 못해도 DB조작가능
+ SQL의 절차적 접근이 아닌 객체지향적 접근으로 생산성 향상



**단점**

+ ORM 만으로 완전한 서비스 구현 어려움





## 3. DB API (DB 조작도구) [[공식문서](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#queryset-api-reference)]

+ Model을 만들면 Django는 객체를 CRUD 할 수 있는 DB-abstract API를 만듦

### [1] DB API 구문

**예시**

+ Classname.objects.all() 
  + objects : manager
  + all() : QuerySet API



**Manager**

+ Django 모델에 DB query 작업이 제공되는 인터페이스



**QuerySet**

+ DB로부터 전달받은 객체 목록



### [2] Shell_plus

+ Django-extensions library 기능 중 하나

  #### (a) 설치 및 실행

  ```bash
  $ pip install ipython
  $ pip install django-extensions
  ```

  ```python
  # settings.py
  INSTALLED_APPS = [
      'django_extensions',
  ]
  ```

  ```bash
  $ python manage.py shell_plus
  ```

  

### [3] CRUD



#### (1) CREATE

**코드**

```shell
# 방법 1
article = Article()
article.title = 'first'
article.content = 'hey!'
article.save()

# 방법 2
article = Article(title='second', content ='haha')
article.save()

# 방법 3
Article.objects.create(title='third', content='yaho')
```



**메서드**

+ save()
  + 객체를 DB에 저장
    + save() 하지 않으면, DB에는 아무영향 안끼침
  + save() 호출 전에는 객체의 ID값 무엇인지 알수 없음
    + ID는 DB에서 계산되기 때문



+ \__str__(self):

  + object를 읽을 수 있는 문자열을 반환하도록 설정가능 (shell_plus 재시작필요)

  ```python
  def __str__(self):
      return self.title
  ```

  



#### (2) READ

**코드**

```shell
# 전체보기
Article.objects.all()

# 속성보기
article.title
article.content
article.created_at

# 1개 가져오기
Article.objects.get(pk=1)

# 여러개 가져오기
Article.objects.filter(content='ha')

```



**메서드**

+ 모두 `Article.objects.___()` 으로 활용



+ all()

  + 현재 QuerySet의 복사본 반환

+ get()

  + 주어진 매개변수와 일치하는 객체를 반환

  + 없다면 DoesNotExist 예외

  + 2개 이상이라면 MultipleObjectsReturned 예외

  + ```shell
    article = Article.objects.get(pk=100)           # 존재하지 않는 경우 예외
    article = Article.objects.get(content='haha')   # 여러개 인 경우 예외
    ```

+ filter()

  + 주어진 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환



#### (3) UPDATE

**코드**

```shell
# 변경하기
article = Article.objects.get(pk=1)
article.title = '제목바꾸기'
article.save()
```



#### (4) DELETE

**코드**

```shell
# 삭제하기
article = Article.objects.get(pk=1)
article.delete()
```





### [4] 크기비교 / values / query



#### (1) \_\_gte, \_\_lte, \_\_gt, \__lt

```python
User.objects.filter(age__gte=30).count()  # age >= 30 인 사람 수
```



#### (2) values

+ SELECT / GROUP BY 에서 column 역할

  

+ SQL의 SELECT에 들어가는 column 이라고 생각

```python
Class.objects.filter(condition).values('colname')

User.objects.filter(age__lt=30).values('fist_name')
```



+ SQL의 GROUP BY의 column 이라고 생각

```python
User.objects.values('country')  # country로 그룹 나뉨
User.objects.values('country').annotate(Count('country'))   # values 별 country 개수
# 여기서는 country별 인원수
```





#### (3) query

+ 쿼리문을 보여줌

  ```python
  print(User.objects.filter(age=30, last_name='김').query)
  ```





### [5]  [Aggregation](https://docs.djangoproject.com/en/3.1/topics/db/aggregation/#aggregation) 

#### (1) Count, Avg , Max, Min, Sum

> [`QuerySet` API reference - annotate()](https://docs.djangoproject.com/ko/3.1/ref/models/querysets/#annotate)
>
> [`QuerySet` API reference - Aggregation functions](https://docs.djangoproject.com/ko/3.1/ref/models/querysets/#aggregation-functions)



```python
# Count 기본
User.objects.filter(age__gte=30).count()  # age >= 30 인 사람 수

# Count
from django.db.models import Count

User.objects.values('country').annotate(Count('country'))

User.objects.values('country').annotate(num_countries=Count('country')) # name 설정

print(User.objects.values('country').annotate(Count('country')).query) # 쿼리문 보기

User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance')) # Avg 와 함께 사용


# Avg
from django.db.models import Avg
User.objects.aggregate(Avg('age'))
User.objects.filter(last_name='김').aggregate(Avg('age'))
>>> {'age__avg': 31.75}

# Max
from django.db.models import Max
User.objects.aggregate(Max('balance'))
>>> {'balance__max': 1000000}

# Sum
from django.db.models import Sum
User.objects.aggregate(Sum('balance'))
>>> {'balance__sum': 14425140}
```



### [6] Annotate (GROUP BY)

+ SQL의 GROUP BY
+ [`QuerySet` API reference - annotate()](https://docs.djangoproject.com/ko/3.1/ref/models/querysets/#annotate)





### [7] startswith / endswith (와일드카드)

```python
User.objects.filter(first_name__startswith='사')  # 이름이 사로 시작하는 사람
User.objects.filter(first_name__endswith='랑')    # 이름이 랑으로 끝나는 사람
```





### [8] order by

```python
User.objects.order_by('-age')  # 내림차순
User.objects.order_by('age')   # 오름차순


# balance 오름차순, age 내림차순으로 10개
User.objects.order_by('balance', '-age')[:10]
```





