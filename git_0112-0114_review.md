[toc]

# 1. CLI 기초

+ CLI(Comand Line Interface)는 명령어를 이용하는 인터페이스이다.
  + 예 : cmd, Git-bash
+ GUI(Graphic User Interface)는 그래픽으로 보여주는 인터페이스로, 눈으로 보고 클릭이 가능하다.
+ Git-bash 는 Window에서 Unix 명령어를 쓸 수 있게 해주는 인터페이스이다.
  + 이를 통해, 명령어를 통일해서 사용할 수 있다.



## 1-1 Git-bash

+ 디렉토리
  1. 루트 디렉토리(Root directory) : ```/ ```로 표기
     + 모든 파일과 폴더를 담고 있는 최상위 폴더
     + Window 경우 보통 C Drive
  2. 홈 디렉토리(Home directory) :  ``` ~``` 로 표기
     + Tilde(틸드) 라고도 부르고, 현재 로그인 된 사용자의 홈 폴더
     + Window 경우 C:/users/ 현재사용자계정
  
+ 경로
  1. 절대 경로
  2. 상대 경로
     + ./ : 현재 작업하고 있는 폴더
     + ../ : 현재 작업하고 있는 폴더의 부모 폴더

+ 터미널 명령어

  | 명령어 | 설명 | 예시 |
  | ---- | ---------------------------------- | ---------- |
  | touch | sddsssssssssssssssssssssssssssssssssssssss | dsdddddd |
  | mkdir |      | ds |
  | ls |      | ds |
  | mv |      | d |
  | cd |      | sd |
  | rm |      | sd |
  | start / open |      | sd |
  | 방향키 |      |      |
  | tab |      |      |
  | ctrl + a |      |      |
  | ctrl + e |      |      |
  | ctrl + w |      |      |
  | ctrl + l |      |      |
  | ctrl + insert |      |      |
  | shfit + insert |      |      |







# 2. Git -1 : 저장소 연결과 상호작용

* 분산 버전 관리 시스템이다. 서버와 각 컴퓨터가 모두 파일을 가지고 있다.
* 장점
  * 분산식 / 버전 관리 용이 / 매일 공부한 것 보여줄 수 있음



## 2-1. 명령어

|명령어   | 설명  | 예시   |
|-------------------------------------|----------------|--------------|
| git init |||
| git add |||
| git commit |||
| git status |||
| git log |       | git log -all --graph --oneline      |
| git remote add <원격저장소 이름> <원격저장소 주소> ||git remote add origin https://github.com/jisy2718/TIL.git|
| git remote rm <원격저장소 이름> ||git remote rm origin|
| git remote -v|||
| git push <원격저장소 이름> <브랜치이름> |||
| git pull   |||
| git clone <원격저장소 주소> ||git clone https://github.com/jisy2718/TIL.git|


## 2-2. 로컬 저장소(git) 관리

```git-bash``` or ```vs code```를 이용해서 진행한다.



* 한 눈에 보기

(my local) 로컬 컴퓨터의 폴더

&darr;    &larr; ```git init```

(git) working directory에서 해당 폴더 관리

&darr;    &larr; ```git add .``` or ```git add filename```

(git) staging area로 해당 file 넘김 

&darr;    &larr; ```git commit -m "commit name"```

(git) commit 으로 staging area의 파일들 넘김







## 2-3. 원격 저장소(github) 연결하기

+ case 1 : git init 후 연결하기

(git) git init이 된 상태

&darr;   &larr; ```git remote add <원격저장소 이름> <주소>```

(git) 원격저장소의 이름을 붙이고, 연결시킴



+ case 2 : 연결하고 복사하기


(git) git init 안 된 상태

&darr;    &larr; ```git clone <원격저장소 주소>```

(git) 로컬저장소(git)으로 원격저장소(github) 내용 가져오고, 원격저장소를 git remote add 함



## 2-4. 로컬(git)과 원격 저장소(github)의 상호작용

+ 원격 저장소로 보내기

​    원격저장소와 연결된 상태

    &darr;   &larr;   ```git push <원격저장소 이름> <브랜치>```

​    로컬(git)의 파일이 원격저장소(github)에 업로드 됨



+ + 만약  처음 ```push```할 때, ```git push -u origin master ```로 ```push```한다면, 이후로 해당 ```원격저장소```에 ```push```할 때 ```git push```만 하면 됨



- 원격 저장소에서 가져오기

​	원격저장소와 연결된 상태

​	&darr;    &larr;  ```git pull <원격저장소 이름> <브랜치>```

​	원격저장소(github)의 업데이트 내용을 로컬(git)에 반영



- .gitignore
  - 특정 파일 혹은 폴더에 대해 git이 관리를 하지 못하도록 지정하는 파일
  - ```.git``` 폴더와 같은 경로에 ```.gitignore```파일을 생성
  - ```.gitignore```에 추가하면, git 폴더 안의 파일 내용 수정 시나 push 할 때, 이를 다 무시하고, 수정 시에도 git status에 표기되지 않음
  - https://www.toptal.com/developers/gitignore 에서 원하는 타입 검색하면, 코드를 만들어 줌
  - 코드 예시
    - *.확장자 : 해당 확장자 전체 관리 안함
    - a.txt : 특정 파일 관리 안함
    - testfolder/ : 특정 폴더 관리 안함



## 2-5. 원격저장소에 .gitignore에 추가했어야 하는 것 push 한 경우

* ```git rm --cached filename``` : 원격저장소에 잘못 push 된 파일에 대하여 진행하면, 

  원격저장소 : 해당 파일이 삭제 /  로컬저장소 : 해당 파일이 삭제되지 않음

* ```git rm filename``` : 원격저장소와 로컬저장소 모두에서 해당 파일 삭제

​	&darr;

+ ```.gitignore```에 해당 파일명 입력하기 후 새로 ```add``` & ```commit```  & ```push```

     &darr;

+ 해당 파일이 ```.gitignore``` 반영되어, 원격저장소에서 삭제되고 업로드 되지 않음




# 3. Git - 2 : Branch & Merge (완성필요)


* 브랜치란 나뭇가지처럼 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구이다.

+ 장점

  + 브랜치는 독립공간을 형성하기 때문에 원본이 안전하다.
  + 하나의 작업은 하나의 브랜치로 나누어 진행되기 때문에 체계적인 개발이 가능하다.

  ```bash
  # 브랜치 목록 확인
  $ git branch
  
  # 원격 저장소의 브랜치 목록 확인
  $ git branch -r
  
  # 새로운 브랜치 생성
  $ git branch <브랜치 이름>
  
  # 특정 커밋 기준으로 브랜치 생성
  $ git branch <브랜치 이름> <commit id>
  
  # 특정 브랜치 삭제
  $ git branch -d <브랜치 이름>
  $ git branch -D <브랜치 이름> #(주의) 강제 삭제 (병합되지 않은 브랜치도 삭제 가능)
  
  #새로운 브랜치 생성
  $ git switch <다른 브랜치 이름>
  # 브랜치를 새로 생성과 동시에 해당 브랜치로 이동
  $ git switch -c <브랜치 이름>
  # 특정 커밋 기준으로 브랜치 생성과 동시에 이동
  $ git switch -c <브랜치 이름> <커밋 id>
  ```



### branch 연습 시나리오

```bash
$ git branch login

text.txt에 master-3 작성
$ git add .
$ git commit -m "master-4"

# login branch에 이동
$ git branch login

# test.txt에 작성한 master-4가 지워졌음을 확인한다.
# login 브랜치와 master branch는 별도의 작업공간이므로 작업내용이 유지되지 않는다.

# login 브랜치에서 커밋 생성
login 브랜치의 test.txt에 login-1을 작성
$ git add .
$ git commit -m "login-1"

# 브랜치가 login 과 master로 갈라진 것을 확인한다.
$ git log --oneline --all --graph


```

#### Merge(병합)

+ Head 를 기준으로 merge를 한다.

```bash
master branch로 head를 옮긴 후에 merge를 진행한다.
# head 옮기기
$ git branch master
$ git branch
```





## Branch

+ 원래 코드와 상관없이 독립적으로 개발을 가능하게 해줌
+ `git` 의 **버전관리를 받는 파일들만** branch 이동시 반영됨 (관리 안 받으면 생성된 거 branch 옮겨도 존재) 
+ 아래에서 `branch_name`은 브랜치 이름

```bash
$ git branch                  # 브랜치 목록 확인
$ git branch branch_name      # branch_name 이라는 branch 생성
$ git branch -d branch_name   # merge 된 branch만 삭제 가능
$ git branch -D branch_name   # 강제로 branch 삭제 가능


# branch 이동 (HEAD 이동을 의미)
$ git switch branch_name      # 해당 branch로 이동 # 해당 branch가 생성된 commit 시점으로
$ git switch -c branch_name   # branch를 새로 생성하고, 바로 이동


# checkout 과 switch 비교
## switch는 새로운 command
$ git checkout                # 역할이 2가지 : Switch branches or restore

# 브랜치 이동
$ git checkout -b branch_name
$ git switch -c branch_name
```





## Merge (병합) [문서](https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EC%99%80-Merge-%EC%9D%98-%EA%B8%B0%EC%B4%88)

+ 3가지 종류 Merge
+ 주의 사항
  + main이 되는 branch로 이동한 후, 다른 branch와 merge 해야함
  + master 는 항상 main branch
+ merge가 된 branch는 역할이 끝났다고 생각하고, 삭제해줘야

```bash
$ git merge branch_name        # branch_name branch를 병합
```



### (1) fast-forward

+ 뒤의 branch를 앞의 branch로 이동 (HEAD가 앞으로 나갈 뿐)
+ master가 과거에 변하지 않고 있을 때, 앞의 branch로 master 이동

+ 최신 commit을 가리키는 branch A와 과거 commit 가리키는 branch B 있을 때, B에서 fast-forward merg 하면 branch B 가  branch A가 가리키는 commit을 가리키게 됨

+ 아래의 상태에서 master에서 merge 진행

  ![fast-forward](https://git-scm.com/book/en/v2/images/basic-branching-4.png)

```bash
$ git merge branch_name(hotfix)       # 현재 main branch와 병합할 branch_name
```

+ fast forward 결과

![after fast forward](https://git-scm.com/book/en/v2/images/basic-branching-5.png)





### (2) 3-way merge (merge commit)

+ 3가지의 commit을 이용해서 merge 진행
  + 2개의 commit이 공통의 조상을 기준으로 merge

![3way merge](https://git-scm.com/book/en/v2/images/basic-merging-1.png)

```bash
$ git merge branch_name(iss53)
```





+ merget 결과 commit 생성 됨

![3waymergeresult](https://git-scm.com/book/en/v2/images/basic-merging-2.png)





### (3) Merge conflict

+ Merge 했을 때, 충돌해서 git이 손 쓸 수 없고, 사용자가 직접 수정해야 함
+ merge 하는 두 브랜치에서 같은 파일의 같은 부분을 동시에 수정하고 merge하면, git은 해당 부분을 자동으로 merge 해주지 못함
+ 반면 동일 파일이라도, 서로 다른 부분을 수정했다면 conflict 없이 자동으로 3-way-commit(merge commit)이 됨

+ 충돌 발생 시 command print된 것으로도 볼 수 있지만 `git status`로도 확인 가능 (Unmerged paths/both-modified)
+ Accept Current Change / Accept Incomming Change / accept Both Change / Compare Changes
  + 위의 것들 선택하거나, 손수 작성하면 됨
  + 그 후 `$ git add  .`
+ `$ git add .` 후에  `$ git commit` 실행하면 자동으로 commit name 설정됨 (VIM 화면 나옴)
  + Merge 된 branch의 이름이 주황글씨로 맨 위에 나옴
  + ESC 후 최하단에 : 입력하면 명령어 입력
    + wq 후 enter 하면 commit 잘 저장되고 끝난 것

## undoing, workflow





## 참고코드

```BASH
$ code .   # VS 코드 실행
$ git log
$ git log --oneline  # log 간략하게 출력
$ git log --oneline  # 이전 시점의 branch로 돌아가면, 해당 시점의 log를 보게됨(HEAD가 가리키는 최신 commit 상태를 보게됨).
$ git log --oneline --all          # 이전 시점의 branch로 돌아가도, 모든 log를 보게됨.
$ git log --oneline --all --graph  # branch와 commit 전체를 볼 수 있음
```





## 참고사항

```bash
HEAD -> master  # HEAD 는 우리가 현재 있는 곳
```

