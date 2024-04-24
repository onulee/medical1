--trnuc 버림, round 반올림
select sysdate,hire_date,sysdate-hire_date,3,round(sysdate-hire_date,3) from employees;

-- 어제 sysdate-1, 내일 sysdate+1
select sysdate-1 어제, sysdate 오늘,sysdate+1 내일,sysdate+100 from dual;

-- m_no - 시퀀스 1-9999 1씩증가 5번 반복해서 저장
-- 퀴즈 m_no,m_yesterday,m_today,m_tomorrow,m_year 날짜컬럼을 가진 테이블 m_date
-- 어제,오늘,내일,1년후 날짜를 저장하시오.

-- seq_m_no 시퀀스 생성
create sequence seq_m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

-- 테이블생성 date,timestamp
create table m_date (
m_no number(4),
m_yesterday date,m_today date,m_tomorrow date,m_year date
);

-- 1개 row 저장
insert into m_date(m_no,m_yesterday,m_today,m_tomorrow,m_year) values (
seq_m_no.nextval, sysdate-1,sysdate,sysdate+1,sysdate+365 
);
-- 검색
select * from m_date;

-- abs절대값, ceil,floor   round,trunc - 자릿수
select abs(hire_date-sysdate) from employees;

-- 날짜의 월을 기준으로 반올림
select hire_date,round(hire_date,'month') from employees;

-- 날짜의 월을 기준으로 버림
select hire_date,trunc(hire_date,'month'),round(hire_date,'month') from employees;

select trunc(hire_date,'month') 기준일 ,hire_date from employees
order by hire_date;

select * from channels;

select period,count(period) from kor_loan_status
group by period
order by period;

select period from kor_loan_status
where period='201111';


select trunc(kor,-1) t_kor,count(trunc(kor,-1)) count from students
group by trunc(kor,-1)
order by t_kor;

-- 날짜의 월을 기준으로 버림
select trunc(hire_date,'month') m_hire_date,count(trunc(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by m_hire_date
;

-- drop table stu_score;
-- drop table emp01;
-- drop table board;

select * from stu_score
order by no;

update stu_score set name='관순스'
where no=10;

select * from stu_score;

update stu_score set avg=round(total/3,3);

-- 2개의 날짜에서 월 간격을 확인
select hire_date,floor(months_between(sysdate,hire_date)),trunc(sysdate-hire_date,2) from employees;

-- 개월 추가
select hire_date,add_months(hire_date,6) from employees;

-- last day
select hire_date,last_day(hire_date),round(hire_date,'d') from employees;

-- 날짜를 기준으로 현재일, 처음일,마지막일
select sysdate 현재일,trunc(sysdate,'month') 처음일,last_day(sysdate) 마지막일 from dual;

-- 특정 요일의 날짜를 확인
select sysdate,next_day(sysdate,'토요일') from dual;

-- 요일의 처음일
select sysdate,trunc(sysdate,'d'),next_day(sysdate,'토요일') from dual;


-- board테이블 default 는 입력시 없을시 지정한 데이터 자동 입력됨.
create table board(
bno number(4) primary key, -- 중복이 안됨,null허용하지 않음. 기본키로 사용됨.
id varchar2(30),
btitle varchar2(1000),
bcontent clob,  -- varchar2(3000) clob - 무제한: varchar2의 타입
bdate date default sysdate,
bhit number default 0,
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values (
board_seq.nextval,'aaa','제목입니다.','내용입니다.',sysdate,0,board_seq.currval,0,0,'1.jpg'
);

insert into board(bno,id,btitle,bcontent,bgroup,bfile) values (
board_seq.nextval,'bbb','이벤트 신청','이벤트를 신청합니다.',board_seq.currval,'2.jpg'
);

select * from board;


-- 형변환 - number, character, date

select sysdate from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'yy/mm/dd') from dual;
select to_char(sysdate,'yyyy') from dual;

-- 문자열 +가 안됨. ko+2024+0001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_mno.nextval,'0000')) from dual;

select to_char(sysdate,'dy'),to_char(sysdate,'day') from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss mon day') from dual;

-- hire_date, yyyy-mm-dd hh:mi:ss mon day

-- am,pm 오전,오후 hh24 24시간으로 표시
select to_char(sysdate,'pm hh24:mi:ss') from dual;

select * from stu_score;

select to_char(c_date,'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

-- 날짜별로 몇개의 데이터가 들어가 있는지 출력하시오.
select c_date,count(c_date) from stu_score
group by c_date
order by c_date;

-- 문자형 사칙연산(+,-,*,/) 안됨. 자리수표시,쉼표표시,날짜형태 표시
-- 숫자형 사칙연산가능 컬럼별 사칙연산가능, 자리수표시(0001-> 안됨.),쉼표표시 안됨. 
-- 날짜형 +,- 연산기능가능,months-between 2개날짜 달 계산 ,날짜유형을 지정해서 출력이 안됨.


-- 문자형 안에 있는 데이터가 숫자이면 자동으로 형변환해서 계산해줌.
-- 문자형 안에 문자가 있으면 자동형변환 불가
select 10 a,100 b,(10+100) ab,20+to_char(100),10+'100' from dual;
select 10 a,100 b,(10+100) ab,to_char(100),10+'100원' from dual;

-- '0000' 빈자리는 0으로 채움, '9999' 빈자리를 빈자리 둠.
select 12340000,to_char(12340000),length(to_char(12340000,'999,999,999')) from dual;
select length(12340000),to_char(12340000),to_char(1234000,'000,999,999'),
length(to_char(12340000,'999,999,999')) from dual;

-- L은 원화 표시
select 12340000,to_char(12340000,'L999,999,999') from dual;
-- $는 $표시
select 12340000,to_char(12340000,'$999,999,999') from dual;
-- 소수점 자리 표시
select 1234.1234,to_char(1234.1234,'000,999.99') from dual;

-- 데이터의 길이 함수
select length('안녕하세요') from dual;
select length(1234000) from dual;

-- 10개자리수 표시
-- 공백제거해서 자리수 확인 trim
select length(trim(to_char(12345,'0000000000'))),length(trim(to_char(12345,'999,999'))) from dual;

-- 퀴즈
-- 123,456,789   100,000
-- 123,456,789 100,000 = 값을 출력하시오. 천단위 표시 할것
-- ￦123,556,789

select 123456789+100000 from dual;
-- 123,456,789 쉼표를 제거 - replace('123,456,789',',','')
-- 타입을 number형으로 변경
-- 더하기를 함.
-- 문자형 타입으로 변경해서 원화,쉼표 표시
-- total = '123,456,789'
-- wire = '100,000'

select (123,456,789)+(100,000) from dual;

select replace('123,456,789',',','') from dual;

select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')), 'L999,999,999'  )
from dual;

select to_char(123456789+100000,'L999,999,999') from dual;

select to_number('0000123') from dual;


-- 날짜형
-- 문자형 +,- 안됨.
select '2024-04-24 11:00:00'-'2024-04-01 10:00:00' from dual;
select to_date('2024-04-24')-to_date('2024-04-01') from dual;
select to_date('2024/04/24')-to_date('2024/04/01') from dual;
select to_date('24/04/24')-to_date('24/04/01') from dual;

select to_date('20240401') from dual;

-- 퀴즈 '20240401'
-- 2024-04-01 타입으로 변경해서 출력하시오.
select to_date('20240401') from dual;
select to_char(to_date('20240401'),'yyyy-mm-dd hh:mi:ss') from dual;

select hire_date from employees
where hire_date >= '20080101'
;

select * from stu_score;

select c_date from stu_score
where c_date = '2024/04/05'
;

select sysdate-hire_date from employees;
select sysdate-to_date('2024/04/01') from dual;

-- 퀴즈
-- 20,000 / 10,000 문자형을 빼기 연산을 해서 10,000 출력하시오.
-- number형변환
select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'99,999'  ) from dual;

-- 퀴즈
select commission_pct from employees;
-- 실제 월급 = 월급 + (월급 * 커미션) 실제월급해서 출력하시오.
-- nvl(데이터,0)
select salary,salary+(salary*nvl(commission_pct,0)),commission_pct from employees;

-- commission_pct null값만 출력하시오.
-- is null
select emp_name,commission_pct from employees
where commission_pct is null;


select manager_id from employees
order by manager_id desc;

-- 퀴즈 manager_id null이면 0 nvl(데이터,0)
select nvl(manager_id,0) from employees
order by manager_id desc
;

-- 퀴즈 manager_id null이면 ceo로 입력하시오.
-- manager_id 타입:number 'ceo'는 타입 문자형 타입 변경을 해야 함.
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc
;












