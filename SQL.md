

## 작성순서

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





### (2) 집계 및 연산함수

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

