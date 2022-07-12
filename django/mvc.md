## 목차





## [1] Framework

+ 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
  + 뼈대를 가지고 작업한다고 생각하면 됨
+ 새로운 어플리케이션을 위한 코드를  다시 작성하지 않고, 재사용할 수 있음





## [2] MVC

+ Framework 구조로 Model, View, Controller
+ MVC가 생겨난 이유
  + 유지 보수가 어려웠음
    + 코드가 많아질 수록, 코드 파악하기 힘들어지고, 갈아 엎는 일이 많아졌음
    + 그래서 유지보수가 편해지는 코드 구성 방식인 MVC가 생겨남

  + 

+ 사용자 인터페이스와 프로그램 로직을 분리해, 서로 영향없이 쉽게 고칠 수 있는 애플리케이션 개발 가능
+ 

<img src="https://mdn.mozillademos.org/files/16042/model-view-controller-light-blue.png" style="width:75%;" />





### (1) Model

+ 앱이 포함해야할 데이터가 무엇인지 정의
  + 응용프로그램의 데이터 구조를 정의하고, 데이터베이스의 기록을 관리(추가, 수정, 삭제)



### (2) View

+ 레이아웃과 화면을 처리

  + 파일의 구조나 레이아웃을 정의

  + 실제 내용을 보여주는 데 사용



### (3) Controller

+ 명령을 모델과 뷰 부분으로 라우팅 함

  + HTTP 요청을 수신하고, HTTP 응답을 반환
  + Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  + view에게 응답의 서식 설정을 맡김
+ 모델과 뷰의 중개자





## [3] MVC를 지키면서 코딩하는 방법

+ Model은 Controller와 View에 의존하지 않아야 함
  + Model 내부에 Controller와 View에 관련된 코드가 있으면 안됨
+ View는 Model에만 의존해야하고, Controller에는 의존하면 안됨
  + View 내부에 Model의 코드만 있을 수 있고, Controller의 코드가 있으면 안됨
+ View가 Model로 부터 데이터를 받을 때는, 사용자마다 다르게 보여주어야 하는 데이터에 대해서만 받아야 함
  + 공통 정보는 View가 자체적으로 갖고 있어야 함
+ Controller(Django의 View) 는 Model과 View(Django의 Template) 에 의존해도 됨
  + Controller 내부에는 Model과 View의 코드가 있어도 됨
+ View가 Model로부터 데이터를 받을 때, 반드시 Controller에서 받아야 함





#### [4] MTV (Django)

+ ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fba6kUr%2FbtqLkfEHZmx%2FJOk37vnKawDkg8YruGqSEk%2Fimg.png)

[출처](https://tibetsandfox.tistory.com/16)

+ Model
  + DB에 저장되는 데이터
+ Template
  + 유저에게 보여지는 화면으로 html 파일
+ View
  + 컨트롤러에 대응되며, 요청에 따라 적절한 로직을ㄹ 수행하여, 결과를 템플릿으로 렌더링하며 응답