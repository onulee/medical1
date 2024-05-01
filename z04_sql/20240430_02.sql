-- employees테이블에서 
-- 사번,이름,월급,실제월급(월급+(월급*커미션)),월급*1410 kor_salary 출력하시오.
-- kor_salary만 원화표시, 천단위표시


select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)),
to_char(salary*1410,'999,999,999')
from employees
;

select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)) from employees;



select department_id,round(avg(salary),2),max(salary),min(salary) from employees
where department_id is not null
group by department_id
order by department_id
;

select * from stu_score
order by no;

-- 홍 이라고 검색하면 홍에 관련된 학생이 모두 출력되도록 하시오.
select * from stu_score
where name like '%홍%'
;

select * from stu_score
where avg>=60
order by no
;

select * from stu_score
where avg<60
order by no
;

select * from stu_score
where kor>=60
order by no
;

-- equi join
-- 사원번호,사원명,부서번호,부서명 을 출력하시오.
select employee_id,emp_name,a.department_id,department_name
from employees a,departments b
where a.department_id = b.department_id and emp_name like '_a%'
and salary>=(select avg(salary) from employees )
;

-- 그리고, 이름 두번째 자리에 a가 들어가는 사원을 검색하시오.
select emp_name from employees
where emp_name like '_a%'
;

-- 월급이 평균이상인 사람만 검색하시오.
select salary from employees
where salary>=(select avg(salary) from employees)
;

select * from employees;

select * from jobs;

-- 사원번호 e,사원명 e,부서번호 e,부서명 d,     직급번호 e,직급명 jobs 출력하시오.
select employee_id,emp_name,a.department_id,department_name,a.job_id,job_title
from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id
;


select * from jobs;

-- 사원번호,사원명,월급,최소월급분,인상분,직급,직급타이틀 출력하시오.
-- 최소월급 몇% 이상을 받고 있는지 출력(최소월급 / 현재월급 * 100)

select employee_id,emp_name,salary,min_salary,to_char(round(((salary-min_salary)/salary)*100,2))||'%',a.job_id,job_title
from employees a, jobs b
where a.job_id = b.job_id
;

-- job_title Manager 글자가 들어가 있는 
-- 사원번호 e,사원명 e,직급번호 e,직급명 j ,월급 e,최대월급 j 을 출력하시오.
select employee_id, emp_name,a.job_id,job_title,salary,max_salary
from employees a,jobs b
where a.job_id = b.job_id and job_title like '%Manager%'
;

select * from jobs;


select a.user_id,user_name,user_phone,user_address1,user_address2
user_address3
from User a, Deliver_address b
where a.user_id = b.user_id
;

create table stu_grade (
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'A',90,100
);
insert into stu_grade values(
'B',80,89
);
insert into stu_grade values(
'C',70,79
);
insert into stu_grade values(
'D',60,69
);
insert into stu_grade values(
'F',0,59
);

commit;

select * from stu_grade;

select avg from stu_score;

-- case when then grade컬럼 90이상 A,80점 B.... 학점을 출력하시오.
select no,name,avg,
case 
when avg>=90 then 'A'
when avg>=80 then 'B' 
when avg>=70 then 'C'
when avg>=60 then 'D' 
else 'F' end as grade 
from stu_score
order by no
;

-- non-equi join
select no,name,avg,grade from stu_score,stu_grade
where avg between low_score and high_score
order by no
;

-- stu_score,stu_grade 같은 컬럼이 없음.
-- 2개 테이블을 join : non-equi join
select * from stu_score;
select * from stu_grade;



update stu_grade set low_score=92
where grade = 'A'
;

update stu_grade set low_score=62,high_score=71
where grade = 'D'
;
update stu_grade set high_score=62
where grade = 'F'
;

commit;

-- 월별매출액을 기준으로 고객등급


-- 지역별 대출합계를 출력하시오.
select * from kor_loan_status;
select region,gubun,sum(loan_jan_amt)
from kor_loan_status
group by region,gubun
order by region
;

select region,sum(loan_jan_amt)
from kor_loan_status
group by region
order by region
;

-- 년도별,지역별,대출합계금액
select substr(period,1,4),region,sum(loan_jan_amt)
from kor_loan_status
group by substr(period,1,4),region
order by region
;


-- 부서별 월급 합계를 출력하시오.
select department_id,sum(salary) a 
from employees
group by department_id
order by a
;

-- 시간대별,연령대별 판매량 총합을 출력하시오.
select * from lotte_product;
select time_cd,age_cd,sum(purh_amt) a
from lotte_product
group by time_cd,age_cd
order by a desc
;

select * from lotte_product;

select * from shop_product;

-- 2024/03/01 이후 이름별, 금액합계를 출력하시오.
select name,sum(amount) from shop_product
where pdate>='2024/03/01'
group by name
;

-- customer_rank테이블 생성
-- rank, lower_amount, high_amount
-- 100만원미만 BRONZE
-- 200만원미만 SILVER
-- 300만원미만 GOLD
-- 300만원이상 PLATINUM

create table customer_rank (
rank varchar2(10) primary key,
lower_amount number,
high_amount number
);


insert into customer_rank values(
'BRONZE',0,999999
);
insert into customer_rank values(
'SILVER',1000000,1999999
);
insert into customer_rank values(
'GOLD',2000000,2999999
);
insert into customer_rank values(
'PLATINUM',3000000,9999999
);

commit;

select * from customer_rank;

-- non-equi join
select no,name,avg,grade from stu_score,stu_grade
where avg between low_score and high_score
;

-- name,sum(amount),rank 출력하시오.
-- non-equi join으로 처리
select name,s_amount,rank from (select name,sum(amount) s_amount from shop_product where pdate>='2024/03/01'
group by name),customer_rank
where s_amount between lower_amount and high_amount
;

--error
select name,sum(amount),rank
from shop_product,customer_rank
where pdate>='2024/03/01' and sum(amount) between lower_amount and high_amount
group by name,rank
;



select * from lotte_product
order by std_ym
;

-- 순번을 새롭게 부여해서 출력해주는 함수
-- rownum, row_number()
select rownum,std_ym,sex_cd,age_cd,time_cd,purh_amt
from lotte_product
;

select rownum rnum,a.* from lotte_product a;


select rnum,std_ym,sex_cd,age_cd,time_cd,purh_amt 
from 
( 
  select rownum rnum,a.* from lotte_product a
) b
where rnum >= 21 and rnum <= 30 ;

select rownum,a.*
from lotte_product a
order by std_ym
;

select rownum,b.*
from ( select * from lotte_product order by std_ym ) b
;

select * from stu_score
order by no;

-- kor점수가 높은순으로 21~30등까지 출력하시오


-- 순번 21,22,23....30번을 부여하세요.
-- ->
select rnum,no,name,kor,eng,math,total,avg,rank,c_date
from (
select rownum rnum,b.* from 
( select a.* from stu_score a
order by kor desc ) b
)
where rnum>=21 and rnum<=30
;

select rownum,a.* from stu_score a;



select * from stu_score 
where no>=21 and no<=30
order by no
;








