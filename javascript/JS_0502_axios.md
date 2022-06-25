[toc]



# AJAX



## [1] XML & JSON

+ 둘 다, 데이터를 표현하는 방법
  + 데이터를 표현하는 방법의 예
    + Table, Excel, dictionary(recode 1줄===1개 객체) & array(전체 dictionary묶기) )
    + XML CONVERTER 로 확인해보기

### (1)XML

+ eXtended Markup Language



#### (a) 개발자도구 : XML 확인

+ 개발자 도구 -> console -> 설정 -> Log XMLHttpRequests

  + console에서 XML log의 POST, GET 자료 볼 수 있음

  + 검색 시 자동완성 되는 검색어 데이터 요청과 응답 볼 수 있음

  + 지도에서 이동할 때마다, 요청과 응답 확인 가능

    

+ Network tap

  + `search?q=` 로 시작하는 파일보면, 자동완성 검색어 데이터 볼 수 있음



### (2) JSON

+ 같은 데이터를 표현하는데 써야하는 byte가 XML보다 적어서 XML에서 JSON으로 대부분 넘어옴





## [2] AJAX 특징

+ 비동기식
  + google 검색에서 자판 1개 누를 때마다, network tab에서 `search?q=` 부분이 계속 update 되면서 **연관검색어** 생김



### (1) XMLHttpRequest (= XMR)

+ XML 뿐 아니라 모든 종류의 데이터 받을 수 있음



#### (a) 예시

+ 한 번에 실행시, 데이터 응답 기다리지 않고, `consle.log()` 실행해서, 데이터 출력 안됨

```html
<body>
  <script>
  const request = new XMLHttpRequest()  // 동기식
  const URL = 'https://jsonplaceholder.typicode.com/todos/1' // 동기식

  request.open('GET', URL)  // 동기식
  console.log('start')      // 동기식
  request.send()    // 이거는 코드 실행 시킨 뒤, 다음 동작으로 넘어감(끝나는 거 안봄 : 비동기식)
  const todo = request.response   // 동기식 : reqeust.send()후에 응답 못받아 왔으면 데이터 없음
  console.log(`${todo}`)          // 동기식
  console.log('end')              // 동기식
  </script>
</body>
```















# Asynchronous JavaScript

## [1] 동기식 & 비동기식

P10 : 페이지 전체를 RELOAD(새로고침) 하지 않고서도 수행되는 비동기성

P15 : 동기식 

+ 순차적, 직렬적 Task 수행
+ 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐 (blocking)
+ JS 는 single threaded
  + 따라서 앞의 코드가 실행 완료되어야, 다음 코드가 실행



P17 : 비동기식

+ 병렬적 Task 수행
+ 요청을 보낸 후 응답을 기다리지 않고, 다음 동작이 이루어짐 (non-blocking)
+ JS 는 single threaded
  + 따라서 기다려주지 않는 방식으로 동작

|           | 동기식                                    | 비동기식                                                    |
| --------- | ----------------------------------------- | ----------------------------------------------------------- |
| Task      | 순차적                                    | 병렬적                                                      |
| 다음 동작 | 요청 보낸 후 응답 받고나서 진행(blocking) | 요청을 보낸 후 응답을 기다리지 않고 다음 동작(non-blocking) |
|           |                                           |                                                             |



## [2] 비동기식

### (1) 비동기식 사용 이유

+ **사용자 경험**
  + 비동기식 코드는 요청과 응답사이에 앱 실행을 함께 진행
    + 데이터를 불러오는 동안, 응답하는 화면을 보여줌 -> 사용자 경험 up
  + 동기식이라면 요청 보내고 응답 받고나서 앱을 실행
    + 데이터를 불러오기 전까지 앱이 멈춤 것처럼 보임





## [3] blocking & non-blocking

+ python

```python
from time import sleep

print('start')
sleep(1)  # 이게 끝날 때까지 다음으로 넘어가지 않음
print('end')

# 코드 1
import requests
URL = ""
print('start')
res = requests.get(URL).json()  # 이게 끝나야 다음 코드 실행
print('end')
```



+ JS

```JS
// python 의 코드1에 해당하는 부분의 JS 버전
<body>
  <script>
  const request = new XMLHttpRequest()  // 동기식
  const URL = 'https://jsonplaceholder.typicode.com/todos/1' // 동기식

  request.open('GET', URL)  // 동기식
  console.log('start')      // 동기식
  request.send() //---이거는 코드 실행 시킨 뒤, 다음 동작으로 넘어감(끝나는 거 안봄 : 비동기식)
  const todo = request.response   // 동기식 : reqeust.send()후에 응답 못받아 왔으면 데이터 없음
  console.log(`${todo}`)          // 동기식
  console.log('end')              // 동기식
  </script>
</body>
```





## [4] cONCURRENCY MODEL

+ Asynchronous JavaScript2 영상에 해당 부분 잘 설명 됨

+ python 은 Web API 없는 single Thread 이므로 혼자 일 다해야 함
  + 시간 함수 같은 것에서 멈춰있음





### (1) Call stack

+ 실행되는 스크립트 전체에서 1순위인 것들 모두 넣음
  + Callback Queue에 대기중인 동작이 있을 때, Call stack이 비는 순간은 모든 1순위 동작이 끝난 후임!



### (2) Web API (=== Browser API)

+ 언제 끝날지 모르는 일은 넘김
  + 시간관련, AJAX 처리
  + `setTimeout()`, `setInterval()`, `XMLHttpRequest()`, DOM events(eventListener), AJAX











# axios

+ return으로 Promise 객체



```js
// 예1 : axios는 parsing (===JSON.parse(res)) 안해도 res.data하면 data 볼 수 있음
const URL = 'https://jsonplaceholder.typicode.com/todos/'
axios.get(URL)
    .then(function(res) {
        console.log(res.data)    //이게 여기 내부에 없으면, res가 undefined뜸 (내부에 있지 않으면 응답 받기전에 실행돼기 때문에)
    })
```



```js
// 예2 : chaining + 화살표함수 = Promise의 가장 큰 장점 중 1개
const URL = 'https://jsonplaceholder.typicode.com/todos/'
axios.get(URL)  // Promise 리턴
 .then(res => res.data) 
 .then(todo => todo.title)
 .then(title => console.log( title ))
 .catch(err =>console.error(err))   // console.error()는 에러 어디서 났는지 알려줌
 .catch(err => {
   if (err.response.status === 404) {
      alert('그딴건 없다.')
      }
  })
 .finally( ()=> console.log('끝!'))
```



```js
// 예 3 : id===10 인 것 가져오는 경우의 코드
axios.get(URL)  // Promise 리턴
  .then(res => {
    const todosArray = res.data                           // 전체 가져오기
    const todo = todosArray.find(todo => todo.id === 10)  //원하는 조건 부분 찾기
    return axios.get(`${URL}${todo.id}`)                  // 원하는 것 가져오기
  })
  .then(res => console.log(res.data))
  .catch(err => {
    if (err.response.status === 404) {
      alert('그딴건 없다.')
    }
  })
  .finally(() => console.log('어쨋든 끝!'))
```











# async & await















# 새로운 표현

+ `console.error()`

+ custom attribute
  + `data-*` 꼴
  + [mdn참고](https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/Use_data_attributes#html_문법)

















P10 : 페이지 전체를 RELOAD(새로고침) 하지 않고서도 수행되는 비동기성

P15 : 동기식 

+ 순차적, 직렬적 Task 수행
+ 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐 (blocking)
+ JS 는 single threaded
  + 따라서 앞의 코드가 실행 완료되어야, 다음 코드가 실행



P17 : 비동기식

+ 병렬적 Task 수행
+ 요청을 보낸 후 응답을 기다리지 않고, 다음 동작이 이루어짐 (non-blocking)
+ JS 는 single threaded
  + 따라서 기다려주지 않는 방식으로 동작



p19 : 왜 비동기를 사용하는가?

+ 사용자 경험

  + 동기식코드라면

    + 데이터를 모두 불러온 뒤 앱이 실행(데이터를 모두 불러올 때까지는 앱이 모두 멈춘 것처럼 보임)
    + 코드 실행을 차단하여 화면이 멈추고 응답하지 않는 것 같은 사용자 경험을 제공

    

  + 비동기식 코드라면

    + 데이터를 요청하고 응답받는 동안, 앱 실행을 함께 진행함
    + 데이터를 불러오는 동안 지속적으로 응답하는 화면을 보여줘서, 더욱 쾌적한 사용자 경험 제공



# P27 JS는 Single threaded





# 일급 객체 (일급 함수)

+ 정의
  + 다른 객체들에 적용할 수 있는 연산을 모두 지원하는 객체(함수)
+ 조건
  + 변수에 할당 가능
  + 인자로 넘길 수 있음
  + 함수의 반환값으로 사용 가능
  + 



# axios

## 코드

```html
<body>
  <h1>Dog API</h1>
  <img src="" alt="dog">
  <br>
  <button>Get dog</button>

  <!-- axios CDN을 삽입한다. -->
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script>
    const API_URI = 'https://dog.ceo/api/breeds/image/random'
    const img = document.querySelector('img')
    
    // 방법 1
    function getDog() {
      // axios를 사용하여 API_URI로 GET 요청을 보낸다.
      // .then 메서드를 통해 요청이 성공적인 경우의 콜백함수를 정의한다.
      // 응답객체의 데이터에서 이미지에 대한 리소스를 img 요소의 src 속성으로 할당한다.   
      axios.get(API_URI)
        .then(response =>{ console.log(response) 
          return response.data })
        .then(data => { img.src = data.message })

 
       }
    
    // 방법2
    function getDog2 () {
      axios.get(API_URI)
      .then(response => response.data)
      .then(data => img.src = data.message )
    }
    
    const button = document.querySelector('button')
    button.addEventListener('click', getDog2)

  </script>
</body>
```





# 참고

+ Threads
  + 프로그램이 작업을 완료하기 위해 사용할 수 있는 단일 프로세스
  + 각 thread(스레드)는 한 번에 하나의 작업만 수행할 수 있음
  + 다음 작업을 시작하려면 반드시 앞의 작업이 완료되어야 함











































































































# 질문사항

+ views.py에서 `JsonResponse`  가 가는 곳

  + 자신을 호출한 곳

  + 여기서는 axios의 return으로 감

  + 그래서 만약 아래처럼 코딩하면 , login 안된 경우에, `redirect('accounts:login')` 가 axios의 return으로 가게 됨. 그래서 아래 코드를 고쳐줘야 함

    ```python
    @require_POST
    def likes(request, article_pk):
        if request.user.is_authenticated:
            #좋아요 상태라면 > 좋아요 취소
            #아무것도 안했으면 > 좋아요
            article = get_object_or_404(Article,pk=article_pk)
            if article.like_users.filter(pk=request.user.pk).exists():
                liked = False
                article.like_users.remove(request.user)
            else:
                liked = True
                article.like_users.add(request.user)
        
    
        #화면을 그리기 위해 필요한 데이터
        # 좋아요 여부, 좋아요 유저수
        # context
    
        # post요청 받았으니까.. db에 적용하고
        # 화면 구성에 필요한 데이터 만들어서 json으로 응답
            context = {
                'liked': liked,
                'count' : article.like_users.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:login')
    ```

    + 고친 코드

      ```python
      # views.py
      return redirect('accounts:login') -> return JsonResponse({'notLogin':True})
      # notLogin으로 해야하는 이유는 Login 한 경우 request.data.notLogin === undefined이고, 이는 false 이기 때문
      
      # 아래 처럼 처리해주면, 정상적으로 return JsonResponse(context) 으로 받아온 경우에는 response.data.notLogin 값이 없어서 False로 떨어짐.
      # index.html
      if (response.data.notLogin == true) {
      	alert('로그인하세요')
      	} else {
                 기존코드
                 }
      ```







+ post 요청 법

  ```js
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value  // 외우기
  
  axios({
    method:'post',
    url: `http://127.0.0.1:8000/articles/${articleId}/likes/`,  
    headers: {'X-CSRFToken': csrftoken} 
    }).then(function(response){    // response에 있는 것은 url로 요청 보낸 후 해당 url 따라간 views.py의 함수의 return 값
        console.log(response)
  })
  ```







+ `ManyToManyField` 
  + 객체 추가 제거시 `add(obj), remove(obj)` 이용