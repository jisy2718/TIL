+ 재귀를 트리형태로 이해하기

+ 연습할 것

  1. 마이클잭슨 문제

  2. branch2, level2 그려놓고 trace 연습

  3. branch2, level2에서 print 중간에 넣고 출력결과 예상해서 맞추기

  4. 원하는 branch, level 코딩, 마지막 도착마다 path 출력하는 연습

     + 각 레벨에서 들리는 branch 표기됨

     + 예
       + 00 01 10 11 에서 00은  level 0에서 0번째 branch, level1에서 0번째 branch

  5. 내가 원하는 형태로 출력 연습

  6. 주사위문제연습 (argument 추가)
     + 주사위 눈금의 합

  7. 가지치기 연습
     + 눈금의 합이 7이하가 되는 것만 출력하시오

+ 백트래킹 문제에서 고려할 것

  + level(tree 깊이), branch(1개 노드의 자식 개수)
  + 가지치기 조건들 전부

  

+ 코드

  ```python
  # 1.마이클잭슨
  def run(n):
      print(n, end='')
      if n==0:
          return
  
      run(n-1)
      print(n, end='')
  run(5)
  #54321012345
  
  
  # 1. trace 연습
  def run2_prof(n):
      if n == 17:
          print()
          return
  
      print(n, end='')
      run2_prof(n+2)
      print(n, end='')
  run2_prof(3)
  
  
  # 2. trace 연습
  def run3(n):
      if n==2:
          return
  
      for i in range(2):
          print(n, end='')
          run3(n+1)
          print(n,end='')
  run3(0)
  
  
  # path 연습
  path=[0]*4
  def run4(level):
      if level==2:
          for i in range(level):
              print(path[i], end='')
          print()
          return
  
      for i in range(2):
          path[level] = i
          run4(level+1)
          path[level] = 0
  run4(0)
  
  
  
  # 4. path 연습
  path =[0]*4
  def run5(level):
      if level==4:
          for i in range(level):
              print(path[i], end='')
          print()
          return
  
      for i in range(3):
          path[level] = i+1
          run5(level+1)
          path[level] = 0
  run5(0)
  >>> 
  1111
  1112
  1113
  1121
  1122
  1123
  1131
  ...
  2121
  2122
  2123
  ...
  3313
  3321
  3322
  3323
  3331
  3332
  3333
  
  
  
  
  # 6. 주사위문제
  path =[0]*10
  n = 3
  def bbq(level, sum):
      global path, n
      if level==n:
          for i in range(level):
              print(path[i], end=' ')
          print("=" + str(sum))
          return
  
      for i in range(6):
          path[level] = i+1
          bbq(level+1, sum+i+1)
          path[level] = 0
  bbq(0,0)
  ```

  

