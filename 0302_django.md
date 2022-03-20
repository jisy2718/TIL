# 기초

## 1. 실행순서

+ **manage.py** 가 있는 곳이 BASE_DIR 이다.

```bash
# 1. 가상환경 활성화 in bash
python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt  # requirements.txt 에 패키지 정리되어있는 경우 진행

```



```bash
th# 2. vs code에서 select interpreter

ctrl + shift + p -> python select interpreter 검색 후
별표 추천으로 뜨는 venv 를 선택
```

![venv](0302_django.assets/venv_interpreter.PNG)

맨 아래 선택



```bash
# 3. 만약 requirements.txt 없다면, 장고 설치 in bash
pip install django==3.2.12

# 4. 프로젝트 생성
django-admin startproject projectname . # . 붙이면 상위폴더 없이 생성됨

# 5. django 서버 시작하기 (활성화)
python manage.py runserver

```



```bash
# 6. 앱 생성
python manage.py startapp appnames # appnames 는 복수형으로 작성

# 7. 앱 등록
# projectname/settings.py 에 들어가서
INSTALLED_APPS = [
# Local apps (우리가 만든 것)
'appnames',

#Third party apps (pip install 하는 것들)
''

# Djnago apps (기본 설치된 것들)
'기본설치된 것들',
]





```



```python
# 8. projectname(folder) urls 에 

## (1) application view 추가   / include 추가
from appnames import views
from django.urls import path, include

## (2) urlpatterns의 path에 articles(appname) & include 추가
path('articles/',include('articles.urls') ) # include의 기능은 articles/~ 라는 url 들어오면 뒷부분 ~ url 부분을 articles.urls 모듈로 보내서 처리함


# 9. articles 에 urls.py 생성 후
from django.urls import path
from . import views
# 처리해야할 목록
# articles/   : 모든 게시글 보여주기:index.html
# articles/new/ : 게시글 작성을 위한 양식 요청 new.html
# articles/create/ : 사용자가 작성한 내용을 DB에 저장
# articles/<int:pk>/ : pk에  해당하는 게시글 내용 보여주기 detail.html
app_name = 'articles'
urlpatterns = [
  path('',views.index,name='index'),
  path('new/',views.new,name='new'),
  path('create/',views.create,name='create'),
  path('<int:pk>/',views.detail,name='detail'),
]
# 여기서 path는 name으로 호출되는 경우 url을 내보내고, url을 받는 경우 views로 보내는 2가지 역할을 함
# app_name = articles로 해서 name_space를 만들어줌. 
# 그래서 여기의 name 들의 정확한 이름은 articles:index  / articles:new / articles:create 와 같음



```



```python
# 10. articles/views.py 작성

# 9에서 views.index 와 같이 사용한 함수들 만들어주기
from django.shortcuts import redirect, render
from .models import Article    #----------까먹지 말기

# Create your views here.
def index(request):
    #여기에서 DB의 게시글 데이터를 가져와야 합니다. 
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request,'articles/index.html', context)

#사용자가 내용을 작성하기 위해 보여주는 양식
def new(request):
    return render(request,'articles/new.html')


#사용자가 작성한 내용을 저장하면 됩니다. 
def create(request):
    #사용자가 보낸 데이터를 받아서 DB에 저장
    # save()
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()
    # return render(request,'articles/index.html')
    return redirect('articles:index')


def detail(request,pk):
    #pk를 아니까.....DB에서 가져오기
    article = Article.objects.get(pk=pk)
    context ={
        'article' : article
    }
    return render(request,'articles/detail.html',context)
```





```html
# 11. html 파일 작성

## (1) BASE_DIR(manage.py가 있는 곳)에
template/base.html 생성 후 작성

  <title>CRUD App</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
   
  </nav>
  {% block content %}
  {% endblock content %}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>



## (2)
settings의 TEMPLATE=[ { 'DIRS':[BASE_DIR/'templates'] } ] 작성

## (3) 10에서 작성한 render의 2번째 성분에 template 요청한 부분들 html작성
articles/templates/articles/index.html


{% extends 'base.html' %}  # base.html을 읽게됨. 드러다 block 나오면 해당 html 문서의 해당 block 부분으로 이동
{% block content %}
  <h1>Index 페이지 입니다.</h1>
  <h1>Articles</h1>
  <a href=" {% url 'articles:new' %} ">[새 글 쓰기]</a>    #url의 밖은 ""여야함.
  <hr>
  {% for article in articles %}
    <p>글 번호 : {{ article.id }}</p>
    <p><a href=" {% url 'articles:detail' article.pk %} ">글 제목 : {{ article.title }}</a></p>
    {% comment %} <p>글 내용 : {{ article.content }}</p> {% endcomment %}
    <hr>
  {% endfor %}

{% endblock content %}


# 위 파일의 읽는 순서
# extends 'base.html' 하면 모든 app의 template 하위로 가서 base.html 찾게 되는데, 11.(2)에서 base.html이 저장되어 있는 곳도 찾아보도록 설정했음
# 그렇게 base.html 찾으면 base.html을 쭉~~ 읽게 됨.
# 그러다가 block 을 만나게되면, index.html에 해당 블록이 있는지 보고, 있다면, 그 블록 사이에 있는 것들을 읽게 됨. 그러다 index.html에서 block이 끝나면, 다시 base.html로 돌아와서 그 뒷부분을 읽게 됨.
# base.html에 block이 있지만 index.html에는 없는 경우, 그냥 넘어가게 됨.
```



+ 아래처럼 class 생성시 `from . import Article` 가능해짐 [models 참고](https://docs.djangoproject.com/en/4.0/topics/db/models/)

```python
# 12. models.py 작성
## Djangodb.models 모듈은 파이썬 object를 DB로 전송하기 위한 기능들 있는 모듈
## models.Model 은 ORM 역할을 할 수 있는 객체로 상위 CLASS/ 여러 method 저장되어있음
## 그래서 Article이 상속받아서 쓸 수 있다.

from turtle import title, update
from django.db import models

# Create your models here.
class Article(models.Model):     
    #필드 정의
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self) -> str:
        return self.title  # instance 이름 치면 해당 값 return 됨
```



```bash
# 13. migration

## (1) model.py 수정사항 migrations / migrate
$ python manage.py makemigrations  # 설계도 만들기 / Model.py에 쓴 것으로 SQL문 짜는 것이 makemigrations
$ python manage.py migrate         # 설계도를 DB에 반영


## (2) migration 된 것 확인
$ python manage.py showmigrations

## (3) migration 된 것 SQL문 확인
$ python manage.py sqlmigrate app_name 0001
```



+ 모델 class object(instance) 생성 가능한 코드

```python
# 1.
article = Article(title = 'title', content='content')
article.save()

# 2
article = Article()
article.title = 'title'
article.content='content'
article.save()

# 3.
Article.objects.create(title='title',content='content')

# 4
article = Article(1(int로된 id), 'title', 'content')
article.save()
```

+ model instance 가져오기

```python
# id=1 인 첫 instance 가져오기
# 1.
Article.objects.all()[0]
# 2.
Article.objects.all().first()
# 3.
Article.objects.all().get(id=1)
```





python shell

```bash
# 14. python object instance 생성과 이를 DB에 입력

## (0) python shell 실행위해 ipython, django extention 설치 및 등록
$ pip install ipython
$ pip install django-extensions

settings의
INSTALLED_APP = [
'django_extensions' ##------------------주의!!!! 여기 추가시 _ 언더바 이용
]#추가하기

## (1) python shell 실행
ipython, django extention설치 해 놓으면

`python manage.py shell_plus` 를 bash 에서 실행하면, models.py에 있는 class 들 모두 import 해서 Object를 생성할 수 있고, 이 Object를 DB에 입력할 수 있게 됨.

## (2) 생성명령어
article = Article(title='first_title',content='first_content') # Object instance 생성
article.save() # DB에 저장
article.delete() # DB에서 삭제?


## (3) 기타명령어
Article.object.all() # 해당 클래스 object instance 모두 보기
Article.object.all().order_by('-pk') # 역순으로 보기

Article.object.get(title='찾고자하는것') # object instance 1개만 있을 때 찾을 수 있음. pk로 이용권장
Article.object.get(pk='찾고자하는것')

Article.object.filter('get과같은방식') # 여러개 있어도 찾을 수 있음

```





+ 가능한 Django Model Field Type [문서](https://docs.djangoproject.com/en/4.0/ref/models/fields/)
  + CharField, TextField, IntegerField, FloatField, DateTimeField, DateField



```python
#사용자가 작성한 내용을 저장하면 됩니다. 
def create(request): # 해당 요청은 데이터를 DB에 저장하라는 것이지, 어떤 페이지를 보여달라는 것이 아님
    #사용자가 보낸 데이터를 받아서 DB에 저장
    # save()
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()
    # return render(request,'articles/index.html')  # 이걸로 return 하면 요청과 페이지가 안맞는 현상이 발생한다.(index페이지에 content 잘 안보이고, 주소창도 create로 되어있음)
    return redirect('articles:index')
    return redirect('articles:detail', article.pk) # 변수 넣는 법(variable routing)
# redirect : 브라우저가 새로운 요청을 만들도록 응답 / 여기서는 index page를 보여주기 위한 요청을 새로 만들어라. 그러면 create라는 url가 아닌 index라는 url을 새로 만들게 됨.
```



+ variable routing
  + url 주소를 변수처럼 이용하는 것
+ 구성요소
  + url path converters (이것들 없어도 작동함/그냥 알려주기 위한 것)
    + str, int,slug
    + `path('<int:pk>/',views.detail,name='detail'),`
      + `pk`가 변수명 선언한것
  +  `path('<int:pk>/',views.detail,name='detail'),` 입력 후, views에서 detail 함수에 pk 를 인자로 넣어줘야함 



+ 상세페이지보기
  + detail/?pageno=15 # detail 이란 url은 바뀌지 않음
  + variable routing   
    + articles/15 # 이건 url 자체가 변경됨
    + 모든 숫자에대해 새로 url 만들 수 없으므로, 해당 숫자를 variable로 보게 됨
    + `path('<int:pk>/',views.detail,name='detail'),`



+ variable routing 진행 순서

```django
{% extends 'base.html' %}
{% block content %}
  <h1>Index 페이지 입니다.</h1>
  <h1>Articles</h1>
  <a href=" {% url 'articles:new' %} ">[새 글 쓰기]</a>
  <hr>
  {% for article in articles %}
    <p>글 번호 : {{ article.id }}</p>
    <p><a href=" {% url 'articles:detail' article.pk %} ">글 제목 : {{ article.title }}</a></p>
    {% comment %} <p>글 내용 : {{ article.content }}</p> {% endcomment %}
    <hr>
  {% endfor %}
{% endblock content %}
  
```

위에 a tag에 href 에 article.pk 넣어주면 이것이 app의 urls로 가고 거기서 `path('<int:pk>/',views.detail,name='detail'),` 로 가서  views로 감





+ 세부게시물 삭제하기 / 수정하기
+ delete.html 만들어야하는데, 여기에 어떤 게시글 삭제할 것인지 요청 같이 보내야 함
+ articles/pk/
+ articles/pk/delete   : 삭제
+ articles/pk/update : 수정



+ 삭제요청

+ 1. urls.py

  ```python
  app_name = 'articles'
  urlpatterns = [
    path('',views.index,name='index'),
    path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete/',views.delete,name='delete'),  # 생성 1
  ]
  ```

+ 2. views.py

  ```python
  ```

  



+ GET & POST
  + form 이용해서 input의 정보 서버로 보낼 때, key-value pair로 보내지는데, input의 name 값이 key 값이다.

+ GET 은 서버에 정보 요청
+ POST 는 서버에 정보 전송



+ GET

  + 쿼리 형태로

  ```url
  http://127.0.0.1:8000/articles/new/?title=%EC%A0%9C%EB%AA%A9%EC%9E%85%EB%8B%88%EB%8B%A4%201111&content=%EB%82%B4%EC%9A%A9%EC%9E%85%EB%8B%88%EB%8B%A4.%201111
  ```

  주소창의 url 을 변경해서 하는 것은 모두 GET 요청임.(form method=GET, a tag의 href)

  

+  POST

  ```HTML
  
  ```

  + csrf token 도 넣어줘야 함



+ shell_plus

  ```python
  # 삭제
  article = Article.object.get(pk=1)
  article.delete()
  ```

  



+ DB API

  + get()

    같은 것



# 2. 웹사이트 만들기



## [1] admin [문서](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)

+ 유의 : url에서 /admin 했는데, OperationalError at /admin/ 뜨면 `$ python manage.py migrate` 해주면 됨



### (1) 계정생성

```bash
# 1. admin 계정 생성
$ python manage.py createsuperuser  # email 은 입력안해도 됨
```



### (2) admin 사이트에 app 가져오기

```python
# 1. appname(folder)의 admin.py 에 작성
# [1] 아래코드 입력시 admin 사이트에 해당 app 가져오고, DB와 상호작용 가능 
from .models import Article
admin.site.register(Article) # 입력

# [2] 원하는 variable이 admin에 뜨도록 하려면
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at')

admin.site.register(Article, ArticleAdmin) # 수정해서 입력
```





## [2] main page

+ `python manage.py runserver`  입력시 로켓말고, 글 목록(게시판) 나오도록



### (1) appfolder(articles) 에서 할 일 

```python
# 1. urls.py 에서 할일
from django.urls import path
from . import views
# articles/ : 모든 게시글 다 보여주기
# articles/new/ : 게시글 작성 양식 요청
# articles/creat/ : 사용자가 작성한 내용 DB에 저장
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new',views.new, name='new'),
    path('create',views.create, name='create')
]

```











## 2. 구성요소

### [1] projectname folder

```bash
projectname(folder)
  __init__.py  # Python 에게 이 디렉토리를 하나의 Python 패키지록 다루도록 지시
  asgi.py      # Asynchronous Server Gateway Interface로 
               # Django application이 비동기식 웹서버와 연결 및 소통하는 것을 도움
               # 배포할 때 이용
  settings.py  # 애플리케이션의 모든 설정을 포함 / 사용
  urls.py      # 사이트의 url과 적절한 views의 연결을 지정 / 사용
  wsgi.py      # Web Server Gateway Interface로
               # Django application이 웹서버와 연결 및 소통하는 것을 도움
               # 배포할 때 이용
manage.py      # Djnago 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
template(folder) # 템플릿
```

### [2] app folder

```bash
appnames(folder)
  migrations(folder)
  __init__.py
  admin.py    # 관리자용 페이지 설정
  apps.py     # 앱의 정보가 작성된 곳
  models.py   # 앱에서 사용하는 모델을 정의하는 곳
  tests.py    # 프로젝트의 테스트 코드를 작성하는 곳
  views.py    # view 함수들이 정의되는 곳
  template(folder) # 템플릿
```

### [3] template(folder)

+ template 는 직접생성해야
+ application과 project 바깥이 생성
+ project 바깥에 있는 template을 application의 template에 상속가능



## 3. 중요 로직

### [1] 코드작성순서

`urls.py` &rarr; `views.py` &rarr; `template`



```python
# 1. urls.py 예
from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', views.movies),
    path('movies/recommendations/',views.recommendations),
]



# 2. views.py 예
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def movies(request):
    pass

def recommendations(request):
    return render(request, 'recommendations.html')

# 3. template 예
# app folder의 template에
index.html, recommndations.html 생성 후 작성
```







# 웹페이지에 데이터 띄우기 위해 해야할 것들

+ 아래는 모두 같은 경로에 위치

## 1. appname folder 

+ models.py에 class 정의

  + ipython, django extention, django extention viewer 설치 해 놓으면

    `python manage.py shell_plus ` 를 bash 에서 실행하면, models.py에 있는 class 들 모두 import 해서 Object를 생성할 수 있고, 이 Object를 DB에 입력할 수 있게 됨.

+ urls.py

  + `from . import views` 넣기
  + `app_name = 'articles'` 추가
  + `urlpatterns `
    + `path('',views.index,name='index')  ` 1
    + `path('new/',views.new, name='new')` 추가 2

+ templates/articles

  + index.html

    + `{% extends 'base.html' %}`

    + `{% block content %}`  내용 작성 `{% endblock content %}`

      

  + new.html

    + `{% extends 'base.html' %}`
    + `{% block content %}`  내용 작성 `{% endblock content %}`





# 2. projectname folder

+ settings.py
  + `INSTALLED_APPS` 에 appname 추가
  + `TEMPLATES = [ 'DIRS' : [BASE_DIR/'templates']   ] ` 입력
+ urls.py
  + `from django.urls import path, include` 추가
  + `urlpatters = [ path('articles/'), include('articles.urls')]` 추가
  + 
  + 



# 3. templates

+ 상속을 위해서 만들기
+ base.html 생성
  + CDN 추가
  + `navbar` 등 원하면 작성
  +  `{% block content %}` `{% endblock content %}` 작성







# 명령어 관련

# 1. shell

`python manage.py shell_plus `



## 2. bash

`python manage.py runserver`













GET 은 서버로부터 데이터 전송받기

POST 는 서버로 데이터 보내기
