[toc]

# 서로소 집합

## [1] 정의 및 활용

### (1) 정의

+ 교집합이 없음
+ 집합에 속한 하나의 특정 멤버(대표자)를 통해 각 집합들을 구분

### (2) 활용

+ 부모-자식 관계만 주어질 때, 이게 몇 개의 트리인가 판단
  + 대표자(root)의 개수를 세면 됨
+ MST 구할 때, kruscal 알고리즘에서 사용



## [2] 표현과 연산

### (1) 표현

+ **하나의 집합을 하나의 트리로 표현**
  + 자식노드가 index / 부모 노드가 value인 트리로 표현
+ 집합의 대표자

  + 루트노드



### (2) 연산

+ Make-set(x) 
  + x를 대표로하는 {x} 집합 생성
+ Find-Set(x)  
  + x를 포함하는 집합의 대표자(root) 찾기
+ Union(x,y) 
  +   x 집합의 대표 원소(root)를, y집합의 대표 원소(root)가 가리키게 함
  + 즉, x 집합의 root를 root로 해서, 두 개의 트리를 합침



### (3) 연산 예시

| 연산                                                         | index    | 1    | 2    | 3    | 4    | 5    | 6    |
| ------------------------------------------------------------ | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
| make_set(1)~(6)                                              | p =      | 1    | 2    | 3    | 4    | 5    | 6    |
| union(1,3)                                                   | p =      | 1    | 2    | 1    | 4    | 5    | 6    |
| union(2,3) <br />3의 대표원소 y 찾아가서,<br /> y의 대표원소를 2의 대표원소 x로 교체 | p =      | 2    | 2    | 1    | 4    | 5    | 6    |
| union(5,6)                                                   | p =      | 2    | 2    | 1    | 4    | 5    | 5    |
| findset(6)                                                   | 5 return |      |      |      |      |      |      |





## [3] 구현 코드

```python
# 1. Make set
N = 6
p = [x for x in range(N+1)] # 스스로가 root(대표자) 가 되도록 초기화

# 2. find set
# 특정 노드 x의 대표자(root) 노드 반환
def find_set(x):
    # 구현 1
    while p[x] != x: # 자기 자신이 부모가 아닌 경우, 부모로 이동
        x = p[x]     # 부모로 이동

    return x

def find_set2(x):
    if p[x] == x:
        return x
    else:
        return find_set2(p[x])

# 3. union(x,y)
# 두 노드를 하나의 집합으로 만들어주는 함수
# y의 대표자(root)가 x의 대표자(root)를 가리키게 함
  # 즉 x의 대표자가 그대로 root / y를 포함하는 tree는 x의 subtree
def union(x,y):
    root_of_x = find_set(x)
    root_of_y = find_set(y)
    p[root_of_y] = root_of_x  # y의 대표자(root)가, x의 대표자(root)를 가리키도록
    
# 4. 위의 표 결과 실행
union(1, 3)
print(p[1:])
union(2, 3)
print(p[1:])
union(5, 6)
print(p[1:])
print(find_set(6))
```





+ 연결된 노드들의 집합에서 대표자를 설정 후, 대표자가 같으면, 서로 연결 시 사이클 발생

+ Union(a,b) 는 a 집합의 대표원소를, b집합의 대표원소가 가리키게 함
+ 즉, 대표자를 tree의 root라고 생각하면 되고, 각 원소들은 자신의 부모만 가리킴
+ 대표자가 같으면 같은 집합





# 그래프 문제

## [1] MST (모든 노드 최소비용 연결)

### (1) PRIM 알고리즘

+ 의미
  + MST에 포함된 정점에서 연결된 간선들 중에 하나씩 **Greedy**하게 선택하면서 MST를 만들어 가는 방식
  
+ 과정

  + 시작 : 임의의 정점 v 선택해서 MST에 포함
    + 반복 : **MST에 포함된 모든 정점에서 최소비용 간선의 정점 u(not in MST)선택**
  + 모든 정점 선택될 때까지, 바로 위 과정 반복
  
+ 특성

  + 사이클 안생김
  + diijkstra 와 유사
  
+ 코드

  ```python
  # 1. arr 이용
  V, E = map(int,input().split())
  arr = [[0]*(V+1) for _ in range(V+1)]
  
  for _ in range(E):
      s, e, w = map(int,input().split())
      arr[s][e] = w
      arr[e][s] = w
  
  def prim(start):
      MST = [0] * (V + 1)
  
      # start 번노드에서 시작한다고 가정
      # start 번노드에서 이동할 수 있는 최소거리 노드 x 로 이동
      # start, x번 노드에서 이동할 수 있는 최소거리노드 x2로 이동
      # MST에 포함되지 않아야 함
      #... 이를 반복
      MST[start] = 1
      w_sum = 0
      for _ in range(1,V):  # 총 V-1 개 간선 선택하면 됨
          min_idx = 0
          min_val = 0xfffffffff
          for i in range(1,V+1):  # 모든 노드들을 돌면서 MST에 들어간 것에서 최소거리 찾으면됨
              if MST[i] == 1:
                  for j in range(1,V+1):
                      if min_val > arr[i][j] and MST[j]==0:
                          min_val = arr[i][j]
                          min_idx = j
          MST[min_idx] = 1
          w_sum += min_val    # 비용 더하기
      print(w_sum)
      return
  prim(1)
  
  
  
  # 2. arrL 이용
  
  V, E = map(int,input().split())
  arrL = [[]*(V+1) for _ in range(V+1)]
  for _ in range(E):
      s, e, w = map(int,input().split())
      arrL[s].append((e,w))
      arrL[e].append((s,w))
  
  def prim(start):
      MST = [0] * (V + 1)
      MST[start] = 1
      w_sum = 0
      for _ in range(1,V): # start 제외 V-1 개 경로 고르면 됨
          min_idx = 0
          min_val = 0xfffffff
          for i in range(1,V+1):
              if MST[i] == 1:
                  for end_weight in arrL[i]:
                      e, w = end_weight
                      if MST[e]==0 and min_val > w :
                          min_val = w
                          min_idx = e
          MST[min_idx] = 1
          w_sum += min_val        # 비용 더하기
      print(w_sum)
      return
  prim(1)
  
  ```

  





### (2) Kruskal 알고리즘

+ 의미

+ 과정

+ 특성

+ 코드

  ```python
  V, E = map(int,input().split())
  edges = []
  for _ in range(E):
      s, e, w = map(int,input().split())
      edges.append([w, s, e])
  
  # make set
  tree = [x for x in range(V+1)]
  
  # find set
  def find_set(x):
      if tree[x] == x:
          return x
      else:
          return find_set(tree[x])
      
  # union set
  def union(x,y):
      root_x = find_set(x)
      root_y = find_set(y)
      tree[root_y] = root_x
  
  # 아래가 Kruskal 알고리즘
  MST = list(range(1,V+1))
  w_sum = 0
  # sorting
  # cycle 안생기면 선택
  # 다 선택하면 끝
  edges.sort()
  for i in range(E):
      w, s, e = edges[i]
      if find_set(s) != find_set(e):
          union(s,e)
          w_sum += w
  print(w_sum)
  ```

  






## [2] 특정 노드에서 다른 노드로 가는 최소 비용 계산

### (1) 중복 방문 BFS로도 구현 가능

+ 의미
  + 방문(현재최소비용)을 표시하는 visited 배열에서, 지났던 곳에 최소비용을 입력하고, 다음에 해당 위치를 더 적은 비용으로 지날 수 있으면, visit 하는 것을 허용

+ 특성
  + 다익스트라로는 시간 초과가 나는데, 중복 방문 BFS는 안나는 문제가 있어서,,, 신기함
    + SWEA의 5250번
+ 코드

```PYTHON
# SWEA 5250 번
# 이동 / 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

T = int(input())
for tc in range(1,T+1):
    # input
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 출발 도착
    sr, sc = 0, 0
    er, ec = N-1, N-1


    # 현재 위치에서, 이동비용 list로 생성
    # 최소 비용으로 이동 후 목적지 인지 확인

    # 최소 비용으로 이동 후, 이동 비용 list update
    # 목적지에 도달할 때까지 반복

    # visited, used , queue 초기화
    INF = 100*1000
    visited = [[INF]*N for _ in range(N)]
    visited[sr][sc] = 0
    queue = [[sr,sc]]
    while queue:
        cr, cc = queue.pop(0)

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # 이동 경로가 유효하고, 기존보다 비용이 적은 경우
            if 0 <= nr < N and 0 <= nc < N and visited[cr][cc] + 1 + max(arr[nr][nc] - arr[cr][cc],0) < visited[nr][nc]:     

                visited[nr][nc] = visited[cr][cc] + 1 + max(arr[nr][nc] - arr[cr][cc],0)
                queue.append([nr,nc])
    # 결과 출력            
    print(f"#{tc} {visited[er][ec]}")
```





### (2) 다익스트라(diijkstra) 알고리즘

+ 의미

  + 시작 노드에서 도착 노드로 갈 때까지, 매 순간 최소 비용으로 이동할 수 있는 노드 선택

+ 과정

  + 시작 노드에서 이동할 수 있는 노드들의 비용 update
  + 현재 최소 비용으로 이동할 수 있는 노드 선택
  + 이동할 수 있는 노드들의 비용 update
  + 현재 최소비용으로 이동할 수 있는 노드 선택 (update와 선택 반복)

+ 특성

  + 음의 가중치를 허용 x

  + 마지막까지 연결한다면, 사실 출발지에서 다른 모든 곳으로 가는 최소비용 계산됨

  + 음의 가중치가 없기 때문에, 한 번 연결된 노드는 무조건 그것이 최소비용임



+ 코드

```python
# SWEA 5251 번 최소이동거리
T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split()) # 마지막 연결지점 번호, 도로의 개수
    adjl = [ [] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int,input().split())
        adjl[s].append([e,w])


    # 다익스트라 구현
    # 매 순간 갈 수 있는 가장 가까운 거리를 이동하면서 순회하면, 그것이 해당 노드까지의 최단거리
    start = 0
    end = N

    # 초기화
    cur_min_list = [10**8]*(N+1)  # 해당 index node 까지의 최소 거리
    cur_min_list[start] = 0

    # visited 로 방문 표기
    visited = [0]*(N+1)
    visited[start] = 1

    # 아래 1. 2.를 반복
    # 1. cur_node(최단거리) 를 경로에 포함한 경우, 최소 비용으로 이동할 수 있는 곳들 update
    # 2. 최소 비용으로 이동할 수 있는 곳으로 이동하고, visited 표시


    cur_node  = start
    # 목적지에 도달하지 않을 때 반복
    while visited[N]==0:   # 한 번 방문하면 start에서 해당 노드까지의 최소거리는 바뀌지 않음

        # 1. cur_node에서 최소 비용으로 이동할 수 있는 곳들 update
        for neighbor in adjl[cur_node]:
            next_node, cur_to_next_cost = neighbor

            # next_node로 이동하는 값을 최소 값으로 업데이트
            # 기존 start -> next_node로 가는 거리  >  (기존 start -> cur_node) -> next_node 로 가는 거리
            if cur_min_list[next_node] > cur_min_list[cur_node] + cur_to_next_cost:
                cur_min_list[next_node] = cur_min_list[cur_node] + cur_to_next_cost


        # 2. 최소거리인 곳으로 이동
        min_cost = 10**8
        min_idx = -1
        # 방문하지 않은 모든 노드들 중 최소거리 찾기
        for node in range(len(cur_min_list)): # 모든 노드
            cost = cur_min_list[node]         # 이동 비용
            if visited[node] == 0 and min_cost > cost:   # 방문하지 않았고, 최소
                min_cost = cost                          # min_cost update
                min_idx = node

        # 최소인 곳 방문
        visited[min_idx] = 1
        cur_node = min_idx


    print(f"#{tc} {cur_min_list[min_idx]}")
```







### (3) 벨만-포드(Bellman-Ford) 알고리즘

+ 특성
  + 음의 가중치 허용

  + 음의 사이클을 찾는 것이 목적 중 하나

  + **노드개수 V개라면 V-1번 순회안에 무조건 최적경로 찾음**

    
  
+ [위키백과참고](https://ko.wikipedia.org/wiki/%EB%B2%A8%EB%A8%BC-%ED%8F%AC%EB%93%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

  + 가중 유향 그래프에서 최단 경로 문제 푸는 알고리즘
  + V,E가 꼭지점과 변의 개수라면, 실행시간은 $O(|V||E|)$
  + 다익스트라보다 느림
    + 다익스트라는 음의 가중치에서 작동못함

+ 과정

  + 매우 큰 값으로 거리 초기화
  + 시작 노드에 대해서 0으로 거리 초기화
  + 전체 노드의 개수 V 만큼 다음을 반복
    + 각 노드에서 가능한 이동 가능한 모든 간선(E)을 확인
      + 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧으면, 거리 갱신

  + 만약 V-1회 반복한 이후인, V번째 반복에서 값이 갱신되면 음수순환 존재




+ 코드

  + ```PYTHON
    # input 방법 1
    arr = [[INF]*(V+1) for _ range(V+1)]
    arr[v1][v2] != INF arr[v1][v2] 비용으로 v1에서 v2로 이동할 수 있도록 데이터 받기
    
    # input 방법 2 : 아래에서 이용
    arr = [[start, end, distance], ... , ...] 꼴로 받기
    
    dist = [INF]*(V+1)
    def bellman_ford(start):
        dist[start] = 0
        
        for v in range(V):
            # 모든 간선에 대해서, 새로운 이동거리가 더 짧을 수 있는지 확인
            for j in range(len(arr)):
                cur = arr[j][0]
                next_node = arr[j][1]
                d = arr[j][2]
                # 만약 cur -> next_node 비용이 기존의 dist[next_node] 보다 적으면 갱신
                if dist[cur] + d < dist[next_node] and dist[cur]!=INF: # 이동가능해야하므로 !INF
                    dist[next_node] = dist[cur] + d
                    if v == V-1:
                        return True # 음의 순환 존재
         return False
                    
                           
                
    ```

  + 



## [3] 모든 정점들에 대한 최소 비용 계산

### (1) 플로이드-워샬(Floyd-Warshall) 알고리즘

+ 한 번 실행하여, 모든 노드 간의 최단 경로를 구할 수 있음
+ 음의 간선(가중치)도 사용 가능
+ 시간 복잡도가 크다 : $O(V^3)$



+ 과정
  + 2차원 인접행렬로 graph 표현
    + 자기자신은 0, 그외는 INF로 초기화
  + 3중 루프를 이용해, i에서 j로 가는 거리와, i에서 k를 거쳐 j로 가는 거리를 비교해서 graph를 update 한다.



+ 코드 ([참고](https://im-so-so.tistory.com/19))

  ```python
  import heapq
  
  n, m, r = map(int, input().split())
  
  INF = float('INF')
  graph = [[INF]*(n+1) for _ in range(n+1)]
  
  # 0 으로 초기화
  for i in range(1, n+1):
      graph[i][i] = 0
  
  # 거리 input 입력
  for _ in range(r):
      a, b, l = map(int, input().split())
      graph[a][b] = l
      graph[b][a] = l
  
  # 거리 비교
  for k in range(1, n+1):
      for i in range(1, n+1):
          for j in range(1, n+1):
              graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
  
  # 위 과정을 통해서, graph[i][j] 는 i에서 j까지가는 최단 거리가 입력되어 있음
  ans = 0
  for i in range(1, n+1):
      tmp = 0
      for j in range(1, n+1):
          if graph[i][j] <= m:
              tmp += items[j]
      ans = max(ans, tmp)
  
  print(ans)
  ```

  
