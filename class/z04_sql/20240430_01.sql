select * from stu_score;

select * from stu_score where name like '_a%' order by no desc
;

desc stu_score;

select a.*,name from board a,member b
where a.id = b.id
;

select bno,a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile 
from board a,member b
where a.id = b.id
;

select round(avg(salary),2) as salary from employees
;


