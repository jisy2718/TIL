[toc]



# pjt - 08 : DB 설계를 활용한 REST API 설계



# 1.





# 2. Fixture

+ db는 원격저장소에 올리지 않음
  + 우리 데이터의 구조를 다 노출시키기 때문에





+ 보내는 사람

```bash
$ python manage.py dumpdata --indent 4 articles.article > articles.json
$ python manage.py dumpdata --indent 4 articles.comment > comments.json
$ python manage.py dumpdata --indent 4 accounts.user > users.json
```



+ 받는 사람

```bash
$ python manage.py loaddata articles.json comments.json users.json
```

+ 위처럼 한번에 load 가능한 이유는 django가 fixtures/ 까지 보기 때문임.

  + 더 안전하게 하려면 folder 구조를 app/fixtures/app/articles.json 해주면 (templates 와 같은 형식으로)

  ```bash
  $ python manage.py loaddata articles/articles.json articles/comments.json accounts/users.json
  ```

  





# 3. query set



















# 4. Project 내용

+ movie actor M : N















## [1] trouble shooting
### (1) fixtures
+ fixtures

  + `python manage.py loaddata movies/actors.json movies/movies.json movies/reviews.json `할 때, json 파일의 형식을 확인해서, models.py 작성하기

  + json에 `fields`에 정의된 fileds들을 models.py 의 Model들의 field로 잘 넣어줘야 함

    ```json
    # movies.json
    {
        "model": "movies.movie",
        "pk": 1,
        "fields": {
            "title": "Act why team bag tell over smile themselves.",
            "overview": "Once feeling according. Follow several Republican best about accept.\nAgency play what report. Know sound shoulder small.",
            "release_date": "1978-01-22T12:48:49Z",
            "poster_path": "New fish right agreement night. Create name yet smile pay west.\nEvent cause method exist detail new. Fire stand happen focus allow eye.",
            "actors": [
                6
            ]
        }
    },
    ```

  + 우리의 경우, movie model의 field에 actors를 안적고, actor model에 역참조로 movie 적었어서, 코드 실행 못했엇음



### (2) serialiers.py

+ serialiers.py

  + 역참조매니저를 class fileds로 선언해주면, Meta에도 넣어줘야 함

    ```python
    class MovieSerializer(serializers.ModelSerializer):
        review = ReviewListSerializer(many=True, read_only=True)  # 이거 역참조 manager임
        class Meta:
            model=Movie
            fields = ('actors','reviews',)
    ```

    



### (3) 협력과정

+ master와 동기화(pull)

+ branch 생성

  + ```bash
    $ git swtich -c branchname
    ```

+ 작업하기

+ 작업끝나면 branch 에 push

  + ```bash
    $ git add .
    $ git commit -m "commit name"
    $ git push origin branchname
    ```

+ 그 후 master branch로 이동

  + ```bash
    $ git switch master

+  원격저장소 master와 동기화

  + ```bash
    $ git pull origin master
    ```

    





### (4) PUT 은 ID, FOREIGN KEY 변경 못함

+ 변경해서 요청해도, 변경되지 않음. 에러는 안뜸





### (5) id값이 아닌 name이나 title 출력

```python
# serializers.py

#--------------------------Review 출력할 대, movie field가 movie id가 아니라 movie title로 출력------
class MovieReviewRelatedField(serializers.RelatedField):  # 추가된 class
    def to_representation(self, value):
        return {'title : %s'%(value.title)}
    
class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieReviewRelatedField(read_only=True)   # 추가
    class Meta:
        model=Review
        fields = '__all__'
        read_only_fields = ('movie',)
        
class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieReviewRelatedField(read_only=True)    # 추가
    class Meta:
        model=Review
        fields =('title','movie',)        
        
#--------------------------------------------------------------------------------
    
    
    
#----------------- Movie 출력할 때, actors field가 actor id가 아니라 actor name으로 출력되도록------
class ActortoMovieField(serializers.RelatedField):
    def to_representation(self, value):
        return {'name : %s'%(value.name)}
    
    
class MovieSerializer(serializers.ModelSerializer):
    actors = ActortoMovieField(read_only=True, many=True)    
    review = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model=Movie
        fields = ('title','actors','review',  
#-------------------------------------------------------------------------------
```







## [2] 느낀점

+ 집단 지성의 위대함을 알았습니다.
+ 너무 오랜시간 하다보니, 오히려 더 헷갈려지는 상황이 발생했습니다. 쉴 때 정리해가면서 해야할 것 같습니다.
+ 함께 하니까 어려운 부분에서도 힘을 낼 수 있었습니다.
+ 하면 할 수록 어렵습니다.

