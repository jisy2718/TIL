[toc]

## 목차

+ [SQL 스터디 플랜](#sql 스터디 플랜)
  + [SQL1](#sql 1)
    + [Day1 select](#day1 select)
    + [20220627](#20220627)
    + [Day2](#Day2-Select-&-Order)
+ [SQL1-공부내용](#sql1-공부내용)
  + [Day1](#Day1)
  + [Day2](#Day2)








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
  + 몫연산자 `%`, `if `문으로 값 대치
+ [627](https://leetcode.com/problems/swap-salary/)
  + `update set`
+ [196](https://leetcode.com/problems/delete-duplicate-emails/)
  + `delete`












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

+ 

