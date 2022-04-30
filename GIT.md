# GIT



## Undoing things

### (1) restore



+ Undoing things
+ reset & revert
+ Git workflow
+ 페어 프로그래밍 안내























# Forking Workflow

+ repo의 소유권이 없는 경우로, 오픈소스에 주로 해당



## 1. 과정

+ 원본저장소 (A:upstream), 복사본저장소 (B:origin), 내 작업공간 (C)



+ 원본(A)을 복사(B) (상단의 **Fork button**으로 복사)
  + Forked 된 repo는 원본에 push 가능
+ 복사(B:origin)한 것을 clone 받음(C : 내가 작업하는 곳)
+ C에서 원본(A)을 upstream이라는 이름으로 remote  
  + `$ git remote add upstream [원본 URL]`
+ 작업시작
  + 브랜치 바꾸기 : `$ git switch -c feature/login`
  + 바꾼 브랜치에서 작업
+ 복사(B) 로 내가 작업한 것 (C) 를 push
  + `$ git push origin feature/login`
+ 복사본(B:origin)에서 원본(A:upstream)으로 pull request 보내기
+ pull request가 원본(A:upstream)에 반영(merge)된다면, C의 B(origin) branch를 연결 삭제
+ C에서 A(origin)에 remote upstream 해놨으므로, 원본(A) 에서 내작업공간(C)으로 내용 가져오기
  + `$ git switch master`
  + `$ git pull upstream master`







+ 내 저장소로 fork
+ fork 한 것을 clone
+ 브랜치만들고 개발하고 fork한 곳으로 push
+ PR(PULL REQUEST, MERGE REQUEST) 만들고 보내기







# 프로젝트 진행

가상환경 설정 및 패키지 설치 & django 프로젝트 생성 & 로컬 저장소 생성

```bash
# pjt 번호에 맞게 폴더 생성 (ex. pjt06)
$ mkdir pjt번호
$ cd pjt번호

# 가상환경 생성, 활성화 및 패키지 설치
$ python -m venv venv
$ pip install -r requirements.txt

# .gitignore(https://gitignore.io) 및 README 파일 생성
$ touch .gitignore README-김싸피.md README-이싸피.md README.md

# 프로젝트 생성
$ django-admin startproject pjt번호 .

# 원격 저장소 생성 및 push
$ git init
$ git add .
$ git commit -m 'First commit'
$ git remote add origin <REMOTE-URL>
$ git push origin master
```


