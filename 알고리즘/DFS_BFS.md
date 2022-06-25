## 목차

+ [BFS](#bfs)
  + [BFS 원리](#BFS 원리)
  + [BFS 코드](#BFS 코드)
+ [DFS](#dfs)
  + [DFS 원리](#DFS 원리)
  + [DFS코드](#DFS 코드)
    + [stack 버전 1](#stack 버전 1)
    + [stack 버전 2](#stack 버전 2)
    + [재귀호출](#재귀호출)



## BFS

#### BFS 원리

+ 한 곳에서 갈 수 있는 경로를 모두 찾고, 후에 순서대로 방문해서, 갈 수 있는 경로를 모두 찾는 것을 반복
  + 즉, 경로를 모두 찾고, 순차적으로 이동
+ FIRST IN FIRST OUT
+ 큐로 구현 가능



#### BFS 코드



## DFS

#### DFS 원리

+ 경로를 찾으면 바로 이동
  + 경로를 찾으면 즉시 이동(stack에 push), 경로를 찾지 못하면, 현재 경로에서 이전 경로로 돌아가서(stack에서 pop) 다시 경로를 찾음.
+ LAST IN FIRST OUT
+ 재귀 / STACK으로 구현 가능
  + 재귀를 호출하는 것은 스택에 집어넣는 것과 똑같음
  + stack으로 DFS 구현시에는 break 이용해서, 새로운 경로 발견 즉시 이동(break 안쓰는 방법도있음)
  + 하지만 재귀에서는, 재귀함수 실행이 해당 위치로 이동을 의미하므로, break 없이 경로 찾으면 함수호출 해주면 됨 / for문에서 경로가 없으면 재귀함수가 호출되지 않아서 재귀함수 호출안되고, 그럼 해당노드가 pop 되는 것



#### DFS 코드

+ ##### 공통부분

  ```python
  #--------------------- 공통으로 필요-----------------------------------------------
  N = 10
  adj = [[0]*N for _ in range(N)]
  visited = [False]*N
  path = []
  
  for i in range(N-1):
      adj[i][i+1] = 1
      adj[i+1][i] = 1
  adj[N-3][N-1] = adj[N-1][N-3] = 1 # N-3 번과 N-1번도 연결
  
  ```
  



+ ##### stack 버전 1

  ```python
  # 1. stack 이용
  stack = []
  top = -1
  top += 1 # 더 큰수로 이동
  start = 0
  stack.append(start)
  path.append(start)
  visited[start] = True
  while stack:
      cur = stack[-1]
      
      for i in range(N-1,-1,-1): # 핵시구조 1
          if adj[cur][i] == 1 and visited[i] == False:
              visited[i] = True
              stack.append(i)
              path.append(i)
              break     # 핵심구조 2
      else:
          stack.pop()   # 핵심구조 3
  
  ```

  

+ ##### stack 버전 2

  + `for-else` 문으로 `stack.append() - stack.pop()` 진행
  + `for` 에 `break` 와 `for-else` 안쓰고 하려면,  맨 위에 현재 노드 찾을 때, `stack.pop()` 하면 됨 

  ```python
  # 버전 1에서 다음처럼 바꾸면 됨
  while stack:
      cur = stack.pop()
      path.append(cur)  # 추가된 부분
      # 갈 수 있는 곳 모두 stack에 넣기
      for i in range(N-1,-1,-1):
          if adj[cur][i] == 1 and visited[i] == False:
              visited[i] = True
              stack.append(i)
              #path.append(i)
              #break
      #else:
          #stack.pop()
  
  ```

  

+ ##### 재귀호출

  ```python
  # 2. 재귀이용
  	# 함수호출이 stack에 append 하는 것이고, 함수 끝나는 것이 stack에서 pop임.
  	
      # v 번 노드에서 경로 찾기
      
      # 방문하지 않은 이동할 곳이 있으면 바로 이동
      
      # 이동할 곳이 없다면 이전 위치로 되돌아가기
  
  def dfs(v): # 이 함수 시작하면, v 번 노드로 이동한다는 의미
      visited[v] = True # v번 노드 방문 표시
      path.append(v)
      for i in range(N-1,-1,-1):
          if adj[v][i] == 1 and not visited[i]:
              dfs(i)
  dfs(0) # 0번 노드에서 길찾기 시작
  print(path)
  
  
  ```

  




