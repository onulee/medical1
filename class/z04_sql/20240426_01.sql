-- ���̺� ����
create table emp01 (
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

-- ���̺���� - ���̺��� �� ������ ��� ����
create table emp02 as
select * from employees;

-- ���̺� ������ �����ϱ�
create table emp03 as
select * from employees where 1=2;

-- ���̺� ������ �ٸ��鼭, �����͸� �����ϱ� ( 3�� -> 14�� )
insert into emp01(emp_id,emp_name,hire_date)
select employee_id,emp_name,hire_date from employees;

-- 1�� ������ �߰�
insert into emp01 values (
 207,'ȫ�浿','2024-04-26'
);

-- ���̺��� ������ �����鼭 �����͸� ���� ( ������ ���� ��� )
insert into emp03
select * from employees;

-- �÷� Ÿ�Ժ���
alter table member
modify(stu_name varchar2(30));

-- �÷� ����
alter table member
drop column pw;

-- �÷� �߰�
alter table member
add (pw varchar2(30));

select * from member;

select mno,id,pw,stu_name,gender from member;
select * from member;

insert into member values (
 seq_mno.nextval,'fff','������','male','1111'
);

-- �÷����� ����
-- �÷������
alter table member modify stu_name invisible;
alter table member modify gender invisible;
-- �÷������ֱ�
alter table member modify stu_name visible;
alter table member modify gender visible;

-- �÷� �Ͻ��� ��� ����
alter table member
set unused(id);

-- ��� ���� ����
alter table member
drop unused columns;


-- ���̺� ����
--drop table s_info;
-- drop table m_date;
drop table emp03;

-- ���̺� �̸� ����
rename emp01 to employees01;

-- [ ���Ἲ �������� ]
-- foreign key�� �ٸ� ���̺��� ������ �Է½� 
-- ����Ǿ� �ִ� ���� ���̺� �Է��Ϸ��� �����Ͱ� �ִ��� Ȯ��

-- drop table employees01;
-- drop table emp02;
-- drop table member;
-- drop table board;

create table member (
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6)
);

insert into member values(
'aaa','1111','ȫ�浿','male'
);

insert into member(id,pw,name) values(
'bbb','1111','������'
);

insert into member(id,pw) values(
'ccc','1111'
);

--����
insert into member(id) values(
'ddd'
);
insert into member(id,pw) values(
'ddd','1111'
);

insert into member(id,pw,name) values(
'a','1111','ȫ�浿'
);

-- �������� : not null -  null���� ����
create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
1,'������','1',1
);

-- �������� : unique -  �ߺ��� ����, null���
create table emp03(
empno number(4) unique,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp03 values(
'1','ȫ�浿','1',1
);

insert into emp03 values(
null,'ȫ�浿','1',1
);

insert into emp03 values(
'3','�̼���','2',2
);

insert into emp03 values(
null,'������','2',2
);

insert into emp03 values(
1,'�豸','3',3
);

-- ����. 1 ȫ�浿 �˻��Ͻÿ�.
select * from emp03
where empno='1';

-- ����. null ȫ�浿 �˻��Ͻÿ�.
select * from emp03
where empno is null and ename='ȫ�浿';
-- ����. null�� ��� ����� �˻��Ͻÿ�.
select * from emp03
where empno is null;

select * from emp03
where empno is not null;

select * from emp03;

Create table emp01 (
Empno number(4) primary key,
Ename varchar2(20) not null,
Job varchar(9),
Deptno number(2)
);

-- 5�� null,1,2,3,1
insert into emp01 values(
1,'ȫ�浿','0001',1
);
insert into emp01 values(
null,'ȫ�浿','0001',1
);

select * from emp01;

select * from emp01
where empno=3;

-- foreign key (�ܷ�Ű)
-- drop table emp01;

-- emp01 ���̺� ����
create table emp01 (
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(6)
);

insert into emp01 values(
1,'ȫ�浿','0001',10
);

insert into emp01 values(
2,'������','0002',20
);

insert into emp01 values(
3,'�̼���','0002',30
);

-- deptno 10-270
insert into emp01 values(
4,'�豸','0003',270
);

-- �ܷ�Ű�� ������ �Ǹ�, deptno�� ���� �����͸� �Է��� �ص� ������ ��.
-- error
insert into emp01 values(
5,'������','0004',1
);

-- foreign key ����
alter table emp01
drop constraint fk_deptno;

commit;

-- emp01 foreign key �߰�
-- fk_deptno ��Ī
-- add constraint ��Ī foreign key(�����÷�) references �ٸ����̺�(�÷��̸�)
alter table emp01
add constraint fk_deptno foreign key(deptno)
references dept01(deptno)
;


select * from dept01;

alter table emp01
modify(deptno number(6));

-- dept01 ���̺� ����
create table dept01(
deptno number(6) primary key,
dept_name varchar2(80)
);

-- �÷��� �����߰�
insert into dept01 (deptno,dept_name)
select department_id,department_name from departments;

-- �÷��� Ÿ�� ����
alter table dept01
modify ( dept_name varchar2(80));

desc dept01;

desc member;
-- 
create table board (
bno number(4) primary key,
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);

insert into board values(
1,'aaa','�Խñ�1','����1'
);
insert into board values(
8,'bbb','�Խñ�8','����8'
);

commit;

select * from board;

alter table board
add constraint fk_id foreign key (id)
references member(id);

-- comment ���̺� ������̺�

create table comments(
 cno number(4) primary key,
 bno number(4),
 cpw varchar2(20),
 ccontent varchar2(1000),
 constraint fk_bno foreign key(bno)
 references board(bno)
);
-- ��۴ޱ�
insert into comments values (
5,5,'1111','��۳���4'
);

-- fk�� ����Ҷ� ���� 
-- fkŰ�� ��ϵǾ� �ִ� ��� �����͸� ������Ű�� ��.
-- fkŰ�� ��ϵǾ� �ִ� �����ʹ� ��� ���� ��Ű�� ��.

delete board where bno=5;

commit;

select * from board;
select * from comments;

select * from board;

-- �ܷ�Ű ����
alter table board drop constraints fk_id;
alter table comments drop constraints fk_bno;

select * from board;
select * from comments;

delete board where bno=1;

alter table board
add constraint fk_id foreign key (id)
references member(id);

-- fk_cno�� ������ �ǵ��� ��.
alter table comments 
add contraint fk_bno foreign key(bno)
references comments(bno) on delete cascade;

delete comments where cno=2;

--- check �������� Ư������ ����, Ư������ �Էµǵ��� ��.
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001', -- �÷��� �����͸� ���� ������ �ڵ����� 0001�� �����.
sal number(7,2) check(sal between 2000 and 20000),
gender varchar2(6) check(gender in('����','����'))
);

insert into emp(empno,ename,job,sal,gender) values(
1,'ȫ�浿','0002',3000,'����'
);

insert into emp(empno,ename,job,sal,gender) values(
2,'������','0003',4000,'����'
);

-- ���� ����,���ڸ� �Է°���
insert into emp(empno,ename,job,sal,gender) values(
3,'�̼���','0004',5000,'��'
);

insert into emp(empno,ename,job,sal,gender) values(
3,'�̼���','0004',5000,'����'
);

insert into emp(empno,ename,job,sal,gender) values(
4,'������','0005',2000,'����'
);

-- ���� 2000~20000
insert into emp(empno,ename,job,sal,gender) values(
5,'�豸','0006',30000,'����'
);

-- check 2000-20000
insert into emp(empno,ename,job,sal,gender) values(
5,'�豸','0006',20000,'����'
);

-- job default '0001' - job �Է��� ������ '0001'
insert into emp(empno,ename,sal,gender) values(
6,'������',10000,'����'
);

select * from emp;







