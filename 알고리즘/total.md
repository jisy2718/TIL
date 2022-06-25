[TOC]



# 후위표기와 계산기











# 백트래킹

## 활용

+ 최적화 문제

+ 결정문제

+ 예
  + 미로찾기, n-Qeen, map coloring, 부분집합, 순열
  
+ 순열

  + 각 요소가 사용되었는지 안되었는지를 알려줄 `used = [0]*N` 필요

    




## 절차

1. 상태 공간 트리의 깊이 우선 검색 실시
1.  각 노드가 유망한지 점검
1. 만일 2의 노드가 유망하지 않으면, 해당 노드의 부모 노드로 돌아가서 검색 계속

+ 해답의 가능성이 있는 경우를 **유망**하다고 함





## DFS 와 백트래킹 차이

+ DFS 는 모든 경우 다 해보고, 끝까지가서 되는지 안되는지 파악
  + 모든 경우의 수 고려

+ 백트래킹은 끝까지 가기 전 경로에서도 되는지 안되는지 파악 (가지치기)
  + 불필요한 경로 조기 차단
+ DFS 와 백트래킹은 코드 구조 같음
  + 백트래킹은 안되는 경우 미리 차단하는 조건 추가된 것









# 부분집합 / 순열

## 1. 부분집합

### [1] 비트 표현



### [2] 부분집합 표현



### [3] 부분집합 합



### [4] 부분집합 합  + 조건 1



### [5] 부분집합 합 + 조건 1, 2





## 2. 순열











# 완전 검색 & 그리디



## 1. 반복과 재귀



## 2. 완전검색기법

+ 모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 적음

+ 이를 기반으로 그리디 기법이나 동적 계획법을 이용해 효율적인 알고리즘을 찾을 수 있음

+ 우선 완전 검색으로 접근하여, 해답 도출 후, 성능 개선을 위해 다른 알고리즘을 사용해서 해답찾기

+ 완전 검색은 전형적으로 순열, 조합, 부분집합과 같은 조합적 문제들과 연관

  + 완전 검색은 조합적 문제에 대한 brute-force 방법

  





## 3. 조합적 문제

+ 여행사 Big sale 문제



### [1] 순열

+ 다수의 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련
  + 예 : Traveling Salesman Problem

#### (1) 순열 생성방법1 (loop)

```python
# 1. {1,2,3}을 이용한 모든 순열
for i1 in range(3):
    for l2 in range(3):
        if l2 != l1:
            for l3 in range(3):
                if l3 != l2 and l3 != l1:
                    print(l1,l2,l3)
```





#### (2) 순열 생성방법2 (최소한의 교환) : 이해가 잘 안가네

```python
# 2. n개원소의 nPn
def perm(i, n):
    if i == n:
        print(p)
        return
    else:
        for j in range(i,N):
            arr[i], arr[j] = arr[j], arr[i]
            print(f"위 i, j : {i} {j}, arr : {arr}")
            perm(i+1,n)
            print(f"아래 i, j : {i} {j}, arr : {arr}")
            print("------------------------------")
        
arr=[1,2,3,4,5]
n = len(arr)
perm(0,n)
```





#### (3) *순열 생성방법3 (used, 재귀 이용)*

+ a의 index에 대해 사전적 순서로 생성됨 (0,1,2 / 0,1,3 / 0,1,4/ 2,3,4 /...)

```python
# 3. used & 재귀 이용해 nPn 구하기
# a = [1,2,3] 경우 3자리 순열
def f(idx, n): # 순열 p[0]*n을 채우는 함수,idx:현재까지 고른개수, n은 주어진 숫자 개수
    if idx == n:
        print("순열완성, 원하는 작업 하세요",p)
        return
    else:
        for i in range(n): # used에서 사용하지 않은 숫자 검색---------이부분이 핵심(loop가 아래에서 재귀적으로 들어가서, 사전적 순서로 순열 만들게 됨)
            if used[i] == 0 : # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1   # 사용함으로 표시
                p[idx] = a[i] # p[n] 결정
                f(idx+1, n)
                used[i] = 0 # a[i]를 다른 위치에서 사용할 수 있도록 함
    return

a = [1,2,3]
p = [0]*3
used = [0]*3
f(0,3)



# 4. used & 재귀 이용해 nPk 구하기
# a = [1,2,3,4,5] 경우 3자리 순열
def f(idx, k, n):  # 순열 p[0]*k을 채우는 함수, idx :현재까지 고른 개수, k :고를 개수, n :주어진 숫자개수
    if idx == k:
        print("순열완성, 원하는 작업 하세요",p)
    else:
        for i in range(n): # used에서 사용하지 않은 숫자 검색
            if used[i] == 0 : # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1   # 사용함으로 표시
                p[idx] = a[i] # p[n] 결정
                f(idx+1, k, n)
                used[i] = 0 # a[i]를 다른 위치에서 사용할 수 있도록 함
    return    
a = [1,2,3,4,5]
k = 3
p = [0]*k
used = [0]*len(a)
f(0,3,5)
```



####  (4) 순열생성방법 4 (사용하지 않은 목록 만들기)

+ 백트래킹 이용해서 해결



### [2] 부분집합

+ 다수의 중요 알고리즘들이 원소들의 그룹에서 최적의 부분집합을 찾는 것
  + 예 : 배낭 짐싸기 (knapsack)

#### (1) 부분집합 생성방법1 (loop)



#### (2) *부분집합 생성방법2 (binary counting)*

+ 부분집합을 생성하기 위한 가장 자연스러운 방법 (원소개수 달라져도 적용가능)

+ binary counting은 사전적 순서로 생성하기 위한 가장 간단한 방법

+ binary counting

  + 원소 수에 해당하는 N개의 비트열을 이용

  + n번째 비트값이 1이면, n번째 원소가 포함되었음을 의미

  + | 10진수 | 이진수 | {A,B,C} |
    | ------ | ------ | ------- |
    | 0      | 000    | {}      |
    | 1      | 001    | {A}     |
    | 2      | 010    | {B}     |
    | 3      | 011    | {A,B}   |
    | 4      | 100    | {C}     |
    | 5      | 101    | {A,C}   |
    | 6      | 110    | {B,C}   |
    | 7      | 111    | {A,B,C} |

    

```python
# 2. 
arr = [3,6,7,1,5,4]
N = len(arr)
for i in range(0,(1<<N)): # 1<<N : 부분집합 개수로 이진수라고 생각
    for j in range(0,N):  # 원소의 수만큼 비트를 비교
        if i & (1<<j):    # i의 j 번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end = ' ')
    print()
```





#### (3) 부분집합 생성방법3

```python
# 3. 비트 & 재귀 이용
def f(i,N): # i : 부분집합에 포함될지 결정할 원소의 인덱스, N : 전체 원소 개수
    if i == N:  # 한 개의 부분집합 완성
        print(bit, end= ' ')
        for j in range(N):
            if bit[j]:
                print(a[j],end= ' ')
        print()
        
    else:
        # 갈림길이 2번 나오면 2개 적어야
        bit[i] = 1
        f(i+1,N) # i + 1 로 이동
        bit[i] = 0 # bit[i] = 1 인 경우는 다 봤으니까, bit[i] = 0인 경우 가지로 탐색
        f(i+1,N) #i +1 로 이동
    return

a = [1, 2, 3]
bit = [0, 0, 0]

f(0,3)
```









### [3] 조합

+ 성질

$$
_nC_r = _{n-1}C_{r-1} + _{n-1}C_r
$$



#### (1) 조합 생성방법1 (재귀호출)

+ 위의 성질 이용

```python
# 1. p43 좀 복잡
arr = [1,2,3,4,5]
n = len(arr)
r = 3
p = [0]*r

def comb(n,r):
    if r == 0:
        print(p)
        return
    elif n < r:
        return
        
        
    else:
        p[r-1] = arr[n-1]
        comb(n-1,r-1)
        comb(n-1,r)
```





#### (2) 조합 생성방법2 (r이 작은 경우 / loop)

```python
# 2. 10개의 원소중 3개를 고르는 조합
a = [0,1,2,3,4,5,6,7,8,9]

def f(i,j,k):
    print(i,j,k)

N = 10
R = 3
for i in range(N-2):
    for j in range(i,N-1):
        for k in rnage(j,N):
            f(a[i],a[j],a[k]) # 완성된 조합 {a[i],a[j],a[k]}로 원하는 작업 f 수행


```



#### (3) ***조합 생성방법3 (재귀)***

+ n과 r이 계속 바뀌는 경우로 **조합 생성방법2** 의 재귀적 표현

```python
# 3. 기본형
def nCr(n,r,s): # n개에서 r개를 고르는 조합, s: 선택할 수 있는 구간의 시작
    if r == 0: # 더 이상 고를 것이 없다
        print(*comb)
    else:
        for i in range(s, n-(r-1)):
            comb[r-1] = a[i]
            # comb[3-r] = a[i] 로 하면 사전순으로 나옴
            nCr(n,r-1,i+1)
    return


n = 5
r = 3
# k = r  아래 변형에 이용
a = [i for i in range(1,n+1)]
comb = [0]*r
nCr(n,r,0)


# 3. 변형 (사전순출력)
def nCr(n,r,s,k): # n개에서 r개를 고르는 조합, s: 선택할 수 있는 구간의 시작, k: 전체 선택해야하는 개수
    if r == 0: # 더 이상 고를 것이 없다
        print(*comb)
    else:
        for i in range(s, n-(r-1)):
            comb[k-r] = a[i] # 로 하면 사전순으로 나옴
            nCr(n,r-1,i+1,k)
    return
```



#### (4) 조합 생성방법4 (재귀)

+ **조합 생성방법3** 과 같음

```python
def nCr(n,r,s,k): # n개에서 r개를 고르는 조합, s: 선택구간 시작, k:고른 개수
    if k == r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1)
            comb[k] = a[i]
            nCr(n,r,i+1,k+1)
    return
n = 5
r = 3
a = [i for i in range(1,n+1)]
comb = [0]*r
nCr(n,r,0,0)
        
```



#### (5) 조합 생성방법5

```python
arr = [1,2,3,4,5]
n = 5
r = 3

def comb(selected, idx, cnt):
    if cnt == r:
        print(selected)
        return
    
    if idx >=n:
        return
        
    selected[idx] = 1
    comb(selected, idx+1, cnt+1)
    selected[idx] = 0
    comb(selected, idx+1, cnt)
```



## 4. 탐욕 알고리즘

+ 탐욕 알고리즘은 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행

  + 지역 최적이지만, 전역최적 보장 없음

  + 예 

    + 거스름돈 문제
    + 활동 선택 문제(회의실 1개에서 최대한 많은 회의를 진행하려면, 회의 배치를 어떻게?)
      + 끝나는 시간이 가장 빠른 것부터 선택해서, 해당 회의 끝난 후에 가장 빨리 끝나는 회의를 반복 선택
      + 구체적 방법은 1. 종료시간이 빠른 순서로 활동 정렬/ 2. 첫활동 선택 / 3.선택한 활동의 종료시간보다 빠르게 시작하는 활동 모두 제거 / 4. 남은 활동들에 위 과정 반복

  + 반례 

    +  배낭짐싸기(Knapsack)(백트래킹,dp이용해야)

    

+ 일단 한번 선택된 것은 번복하지 않음

  + 알고리즘이 단순하고, 제한적인 문제들에 적용





+ **원문제의 최적해 = 탐욕적 선택 + 하위 문제의 최적해**





### [1] 동적계획법(DP)와 비교

| 탐욕                                      | DP                                                         |
| ----------------------------------------- | ---------------------------------------------------------- |
| 매 단계에서, 지역 최적 선택 (top-down)    | 매 단계의 해결은, 해결한 하위 문제의 해를 기반 (Bottom-up) |
| 하위 문제를 풀기전에 선택이 먼저 이루어짐 | 하위문제 우선 해결                                         |
| 빠르고 간결                               | 좀 더 느리고 복잡                                          |





### [2] 대표적 탐욕기법 알고리즘

| 알고리즘            | 목적                                                   | 설명                                                         | 대상   |
| ------------------- | ------------------------------------------------------ | ------------------------------------------------------------ | ------ |
| Prim                | N개 노드에 대한 최소 신장 트리(MST) 찾기               | 서브트리 확장하면서 MST 찾기                                 | 그래프 |
| Kruskal             | N개 노드에 대한 최소 신장 트리(MST) 찾기               | 싸이클이 없는 서브 그래프를 확장하면서 MST 찾기              | 그래프 |
| Dijkstra            | 주어진 정점에서, 다른 정점들에 대한 최단경로 찾기      | 주어진 정점에서 가장 가까운 정점을 찾고, 그 다음 정점을 반복해서 찾기 | 그래프 |
| Huffman tree & code | 문서의 압축을 위해, 문자들의 빈도수에 따라 코드값 부여 | 출현 빈도가 낮은 문자부터 선택해, 이진트리 완성하고, 코드값 부여 | 문자열 |

+ Prim 과 Dijkstra가 상당히 비슷









# 분할정복/백트래킹 

## 1. 분할정복[옮기기 완료]

+ Top-down approach
+ 분할 -> 정복 -> 통합
  + 분할 : 해결할 문제를 여러 개의 작은 부분으로 나눔
  + 정복 : 나눈 작은 문제를 각각 해결
  + 통합 : 해결된 답을 모음



### [1] 분할 정복 기반 알고리즘

#### (1) 거듭제곱

+ 반복으로 하면 O(n)의 시간이 들지만, 분할 정복으로하면, O(logn)


#### (2) 병합정렬 (merge sort)

+ 여러 개의 정렬된 자료의 집합을 병합하여, 한 개의 정렬된 집합으로 만드는 방식

+ 시간복잡도 : O(logn)

+ 자바의 경우 자료가 큰 경우에 내장으로 활용

  + 자바의 경우 자료가 작으면 quick sort 이용

+ 서로 다른 파일의 것들 가져와서 병합하는 경우에도 활용

  

##### (a) 단계

+ 분할단계
  + 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 계속

+ 병합단계
  + 2개의 부분집합을 정렬하면서 하나의 집합으로 병합



##### (b) 복잡도

+ 시간
  + 평균 O(nlogn)

+ 메모리

  + O(n) 사용으로 큼
  + 저장공간은 temp로 이용하고, idx를 전달해서 정렬

  



##### (c) 코드

```python
# 1. 배열이용

def merge_sort1(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort1(L[:mid])  # 리스트 복사해서 넘기므로 메모리 O(n)만큼 필요
    right = merge_sort1(L[mid:])  # 이렇게 슬라이싱 하면, 여기서도 n 만큼 시간 듦

    return merge(left, right)


def merge(left, right):
    global cnt
    l, r = 0, 0  # k는 삽입되는 index 위치
    result = []  # 결과 내보내는 것도 메모리 필요

    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left)  and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1


    result += left[l:] + right[r:]
    return result

# 2. index + 배열 이용
def merge_sort2(L,start, end):
    if start == end:
        return [L[start]]
    mid = start + (end - start) // 2 # 짝수일 때, 좌측 mid 선택

    left = merge_sort2(L, start, mid)
    right = merge_sort2(L, mid+1 , end)
    return merge(left, right)

#-------------------------------------------------------------------------------------#

# 3. index 이용
def merge_sort3(L, start, end):
    if start == end:
        return
    mid = start + (end-start) // 2  # 2개 남았을 때, 좌측 mid 선택되도록
    mid = (start+end)//2
    # print(L,start,mid,end)
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
    # L[start:end+1] = result


L = [10,9,4,1,5,2,8]
merge_sort3(L,0,6)
print(L)
 #------------------------------------------시간측정-----------------------------------
import time
L = [10,9,4,1,5,2,8,1,3,2,1,3,2,1,3,5,5,5,5,66,6,76,3,4532,4,14,21,421,4,214,214,12,321,3235,1,325,43,5,346,34643,234]*100
n = len(L)

s1 = time.time()
for _ in range(100):
    L = [10, 9, 4, 1, 5, 2, 8, 1, 3, 2, 1, 3, 2, 1, 3, 5, 5, 5, 5, 66, 6, 76, 3, 4532, 4, 14, 21, 421, 4, 214, 214, 12,
         321, 3235, 1, 325, 43, 5, 346, 34643, 234] * 100
    merge_sort1(L)
# print(r)
e1 = time.time()


L = [10,9,4,1,5,2,8,1,3,2,1,3,2,1,3,5,5,5,5,66,6,76,3,4532,4,14,21,421,4,214,214,12,321,3235,1,325,43,5,346,34643,234]*1000
s2 = time.time()
for _ in range(100):
    L = [10, 9, 4, 1, 5, 2, 8, 1, 3, 2, 1, 3, 2, 1, 3, 5, 5, 5, 5, 66, 6, 76, 3, 4532, 4, 14, 21, 421, 4, 214, 214, 12,
         321, 3235, 1, 325, 43, 5, 346, 34643, 234] * 100
    merge_sort2(L,0,n-1)

e2 = time.time()


s3 = time.time()
for _ in range(100):
    L = [10, 9, 4, 1, 5, 2, 8, 1, 3, 2, 1, 3, 2, 1, 3, 5, 5, 5, 5, 66, 6, 76, 3, 4532, 4, 14, 21, 421, 4, 214, 214, 12,
         321, 3235, 1, 325, 43, 5, 346, 34643, 234] * 100
    merge_sort3(L,0,n-1)
e3 = time.time()

print(f"{e1-s1:.10f} {e2-s2:.10f}  { e3-s3:.10f}") # 속도가 비슷해..
    
```







#### (3) 퀵 정렬

##### (a)  단계

+ 주어진 배열을 두 개로 분할하고, 각각을 정렬

  

##### (b) 복잡도

+ 시간
  + 평균 O(nlogn)
  + 최악 O(n^2) : 이미 많이 정렬되어있는데, pivot을 양 끝에서 정할 때
+ 공간
  + 평균 O(logn) : 재귀때문
  + 최악 O(n)





##### (c) 코드

```python
# left, right : 정렬하고자 하는 구간
def quick_sort(L:list, left:int, right:int):
    if left < right:
        pivot_loc = partition(L,left, right) # pivot으로 정한 값의 위치
        quick_sort(L, left, pivot_loc-1)
        quick_sort(L, pivot_loc+1, right)
```



##### (d) partition code

+ **pivot 값 기준으로, 작은 값, 큰 값 분리 하는 용도**
+ pivot은 좌 끝 값, 우 끝 값, 배열의 임의의 3개 값의 중간값 등으로 이용



###### (d)-1 : Hoare partition

+ 좌측 끝(i)와 우측 끝(j) 에서 안쪽으로 좁혀가며 pivot의 위치 찾기
+ 아래는 좌측 끝 값을 pivot으로 한 경우 코드

```python
# 1. Hoare partition : 제일 많이 쓰임 / 좌,우 맨 끝에서 시작해서, 안쪽으로 오면서 pivot 위치찾기
def partition(L, left, right): 
    pivot = L[left] # 이 경우, 왼쪽 끝값으로 pivot 설정
    i = left
    j = right
    # |pivot=i|작|작|큰|작|큰|큰|작|큰|큰=j| 로 시작
    while i <= j :
        # 아래 i<=j 등호는 [5,1] 정렬하는 경우 생각해면 이해감
        # 즉 등호는 j가 pivot의 올바른 위치에서 시작하는 경우에 발생
        
        while i<=j and L[i] <= pivot: # 왼편에서 pivot보다 큰 값을 찾는 것
            i += 1
            # 아래는 while문에서 움직이는 것 표현
            # |pivot|작=i|작|큰|작|큰|큰|작|큰|큰=j|
            # |pivot|작|작=i|큰|작|큰|큰|작|큰|큰=j|
            # |pivot|작|작|큰=i|작|큰|큰|작|큰|큰=j|
        while (i <=j 생략가능) and L[j] > pivot:# 오른편에서 pivot보다 작은 값 찾는 것
            j -= 1
        if i < j:
            L[i], L[j] = L[j],L[i]
            # |pivot|작|작|큰=i|작|큰|큰|작=j|큰|큰| 여기서 i,j index원소 교환. 작: pivot보다 작은 것, 큰 : pivot 보다 큰 것
            
    # 마지막에 j가 i보다 작아지면서 끝남
    # 이 경우 |pivot|작|작|작|작 = j|큰 = i|큰|큰|큰| 과 같이 끝나는 것임
    # 그래서 pivot과 j 번재 index 값을 교환
    L[left], L[j] = L[j], L[left]    
    return j

```

###### (d)-2 : Lomuto partition

+ 우측 끝 값을 pivot으로 사용한 경우

```python
# 2. Lomuto partition : 코드 간결하지만, 1.보다 느림
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
        
    L[i+1], L[right] = L[right], L[i+1]
    return i + 1
    
              
    
    
    
```



+ Lomuto partition

| i    | left, j |       |      |       |         |       |       |       | right     |
| ---- | ------- | ----- | ---- | ----- | ------- | ----- | ----- | ----- | --------- |
| j=   | 3  : i  | 2 : j | 4    | 6     | 9       | 1     | 8     | 7     | 5 = pivot |
|      | 3       | 2     | 4    | 6     | 9       | 1     | 8     | 7     | 5         |
|      | 3       | 2     | 4    | 6     | 9       | 1     | 8     | 7     | 5         |
|      | 3       | 2     | 4    | 6     | 9       | 1     | 8     | 7     | 5         |
|      | 3       | 2     | 4    | **6** | **9**   | 1     | 8     | 7     | 5         |
|      | 3       | 2     | 4    | *1*   | **9**   | *6*   | 8     | 7     | 5         |
|      | 3       | 2     | 4    | 1     | **9**   | **6** | **8** | **7** | 5         |
|      | 3       | 2     | 4    | 1     | ***5*** | 6     | 8     | 7     | 9         |



#### (4) 이진 검색 (binary search)

+ 자료가 정렬된 상태여야 함
+ 100만개 대상에서 1000번 찾는 거 해야하는 경우, 빠르게 가능



##### (a) 과정

+ 중앙 원소 고르기
+ 중앙 원소와 찾고자 하는 값 비교 후, 좌, 우 중 한 곳으로 이동해서, 과정 반복

##### (b) 코드

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







## 2. 백트래킹 [옮기기 완료]

+ 교재에서는 DFS 도중 유망한지 점검해서, 유망하지 않으면 가지치기 함

+ code

  ```python
  ```

  

### [1] 예시

#### (1) N-queen

+ 체스에서 N 개의 퀸을 서로 공격하지 못하게 배열하는 경우의 수 

##### (a) 코드

```python
def nqueen(arr:체스판, cur_node):
    if promising(cur_node):
        if cur_node에서 전체 답이 구해졌다:
            해에 추가
        else:
            for child of cur_node:
                nqueen(child)
                
def nqueen(arr, cur_node):
    if cur_node가 답 완결:
        해에추가
    else:
        for child of cur_node:
            if promising(child):
                nqueen(child)

# 2차원 arr의 index에 대해, 
# 오른쪽 아래 방향(\) 대각선은 (r,c)에서 r-c = -(N-1), -(N-2) , ... 0, 1, ... N-2, N-1         # 왼쪽 아래 방향(/) 대각선은 (r,c)에서 r+c = 0, 1, 2, 3, ... , 2N-2  
N = 8
arr = [[0]*N for _ in range(N)]
col = [0]*N
right_diag = [0]*(2*N-1) # r-c = -(N-1), -(N-2) , ... 0, 1, ... N-2, N-1  
left_diag = [0]*(2*N-1) # r+c = 0, 1, 2, 3, ... , 2N-2
result = 0
def nqueen(cur_r):
    r  = cur_r
    if r == N:
        result += 1
        
    else:
        for c in range(N):
           cr, cc = r, c
           if promising(cr,cc):
                col[cc] = 1
                right_diag[N-1 +(cr-cc)] = 1
                left_diag[cr+cc] = 1
                nqueen(cr + 1)
                col[cc] = 0
                right_diag[N-1 +(cr-cc)] = 0
                left_diag[cr+cc] = 0
                
    return


def promising(cr,cc):
    if col[cc] == 0 and right_diag[N-1+(cr-cc)] == 0 and left_diag[cr+cc] == 0:
        return True
    else:
        return False
       
    
```







## 3. 트리









# 그래프 & 백트래킹

+ 참고 : 2차원 배열의 조합생성방법
  + 1차원 배열에 2차원 배열 모두 저장한 후, 1차원 배열에서 조합 생성









# 그래프(04/01)

+ 그래프는 아이템들과 이들 사이의 연결 관계를 표현
+ N:N 관계를 가지는 원소들 표현에 용이
  + 선형 자료구조나 트리 자료구조로 표현하기 어려움



+ 문제 풀이 과정
  + 문제 -> 그래프화 -> 탐색
+ 경로
  + 단순 경로
    + 경로 중 정점을 최대 1번만 지나는 것
  + 사이클

## 1. 그래프 유형

+ 무향 그래프

+ 유향 그래프 

  + 무향 그래프, 유향 그래프는 데이터 저장할 때 딱 결정됨

    

+ 가중치 그래프 (Weighted Graph)

+ 사이클 없는 방향 그래프 (DAG, Directed Acylic Graph)

+ 완전 그래프
  + 정점들에 대해 모든 간선을 가진 그래프





## 2. 그래프 표현

+ 간선의 정보를 저장하는 방식, 메모리나 성능을 고려해서 결정

+ 저장방법

  ```python
  V, E = map(int,input().split())  # 정점 개수 / 간선 개수
  arr = list(map(int,input().split())) # 출발, 도착 정보 0 1 1 2 2 5 3 1 꼴
  adjM = [[0]*V for _ in range(V)] # 무향그래프(인접행렬)
  adjD = [[0]*V for _ in range(V)] # 유향그래프(인접행렬)
  adjL = [[]* V for _ in range(V)] # 인접리스트
  
  for i in range(E):
      v1, v2 = arr[i*2], arr[i*2+1]
      # 1. 인접행렬(무향그래프)
      adjM[v1][v2] = 1
      adjM[v2][v1] = 1
      # 1. 인접행렬(유향그래프)
      adjD[v1][v2] = 1
    
      # 2. 인접리스트(무향그래프)
      adjL[v1].append(v2)
      adjL[v2].append(v1)
      
      # 2. 인접리스트(유향그래프)
      adjL[v1].append(v2)
  ```

  

### [1] 인접 행렬

+ V x V  크기의 2차원 배열 이용해서 간선 정보 저장

+ 배열의 배열 (포인터 배열)

  ```python
  V, E = map(int,input().split())  # 정점 개수 / 간선 개수
  arr = list(map(int,input().split())) # 출발, 도착 정보 0 1 1 2 2 5 3 1 꼴
  adjM = [[0]*V for _ in range(V)] # 무향그래프(인접행렬)
  adjD = [[0]*V for _ in range(V)] # 유향그래프(인접행렬)
  adjL = [[]* V for _ in range(V)] # 인접리스트
  
  for i in range(E):
      v1, v2 = arr[i*2], arr[i*2+1]
      # 배열(무향그래프)
      adjM[v1][v2] = 1
      adjM[v2][v1] = 1
      # 배열(유향그래프)
      adjD[v1][v2] = 1
    
      # 인접리스트(무향그래프)
      adjL[v1].append(v2)
      adjL[v2].append(v1)
      
      # 인접리스트(유향그래프)
      adjL[v1].append(v2)
      
  ```

  



#### (1) 성질

+ 무향 그래프
  + i번째 행의 합 = i 번째 열의 합 = V_i의 차수
+ 유향 그래프
  + 행 i의 합 = V_i의 진출 차수
  + 열 i의 합 = V_i의 진입 차수



#### (2) 단점

+ 저장 공간을 많이 차지
  + 노드 개수가 1000 개 넘어가면 **인접리스트** / **간선의 배열** 고려



### [2] 인접리스트

+ 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장

  

  

#### (1) 장점

+ 인접행렬보다 메모리 조금 차지









### [3] 간선의 배열

+ 간선(시작정점, 끝정점)을 배열에 연속적으로 저장
+ 노드의 수가 간선의 수보다 훨씬 많은 경우 활용



+ | 간선개수 | 시작 정점 | 도착 정점 |
  | -------- | --------- | --------- |
  | 1        | 0         | 1         |
  | 2        | 0         | 2         |
  | 3        | 5         | 1         |





## 3. 그래프 순회

+ DFS, BFS

### [1] DFS

+ 지나왔던 정점의 정보를 저장해야함

+ 가장 최근에 방문했던 정점을 저장하거나 활용하기 위해 STACK, 재귀 이용

  



#### (2) 구현방법

+ STACK

  + stack에 넣기, visited 처리하기, 해당 노드에서 원하는 작업하기
  + 위 3가지의 배치에 따라 여러 구현 가능
    + stack 넣기 & visited 처리를 같은 위치에서 진행 -> pop 한 후 작업 진행
    + visited 처리 & 원하는 작업을 같은 위치에서 진행 -> pop 한 후, not visited 경우에 visted 처리 & 작업수행
  + 재귀로 구현 시, dfs() 호출하는 것이 stack에서 visitedFalse Node를 pop 하는 것과 같음

  

+ 재귀 구현

+ ```PYTHON
  # 1. 단순 dfs
  def dfs(G,v):
      visited[v] = True # 방문 설정
      
      for neighbor of v:
          if visited[neighbor] == False:
              dfs(G,neighbor)
  
              
  # 2. 모든 경로 구하기 dfs
   # 다른 경로 찾아서, 이전 단계로 return 한 후에 현재에게 돌아오는 것은 가능
  def dfs(G,v): 
  	visited[v] = True # 방문 설정
      for neighbor of v:
          if visited[neighbor] == False:
              dfs(G,neighbor)
          visited[neighbor] = False # 모든 경로 구하는 dfs 코드 
          
  # 3. 인접행렬 이용 단순 dfs
  def dfs1(v):
      visited[v] = 1
      print(v,"에서 진행할 작업")
      # v에 인접한 모든 노드에 대해
      for j in range(V):
          if adjM[v][j] == 1 and visited[j]==0: # 인접됐고, 방문x라면
              dfs1(j)
              
              
  # 4. 인접리스트 이용
  def dfs2(v):
      visited[v] = 1
      print(v,"에서 작업")
      for j in adjL[v]:
          if visited[j]==0:
              dfs2(j)
  
  ```



+ stack 구현

+ ```python
  # 1. 내가 주로 쓰는 법
  stack = [start]
  while stack:
      cur = stack[-1]
      
      for neighbor in adjL[cur]:
          if visited[neighbor]==False:
              stack.append(neighbor)
              visited[neighbor] = True
              break
      else:
          stack.pop()         
  
  # 2. stack / 인접리스트
  # 이 방법의 단점은 같은 노드가 중복돼서 stack에 들어감 -> stack의 크기를 미리 정할 수 없음
  stack = [start]
  while stack:
      cur = stack.pop()
      if visited[cur] == False:
          visited[cur] = True # 원하는 작업
          print(여기서 원하는 작업 진행)
          for neighbor in adjL[cur]:
              if visited[neighbor] == False:
                  stack.append(neighbor)
              
  # 3. stack/ 인접리스트 2
  # stack에 넣기 & visited 같이 진행
  stack = [start]
  visited[start] = True
  while stack:
      cur = stack.pop()
      print(여기서 원하는 작업 진행) # 원하는 작업
      for neighbor in adjL[cur]:
          if visited[neighbor]==False:
              stack.append(neighbor)
              visited[neighbor] = True
              
  ```

+ ```python
  # 내가 주로 쓰는 법의 이동경로 print 방법
  # version1, version2는 이동 순서 똑같은데, version1 은 중복되지 않게 방문된 곳 print함
  # version2는 모든 이동 경로를 print해서 중복되서 나옴
  #---------------------------------------------------version 1
  stack.push(1)
  # visited[1] = 1
  
  while not stack.is_empty():
      top = stack.top.value
      if visited[top] == 0:
  
          print(top, end=' ')
      visited[top] = 1
      # 경로 발견 즉시 이동
      for i in range(1,N+1):
          if adj[top][i] == 1 and visited[i] == 0 :
              stack.push(i)
              # visited[i] = 1
              break
  
      else:
          stack.pop()
  
  
  #-----------------------------------version 2-------------------
  stack = MyStack()
  stack.push(1)
  visited[1] = 1
  
  while not stack.is_empty():
      top = stack.top.value
      # if visited[top] == 0:
      #
      #     print(top, end=' ')
      # visited[top] = 1
      # 경로 발견 즉시 이동
      for i in range(1,N+1):
          if adj[top][i] == 1 and visited[i] == 0 :
              stack.push(i)
              visited[i] = 1
              break
  
      else:
          stack.pop()
  ```

+ 



### [2] BFS

#### (1) 정의

+ 탐색 시작점의 인접한 정점들을 모두 차례로 방문한 후에, 방문했던 정점을 시작으로하여 다시 인접한 정점들을 차례로 방문
+ 인접한 정점들에 대해 탐색한 후, 차례로 너비우선탐색을 해야해서 큐를 활용

+ 속도가 가장 빠른 구현
  + front, rear 로 위치 표시하고 ,enQueue 이용 (덱보다 빠름)





#### (2) 구현

+ Queue 이용

+ ```python
  # 1.
  queue = [start]
  visited[start] = 1
  while queue:
      cur = queue.pop(0)
      for neighbor in adjL[cur]:
          if visited[neighbor]==0:
          	queue.append(neighbor)
              visited[neighbor] = 1 + visited[cur] # start와의 거리를 알 수 있음
  ```



#### (3) 활용

+ 비상연락망
  + 동시에 최대 몇 사람이 연락을 받겠는가?
  + #1.의 구현 후, visited 배열 원소를 count 배열로 횟수 세면 됨



# MST

## 1. 서로소 집합

+ 교집합이 없음
+ 집합에 속한 하나의 특정 멤버(대표자)를 통해 각 집합들을 구분



### [1] 활용

+ 부모-자식 관계만 주어질 때, 이게 몇 개의 트리인가 판단



### [2] 상호 배타 집합 표현/연산

#### (1) 트리 이용

+ **하나의 집합을 하나의 트리로 표현**

+ 대표자

  + 루트노드

+ 자식 노드가 부모 노드를 가리킴

  

  

#### (2) 트리 표현/연산

+ 자식노드를 INDEX, 값을 부모노드로 하는 배열로 트리표현

  + 대표자(root)가 몇 개인지 세면 몇 개 트리인지 알 수 있음

+ 연산 3가지

  + Make-set(x) : x를 대표로하는 {x} 집합 생성
  + Find_Set(x) : x를 포함하는 집합 찾기
  + Union(x,y) :  x 집합의 대표 원소를, y집합의 대표 원소가 가리키게 함
    + x,y집합 합치는 것
    + `p[Find_set(x)] = Find_set(y)` 로 구현

+ 설명

  | 연산                                                         | index    | 1    | 2    | 3    | 4    | 5    | 6    |
  | ------------------------------------------------------------ | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
  | make_set(1)~(6)                                              | p        | 1    | 2    | 3    | 4    | 5    | 6    |
  | union(1,3)                                                   | p        | 1    | 2    | 1    | 4    | 5    | 6    |
  | union(2,3) <br />3의 대표원소 y 찾아가서,<br /> y의 대표원소를 2의 대표원소 x로 교체 | p        | 2    | 2    | 1    | 4    | 5    | 6    |
  | union(5,6)                                                   | p        | 2    | 2    | 1    | 4    | 5    | 5    |
  | findset(6)                                                   | 5 return |      |      |      |      |      |      |

  

+ 코드

+ ```PYTHON
  # a = 1, b = 2 ,,로 생각
  # 1. Make-Set(a) ~ Make-set(f) : set(tree) 초기화
  [x,1,2,3,4,5,6] #: index와 같은 값으로 초기화 된 배열을 이용
  
  # 2. Union(c,d) : set 합치기 - 대표원소 c인 것과 d인 것 합치고, 대표원소는 c로
  [x,1,2,3,3,5,6] # index가 자식이고, value가 부모(대표자 아님!)
  
  Union(e,f) -> [x,a,b,c,c,e,e]
  Union(d,f) -> [x,a,b,c,c,c,e]  # f의 대표원소까지 쭉 찾아가서, 그 대표원소가 d의 대표원소를 가리키도록 (자기 자신을 가리킬 때까지 따라가야 그것이 대표)
  
  # 3. Find-set(d)
  
  
  
  ```

  

  

## 2. MST (최소신장트리)

### [1] 활용

+ 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
+ 두 정점 사이의 최소 비용 경로 찾기



### [2] 정의

+ Spanning Tree(신장트리)
  + n 개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

+ Minimum Spanning Tree(최소신장트리)
  + 무방향 가중치 그래프에서 신장트리를 구성하는 간선들의 가중치의 합이 최소가 되는 신장트리



### [3] 표현

+ 2차원 arrL\[r]\[c] =weight_{rc} 로 생성 (인접리스트활용)
+  

### [4] 존재성 증명

+ 수학적 귀납법으로 증명가능

  ```python
  # k : 노드개수
  1. k = 2 경우
   - 아무 노드 선택해서 최소비용간선 선택하면 MST
  
  2. k =< n 경우 MST 일 때, k = n+1에서 MST임을 보이자
  1) n+1개 node 중 아무것이나 1개를 없다고 생각하기
  2) 나머지 n개 node들은 가정에 의해 MST_n 를 찾음(더 여러개의 tree로 쪼개어 질 수도 있음/그래도 아래과정은 같음)
  3) 이제 1)에서 없다고 생각한 n+1 번 노드가 MST_n과 연결된 간선들을 모두 탐색
  4) 만약 n+1 번 노드가 MST_n과 r 개 node가 연결되었다고 가정한다면
   4-1) r개의 node를 m1, m2, ..., mr 로 표기 
   4-2) m1, m2, ..., mr 과 연결된 기존 MST_n 의 노드들을 a1, a2, ... , ar (1~n사이값)로 표기
   4-3) n+1과 m1, m2, ..., mr 중 최소 비용 간선 선택
   4-4) 그럼 현재 n+1개 노드는 모두 연결되어 있음
   4-5) 나머지 {m1, m2, ..., mr}-{최소비용 mi} 와 연결된 a1, a2, ..., ar 과의 간선값들 중 (n+1 <-> mi) < (mi <-> ai) 인 경우에 기존 연결을 끊고, n+1 번 노드와 연결 (기존 연결보다 n+1과의 연결 비용이 적다면)  : 즉 현재 MST에 연결된 간선 가중치보다 n+1 번과 연결된 간선 가중치가 더 좋으면 간선 바꾸기 ( 간선을 끊으면 2개의 트리로 분리되므로 다시 n+1과 이어주면 됨)
  5) MST_(n+1) 완성
  ```

  

### [4] MST 찾는 알고리즘

+ 정점이 많은 경우 어떤 방법이 좋을지 생각해봐야 함
+ 전체 그래프에서 **MST는 여러개 일 수 있음**
  + 각 알고리즘은 여러 MST 중 하나를 만들게 됨


#### (1) Prim 알고리즘

+ 의미
  + MST에 포함된 정점에서 연결된 간선들 중에 하나씩 **Greedy**하게 선택하면서 MST를 만들어 가는 방식

+ 과정
  + 시작 : 임의의 정점 v 선택해서 MST에 포함
    + 반복 : **MST에 포함된 모든 정점에서 최소비용 간선의 정점 u(not in MST)선택**
  + 모든 정점 선택될 때까지, 바로 위 과정 반복
+ point
  + 서로소인 2개의 집합 정보를 유지(visted로 구분)
    + MST에 선택된 정점들 표현
    + MST에 선택되지 않은 정점들 표현
  + 사이클 형성 방지해서 선택
  + **이미 선택된 노드들 사이의 간선관계는 바뀔 수 없음!**
    + 바뀔 수 있다고 가정하면 모순



+ 코드

  ```PYTHON
  V, E = map(int,input().split())
  adjM = [[0]*(V+1) for _ in range(V+1)]
  adjL = [[]*(V+1) for _ in range(V+1)]
  for _ in range(E):
      u, v, w = map(int,input().split())
      adjM[u][v] = w
      adjM[v][u] = w
      
      # 인접리스트 방법
      adjL[u].append((v,w))
      adjL[v].append((u,w))
      
  #-----------------------prim1 미완성 key 이용------------------
  def prim1(r, V):
      MST = [0]*(V+1) # MST 포함여부
      key = [10000]*(V+1) #  key : 가중치 
      key[r] = 0     # 시작 정점의 key값 
      for _ in range(V):
          u = 0
          minV = 100000
          # key 값 최소 찾기
          for i in range(1,V+1):
              if MST[i] == 0 and key[i] <minV:
                  u = i
                  minV = key[i]
          MST[u] = 1
          for v in range(V+1):
              if MST[v] == 0 and adjM[u][v] >0 : # 새로 추가된 노드 u에서 MST에 포함안된 연결노드들 KEY값에 반영
                  key[v] = min(key[v], adjM[u][v]) # key 값을 update
  
                  
  #--------------이걸로 이해하기-----------------------------------------
  def prim2(r, V):
      MST = [0]*(V+1) # MST 포함여부
      MST[start] = 1    # 시작 노드 start
      weight_sum = 0         # MST 가중치 합
      for _ in range(V):
          min_idx = 0  # 내가 선택할 정점 번호를 초기화
          minV = 100000
          for i in range(1,V+1):
              if MST[i] == 1: # 현재 연결된 것들에서 최소 가중치 간선 찾기
                  for j in range(1,V+1):
                      if 0 <adjM[i][j] < minV and MST[j]== 0: # 기존의 것과 연결안되어 있고, 최소비용간선이면 update
                          min_idx = j
                          minV = adjM[i][j]
          weight_sum += minV
          MST[min_idx] = 1
  ```
  
  



#### (2) Kruskal 알고리즘

+ 정점 수 많을 때 prim 보다 효과적

+ 의미
  + 최소값 간선을 하나씩 선택해서 MST를 찾는 알고리즘
+ 과정
  + 모든 간선을 가중치에 따라 오름차순 정렬
  + 가중치가 최소인 간선부터 선택하면서 트리를 증가
    + 사이클이 존재하면 다음 순서 가중치 간선 선택(사이클 생기는 것은 고려 x)
  + n-1개 간선이 선택될 때까지 바로 위 과정을 반복
+ point
  + 사이클 존재 안하도록 잘 하기
  + **disjoint set(상호배타 집합) 사용**
  + Find_Set(a), Union_Set(a,b) 이용
    + Find_Set(a) != Find_Set(b): 서로 다른 트리라면
      + Union_set(a,b) 인듯?





## 3. 최단경로

### [1] 정의

+ 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로



###  [2] 

#### (1)다익스트라(diijkstra) 알고리즘

+ 시작 정점에서 거리가 최소인 정점을 선택해 나가면서, 최단 경로를 구하는 방식

+ 음의 가중치 허용 x

+ Greedy 기법사용한 것으로, MST prim 과 유사


+ 출발점만 있으면, 나머지 모든 정점을 지나는 최소값을 알 수도 있음

+ 과정


  + 인접행렬(값이 비용)과 비용리스트(무한대로초기화), 선택된 정점집합 필요

  + 아래는 a에서 f까지 가는 최소비용 구하는 과정

  + ![다익스트라](0214_알고리즘.assets/다익스트라.PNG)

  + | 선택된 노드들(아래)                           | a    | b     | c     | d     | e     | f     |
    | --------------------------------------------- | ---- | ----- | ----- | ----- | ----- | ----- |
    | a 기준으로 최소비용 (a 선택된 상태)           | 0    | **2** | 4     | inf   | inf   | inf   |
    | a->b 상태에서 최소비용 (a,b 선택된 상태)      | 0    | 2     | **3** | 9     | inf   | inf   |
    | a->b->c 상태에서 최소비용 (a,b,c 선택된 상태) | 0    | 2     | 3     | 9     | **6** | inf   |
    | a->b->c->e 상태에서 최소비용                  | 0    | 2     | 3     | **8** | 6     | 11    |
    | a->b->c->e->d  상태에서 최소비용              | 0    | 2     | 3     | 8     | 6     | **9** |

    




#### (2) 벨만-포드 (Bellman-Ford) 알고리즘

+ + 음의 가중치 허용


### [3]
+ 플로이드- 워샬(Floyd-Warshall) 알고리즘
  + DP에서 나옴





# 백트래킹



+ 





# 참고사항

## 1. SWEA

+ 제한시간 1초문제 : C/C++ 기준 10억번 반복 (1억 반복에 10억연산의미)
  + 1억회 반복정도로 해야, 안전하게 다른 연산까지 가능
  + 12! = 4억7900만





## 2. 일반사항

### [1] Linked List / Array List

+ Linked List
  + 장점은 삽입/삭제 많을 때 유리
  + 크기 고정 x
  + 다음 요소의 주소를 저장
  + 

+ array list는 크기 고정되게 만드는 것
  + 장점은 idx 접근이 빠름
  + 요소 접근이 많을 때 유리



+ 전체 stack or queue의 크기를 어느정도 아는 경우
  + 메모리를 좀 희생해서, 선형 stack or queue 만들어서, 여기서 idx로 접근하는 것이 빠름
  + 즉 top이라는 변수가 어떤 idx를 가리키게 해서, 배열을 변경하는 것이 아니라 idx를 왔다갔다 하면서 top이 가리키는 idx에 값을 집어 넣기
  + stack 구현할 때, node를 top으로 두지 않고, top의 위치를 top이 가리키게 하는 게 더 빠름
  + **요약하면**
    + stack이 arr로 구현되어 있을 때, pop,push 연산하면, arr 을 크기 맞춰서 새로 만든 후 기존의 arr을 복사해야함 -> 시간 오래걸림
    + 따라서 stack의 maximum 크기를 알고 있다면, 그 크기만큼 arr 선언해둔 후, top 이라는 idx를 이용해 왔다갔다하며 idx 접근을 하도록 구현하는 것이 더 빠름





### [2] global 변수

+ 함수내에서 변수 이용시 언제 global 을 이용해야 하는가?
  + 함수내에서 global 변수에 assign(=)이 발생하고, 값이 바뀌는 경우에 사용해야 함
+ 예:
  + 힙에서 마지막 위치를 가리키는 last 변수는 global 변수로 이용해야 함
  + 순열의 수 구할 때, used = [배열] 의 경우, used는 주소를 참조하는 것이기 때문에, 배열이 바뀌어도, used  가 가지고 있는 값은 안바뀌어서, global로 안써도 됨

+ LEGB 순으로 변수명 탐색하는데, 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 불가
  +  그 이유는 함수는, 그것 자체로 실행되고 끝나는 것이고, 밖의 것을 건들지 않는 것이 원칙이기 때문
