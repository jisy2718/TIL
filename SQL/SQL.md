[toc]





## 작성 및 실행 순서

### (1) 기본형

```SQL
# 기본형
SELECT * FROM _
WHERE colname = "조건" and ...
GROUP BY colname
HAVING 
ORDER BY colname asc, colname2 desc
LIMIT

```

```SQL
# 다음 순으로 실행됨
FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
```





### (2) Join

```sql
# join

```





## 문법

### (1) where

| 연산자               | 의미                                         | 예                                                           |
| -------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| =, !=, <, >          | 1가지 조건                                   | col = '조건'                                                 |
| IN("A","B","C")      | A,B,C 중 1개라도 만족하면                    | col IN ("A","B","C")                                         |
| Between "A" AND "B"  | A와 B사이에 있는 값                          | col between "1" and 10<br />col between "2022-06-21" and "2022-08-23" |
| IS NULL, IS NOT NULL | NULL / NOT NULL 인 값 추출                   | col IS NULL / col IS NOT NULL                                |
| LIKE "비교"          | % : 모든 글자(글자없어도가능)<br />_ : 1글자 | col LIKE "가%" => 가, 가나, 가나다, 가나다라,...<br />col Like "가_" => 가나 |
| AND / OR             | 여러 조건 이용시                             |                                                              |





### (2) 집계함수

#### MIN, MAX

```SQL
SELECT MIN(colname), MAX(colname2) FROM _
```

+ MIN, MAX 1개 값 가져옴



#### COUNT, SUM, AVG

```SQL
SELECT count(*) AS count, SUM(numeric_column) AS total_sum, AVG(nuemeric_column) FROM _
```

+ COUNT는 row의 개수를 세어줌
+ sum, avg는 numeric column의 합, 평균





#### DISTINCT

```sql
SELECT DISTINCT(colname) FROM _
SELECT COUNT(DISTINCT(colname)) FROM _  # 다른 함수와 함께 사용 가능
```

+ 유일한 column만 선택



### (3) DATETIME

#### 형변형

+ **2014-12-27 12:59:00** 과 같은 꼴의 데이터의 경우, 세부내용 추출방법

```SQL
DATE(DATETIME) -> 2016-06-25 00:00:00 꼴

YEAR(DATETIME)   -> 정수
MONTH(DATETIME)  -> 정수
DAY(DATETIME)    -> 정수

HOUR(DATETIME)   -> 정수
MINUTE(DATETIME) -> 정수
SECOND(DATETIME) -> 정수
```

+ 위 처럼 추출한 것을 `WHERE`, `GROUP BY` 에 사용가능



#### 연산

+ 뺄셈연산으로 기간 비교 가능 (프로그래머스 오랜기간보호한동물(2))

  ```sql
  # 기간의 차이가 큰 순으로 정렬할 때
  SELECT ins.animal_id , ins.name from animal_ins as ins
  right join animal_outs as outs
  on ins.animal_id = outs.animal_id
  order by outs.datetime - ins.datetime desc # 이와같이 사용 가능
  limit 2
  ```

  





### (4) UNION / UNION ALL

+ 두 개의 TABLE을 하나로 합치는 명령어 (행을 늘리는 방식으로 합침 == 아래로 길어지게 합침)

  ```SQL
  # UNION 의 경우 중복행이 있다면 제거
  SELECT * FROM TABLE1
  UNION (DISTINCT 가 생략되어 있음)
  SELECT * FROM TABLE2;
  
  # UNION ALL의 경우 중복도 포함 시킴
  SELECT * FROM TABLE1
  UNION ALL
  SELECT * FROM TABLE2;
  ```

  

  



### (5) WITH RECURSIVE

+ SQL에서 재귀커리를 이용하는 명령어

  ```SQL
  # 기본 꼴
  WITH RECURSIVE 테이블명 AS (    # 재귀과정을 진행하며, 만들 임시 TABLE
      SELECT 초기값 AS 별명
      UNION ALL
      SELECT 별명 반복식 FROM 테이블명 WHERE 반복 멈추는 조건
  )
  
  # 예시(0~23 생성하기)
  WITH RECURSIVE HOURS_TABLE AS(
       SELECT 0 AS 24HOUR  # 결과물에 보여질 COLNAME
       UNION ALL
       SELECT 24HOUR+1 FROM HOURS_TABLE WHERE 24HOUR<24 )
  
  SELECT * FROM HOURS_TABLE
  
  >>>
  24HOURS
  -------
  0
  1
  2
  3
  4
  5
  ...
  22
  23
  ```







### (6) JOIN & ON

**기능 및 작동** (수정)

+ 2 개의 TABLE을 합칠 수 있게 해줌

+ JOIN 방법 + ON 조건을 이용해서 TABLE의 JOIN 방법을 정하고, ON 뒤의 조건에 맞게 데이터 조작

  ```SQL
  SELECT TABLE1_COL2, TABLE2_COL3 FROM TABLE1
  LEFT OUTER JOIN TABLE2
  ON (TABLE1_COL1 = TABLE2_COL2)
  ```

  + 위 경우 TABLE1_COL1과 TABLE2_COL2 값이 같은 행들이 모두 붙게 됨

  

**종류**

+ 3가지 JOIN 존재

  

**1. OUTER JOIN**

+ 기능

  + 기준 TABLE의 전체 데이터에 대해서 결과 보여줌

  + 즉, ROW의 개수는 기준 TABLE의 ROW 개수

    

+ 3가지 방향 존재

  + `LEFT` : 왼쪽 테이블 기준 값이 출력

  + `FULL` : 왼쪽 + 오른쪽 테이블 모두의 값이 출력

  + `RIGHT` : 오른쪽 테이블 기준 값이 출력



**2. INNER JOIN**

+ 기능
  + 두 개의 TABLE 모두에 있는 데이터의 결과만 보여줌



**3. CROSS JOIN**







### (7) NULL 대치법

**IFNULL(COL,대치할 것)**

+ NULL인 값을 다른 값으로 바꾸는 방법

  ```SQL
  SELECT COL1, IFNULL(NAME,"No name") AS NAME FROM MY_TABLE
  ORDER BY COL1
  ```

  + NAME 열의 값이 NULL인 경우 "No name"으로 출력







## 프로그래머스

### (1) GROUP BY

+ [프로그래머스 입양시각 구하기(2)](https://programmers.co.kr/learn/courses/30/parts/17044)

  ```SQL
  WITH RECURSIVE TOTAL_HOUR AS (   # WITH를 이용해 0~23이 존재하는 TABLE을 생성한다.
     SELECT 0 AS 24HOURS
     UNION ALL
     SELECT 24HOURS + 1 FROM TOTAL_HOUR WHERE 24HOURS < 23 # 0~23이 존재하는 TABLE 생성
  )
  SELECT 24HOURS AS HOUR, COUNT(HOUR(DATETIME)) FROM TOTAL_HOUR 
  LEFT OUTER JOIN ANIMAL_OUTS     # TOTAL_HOUR이 LEFT이고, LEFT OUTER를 LEFT것 기준 전체
  ON (24HOURS = HOUR(DATETIME))   # JOIN 조건
  GROUP BY 24HOURS
  ```






### (2) IF문

+ **IF(조건, 조건만족시, 조건 불만족시)** [프로그래머스 중성화여부 파악하기](https://programmers.co.kr/learn/courses/30/parts/17047)

```SQL
SELECT animal_id, name, if(SEX_UPON_INTAKE like "%Neutered%" or SEX_UPON_INTAKE like "%spayed%", "O", "X") from animal_ins
order by animal_id
```







## LEET CODE

### (1) NULL 처리 하는 법

+ [LETTCODE 176](https://leetcode.com/problems/second-highest-salary/)

  ```SQL
  # 1. 데이터 없는 경우 NULL로 처리되는 경우
  select (select distinct salary from employee order by salary desc limit 1 offset 1) as SecondHighestSalary  # 아무래도 없는 데이터를 SELECT하면 NULL 처리 되는 것 같다.
  
  # 2. 데이터 없는 경우, NULL 처리 안되고 그냥 공백되는 경우
  select distinct salary as SecondHighestSalary
  from Employee
  order by salary DESC
  limit 1 offset 1;
  ```

  
