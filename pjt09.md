[toc]

# 구글 로그인하는 방법

## library

+ Django Library : allauth





## 코드

### [1] settings.py

```
INSTALLED_APPS = [
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',            # 이거 쓰면 반드시 SITE_ID 지정해야함

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    ... ]
SITE_ID = 1
```







## 주의사항

+ `'django.contrib.sites' ` 사용시, `SITE_ID=1(다른숫자도가능한듯)` 설정필요

+ Oauth2 검색해서 로그인이 되는 원리 파악하기
+ GCP
  + oaUTH 동의화면
    + 실제 서비스 할 때는 다 적어줘야 함.
  + 사용자 인증 정보
    + 사용자 인증정보 -> OAuth 클라이언트 ID 만들기 -> 
    + 승인된 리디렉션 URI(워드 6번)
      + http://127.0.0.1:8000/accounts/google/login/callback/
    + 만들기 클릭
    + 결과
      + 클라이언트 id 
        + 694737255622-9v0va27tbc4mu4p3bpofgf4cnou8cnmu.apps.googleusercontent.com
      + 클라이언트 보안 비밀번호
        + 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
  + Django 과정
    + template root 추가
    + accounts/login.html 에서 구글로그인 되도록 수정(Social account Tag in Template tap)
      + https://django-allauth.readthedocs.io/en/latest/templates.html#account-tags
    + **SOCIALACCOUNT_LOGIN_ON_GET (=False)** 를 True로 settings.py에 SITE-ID 아래에  = True 해주기 (필수아님)
      + `SOCIALACCOUNT_LOGIN_ON_GET=True`
    + 오늘은 movies/views.py 채우는 것이 핵심
      + paginator 는 `from django.core.paginator import Paginator`
        + views.py 에는 위의 예시코드 복붙
        + index.html에는 bootstrap5 로 예쁘게 만들기





+ api_view, Response 있어야 DRF 사용가능 in views.py













# pjt 09(프로젝트 관련)


## 할일

+ community/views.py

  + like

+ movies/views.py 의

  + index
  + detail
  + recommended

+ movies/templates의

  + index
  + detail
  + recommended

  



## 문제사항

### [1] follower

+ 팔로우 클릭시 json 파일 화면이 로드되는 문제
  + profile.html 의 script block에 작성했는데, base.html에 script block을 작성하지 않았음....하



### [2] ManyToMany

+ ManyToMany 불러오는 방법 `movie.genres.all()`

  + ```python
    # movies/models.py
    # 모델이 이런 경우, Movie에서 Genre 가져오려면
    class Genre(models.Model):
        name = models.CharField(max_length=50)
    
    class Movie(models.Model):
        title = models.CharField(max_length=100)
        release_date = models.DateField()
        popularity = models.FloatField()
        vote_count = models.IntegerField()
        vote_average = models.FloatField()
        overview = models.TextField()
        poster_path = models.CharField(max_length=200)
        genres = models.ManyToManyField(Genre)
    ```

  + 아래 처럼 불러오면 됨

  + ```html
    # movies/detail.html
    
    movie.genres.all()로 가져올 수 있음
    
    <p> genre: {% for genre in movie.genres.all %} {{ genre.name }}{% endfor %} </p>
    
    ```





## 추천알고리즘

### [1] 알고리즘

+ 유저가 장르를 선택해서, 서버에 보내면, 해당 장르의 평점이 가장 높은 영화 10개를 추천합니다.



### [2] 과정

+ movies/index.html에서 유저가 선택한 장르를 movies.views.py로 가져옴

  + 방법은 

  + index.html에서

    + form의 GET 요청으로 보내고,select tag에 **`name="user-select"`** 로하고

    + ```html
      <form action=" {% url 'movies:recommended' %}" method="GET">
          {% csrf_token %}
          <select name="user-select" class="form-select" aria-label="Default select example">
            <option selected> 추천 장르 선택 </option>
            {% for genre in genres %}
              <option value="{{ genre.name }}"> {{ genre.name }}</option>      
            {% endfor %}     
          </select>
          <input type="submit">
        
        </form>
      ```

      

  + view.py에서 아래와 같이 하면, 가져올 수 있음

    + ```python
      @require_http_methods(['GET'])
      def recommended(request):
          genre = request.GET.get('user-select') #드라마
          # print(genre)
          genre_id = get_object_or_404(Genre, name=genre).id
          # print(genre_id)
          movies = Movie.objects.filter(genres=genre_id).order_by('-vote_average')[:10]
          context = {
              'movies':movies,
              'genre' : genre
          }
          return render(request, 'movies/recommended.html', context)
      ```

      



