[toc]

# Django HW&WS


## 0419 (DB-05)

### HW : 1, 3, 4, 5, 6, 7, 8, 10



## 0420 (Django-09 REST Framework 1)

### HW : 1, 2, 3, 4

### WS : `return Response(serializer.data)` 의 개발자모드 Response type이 html로 나오는 이유





## 0421 (Django-10 REST Framework 2)

### HW : 1, 2, 3

### WS























# JS HW&WS

## 0425 (JS - 기초1)

### HW



## 0426( JS - 기초2)

### HW : 1-1, 1-3, 2

###  WS :  회문 / str.split('') / arr.reverse() / arr.join(' ')





## 0427( JS - 기초3)

### HW : 1, 2-2, 2-3, 2-4

###  WS : 1 -  a tag 속성 / 2 - create, append / 3 - innertext 위치

+ 1 번

+ ```js
    <a id="anchor" href="">GOOGLE</a>
    <script>
      /*
        JavaScript 코드만을 활용하여 a#anchor 요소를 아래와 같이 수정합니다.
          1) a 태그에 text-decoration-none 클래스를 추가합니다.
          2) a 태그의 href 속성은 https://google.com/ 입니다.
          3) a 태그의 target 속성은 _blank 입니다. (새 탭에서 열기)
      */
     const google = document.querySelector('#anchor')
     google.setAttribute('href','https://google.com/')
     google.setAttribute('target','_blank')
    </script>
  ```

+ 2번

  + ```html
     <div id="app"></div>
      <script>
        // div#app 요소 선택
        const app = document.querySelector('#app')   
        // h1 태그를 createElement 로 생성
        const h1Tag = document.createElement('h1')
      
        // 생성한 h1태그의 내용을 '오늘의 Todo' 로 설정
        h1Tag.innerText = '오늘의 Todo'
      
        // ul, li 태그들을 생성 및 내용 추가
        const ulTag = document.createElement('ul')
        const il1 = document.createElement('li')
        const il2 = document.createElement('li')
        const il3 = document.createElement('li')
      
        il1.innerText = '양치하기'
        il2.innerText = '공부하기'
        il3.innerText = '휴식하기'
        
        // 각 태그들을 적절하기 div#app 요소에 자식요소로 추가. (#app > ul > li)
        app.append(h1Tag)
        app.append(ulTag)
        ulTag.append(il1, il2, il3)
      </script>
    ```

+ 3번

  + ```js
        const cardsSection = document.querySelector('#cardsSection')
    
        function createCard(title, content) {
          // 여기에 카드를 작성하시오.
          // 1. 요소생성
          const article = document.createElement('article')
          const div1 = document.createElement('div')
          const div2 = document.createElement('div')
          const h5 = document.createElement('h5')
          const p = document.createElement('p')
          
          // 2. 값넣기
          article.setAttribute('class', 'col-4')
          div1.setAttribute('class','card m-1')
          div2.setAttribute('class','card-body')
          h5.setAttribute('class', 'card-title')
          p.setAttribute('class','card-text')
          
          h5.innerText = title
          p.innerText = content
    
          // 3. 자식관계
          article.append(div1)
          div1.append(div2)
          div2.append(h5)
          h5.append(p)
    
          //-----------------------왜 여기에 넣으면 제대로 추가 안되는가?-----------
          // h5.innerText = title
          // p.innerText = content
    
    
          return article
        }
    
        // 카드 생성
        const newCard = createCard('Hello', 'World')
    
        // DOM에 추가
        cardsSection.appendChild(newCard)
    ```

  + 
