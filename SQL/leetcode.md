[toc]

## 목차

+ [SQL 스터디 플랜](#sql 스터디 플랜)
  + [SQL1](#sql 1)
    + [Day1 select](#day1 select)
    + [20220627](#20220627)
    + [Day2](#Day2-Select-&-Order)
    + [Day3 String processing function](#day3-string-processing-function)
    + [Day4 Union & Select](#day4-union-&-select)
    + [Day5 Union](#day5-union)
    + [Day6 Union](#Day6-Union)
    + [Day7 Function](#Day7-Function)
    + [Day8 Function](#Day8-Function)
    + [Day9 Control of Flow](#Day9-Control-of-Flow)
    + 
+ [SQL1-공부내용](#sql1-공부내용)
  + [Day1](#day1)
  + [Day2](#day2)
  + [Day3](#day3)
  + [Day4](#day4)
  + [Day6][#Day6]
  + [Day7](#Day6)
  + [Day8](#Day8)








## SQL 스터디 플랜

### [SQL 1](https://leetcode.com/study-plan/sql/?progress=sa467n3)

#### Day1 Select

+ 595
+ [1757](https://leetcode.com/problems/recyclable-and-low-fat-products/)
+ 584
+ [183](https://leetcode.com/problems/customers-who-never-order/)
  + 두 개의 TABLE 이용



#### 20220627

+ [607](https://leetcode.com/problems/sales-person/)
  + 3 개의 table 이용 / join활용



#### Day2 Select & Order

+ [1873](https://leetcode.com/problems/calculate-special-bonus/)
  + 몫연산자 `%`, `IF`문으로 값 대치
+ [627](https://leetcode.com/problems/swap-salary/)
  + `update set`
+ [196](https://leetcode.com/problems/delete-duplicate-emails/)
  + `delete`





#### Day3 String processing function

**다시풀기**

+ [1667](https://leetcode.com/problems/fix-names-in-a-table/)
  + `UPPER(), LOWER(), SUBSTRING(), CONCAT()`

+ [1484](https://leetcode.com/problems/group-sold-products-by-the-date/)
  + `GROUP_CONCAT(field_name ORDER BY filed_name SEPORATOR ',')`

+ [1527](https://leetcode.com/problems/patients-with-a-condition/)
  + `LIKE "%"` 

  



#### Day4 Union & Select

+ [1965](https://leetcode.com/problems/employees-with-missing-information/)
  + `UNION()`
+ [1795](https://leetcode.com/problems/rearrange-products-table/)
  + `UNION()`
+ [608](https://leetcode.com/problems/tree-node/)
  + `CASE WHEN`

+ [176](https://leetcode.com/problems/second-highest-salary/)
  + `null`을 만들기 위해, 이중 select 문이용





#### Day5 Union

+ [175](https://leetcode.com/problems/combine-two-tables/)
  + `LEFT JOIN`
+ [1581](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/)
  + `LEFT JOIN`
  + 손님 TABLE, 거래 TABLE 이용해서, 거래 없는 손님 찾기
+ [1148](https://leetcode.com/problems/article-views-i/discuss/422348/Three-approaches-(MYSQL))
  + 3가지 방법의 풀이해보기
    + distinct 이용
    + 이중 select 이용
    + distinct 대신 group by 이용




#### Day6 Union

+ [197](https://leetcode.com/problems/rising-temperature/)

  + 날짜연산

  + `subdate(날짜, +- 숫자하면, 그만큼의 날을 더하거나 빼기)`

    + 예

      ```sql
      subdate(2022-01-03, 2) => 2022-01-05
      subdate(2022-01-03, -2) => 2022-01-01
      ```

+ [607](https://leetcode.com/problems/sales-person/)
  + 3개 table 연산





#### Day7 Function

+ [1141](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/)
  + `datediff(날짜1, 날짜2) = 날짜1 - 날짜2 의 정수 output` 이용!

+ [1693](https://leetcode.com/problems/daily-leads-and-partners/)
  + `group by` 에 2개 컬럼 

+ [1729](https://leetcode.com/problems/find-followers-count/)



#### Day8 Function

+ [586](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/)
  + 주문자, 주문번호가 주어질 때, 가장 주문 많이한 사람 찾기
  + `group by` & `order by` 이용

+ [511](https://leetcode.com/problems/game-play-analysis-i/)
  + 플레이어들의 로그인 기록이 있을 때, 각 플레이어의 첫 로그인 날짜 구하기
+ [1890](https://leetcode.com/problems/the-latest-login-in-2020/)
  + timestamp 에서 특정 년도를 조회하는 여러 방법 해보기
    + year 함수
    + like 2020% 등 : 이게 더 빠름!
+ [1741](https://leetcode.com/problems/find-total-time-spent-by-each-employee/)
  + `select` 에서 - (빼기) 연산 가능
  + 여러 날짜에 대해 노동자들의, 들어가는 시간, 나가는 시간 주어 졌을 때, 각 날짜별로 노동자들의 노동시간 합 구하기





#### Day9 Control of Flow

+ [1393](https://leetcode.com/problems/capital-gainloss/)
  + 사고 판 내역이 한 테이블에 있을 때, 이익이 얼마인지!
  + `if`로 - 만들어 주기
+ [1407](https://leetcode.com/problems/top-travellers/)
  + 명단 테이블과 이동거리 테이블이 있을 때, 각 사람들의 이동거리를 합해서 많이 이동한 순으로 보여주기
  + `left join`, `if` 로는 null을 0으로 처리

+ [1158](https://leetcode.com/problems/market-analysis-i/)
  + 2개 테이블 join 할 때, on에 and조건 넣으면 null도 0으로 처리할 수 있음
    + where에 넣으면 처리가 안됨..null인 것들이 없어져서 0으로 못만듦.





## SQL1-공부내용

### Day1

+ where 절에서, 2개의 컬럼에 대해서 `or` 이용시, 각 컬럼에 대해서 where 적용한 후, `UNION` 하는 것이 더 빠름인 줄 알았으나, 그렇지 않음

  + [595번참고](https://leetcode.com/problems/big-countries/discuss/103561/Union-and-OR-and-the-Explanation)

+ boolean 응답을 percentage로 바꾸는 방법

  + low_fats = Y 이거나 recyclable = Y 인 비율 구하는 코드

  + ```sql
    SELECT ROUND(AVG(CASE WHEN low_fats = 'Y' OR recyclable = 'Y' THEN 1 ELSE 0 END),2) AS PERCENTAGE from products
    ```

  + [1757번참고](https://leetcode.com/problems/recyclable-and-low-fat-products/discuss/1062936/SQL-1-liner-solution-(This-is-a-FB-DE-interview-question))

+ `NULL` 값의 경우 `COL !=2` 와 같이 하면 잡히지 않음. `COL IS NULL` 처럼 잡아줘야 함
  
  + [584번참고](https://leetcode.com/problems/find-customer-referee/)



### Day2

+ `DELETE FROM 테이블이름 WHERE 조건들;`

  + ```sql
    # p1 테이블에서, p2 테이블과 email 같고, id가 큰 것 삭제
    delete p1 from person p1, person p2
    where p1.email = p2.email and p1.id > p2.id;
    ```

  + 

+ `UPDATE 테이블이름 SET 컬럼이름 = 설정할 값 WHERE 조건들;`

  + salary table의 sex column의 값을 서로 바꾸기 : update & set

  ```sql
  update salary
  set sex = if(sex='m','f','m');
  ```





### Day3

+ 첫글자만 대문자만들기

  ```SQL
  select Users.user_id, CONCAT(UPPER(SUBSTR(Users.name,1,1)), SUBSTR(LOWER(Users.name),2)) name               from Users 
  ```

+ [GROUP_CONCAT 블로그참고](https://fruitdev.tistory.com/16)

  

  + ```
    1. 기본형 : group_concat(필드명)
    2. 구분자 변경 : group_concat(필드명 separator '구분자')
    3. 중복제거 : group_concat(distinct 필드명)
    4. 문자열 정렬 : group_concat(필드명 order by 필드명)
    ```






### Day4

+ `[]`를 `NULL`로 만들려면, `[]`를 SELECT 하면 됨

  + ```sql
    select (select distinct salary 
    from employee
    order by salary desc
    limit 1 offset 1) SecondHighestSalary
    ```

+ `IFNULL` 사용법

  + `IFNULL(컬럼명, "NULL시 대체값")`
  + `IF(IS NULL(컬럼명), "NULL시 대체값", "NULL 아닐 경우 값")`





### Day6

+ `subdate(date, 숫자)` 연산방법

  ```SQL
  subdate(2022-01-03, 2) => 2022-01-05
  subdate(2022-01-03, -2) => 2022-01-01
  ```

+ 같은 table의 서로 다른 행끼리도 연산 가능하다.

  아래 처럼 하면, 같은 table의 앞, 뒤 행 끼리의 열(컬럼)에 대해서 연산이 진행됨

  ```sql
  select w2.Id id
  from weather w1, weather w2
  where subdate(w2.recordDate, 1) = w1.recordDate AND w1.temperature < w2.temperature
  ```

  



### Day7

+ `datediff(날짜1, 날짜2)`

  + 날짜1 - 날짜2 를 정수 output

    

+ `timestampdiff(단위, 날짜1, 날짜2)`

  + 단위로는
    + second, minute, hour, day
    + week, month, quarter, year



### Day8

+ where에서 timestamp에 대해서, 특정 년도 고를 때, year 보다 like 이용하는 것이 빠름
+ select 문에서 - 연산 가능하다.
