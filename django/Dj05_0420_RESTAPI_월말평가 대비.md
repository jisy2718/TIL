[toc]

# 0425 REST API 월말평가 대비



# 0. settings.py

```python
INSTALLED_APPS = [
    'movies',
    'django_seed',
    'django_extensions',
    'rest_framework',       # 해당 Library 이용
]
```



# 1. models.py

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



# 2. serializers.py

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

  





# 3. urls.py

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



# 4. views.py

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

  