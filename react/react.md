[toc]

## 목차

+ [1.코딩애플](#1.-코딩애플)
  + [기초0강](#[1]-기초-0강)
  + [기초1강 - 설치 및 세팅](#[2]-기초-1강-:-설치-및-세팅)
    + [(3) 궁금증 해소](#(3)-궁금증-해소)
  + [기초 2강 - JSX](#[3]-기초-2강-:-JSX)
  + [기초 3강 - state](#[4]-기초-3강-:-state)
  + [기초 4강 - 이벤트리스너](#[5]-기초-4강-:-이벤트리스너)



+ [참고](#[99]-참고)



# 1. 코딩애플



## [1] 기초 0강

+ React 쓰는 이유 및 특징

  + 앱 만들기, 발행하기 쉽고, UX적으로 뛰어남

  + 2020 이후로, class 없어져서 만만해짐

  + JS 기초지식 필요

    + 기초지식 없으면 어려움

      

+ 강의 목적

  + 혼자서도 잘하는 사람 양성하는 커리큘럼
  + 있어보이는 실전 프로젝트 제작
    + 쇼핑몰 & 블로그



### (1) Web-app의 장점

+ 모바일앱으로 발행이 쉬움
+ 앱처럼 뛰어난 UX
+ 그냥 웹사이트보다 비즈니스적 강점



### (2) 필요사전지식

+ var, let, const, if else, for, function return, array object, addEventListener, HTML/CSS



## [2] 기초 1강 : 설치 및 세팅

+ 에러나는 경우 참고 [링크](https://codingapple.com/unit/react1-install-create-react-app-npx/?id=2305)

### (1) 설치과정

+ Node.js 최신버전 설치
+ visual studio code(에디터) 설치
+ open folder
+ 에디터의 터미널열어서 npx create-react-app 프로젝트명 입력
+ 방금 생성된 프로젝트명 폴더를 에디터로 오픈 해서 src > App.js에서 코드짜면 되고
+ **미리보기** 띄우려면 터미널 열어서 `npm start` 하면 됨



### (2) 블로그 생성 프로젝트

+ `npx create-react-app blog`

  + `npx` : 라이브러리 설치 도와주는 명령어(nodejs 설치 되어 있어야 이용가능)
  + `create-react-app` : react setting 다 된 boilerplate 만들기 쉽게 도와주는 라이브러리
  + `blog` : blog라는 이름의 react project

  





### (3) 궁금증 해소

+ Node.js 설치 이유
  + 설치 이유는 [create react app](https://create-react-app.dev/) 이라는 라이브러리 사용하기 위해서
  + 또한 Nodejs 설치하면 npm 이라는 툴 이용 가능

+ 생성된 react app

  + App.js

    + App.js는 메인페이지에 들어갈 HTML 짜는 곳

    + 실제 메인 페이지는 public > index.html 임

    + src > index.js가 App.js 의 내용을 public > index.html에 반영되도록 해줌 

      + ```js
        // index.js
        // id가 root인 div 태그에다가, App.js의 모든 내용 넣어주세요
        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(
          <React.StrictMode>
            <App />
          </React.StrictMode>
        );
        ```

        

  + node_modules
    + 설치한 라이브러리 모두 모은 폴더
      + creat react app 실행 위해서는 수많은 라이브러리 필요
  + public
    + static 파일 보관함
    + public 폴더에 넣으면 빌드, 배포할 때 압축되지 않고, 그대로 있음
  + src
    + 소스코드 보관함
    + APP.js 에 작성
  + package.json
    + 내가 설치한 라이브러리의 이름과 버전을 다 모아둠
      + npm으로 설치할 때마다, 자동으로 update 됨
  + 









## [3] 기초 2강 : JSX

### (1) App.js 작성

+ 함수 return 부분에 그냥 HTML 작성하면 됨 (HTML 처럼 보이지만 사실 JSX임)

  + ```JS
    function App() {
      return (
          여기에 그냥 다 작성하면 됨
        <div className="App">
          
        </div>
      );
    }
    ```



### (2) 작성법(JSX)

+ class 넣을려면 JSX는 `class` 못쓰고, **`className` 써야함**

  + style은 App.css에 넣어주면 됨

+ **데이터 바인딩**

  + `{}` 쓰고, 변수 넣으면 됨

    + src, id, href, className 등의 속성에도 가능

  + 아래는 데이터 바인딩 (이미지 넣기, 함수값 넣기, 변수 넣기) 3가지 예

    + ```js
      import logo from './logo.svg';   // logo.svg를 넣고 싶다.
      import './App.css';
      
      function App() {
      
        let posts = '강남 고기 맛집';  // 서버에서 가져온 데이터라고 칩니다.
        
        // 비교 1: 전통적 js 데이터 바인딩
        //document.getElementById().innerHTML = ''? 와 같이 했어야 함
      
        function 함수(){
          return 100
        }
        
        return (
          <div className="App">
            <div className="black-nav">
              <div> 개발 Blog </div>
            </div>
            <img src={ logo }></img>  // 이미지 바인딩해서 넣기
            <h4> 블로그 글 </h4>      
            <h4> { posts } </h4>     // 변수 바인딩해서 넣기
            <h4> { 함수() } </h4>    // 함수값 바인딩해서 넣기
          </div>
        );
      }
      
      export default App;
      
      
      ```

    + 

+ style 속성 집어 넣을 때

  + 아래 처럼은 불가

    ```html
    <div style="font-size : 16px"> </div>
    ```

    + js에서 쓸 수 있는 민감한 기호들이 많아서, 위처럼은 불가

  + 무조건 `{}` 안에 object 형식으로 넣어주면 됨

    + ```html
      # 방법 1
      <div style={ {color : 'blue', fontSize : '30px'} } > </div>
      
      # 방법 2
      let posts = {color : 'blue', fontSize : '30px'}  ( return 위쪽에 적기)
      <div style={ posts } > </div>
      ```

    + 





## [4] 기초 3강 : state

+ 코드 [링크](https://codingapple.com/unit/react-3-state-usestate-hook/?id=2305)

+ **자주 바뀌고, 중요한 데이터는 state에 저장**

  

### (1) 데이터 저장

#### (a) 저장 방법

+ 변수에 저장

+ state 만들어서 저장

  + ES6 destructuring 문법 이용

    + ```js
      let [글제목,글제목변경] = useState('남자 코트 추천'); // 이렇게 코딩하면 이 자리에는 array가 남음 [a=남자코트추천,b=state정정해주는함수] 꼴
      ```

#### (b) state 사용법

+ state 는 변수 대신 쓰는 데이터 저장 공간

+ `useState()`를 이용해 만들어야 함

  + `useState() 는 [a,b]` 꼴로 저장됨

  + 문자, 숫자, array, object 모두 저장 가능

  + ```js
    import { useState } from 'react';
    
    import './App.css';
    
    function App() {
      // ES6 destructuring 문법
      // array안의 [10,100] 두 개의 데이터를, 두 개의 변수에 답고 싶으면 아래 처럼 하면 됨.
      // 원래 useState('남자 코트 추천') 은 ['남자 코트 추천', 함수] 임
      let [글제목,글제목변경] = useState('남자 코트 추천');  // 이렇게 코딩하면 이 자리에는 array가 남음 [a=남자코트추천,b=state정정해주는함수] 꼴
      
      return (
        <div className="App">
          <div className="black-nav">
            <div> 개발 Blog </div>
          </div>
    
          <div className="list">
            <h3> { 글제목 } </h3>
            <p> 2월 17일 발행</p>
            <hr/>
          </div>
    
        </div>
      );
    }
    
    export default App;
    ```

  + ```js
    let [글제목2, 글제목변경2] = useState(['남자 코트 추천','최고']) 이렇게 한다면
    <h3> { 글제목2 } </h3> => 남자 코트 추천최고  로 나옴
    <h3> { 글제목2[0] } </h3> => 남자 코트 추천
    <h3> { 글제목2[1] } </h3> => 최고
    ```

+ 





#### (c) state 쓰는 이유

+ 웹이 App처럼 동작하게 만들고 싶어서
  + App처럼 동작하게 하려면, 자주 변경되는 모든 데이터를 state로 저장해야함
+ **state를 담고 있는 데이터가 바뀌면, HTML이 자동으로 재렌더링 됨**
  + 제목 정렬이나 제목 수정 등의 데이터 조작시 새로고침 없이 재렌더링 됨
  + 그냥 변수에 넣은 데이터가 바뀌면, 새로고침 해야 재렌더링 됨





## [5] 기초 4강 : 이벤트리스너



### (1) 좋아요 버튼













## [99] 참고

+ 문법 권장 사항 잡아주는 거 안하려면
  + App.js 제일 상단에 `/* eslint-disable */` 입력
  + eslint라는 기본으로 설치된 것이 문법 잡아주는데, 그거 안한다는 것
