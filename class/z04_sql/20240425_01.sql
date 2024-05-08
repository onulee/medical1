-- 어제,오늘,내일
select sysdate-1,sysdate,sysdate+1 from dual;

-- 오늘, 이달의 첫일, 이달의 마지막일
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;

-- 두날짜간 일수, 두날짜간 달수
select round(sysdate-hire_date,3),trunc(months_between(sysdate,hire_date),2) from employees;

-- trunc 일단위 버림, group by 그룹함수
select trunc(kor,-1) kor,count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor;


-- 2008-01-01
select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm') from employees;
-- 퀴즈. hire_date 날짜에서 월만 출력하시오.
select to_char(hire_date,'mm') hire_date,count(to_char(hire_date,'mm')) from employees
group by to_char(hire_date,'mm')
order by hire_date;

-- 퀴즈. hire_date yyyy 년도,년도별 인원수를 출력하시오.
select to_char(hire_date,'yyyy') hire_date,count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;

-- 형변환 - number, character, date
-- number 사칙연산가능, 쉼표표시안됨,원화표시안됨.
-- char 사칙연산(+,-)안됨, 쉼표표시가능,원화표시가능
-- date +,-가능 날짜출력형태는 변경불가

-- 시퀀스,날짜의 년도를 가지고 학번을 부여하시오.
-- stu_seq시퀀스를 가지고 5개 학번을 출력해보세요.
-- ko+2024+0001
select 'ko'||'2024'||'0001' from dual;
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;


-- 문자형타입
-- 123,456,789 , 156,778  , 더하기값 
-- (123,456,789)+(100,000) = 123556789 출력하시오.

select to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')) from dual;
select to_char(to_number('123,456,789','999,999,999')+to_number('100,000','999,999'),'999,999,999') from dual;

select to_char(salary,'999,999') from employees;


-- 숫자타입를 날짜타입으로 변경
select 20240425+3 from dual;
select to_char(20240425+3) from dual;
select to_date(20240425) from dual;

-- 숫자타입을 날짜타입으로 변경
select emp_name,hire_date from employees
where hire_date > to_date(20070101)
order by hire_date;

-- 퀴즈. 01,05,08월 입사한, 사원이름 2번째에 a가 들어가 있는 사람을 출력하시오.
-- 1. 입사
select hire_date from employees
where to_char(hire_date,'mm')='01' or to_char(hire_date,'mm')='05' or to_char(hire_date,'mm')='08';

select hire_date from employees
where to_char(hire_date,'mm') in ('01','05','08');

-- 2. 이름
select emp_name from employees
where emp_name like '_a%';

-- 3. 입사일, 이름 합치기
select emp_name,hire_date from employees
where emp_name like '_a%' and to_char(hire_date,'mm') in ('01','05','08')
order by hire_date;


-- 퀴즈. 20070101 이후 입사한 사원이름 a가 들어가 있는 사람을 출력하시오.
select emp_name,hire_date from employees
where hire_date > to_date(20070101) and emp_name like '%a%'
order by hire_date;

-- 문자타입을 날짜타입으로 변경
select sysdate-to_date('20240401') from dual;

select sysdate,'2024-04-01',sysdate-to_date('2024-04-01') from dual;

select * from m_date;



create table eventDate (
eno number,
e_today date,
e_choice_day date,
e_period number
);

-- 입력시 날짜타입에 문자(형태-날짜형태)를 입력해도 저장됨.
-- 날짜와 문자를 빼기는 불가능, 그래서 문자를 날짜타입으로 변경해야 함.
insert into eventDate values(
seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01')
);

select * from eventDate;

-- 문자타입을 숫자타입으로 변경
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

-- null을 0으로 취환 nvl()
select salary, commission_pct,salary+(salary*nvl(commission_pct,0)) from employees;

-- manager_id null ceo글자
select manager_id from employees 
order by manager_id desc;

-- 숫자타입을 문자타입으로 변경
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc
;

--- 그룹함수 : sum,avg,count(),count(*),min,max

-- 개수 count
select count(*) from employees;
-- 결과값 : 107명
select count(emp_name) from employees;
-- null값이 있으면 제외 - 결과값 : 106명
select count(manager_id) from employees;
select emp_name,manager_id from employees;

-- sum : 총합
select sum(salary) from employees;

-- avg : 평균
select avg(salary) avg_sal from employees;

-- min : 최소값, max:최대값
select min(salary),max(salary) from employees;

-- 퀴즈. 6461달러보다 높은 사람을 출력하시오.
select emp_name,salary from employees
where salary > (select avg(salary) avg_sal from employees);

select min(salary) from employees;

-- 퀴즈 최소월급을 받는 사람의 사번,이름을 출력하시오.
select employee_id,emp_name,salary from employees
where salary=(select min(salary) from employees);

-- 퀴즈 최대월급 받는 사람의 사번,이름을 출력하시오.
select employee_id,emp_name,salary from employees
where salary=(select max(salary) from employees);

-- 부서번호가 50번인 사원만 전체 월급
select department_id,salary from employees;

select sum(salary) from employees
where department_id = 100;

select count(*) from stu_score;

-- 퀴즈. stu_score kor점수가 80점이상인 학생을 출력하시오.
select kor from stu_score
where kor>=80;

-- 퀴즈. 국어점수에서 국어점수 평균이상, 영어점수에서 영어점수 평균이상인 학생을 출력하시오.
select count(*) from stu_score
where kor>=(select avg(kor) from stu_score) 
and eng>=(select avg(eng) from stu_score)
;

create table s_info (
sno number,
s_count number
);

insert into s_info values(
stu_seq.nextval,2000
);

insert into s_info values(
stu_seq.nextval,( select count(*) from stu_score
where kor>=(select avg(kor) from stu_score) 
and eng>=(select avg(eng) from stu_score)   )
);

select * from s_info;

-- 퀴즈. 월급이 최대, 최소, 평균인 사원을 출력하시오.
-- 3명 출력
select emp_name,salary from employees
where salary=(select max(salary) from employees)
or salary=(select min(salary) from employees) 
or salary=(select avg(salary) from employees) 
; 

-- 최대값
select emp_name,salary from employees 
where salary =(select max(salary) from employees)
;


-- 평균값보다 낮은사원 중에 최대값인 사원을 출력하시오.
-- 1. 평균값보다 낮은 사원을 검색
-- 2. 검색된 사원중에 최대값을 검색
select emp_name,salary from employees
where salary = 6400;

select emp_name,salary from employees
where salary = ( 
select max(salary) from (
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
)
);


-- 평균보다 낮은값 107명
--select max(salary) from (테이블)

-- 56명 최대값 6400
select max(salary) from (
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
)
;

-- 56명의 결과값
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
;

-- 문자함수
-- lpad,rpad 빈공백 채우기
select emp_name,lpad(emp_name,15,'#') from employees;
select emp_name,rpad(emp_name,20,'@') from employees;

-- ltrim, rtrim 지정한 문자를 잘라내고 출력
select emp_name,ltrim(emp_name,'Do') from employees;

-- ko20240001
select 'ko20240001',ltrim('ko20240001','ko2024') from dual;

--substr(데이터,순서,개수)  ex)substr('abcdefg',3,3) -> cde
select emp_name, substr(emp_name,3,4) from employees;

select job_id from employees;

--퀴즈. job_id 앞 두글자와 사원번호를 결합해서 출력하시오.
select substr(job_id,0,2)||employee_id from employees;

-- length : 문자열의 길이
select emp_name, length(emp_name) from employees
where length(emp_name)>15;

-- 날짜함수 +,- 가능, 날짜데이터 끼리 더하기는 안됨.
-- 날짜데이터 +,- 숫자 가능
select sysdate+1 from dual;

-- 날짜데이터 - 날짜데이터 가능
select sysdate - hire_date from employees;

-- 날짜데이터 + 날짜데이터 불가능
select sysdate + hire_date from employees;

select sysdate,trunc(sysdate,'month'),round(sysdate,'month') from dual;

select round(sysdate,'year') from dual;

-- 개월수 추가,축소
select sysdate,add_months(sysdate,-2) from dual;

-- ceil올림, floor버림, mod나머지, power제곱
select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;


-- 퀴즈. 사원명 입사일 출력
select emp_name||to_char(hire_date,' yyyy"년" mm"월" dd"일" day') from employees;


-- 퀴즈. 사원명, 자리수 9자리 빈공백 0으로 표시 
-- salar*1400 앞에 원화표시와 쉼표를 넣어 출력하시오.
select salary, to_char(salary*1400, 'L000,000,000' ) from employees;

-- 자신의 생일과 자신의 생일이 속하 달의 마지막날짜
--- '2010-10-10'
select trunc(to_date('2010-10-10'),'month'),'2010-10-10',last_day('2010-10-10') from dual;

select * from member;

desc member;

-- DDL(data denfinition language)

-- 컬럼추가, 수정, 삭제 
-- 위 commit,rollank이 안됨. 바로 저장됨. 
alter table member add gender varchar2(6) default 'female' not null;
desc member;

-- 컬럼수정 
-- 컬럼이름변경
alter table member rename column name to stu_name
;

-- 타입변경
alter table member modify(stu_name varchar2(50));

-- 기존의 데이터가 변경하려는 크기보다 작을때만 가능
update member set stu_name='';
alter table member modify(stu_name varchar2(6));
-- 컬럼의 타입을 변경하려면 컬럼데이터가 빈공백이거나 null일때 가능
alter table member modify(stu_name number(4));
desc member;
select stu_name from member;


-- 컬럼삭제 - commit,rollback 이 없음.
-- alter table member drop column phone;


select * from member;

update member set gender = 'male';

commit;










