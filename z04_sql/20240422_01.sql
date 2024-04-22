select * from employees;

select employee_id,emp_name from employees;

select salary from employees;

-- Ÿ�� : number +,-,*,/ ����
select salary, salary * 1400 k_sal,salary*1400*12 as y_sal from employees;

select * from stu_score;

select no,name,kor,eng,math,total,avg,rank from stu_score;

-- ���̽�.

select department_id from employees;

select nvl(department_id,0) from employees;

select * from employees;

-- ��Ī : as���, "" : Ű���带 �ִ� �״�� ���
select salary, salary + (salary*nvl(commission_pct,0)) as "real_sal*" from employees;

-- �ѱ� ��밡��
select salary as "���" from employees;

-- 

select * from departments;

-- �μ���ȣ, �μ��̸��� ����Ͻÿ�.
select department_id,department_name from departments;

-- �������� �����͸� 1���� ���ļ� �Ѱܾ� �� ��� concat
-- concat : ȫ�浿,������,�̼���,������,�豸 -> split(",") : �и� 

select * from stu_score;

-- concat ||
select kor||','||eng||','||math stu from stu_score;

select kor+eng+math as total,(kor+eng+math)/3 from stu_score;

-- �ߺ����� : distinct
-- where : ������ not �����ϰ� �˻��Ϸ��� is not null
select distinct department_id from employees where department_id is not null;

-- manager_id

select manager_id from employees;

select distinct manager_id from employees;
select distinct manager_id from employees where manager_id is not null;


select * from employees;

select employee_id,salary from employees
where employee_id = 200 or employee_id = 201 or employee_id=202;

select * from employees
where employee_id >= 200 and employee_id <=203;

select * from employees
where employee_id <= 150 or employee_id>=200;

-- department_id 10,30,50�� �ش�Ǵ� ����� ����Ͻÿ�.
select employee_id,department_id,salary from employees
where department_id = 10 or department_id = 30 or department_id = 50;

-- ���� 6000 ~ 9000 ������ ����� ����Ͻÿ�.
-- ���� order by �÷� asc : ��������,desc : ��������
select salary from employees where salary>=6000 and salary<=9000
order by salary desc
;
-- ���� 6000,7000,8000 �� ����� ����Ͻÿ�.
select salary from employees
where salary =6000 or salary=7000 or salary = 8000;

-- �μ���ȣ�� 50���̸鼭, ������ 8000 �̻��� ����� ����Ͻÿ�.
select department_id,salary from employees
where department_id=50 and salary >= 8000;

-- stu_score ȫ�浿 ����Ͻÿ�.
select * from stu_score
where name = 'ȫ�浿';

-- ��������
select hire_date from employees
order by hire_date asc
;
-- ��������
select hire_date from employees
order by hire_date desc
;

select emp_name,hire_date from employees
where hire_date >= '02/01/01'
order by hire_date asc
;

select hire_date,hire_date+100 from employees;
-- �ݿø� round
select round(sysdate-hire_date,2) from employees;

select * from employees;

-- ������ġ��� +������ �Ұ���, ||��ɾ� ���
select emp_name||email from employees;

-- �Ի��� 05�� �̻� 06�� �����̸鼭 ������ 6000 �޷� �̻��� ����� �Ի��� �������ķ� ����Ͻÿ�.
select emp_name,hire_date,salary from employees
where hire_date >= '05/01/01' and hire_date <= '06/12/31' and salary >=6000
order by hire_date desc
;

-- !=, <>,^=, not
select department_id from employees
where department_id != 10 and not department_id = 50
order by department_id
;

-- salary 5000 �̻� 9000 ����
select emp_name,salary from employees
where salary >= 5000 and salary <= 9000
order by salary
;

-- ����� 99�� �̻��� �л��� �˻��Ͻÿ�.
select * from stu_score
where avg>=99
;

select * from students;

update students set name='������' 
where no = 10
;

commit;

select * from students;

-- students
-- ��� 70, ��� 75�� �̻��� �л��� ����Ͻÿ�.
select name,kor,avg from students
where kor>=70 and avg>=75
;

-- �������� 80, �������� 70, �������� 90 �� �л��� ����Ͻÿ�.
select name,kor from students
where kor=80 or kor = 70 or kor = 90;

-- in ���� ������ �ʵ尡 �������� �� �߿� �ϳ��� �˻��� ���
select name,kor from students
where kor in(80,70,90);

select name,kor from students
where kor not in(80,70,90);


update students set kor=100 
where no=1;

rollback;

select * from students
where no = 1;

-- ����
update students set kor=100, total = 100+eng+math, avg = (100+eng+math)/3
where no=1;


-- �������� 70 ~ 90 �̻� �л��� ����Ͻÿ�.
select kor from students
where kor > 70 and kor <= 90
;

-- 100��
select * from students;

-- 27�� between a and b : a���� ũ�ų� ���� b���� �۰ų� ���� �� �˻�
select kor from students
where kor between 70 and 90
;

-- 73�� not between a and b : a���� ũ�ų� , b���� ������ �˻�
select kor from students
where kor not between 70 and 90
;

-- ��¥�� between a and b

select hire_date from employees
order by hire_date;

-- �Ի��� 99�⺸�� ũ�ų� ����, 01�� ���� �۰ų� ���� ��� �˻�
select hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date asc
;

-- �̸��˻�
select * from students
where name='ȫ�浿'
;

-- like �˻� : Ư���ܾ ���ԵǾ� �ִ� ���� �˻�
-- ȫ% : ȫ���� ���۵Ǵ� �ܾ� �˻�
select * from students
where name like 'ȫ%'
;

-- %�� : ������ ������ �ܾ� �˻� 
select * from students
where name like '%��'
;

-- %��% : Ư���ܾ ���ԵǾ� �ִ� �ܾ� �˻�
select * from students
where name like '%��%'
;

-- _ : �� ĭ ������ ���, �� �տ� 1���� �ܾ �����鼭 ���� ���ԵǾ� �ִ� �ܾ� �˻�
select * from students
where name like '_��%'
;


select * from students;

-- 3��°�� t�� �� �ִ� �̸� �˻�
-- __t
select * from students
where name like '__t%'
;

-- �̸��� 4�ڸ���, 3��° r�� �� �ִ� �̸� �˻�
select * from students
where name like '__r_'
;

select * from students
where name like '__r%' and length(name) = 4
;

-- �̸� ���̰� 4�ڸ� �ΰ� �˻�
select name from students
where length(name) = 4
;

-- �̸��� A�� ���۵Ǵ� �л� �˻�
select no,name from students
where name like 'A%'
;

-- �̸��� a�� �� �ִ� �л� �˻�
select no,name from students
where name like '%a%'
;

-- ��ҹ��� ���о��� a�� �� �ִ� �л� �˻�
-- �ҹ��� ��ȯ(lower), �빮�� ��ȯ (upper), ù���� �빮�� (initcap)
select no,name from students
where lower(name) like '%a%'
;

-- a�� ���Ե��� ���� �̸��� �˻�
select no,name from students
where lower(name) not like '%a%'
;


select manager_id from employees;

-- manager_id 100�� ��� �˻�
select employee_id,emp_name,manager_id from employees
where manager_id = 100
;

-- null �� ��񱳰� �ȵ�.
select employee_id,emp_name,managaer_id from employees
where manager_id = null
;

-- null���� is null ��ɾ� ���
select employee_id,emp_name,manager_id from employees
where manager_id is null
;

select * from employees
where manager_id is not null
;

select * from stu_score;

-- �ѱ� ���� ����
select * from stu_score
order by name asc
;


select * from students;


-- 1�� ���������� �������� �� ����, ���� ������ ���, ���������� �������� ����
select * from students
order by kor desc, eng asc
;

-- total�� ��������

select * from students
order by total desc
;

-- �÷��߰�
alter table students add rank number(3);

-- �÷�Ÿ��
desc students;

select * from students;

update students set rank=0;

commit;

-- ���
select no,rank() over(order by total desc) as rank from students
;

select no,rank() over(order by total desc ) as ranks from students
;

update students s1 set rank = (select ranks 
from (select no, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no )
;

update students s1 set rank = 13
where no = 1
;

update students set rank=0;
select no,rank from students;




-- ����
update students set rank = 13
where no = 1
;

select * from students
where kor>=70;


select * from (���̺�);


select * from (select * from students where avg>=80)
where kor>=70
;


























