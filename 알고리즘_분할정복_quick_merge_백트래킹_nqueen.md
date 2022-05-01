[toc]

# 분할 정복

## [1] 의미

+ Top-down approach
+ 분할 -> 정복 -> 통합

  + 분할 : 해결할 문제를 여러 개의 작은 부분으로 나눔
+ 정복 : 나눈 작은 문제를 각각 해결
  + 통합 : 해결된 답을 모음





## [2] 분할 정복 기반 알고리즘

### (1) 거듭제곱

+ 반복으로 하면 O(n)의 시간이 들지만, 분할 정복으로하면, O(logn)



### (2) 이진 검색 (binary search)

+ 효과 및 조건
  + 자료가 정렬된 상태여야 함
  + 100만개 대상에서 1000번 찾는 거 해야하는 경우, 빠르게 가능




+ 과정


  + 중앙 원소 고르기


  + 중앙 원소와 찾고자 하는 값 비교 후, 좌, 우 중 한 곳으로 이동해서, 과정 반복


#### 

+ 코드

```python
# 1. 반복문 이용
# L : 배열, n : L의 크기, goal_num : 찾고자 하는 목표값
def bs(L, n, goal_num):
    low = 0
    high = n-1
    
    while low <= high:
        mid = low + (high-low)//2 # 짝수개 존재시, 왼쪽 것이 mid / overflow 방지
        
        if L[mid] == goal_num:
            return mid
        elif L[mid] > goal_num:
            high = mid - 1
        else: # L[mid] < goal_num
            low = mid + 1
    return -1 # goal_num not in L
        

# 2. 재귀 이용
def bs(L, low, high, goal_num):
    if low > high:
        return -1
    
    else:
        mid = low + (high-low)//2
        if L[mid] == goal_num:
            return mid
        elif L[mid] > goal_num:
            return bs(L,mid+1, high, goal_num)
        else: # L[mid] < goal_num:
            return bs(L,low, mid-1, goal_num)
```



---

### (3) Merge sort

+ 단계
  + 분할단계
  
    + 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 반씩 분할 계속
  
  + 병합단계
  
    + 2개의 부분집합을 정렬하면서 하나의 집합으로 병합
  
      
  
+ 복잡도
  + 시간
    + 평균 O(nlogn)
    + 최악 O(nlogn)
    + 최상 O(nlogn)
    
  + 공간
    + O(n)
    
    +  idx를 전달해서 정렬하면 더 빠르다?
    
      
  
+ 코드 3가지

```python
# sol 1. 배열이용

def merge_sort1(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort1(L[:mid])  # 리스트 복사해서 넘기므로 메모리 O(n)만큼 필요
    right = merge_sort1(L[mid:])  # 이렇게 슬라이싱 하면, 여기서도 n 만큼 시간 듦

    return merge(left, right)


def merge(left, right):
    l, r = 0, 0  # k는 삽입되는 index 위치
    result = []  # 결과 내보내는 것도 메모리 필요

    while l < len(left)  and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:] + right[r:]
    return result
```



```python
# sol 2. 배열 + index 이용
def merge_sort2(L,start, end):
    if start == end:
        return [L[start]]
    mid = start + (end - start) // 2 # 짝수일 때, 좌측 mid 선택

    left = merge_sort2(L, start, mid)
    right = merge_sort2(L, mid+1 , end)
    return merge(left, right)

```



```python
# sol 3. index 이용
def merge_sort3(L, start, end):
    if start == end:
        return
    # 짝수 개 남았을 때, 좌측이 mid 선택되도록 2개 중 1개 이용
    mid = start + (end-start) // 2 
    mid = (start+end)//2

    merge_sort3(L, start, mid)
    merge_sort3(L, mid+1 , end)      # mid 부터 우측
    merge3(L, start,mid,end)

# merge 해야하는 길이와 같은 리스트 만들어서, merge 후, L에 다시 복사
def merge3(L, start, mid, end):
    result = []
    i = start # left의 시작점
    j = mid+1   # right의 시작점

    while i <= mid and j <= end:
        if L[i] <= L[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(L[j])
            j += 1

    if i == (mid+1):
        result += L[j:end+1]

    if j == end+1:
        result += L[i:mid+1]

    # 결과를 L에 복사
    for i in range(start,end+1):
        L[i] = result[i-start]
```





---

### (4) Quick sort

+ 의미
  + 정렬을 원하는 1차원 배열 L에서 PIVOT 원소(배열의 특정 위치원소 / 아래의 경우 맨 앞 원소 이용) 의 정렬 위치를 정해주고, 이를 기준으로 반으로 나눠서(partition) 정렬하기를 반복

    

+ partition 의미

  + **pivot 값 기준으로, 작은 값, 큰 값 분리 하는 용도**

  + pivot은 좌 끝 값, 우 끝 값, 배열의 임의의 3개 값의 중간값 등으로 이용

    

+ partition algorithms

  + Hoare partition
    + 좌측 끝값을 pivot

  + Lomuto partition
    + 우측 끝값을 pivot




+ 복잡도
  + 시간
    + 평균 O(nlogn)
    + 최악 O(n**2) / 이미 많이 정렬되어 있는데, pivot을 양 끝으로 정할 때
    + 최상 O(nlogn)
  + 공간
    + O(logn)



+ 코드

```PYTHON
def quick_sort(L,left,right):
    # 피벗을 선정하고
    # 피벗을 기준으로 큰값과 작은값으로 구분 후
    # 작은 부분 정렬
    # 큰 부분 정렬
    if left < right:
        # print(L)
        pivot_loc = partition(L,left,right)
        quick_sort(L, left, pivot_loc-1)
        quick_sort(L, pivot_loc+1, right)

# partition1 : Hoare partition
def partition(L,left,right):
    pivot = L[left]
    i = left
    j = right
    while i <= j:
        while i <= j and L[i] <= pivot:
            i += 1
        while i <= j and pivot < L[j]:  # 여기 조건은 i <= j 없어도 됨
            j -= 1
        # pivot보다 큰 수가 picot 보다 작은 수보다 앞에 있는 경우 자리 교환
        if i < j:
            L[i],L[j] = L[j],L[i]
            
    L[left], L[j] = L[j], L[left]
    return j


# partition2 : Lomuto partition : 코드 간결하지만, Hoare 보다 느림
def partition(L,left,right)
    pivot = L[right]
    i = left - 1
    for j in range(left,right+1):
    # i|작=j|작|작|큰|큰|작|큰|큰|pivot| 에서 시작
        if L[j] <= pivot:
            i += 1                   # if 문이 계속 만족되면 이 부분에서 i가 j와 같아짐
            L[i], L[j] = L[j], L[i] # -** 에서의 i가 i+=1 되고, i와 j 위치 교환
        # 만약 if 문이 만족안되면, j는 for loop으로 커지고, i는 그대로라 j와 i의 차가 커짐
        # 만약 연속 n 번 if 문 만족안하면, 여기 위치에서 j = i + n 임 -*
        # 즉 *에서의 상태는 i의 바로 오른쪽에는 pivot보다 큰 것이 n개 연속있음 -**
        # 즉 이와 같음 : |작|작|작=i|큰|큰|작=j|큰|큰|pivot| -**
        
        L[i+1], L[j] = L[j], L[i+1]
        return i + 1

    
L = [1,3,2]
quick_sort(L,0,len(L)-1)
print(L)
```



+ Lomuto partition 예시

| i 시작 | j시작 / left |          |          |            |             |           |           |           | right     |
| ------ | ------------ | -------- | -------- | ---------- | ----------- | --------- | --------- | --------- | --------- |
| i      | 3  : j       | 2        | 4        | 6          | 9           | 1         | 8         | 7         | 5 = pivot |
|        | 3  : i, j    | 2        | 4        | 6          | 9           | 1         | 8         | 7         | 5         |
|        | 3 : i        | 2 : j    | 4        | 6          | 9           | 1         | 8         | 7         | 5         |
|        | 3            | 2 : i, j | 4        | 6          | 9           | 1         | 8         | 7         | 5         |
|        | 3            | 2 : i    | 4 : j    | 6          | 9           | 1         | 8         | 7         | 5         |
|        | 3            | 2        | 4 : i, j | 6          | 9           | 1         | 8         | 7         | 5         |
|        | 3            | 2        | 4 : i    | **6** : j  | **9**       | 1         | 8         | 7         | 5         |
|        | 3            | 2        | 4 : i    | **6**      | **9**  : j  | 1         | 8         | 7         | 5         |
|        | 3            | 2        | 4        | **6** : i  | **9**       | 1 : j     | 8         | 7         | 5         |
| swap   | 3            | 2        | 4        | ***1***: i | **9**       | **6** : j | 8         | 7         | 5         |
|        | 3            | 2        | 4        | ***1***: i | **9**       | **6**     | **8** : j | 7         | 5         |
|        | 3            | 2        | 4        | ***1***: i | **9**       | **6**     | **8**     | **7** : j | 5         |
|        | 3            | 2        | 4        | ***1***: i | **9**       | **6**     | **8**     | **7**     | 5 : j     |
|        | 3            | 2        | 4        | ***1***    | **9** : i   | **6**     | **8**     | **7**     | 5 : j     |
| swap   | 3            | 2        | 4        | ***1***    | ***5*** : i | **6**     | **8**     | **7**     | **9**     |
| 종료   | 3            | 2        | 4        | ***1***    | ***5***     | **6**     | **8**     | **7**     | **9**     |









# 백트래킹

## [1] 개념



### (1) 개념 및 DFS 와 차이

+ DFS 는 모든 경우 다 해보고, 끝까지가서 되는지 안되는지 파악

+ 백트래킹은 끝까지 가기 전 경로에서도 되는지 안되는지 파악 (가지치기)

  + 불필요한 경로 조기 차단

  + DFS와 같은 코드 구조이지만,  유망한 경로인지 탐색하여 유망하지 않으면, 탐색을 미리 그만두는 과정이 포함된 것

    

### (2) 절차

1. 상태 공간 트리의 깊이 우선 검색 실시
1. 각 노드가 유망한지 점검
1. 만일 2의 노드가 유망하지 않으면, 해당 노드의 부모 노드로 돌아가서 검색 계속

+ 해답의 가능성이 있는 경우를 **유망**하다고 함



### (3) 활용

+ 최적화 문제

+ 결정문제

+ 예
  + 미로찾기, n-Qeen, map coloring, 부분집합, 순열

+ 순열

  + 각 요소가 사용되었는지 안되었는지를 알려줄 `used = [0]*N` 필요



## [2] 문제들
### (1) N-Queen

+ 의미
  + NxN 체스판에서 N개의 queen들이 서로 공격하지 못하도록, 배치하는 경우의 수
+ 코드 1~2

```python
# sol 1. 대각선 합 성질 이용
def nqueen(cur_r):
    global result
    r = cur_r
    if r == N:
        result += 1

    else:
        for c in range(N):
            cr, cc = r, c
            if promising(cr, cc): # cr, cc가 유망한지 탐색
                col[cc] = 1
                right_diag[N - 1 + (cr - cc)] = 1
                left_diag[cr + cc] = 1
                nqueen(cr + 1)
                col[cc] = 0
                right_diag[N - 1 + (cr - cc)] = 0
                left_diag[cr + cc] = 0
    return


def promising(cr, cc):
    if col[cc] == 0 and right_diag[N - 1 + (cr - cc)] == 0 and left_diag[cr + cc] == 0:
        return True
    else:
        return False

for i in range(1,16):
    N = i

    arr = [[0]*N for _ in range(N)]
    col = [0]*N
    right_diag = [0]*(2*N-1) # \ 방향 대각선 r-c = -(N-1), -(N-2) , ... 0, 1, ... N-2, N-1    \\\\\ + N -1 = -> 0, 1, 2 ,, 2N-1
    left_diag = [0]*(2*N-1) # / 방향 대각선 r+c = 0, 1, 2, 3, ... , 2N-2 //
    result = 0
    nqueen(0)
    print(f"N : {N}, result : {result}")
```



```python
# sol 2. dfs 이용

def check(sr, sc):
    # column
    for r in range(sr-1,-1,-1):
        # column
        if visited[r][sc] == 1:
            return False
        # 좌측 위 대각선
        if 0 <= sc - (sr-r) and visited[r][sc-(sr-r)] == 1:  # column이 1,2,3,4,... 씩 index 줄어야
            return False
        # 우측 위 대각선
        if sc + (sr-r) < N and visited[r][sc+(sr-r)] == 1:   # column이 1,2,3,4,... 씩 index 늘어야
            return False
    return True

def dfs(r):
    global cnt
    if r == N:
        cnt += 1
        return
    else:
        for c in range(N):
            if check(r,c):
                visited[r][c] = 1
                dfs(r+1)
                visited[r][c] = 0


N = int(input())
visited = [[0]*N for _ in range(N)]
cnt = 0
dfs(0)
print(cnt)


```

