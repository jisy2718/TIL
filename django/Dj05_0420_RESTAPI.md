[toc]



# Django 05 - REST API

# REST API 이용시 

## [1] VSCODE 작성해야 되는 부분

+ project_folder

  + settings.py 
    + app_name 추가
  + urls.py
    + include app_name.urls

+ app_folder

  + urls.py
  + models.py
  + serializers.py
  + views.py

  

## [2] serializers.py 역할

+ 이전에 배운 **ModelForm의 역할도 같이**함

  + Model의 field를 채워줄 때, serializer에서 filed 채워줘도 됨

  + 예

    ```python
    # models.py
    class Music(models.Model):
        artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
    
    # views.py
    # music 생성
    @api_view(['POST'])
    def music_create(request,artist_pk):
        artist = get_object_or_404(Artist, pk=artist_pk)
        serializers = MusicSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(artist=artist)           # 해당부분 !
            return Response(serializers.data, status=status.HTTP_201_CREATED)
    ```

    + 위 처럼 `is_valid()` 에 인자 덜 채운채로 통과하려면 

    + serializers.py에서 read_only_fields 설정해줘야 함

      ```python
      # serializers.py
      class MusicSerializer(serializers.ModelSerializer):
          class Meta:
              model=Music
              fields = ('id','title','artist',)
              read_only_fields = ('artist',)
      ```


+ `ModelSerializer` 의 경우 Model의 역할도 같이 함





# HTTP

## [1] JSON 응답

+ 지금까지는 Client(browser)의 요청에 server가 html을 응답하면, client가 html 파일 그려냈음
+ 앞으로는 서버는 html응답이 아니라, data(JSON, XML, text, html)로 응답할 것임
  + data로 응답하는 이유
    + 앞으로는 화면을 미리 그려놓고, 화면 내의 특정 부분의 JS 코드가 요청을 보내고 응답을 받게됨
    + JS역할 : 응답받은 data를 화면에 띄우기
  + JSON : 정형데이터로 형식이 있는 문자열임
    + 그냥 문자열이므로, Client가 꾸미지 않고 그냥 내용 그려내고 끝



## [2] HTTP response status codes

+ 1xx : Informational responses

+ 2xx : Successful responses

+ 3xx : Rediriection messages

+ 4xx : Client error responses

+ 5xx : Server error responses

  + `is_valid()` 통과 못하면 500 error

    + 예 `serializers.is_valid()` 

      


## [3] 웹에서의 리소스 식별

### (1) 리소스

+ 리소스(resource, 자원)
  + HTTP 요청의 대상
  + 문서, 사진 등 무엇이든 가능
  + 각 리소스는 리소스 식별을 위해 HTTP 전체에서 사용되는 URI(Uniform Resouce Idenrtifier)로 식별됨
  + 

### (2) URI

+ Uniform Resource Identifier
  + 통합자원식별자
  + 인터넷의 자원을 식별하는 유일한 주소
  + 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열
+ 하위 개념
  + URL, URN
  + URL과 URI 같은 개념으로 사용하기도 함



#### URL/URN

**URL** (Uniform Resource Locator)

+ 통합 자원 위치
+ 네트워크 상에 자원이 어디있는지 알려주기 위한 약속
  + 과거에는 실제 자원의 위치를 나타냈지만, 현재는 추상화된 의미론적 구성
    + 과거 예 : ~~/~.html 처럼 직접 html 위치 나타냄
+ 다른 이름 : 웹주소, 링크



+ 

**URN**(Uniform Resource Name)

+ 통합 자원 이름

+ URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름
+ 예
  + ISBN
  + 

#### URI 구조

+ 예
  + https://www.example.com:80/path/to/myfile.html/?key=value#quick-start



##### Scheme (Protocol)

+ 브라우저가 사용해야 하는 프로토콜
  + http(s), data, file, ftp 등
  + **https://**www.example.com:80/path/to/myfile.html/?key=value#quick-start

##### Host

+ 요청을 받는 웹 서버의 이름

  + https://**www.example.com**:80/path/to/myfile.html/?key=value#quick-start
  + Domain name 활용

+ IP address를 직접 사용할 수도 있지만, 실제로 사용시 불편하므로 별로 사용 x

  + 142.251.42.142 가 구굴의 실제 IP address

  

##### Port

+ 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 문으로 보통 생략되어서 나타남
  + https://www.example.com**:80**/path/to/myfile.html/?key=value#quick-start
+ http 프로토콜 표준포트
  + HTTP 80
  + HTTPS 443

##### Path

+ 웹 서버 상의 리소스 경로

+ 초기에는 실제 파일이 위치한 물리적 위치 나타냈지만 현재는 추상화된 형태의 구조로 표현

  + https://www.example.com:80**/path/to/myfile.html**/?key=value#quick-start

    

##### Query (식별자/쿼리스트링파라미터)

+ Query String Parameters

+ 웹 서버에 제공되는 추가적인 매개변수

  +  `&` 로 구분되는 key-value

  + https://www.example.com:80/path/to/myfile.html**/?key=value**#quick-start

  + 검색 같은 것 할 때 주로 나타남

    

##### Fragement

+ Anchor로 자원 안에서의 북마크의 한 종류
+ 브라우저에게 해당 HTML 문서의 특정 부분을 보여주기 위한 방법
+ 브라우저에게 알려주는 요소이기 때문에  fragment identifier(부분식별자)라고 부름
  + `#` **뒷 부분 요청은 서버에 전송x**
    + 브라우저가 식별해서 이동시켜줌
  + https://www.example.com:80/path/to/myfile.html/?key=value**#quick-start**









# Response















# RESTful API

+ REST 방식을 따르는 API

## [1] API

+ API

  + Application Programming Interface
  + 미리 기능을 만들어두고, 다른 어플들이 그 기능을 사용할 수 있도록 인터페이스를 만들어 놓은 것
  + 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
    + Youtube API, Naver Papago API

  

+ 응답 데이터 타입

  + HTML, XML, JSON

  

  

  

## [2] REST

### (1) 의미

+ REpresentational State Transfer

#### 구성

+ 자원
  + URI
+ 행위
  + HTTP Method ( 자원을 이용하기 위한 방법 : GET, POST, PUT, DELETE )
+ 표현
  + 행위의 결과를 데이터로 받을 것인데, 그 중에 JSON으로 받겠음







### (2) JSON

+ JS 표기법을 따르는 단순 문자열
+ 앞으로 JSON 문자열 반환하도록, 프로그래밍







 # REST API 코드(핵심사항)

+ pjt 08 내용에서 발췌

## [1] settings.py

```python
INSTALLED_APPS = [
    'movies',
    'django_seed',
    'django_extensions',
    'rest_framework',       # 해당 Library 이용
]
```



## [2] models.py

+ 1 : N 경우
  + `on_delete = models.CASCADE`

```python
class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='review', on_delete=models.CASCADE)
```



+ N : M 경우

  +   `actors = models.ManyToManyField(Actor, related_name='movie')   `

  ```python
  class Actor(models.Model):
      name = models.CharField(max_length=100)
                              
  class Movie(models.Model):
      title = models.CharField(max_length=100)
      actors = models.ManyToManyField(Actor, related_name='movie')       
  ```

  + 위와 같이 작성시 table name은 **appname_movie_actors**



## [3] serializers.py

+ Import

  ```python
  from rest_framework import serializers
  from .models import Movie, Actor, Review
  ```



+ serializers.RelatedField

  + Review model에서 Movie 가져올 때, 화면에 id가 아닌, movie title로 정보 나오게 됨
  + Movie model에서 Actor 가져올 때, 화면에 id가 아닌 actor name으로 정보 나오게 됨

  ```python
  class MovieReviewRelatedField(serializers.RelatedField):
      def to_representation(self, value):
          return {'title : %s'%(value.title)}
  
  class ActortoMovieRelatedField(serializers.RelatedField):
      def to_representation(self, value):
          return {'name : %s'%(value.name)}
  ```



+ serializers.ModelSerializer

  ```python
  class ActorListSerializer(serializers.ModelSerializer):
      class Meta:
          model=Actor
          fields = ('name',)
  
  class ReviewListSerializer(serializers.ModelSerializer):
      movie = MovieReviewRelatedField(read_only=True)
      class Meta:
          model=Review
          fields =('title','movie',)
  
  class MovieSerializer(serializers.ModelSerializer):
      actors = ActortoMovieRelatedField(read_only=True, many=True)    
      review = ReviewListSerializer(many=True, read_only=True)
      class Meta:
          model=Movie
          fields = ('title','actors','review',)
  
  class ActorSerializer(serializers.ModelSerializer):
      movie = MovieSerializer(many=True, read_only=True)
  
      class Meta:
          model=Actor
          fields='__all__'
  
  class MovieListSerializer(serializers.ModelSerializer):
      
      class Meta:
          model=Movie
          fields = ('title',)
  
  class ReviewSerializer(serializers.ModelSerializer):
      movie = MovieReviewRelatedField(read_only=True)
      class Meta:
          model=Review
          fields = '__all__'
          read_only_fields = ('movie',)
  ```



+ 역참조하는 게시글 수 count 하기

  + `serializers.IntegerField` 이용해서, `source`, `read_only` 인자 활용

  ```python
  # models.py
  class Article(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 역참조
      content = models.TextField()
  
  # serializers.py
  class ArticleSerializer(serializers.ModelSerializer):
      # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
      comment_set = CommentSerializer(many=True, read_only=True)
      comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
      cards = CardSerializer(many=True,  read_only=True)
  
      class Meta:
          model = Article
          fields = '__all__'
  
  ```

  





## [4] urls.py

+ URL 마다의 기능은 , pk 들어가는지 유무에 따라 달라짐
  + pk 안들어가도 되면
    + **GET** 전체 리스트 &  **POST** 새로운 object
  + pk 들어가야 되면
    + 자신의 pk만 들어간다면
      + **GET** detail, **PUT** 수정, **DELETE**
    + review 처럼 다른 객체 pk 필요하면
      + **POST** 새로운 object

```python
from django.urls import path
from . import views

urlpatterns = [
    path('actors/',views.actor_list),         # GET & POST (total list, make actor)
    path('actors/<int:actor_pk>/',views.actor_detail),  # GET, PUT, DELETE
    path('reviews/',views.review_list),       # GET - total list
    path('reviews/<int:review_pk>/',views.review_detail),   # GET, PUT, DELETE
    path('movies/<int:movie_pk>/reviews/',views.creat_review), # POST - make review
]
```



## [5] views.py

+ status의 HTTP 종류들 알기
  + `return Response(serializer.data, status=status.HTTP_201_CREATED) `
+ `serializer.is_valid(raise_exception=True)`
  + instance 수정 시, 유효하지 않은 입력 들어오면,  400 error ()
  + [rest 공식문서](https://www.django-rest-framework.org/api-guide/serializers/#raising-an-exception-on-invalid-data)
+ 



+ import

  ```python
  from rest_framework import status                #
  from rest_framework.response import Response     #
  from rest_framework.decorators import api_view   #
  from django.shortcuts import get_list_or_404, get_object_or_404
  from .models import Actor, Movie, Review
  from .serializers import ActorListSerializer, ActorSerializer,MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer
  ```



+ **GET** List

  ```python
  @api_view(['GET'])
  def actor_list(request):
      actors = get_list_or_404(Actor)
      serializer = ActorListSerializer(instance=actors, many=True)
      return Response(serializer.data)
  ```

  

+ **POST**

  ```PYTHON
  @api_view(['POST'])
  def creat_review(request, movie_pk):
      movie = Movie.objects.get(pk=movie_pk)
      serializer = ReviewSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(movie=movie)
          return Response(serializer.data, status=status.HTTP_201_CREATED) 
  ```



+ **GET** detail, **PUT** 수정, **DELETE**

  ```python
  @api_view(['GET','PUT','DELETE'])
  def review_detail(request, review_pk):
      review = get_object_or_404(Review, pk=review_pk)
      if request.method == 'GET':
          serializer = ReviewSerializer(instance=review)
          return Response(serializer.data)
      
      elif request.method == 'PUT':
          serializer = ReviewSerializer(instance=review, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  
  
      elif request.method == 'DELETE':
          review.delete()
          data = {'delete': f'{review_pk}번 리뷰가 삭제되었습니다.'}
          return Response(data, status=status.HTTP_204_NO_CONTENT)
  ```

  







# 1 : N Relation

## [1] 특정 게시글에 작성된 댓글 목록 출력 (기존 필드 override)

### (1) 구현 방법 1 : `PrimaryKeyRelatedField`



### (2) 구현 방법 2 : `Nested relationships`





## [2] 특정 게시글에 작성된 댓글 개수 구하기 (새로운 필드 추가)







# Library

+ settings.py

  + 'django_seed',

  + 'django_extensions',

  + 'rest_framework',

    + ```bash
      $ pip install djangorestframework   
      ```

      



# 말씀내용

+ 500 에러는 서버가 뻗어서 작동하지 않는것

+ [request.POST, request.data 차이](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)

  ```python
  request.POST  # Only handles form data.  Only works for 'POST' method.
  request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
  ```

  

+ comment 생성시 is_valid() 통과위해서

  ```python
  # views
  @api_view(['GET','POST'])    
  def comment_list(request):
      if request.method =='GET':
          comments = get_list_or_404(Comment)
          serializer = CommentSerializer(comments, many=True)
          return Response(serializer.data)
  
      elif request.method =='POST':
          serializer = CommentSerializer(data = request.data)
          if serializer.is_valid(raise_exception=True):    # 여기 통과하기 위해서! read_only필요 /  안하면 article field 가 현재 serializer에 채워지지 않아서 validation통과불가
              serializer.save(article=article)
              return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  
  
  
  # serializers.py
  
  class CommentSerializer(serializers.ModelSerializer):
      class Meta:
          model = Comment
          fields = '__all__'
          read_only_fields = ('article',)
  
  
  ```

  

+ 알아야할 것

  + 모델관계설정
  + serializer 만드는 방법
  + views.py의 함수 작성 잘 알기
  
  + 가상환경 만들고, requirements.txt 를 가상환경에 설치하는 방법도 나옴





# 궁금한 것

+ 굳이 article_list에서 create 해야하나?

  + URL 최소화하고, HTTP METHOD로 행위를 표현하려고 하니까 ` path('articles/', views.article_list),       # 리스트, 생성`  여기서 articles 를 생성까지 함

  + REST API 는 내가 하려는 행위를 HTTP METHOD로 표현하고, 서버 내부에서 어떻게 동작되는지 최대한 숨기려는 것이 권장사항

    

  + 만약 `path('articles/create/',views.create)` 와 같이하면, 내가 하려는 행위가 URL에도 나오게 됨

    
  
  + 또한 R,U,D 는 article pk가 있어야 할 수 있는 것이므로, 그냥 article pk를 쓰는 detail에서 모두 처리하는 것임





+ serializer에서 역참조 어떻게 이루어지는지?

  + ```python
    # serializers.py
    
    class ArticleSerializer(serializers.ModelSerializer):
        comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # 역참조도 같이 serialize 하겠다
        # comment_set = CommentSerializer(many=True, read_only=True)     
        comment_count = serializers.IntegerField(source='comment_set.count', read_only =True)   # 이건 새로 만든 것            
    ```

    + 위에서, `comment_set` 은 새로 만든 필드가 아니라, 기존에 있는 역참조 매니저임. 이 경우가 overide 경우임. powershell에서 `dir(article) (의미 : dir(object))` 하면 method? 들 볼 수 있음
    + `comment_count`는 필드를 새로 만드는 경우

  

  + OVERIDE / 창조 2개 종류 필드가 있음
    + OVERIDE
      + primaryKey는 기존에 있는 filed를 이용하는 것(override)
      + serializer에서 overide 경우에 = 의 의미는 JSON의 출력할 KEY값을 만들어 내는 것은 맞는데, 기존의 것을 이용해서, 뒤에 부분이 동작 `  \# comment_set = CommentSerializer(many=True, read_only=True)  `
    + 창조
      + 그냥 이전에 하듯이 `serializers.~~fields()` 로 하면 됨
      + 





+ postman에서 comment를 추가할 때, 꼭 article pk 넣어줘야 하는가?
  + serializers.py에 read_only_fields 에 article추가해주면 안해도 됨. 
    + `read_only_fields = ('article',)`
  + 위처럼 추가 안해주면 `is_valid()`를 통과하지 못함







+ 