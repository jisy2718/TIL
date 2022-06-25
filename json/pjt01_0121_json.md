# project 1

## 1. 진행한 상황

### [1] problem_a

+ 쇼생크탈출에 대한 영화 정보가 담겨있는 ```./data/movie.json``` 파일로부터, 쇼생크탈출 영화의 

  **id, title, poster_path, vote_average, overview, genre_ids(숫자형)** 정보를 뽑아내어 출력하였음.



### [2] problem_b

+ 쇼생크탈출에 대한 영화 정보가 담겨있는 ```./data/movie.json```  파일로부터, 쇼생크탈출 영화의 

  **id, title, poster_path, vote_average, overview, genre_ids(숫자형)** 정보를 뽑아냄.

  이후 **genre_ids(숫자형)** 의 값에 대응되는  **genre_names(문자형) ** 정보가 있는```./data/genres.json``` 파일로 부터 **genre_ids(숫자형)**  정보를 **genre_names(문자형)** 정보로 바꾸어서  쇼생크탈출의 **id, title, poster_path, vote_average, overview, genre_ids(문자형)** 정보를 출력하였음.

  

### [3] problem_c

* 20개의 영화에 대한 정보가 담겨있는 ```./data/movies.json``` 파일로부터, 위의 **problem_b**의 과정을 반복하여, 20개 영화의 정보를 모두 출력하였음.



### [4] problem_d

+ 20개의 영화에 대한 정보가 담겨있는 ```./data/movies.json``` 파일과 

  각 영화별 **수익 정보(revenue)**가 담겨있는  ```./movies/id.json``` (각 영화의 **id**가 json 파일로 저장되어 있음) 꼴의 20개 파일들로 부터

  각 영화별 수익 정보(revenue)를 비교하여, 수익이 가장 높은 영화 **title(제목)**을 출력하였음.



+ ```./data/movies.json``` 파일(A)의 **id** 를 이용하여, 각 영화의```./movies/id.json``` 파일(B)을 열어,  ```./movies/id.json``` 파일(B)의 **title, revenue** 정보를 가져와야 했음.

  따라서 

  1. 파일(A)에서 각 영화의 **id** 존재여부, 
  2. 해당 **id**에 해당하는 파일(B)의 존재유무,
  3. 파일(B)가 존재할 때, **title, revenue** 정보의 존재유무  

  를 고려하여 함수를 구현하였음



### [5] problem_e

+ **problem_d**와 같은 방식인 함수를 구현하였음

  하지만 이 문제의 경우 ```./movies/id.json``` 파일들로부터 **개봉일 정보(release_date)**를 가져와서,

  12월에 개봉하는 영화들의 리스트를 반환하는 함수를 구현하였음



## 2. 사용한 데이터

1.  ```./data/movie.json``` : 쇼생크탈출 영화에 대한 **adult, backdrop_path, genre_ids, id, original_language, original_title, overview, popularity, poster_path, release_date, title, video, vote_average, vote_count** 정보를 담고 있음

   

2. ```./data/movies.json``` : TMDB기준 평점이 높은 20개의 영화에 대해서 1. 과 같은 종류의 정보를 담고 있음

   

3. ```./data/genres.json``` : **genre_ids(숫자형)**과 이에 대응되는 **genre_ids(문자형)** 정보를 담고있음

   

4. ```./movies/id.json``` : ```id```에는 각 영화의 ```id```가 숫자로 들어가는 형식으로 20개 영화에 대해서 각각 파일이 존재하여 총 20개의 파일이 존재

   

   각 파일은 **adult, backdrop_path, belongs_to_collection, budget, genres, homepage, id, imdb_id, original_language, original_title, overview, popularity, poster_path, production_companies, production_countries, release_date, revenue, runtime, spoken_languages, status, tagline, title, video, vote_average, vote_count**에 대한 정보를 담고 있음

   

   ```./data/movie.json```과 비교하여 **belongs_to_collection,  budget,  genres,  homepage, imdb_id, production_companies, production_countries, revenue, runtime, spoken_languages, status, tagline** 정보를 더 담고 있고, **genre_ids** 에 대한 정보가 없음

   

## 3. 배운 점

* ```try-except```를 사용해 보고, 어떤 상황에서 사용하는지 경험함
* ```continue```를 사용해 보고, 어떤 상황에서 사용하는지 경험함
* 코드를 짤 때, 세부적인 예외를 고려하는 데에서 시간이 많이 든다는 것을 몸소 경험함
* 세부적인 예외를 고려하기 위해서는, 문제를 구조화하는 것이 중요하다는 것을 느낌

+ 좀 더 일반화 될 수 있도록, 코드를 짜는 것이 재미있었음

+ json 파일을 python으로 읽는 방법

  ```python
  import json
  # __name__ == '__main__' 의 경우, 스크립트 파일이 메인으로 동작할 때와 모듈로 사용될 때를 구분
  if __name__ == '__main__':
  	read_json = open(filename, encoding='UTF8')
  	trans_dict = json.load(read_json) # trans_dict에 dictionary 형태로 데이터가 저장됨
  ```

  + ``` __name__```(모듈의 이름이 저장되는 변수)에는 ```import```로 가져온 모듈의 이름이 저장됨
  + python 인터프리터가 최초로 작동시킨 스크립트 파일의 ```__name__```에는 ```__main__```이 저장됨

