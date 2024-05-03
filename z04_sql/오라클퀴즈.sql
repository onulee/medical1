-- [ 1 ] 사원정보(Employees) 테이블에서 
-- 사원번호, 이름, 급여, 부서, 입사일, 상사의 사원번호를 출력하시오. 
-- 이때 이름은 이름과 직급을 연결하여 Name이라는 별칭으로 출력하시오(107행).

select employee_id,emp_name ||'/'||job_id as Name,salary,department_id,hire_date,manager_id 
from employees;

--[ 2 ] 사원정보(Employees) 테이블에서 
-- 사원의 이름은 Name, 업무는 Job, 급여는 Salary, 연봉에 $100씩 보너스를 추가하여 계산한 값은 Increase Ann_Salary,
-- 급여에 $100 보너스를 추가하여 계산한 연봉은 Increase Salary라는 별칭을 붙여 출력하시오(107행).

select emp_name as Name,job_id as Job,salary,salary*100*12 "Increase Salary"
from employees;

-- [ 3 ] H R 부서에서 예산 편성 문제로 급여 정보 보고서를 작성하려고 한다. 
-- 사원정보(Employees) 테이블에서 급여가 $7,000~$10,000 범위 이외인 사람의 
-- 이름 및 급여를 급여가 적은 순서로 출력하시오(75행).

select emp_name,salary from employees
where salary<7000 or salary > 10000
order by salary
;

--- 월급이 7000보다 크고 10000 작은 사원
select emp_name,salary from employees
where salary between 7000 and 10000
;
-- not을 사용 반대사원을 출력
select emp_name,salary from employees
where salary not between 7000 and 10000
order by salary asc
;

-- [ 4 ] 사원의 이름(emp_name) 중에 ‘e’ 및 ‘o’ 글자가 포함된 사원을 출력하시오.
-- 이때 머리글은 ‘e or o Name’이라고 출력하시오(8행).

select emp_name from employees
where lower(emp_name) like '%o%' or lower(emp_name) like '%e%'
order by emp_name;

-- [ 5 ] 이번 분기에 60번 IT 부서에서는 신규 프로그램을 개발하고 보급하여 회사에 공헌하였다. 
-- 이에 해당 부서의 사원 급여를 12.3% 인상하기로 하였다. 
-- 60번 IT 부서 사원의 급여를 12.3% 인상하여 정수만(반올림) 표시하는 보고서를 작성하시오. 
-- 보고서는 사원번호, 이름(Name으로 별칭), 급여, 인상된 급여(Increase Salary로 별칭)순으로 출력하시오(5행).

select employee_id,emp_name as Name,department_id,salary,round(salary+salary*0.123) from employees
where department_id = 60
;

-- [ 6 ] 모든 사원의 연봉을 표시하는 보고서를 작성하려고 한다. 
-- 보고서에 사원의 이름, 급여, 수당여부에 따른 연봉을 포함하여 출력하시오. 
-- 수당여부는 수당이 있으면 “Salary + Commission”, 
-- 수당이 없으면 “Salary only”라고 표시하고, 별칭은 적절히 붙이시오. 
-- 또한 출력 시 연봉이 높은 순으로 정렬하시오(107행).

select emp_name,salary,salary+salary*nvl(commission_pct,0) as comm_salary,
commission_pct,
-- 1. case when then
-- case when commission_pct is null then 'Salary only'
-- when commission_pct is not null then 'Salary + Commission'
-- end as "commission_isNull"
-- 2. decode
-- decode(commission_pct,null,'Salary only','Salary + Commission')
-- decode ( department_id,
-- '10','A',
-- '20','B',
-- '30','C' ) as dept
-- 3. nvl2
nvl2(commission_pct,'Salary + Commission','Salary only')
from employees
order by salary desc
;

-- [ 7 ] 각 사원이 소속된 부서별로 급여 합계, 급여 평균, 급여 최댓값, 급여 최솟값을 집계하고자 한다. 
-- 계산된 출력값은 여섯 자리와 세 자리 구분기호-천단위, $ 표시와 함께 아래와 같이 출력하시오. 
-- 단, 부서에 소속되지 않은 사원에 대한 정보는 제외하고, 
-- 출력 시 머리글은 "그룹함수명"을 별칭(alias) 처리하시오(11행).

select department_id,
to_char(sum(salary),'$000,999,999') sum_sal,
to_char(round(avg(salary),2),'$000,999,999') avg_sal,
to_char(max(salary),'$000,999,999') max_sal,
to_char(min(salary),'$000,999,999') min_sal 
from employees
group by department_id
;

-- [ 8 ] 사원들의 직급(job_id)별 전체 급여 평균이 $10,000보다 큰 경우를 조회하여 직급별 급여 평균을 출력하시오. 
-- 단 업무에 사원(CLERK)이 포함된 경우는 제외하고 전체 급여 평균이 높은 순서대로 출력하시오(7행).

select job_id,avg(salary) from employees
where job_id not like '%CLERK%'
-- 일반컬럼의 조건을 넣는 곳
group by job_id
having -- 그룹컬럼의 조건을 넣는 곳
avg(salary)>10000
;

-- outer join
-- [ 9 ] 각 사원과 직속 상사와의 관계를 이용하여 다음과 같은 형식의 보고서를 작성하고자 한다.
-- (예) 홍길동은 허균에게 보고한다 → Eleni Zlotkey 보고대상자 -> Steven King
-- 어떤 사원이 누구에게 보고하는지 위 예를 참고하여 출력하시오. 
-- 단, 보고할 상사가 없는 사원이 있다면 그 정보도 포함하여 출력하시오. (107행).
select a.employee_id,a.emp_name,a.manager_id,b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id(+)
;

-- [ 10 ] Employees, Departments 테이블의 구조를 파악한 후 
-- 사원 수가 다섯 명 이상인 부서의 부서이름과 사원 수를 출력하시오. 
-- 이때 사원 수가 많은 순으로 정렬하시오(5행).
-- 1. 부서번호,사원수
-- 2. 사원수 >= 5
-- 3. 사원수별 정렬

select department_id,count(department_id)
from employees
group by department_id
having count(department_id)>=5
order by count(department_id) desc
;

-- [ 추가 ] HR 부서의 어떤 사원은 급여정보를 조회하는 업무를 맡고 있다. 
-- Tucker가 포함된 사원보다 급여를 많이 받고 있는 사원의 이름, 업무, 급여를 출력하시오(15행).
select salary from employees
where emp_name like '%Tucker%'
;

select salary from employees
where salary > (select salary from employees
where emp_name like '%Tucker%')
;

-- 전체평균 월급이상인 사원의 월급 출력
select salary from employees
where salary > (select avg(salary) from employees)
order by salary desc
;

-- [ 추가 ] 모든 사원의 소속부서 평균연봉을 계산하여 사원별로 이름, 직급, 
-- 급여, 부서번호, 부서평균연봉(Department Avg Salary로 별칭)을 출력하시오(107행).

select avg(salary) from employees;

-- join
select salary,a.department_id,avg_salary 
from employees a, (select department_id,round(avg(salary),2) avg_salary from employees group by department_id ) b
where a.department_id = b.department_id
;

select emp_name from 
(select * from employees where salary>(select avg(salary) from employees) )
where emp_name like '%a%'
;

select * from employees where salary>(select avg(salary) from employees);


-- equi join
select salary, a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id
;

select emp_name,job_id,salary,department_id ,
( 
select round(avg(salary),2) from employees a 
where department_id = e.department_id
)
from employees e;

-- 
select round(avg(salary),2) from employees a 
where department_id = 10
;

create table daum_movie(
 dno number(4),
 title varchar2(100),
 img varchar2(100),
 audience number(10),
 ddate date
)
;

-- img 크기 변경
alter table daum_movie modify img varchar2(300);


select * from daum_movie;
create table coupang(
 cno number(4),
 title varchar2(100),
 img varchar2(300),
 price number(10),
 grade number(10),
 eval_num number(10)
)
;

alter table coupang modify title varchar2(500);

select * from coupang;

create table mmdate (
mdate date
);

insert into mmdate values (TO_DATE('2024-06-27 06:00:00','yyyy-mm-dd HH24:MI:SS') );




