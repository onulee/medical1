-- ����,����,����
select sysdate-1,sysdate,sysdate+1 from dual;

-- ����, �̴��� ù��, �̴��� ��������
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;

-- �γ�¥�� �ϼ�, �γ�¥�� �޼�
select round(sysdate-hire_date,3),trunc(months_between(sysdate,hire_date),2) from employees;

-- trunc �ϴ��� ����, group by �׷��Լ�
select trunc(kor,-1) kor,count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor;


-- 2008-01-01
select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm') from employees;
-- ����. hire_date ��¥���� ���� ����Ͻÿ�.
select to_char(hire_date,'mm') hire_date,count(to_char(hire_date,'mm')) from employees
group by to_char(hire_date,'mm')
order by hire_date;

-- ����. hire_date yyyy �⵵,�⵵�� �ο����� ����Ͻÿ�.
select to_char(hire_date,'yyyy') hire_date,count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;

-- ����ȯ - number, character, date
-- number ��Ģ���갡��, ��ǥǥ�þȵ�,��ȭǥ�þȵ�.
-- char ��Ģ����(+,-)�ȵ�, ��ǥǥ�ð���,��ȭǥ�ð���
-- date +,-���� ��¥������´� ����Ұ�

-- ������,��¥�� �⵵�� ������ �й��� �ο��Ͻÿ�.
-- stu_seq�������� ������ 5�� �й��� ����غ�����.
-- ko+2024+0001
select 'ko'||'2024'||'0001' from dual;
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;


-- ������Ÿ��
-- 123,456,789 , 156,778  , ���ϱⰪ 
-- (123,456,789)+(100,000) = 123556789 ����Ͻÿ�.

select to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')) from dual;
select to_char(to_number('123,456,789','999,999,999')+to_number('100,000','999,999'),'999,999,999') from dual;

select to_char(salary,'999,999') from employees;


-- ����Ÿ�Ը� ��¥Ÿ������ ����
select 20240425+3 from dual;
select to_char(20240425+3) from dual;
select to_date(20240425) from dual;

-- ����Ÿ���� ��¥Ÿ������ ����
select emp_name,hire_date from employees
where hire_date > to_date(20070101)
order by hire_date;

-- ����. 01,05,08�� �Ի���, ����̸� 2��°�� a�� �� �ִ� ����� ����Ͻÿ�.
-- 1. �Ի�
select hire_date from employees
where to_char(hire_date,'mm')='01' or to_char(hire_date,'mm')='05' or to_char(hire_date,'mm')='08';

select hire_date from employees
where to_char(hire_date,'mm') in ('01','05','08');

-- 2. �̸�
select emp_name from employees
where emp_name like '_a%';

-- 3. �Ի���, �̸� ��ġ��
select emp_name,hire_date from employees
where emp_name like '_a%' and to_char(hire_date,'mm') in ('01','05','08')
order by hire_date;


-- ����. 20070101 ���� �Ի��� ����̸� a�� �� �ִ� ����� ����Ͻÿ�.
select emp_name,hire_date from employees
where hire_date > to_date(20070101) and emp_name like '%a%'
order by hire_date;

-- ����Ÿ���� ��¥Ÿ������ ����
select sysdate-to_date('20240401') from dual;

select sysdate,'2024-04-01',sysdate-to_date('2024-04-01') from dual;

select * from m_date;



create table eventDate (
eno number,
e_today date,
e_choice_day date,
e_period number
);

-- �Է½� ��¥Ÿ�Կ� ����(����-��¥����)�� �Է��ص� �����.
-- ��¥�� ���ڸ� ����� �Ұ���, �׷��� ���ڸ� ��¥Ÿ������ �����ؾ� ��.
insert into eventDate values(
seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01')
);

select * from eventDate;

-- ����Ÿ���� ����Ÿ������ ����
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

-- null�� 0���� ��ȯ nvl()
select salary, commission_pct,salary+(salary*nvl(commission_pct,0)) from employees;

-- manager_id null ceo����
select manager_id from employees 
order by manager_id desc;

-- ����Ÿ���� ����Ÿ������ ����
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc
;

--- �׷��Լ� : sum,avg,count(),count(*),min,max

-- ���� count
select count(*) from employees;
-- ����� : 107��
select count(emp_name) from employees;
-- null���� ������ ���� - ����� : 106��
select count(manager_id) from employees;
select emp_name,manager_id from employees;

-- sum : ����
select sum(salary) from employees;

-- avg : ���
select avg(salary) avg_sal from employees;

-- min : �ּҰ�, max:�ִ밪
select min(salary),max(salary) from employees;

-- ����. 6461�޷����� ���� ����� ����Ͻÿ�.
select emp_name,salary from employees
where salary > (select avg(salary) avg_sal from employees);

select min(salary) from employees;

-- ���� �ּҿ����� �޴� ����� ���,�̸��� ����Ͻÿ�.
select employee_id,emp_name,salary from employees
where salary=(select min(salary) from employees);

-- ���� �ִ���� �޴� ����� ���,�̸��� ����Ͻÿ�.
select employee_id,emp_name,salary from employees
where salary=(select max(salary) from employees);

-- �μ���ȣ�� 50���� ����� ��ü ����
select department_id,salary from employees;

select sum(salary) from employees
where department_id = 100;

select count(*) from stu_score;

-- ����. stu_score kor������ 80���̻��� �л��� ����Ͻÿ�.
select kor from stu_score
where kor>=80;

-- ����. ������������ �������� ����̻�, ������������ �������� ����̻��� �л��� ����Ͻÿ�.
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

-- ����. ������ �ִ�, �ּ�, ����� ����� ����Ͻÿ�.
-- 3�� ���
select emp_name,salary from employees
where salary=(select max(salary) from employees)
or salary=(select min(salary) from employees) 
or salary=(select avg(salary) from employees) 
; 

-- �ִ밪
select emp_name,salary from employees 
where salary =(select max(salary) from employees)
;


-- ��հ����� ������� �߿� �ִ밪�� ����� ����Ͻÿ�.
-- 1. ��հ����� ���� ����� �˻�
-- 2. �˻��� ����߿� �ִ밪�� �˻�
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


-- ��պ��� ������ 107��
--select max(salary) from (���̺�)

-- 56�� �ִ밪 6400
select max(salary) from (
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
)
;

-- 56���� �����
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc
;

-- �����Լ�
-- lpad,rpad ����� ä���
select emp_name,lpad(emp_name,15,'#') from employees;
select emp_name,rpad(emp_name,20,'@') from employees;

-- ltrim, rtrim ������ ���ڸ� �߶󳻰� ���
select emp_name,ltrim(emp_name,'Do') from employees;

-- ko20240001
select 'ko20240001',ltrim('ko20240001','ko2024') from dual;

--substr(������,����,����)  ex)substr('abcdefg',3,3) -> cde
select emp_name, substr(emp_name,3,4) from employees;

select job_id from employees;

--����. job_id �� �α��ڿ� �����ȣ�� �����ؼ� ����Ͻÿ�.
select substr(job_id,0,2)||employee_id from employees;

-- length : ���ڿ��� ����
select emp_name, length(emp_name) from employees
where length(emp_name)>15;

-- ��¥�Լ� +,- ����, ��¥������ ���� ���ϱ�� �ȵ�.
-- ��¥������ +,- ���� ����
select sysdate+1 from dual;

-- ��¥������ - ��¥������ ����
select sysdate - hire_date from employees;

-- ��¥������ + ��¥������ �Ұ���
select sysdate + hire_date from employees;

select sysdate,trunc(sysdate,'month'),round(sysdate,'month') from dual;

select round(sysdate,'year') from dual;

-- ������ �߰�,���
select sysdate,add_months(sysdate,-2) from dual;

-- ceil�ø�, floor����, mod������, power����
select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;


-- ����. ����� �Ի��� ���
select emp_name||to_char(hire_date,' yyyy"��" mm"��" dd"��" day') from employees;


-- ����. �����, �ڸ��� 9�ڸ� ����� 0���� ǥ�� 
-- salar*1400 �տ� ��ȭǥ�ÿ� ��ǥ�� �־� ����Ͻÿ�.
select salary, to_char(salary*1400, 'L000,000,000' ) from employees;

-- �ڽ��� ���ϰ� �ڽ��� ������ ���� ���� ��������¥
--- '2010-10-10'
select trunc(to_date('2010-10-10'),'month'),'2010-10-10',last_day('2010-10-10') from dual;

select * from member;

desc member;

-- DDL(data denfinition language)

-- �÷��߰�, ����, ���� 
-- �� commit,rollank�� �ȵ�. �ٷ� �����. 
alter table member add gender varchar2(6) default 'female' not null;
desc member;

-- �÷����� 
-- �÷��̸�����
alter table member rename column name to stu_name
;

-- Ÿ�Ժ���
alter table member modify(stu_name varchar2(50));

-- ������ �����Ͱ� �����Ϸ��� ũ�⺸�� �������� ����
update member set stu_name='';
alter table member modify(stu_name varchar2(6));
-- �÷��� Ÿ���� �����Ϸ��� �÷������Ͱ� ������̰ų� null�϶� ����
alter table member modify(stu_name number(4));
desc member;
select stu_name from member;


-- �÷����� - commit,rollback �� ����.
-- alter table member drop column phone;


select * from member;

update member set gender = 'male';

commit;










