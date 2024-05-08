select * from employees;

select name from stu_score;
-- 이름검색
select * from stu_score where id like '%a%'
order by no
;
-- row_number() over()
-- 11~20까지 출력하시오.

select rownum,a.* from stu_score a
order by no
;

select count(*) from ( select row_number() over(order by no) rnum,a.* from stu_score a
where id like '%a%' )
;

select count(*) from ( select row_number() over(order by no) rnum,a.* 
from stu_score a where id like '%a%' )
;


select * from ( select row_number() over(order by no) rnum,a.* from stu_score a
where id like '%am%' ) 
;


create table melon (
mno number primary key,
rank number,
v_rank number,
img varchar2(100),
title varchar2(100),
singer varchar2(100),
likeNum number
);

desc melon;

select count(*) from stu_score where id like '%a%';


select * from students
order by id;

select no,id||to_char(no) from students 
order by id;

-- 


select id from students;

rollback;


create table yanolja (
yno number primary key,
img varchar2(100),
title varchar2(100),
grade number,
grade_num number,
price number
);

alter table yanolja modify img varchar2(300);  
alter table melon modify img varchar2(300);  

insert into melon values (
melon_seq.nextval,1,0,'https://cdnimg.melon.co.kr/cm2/album/images/114/74/894/11474894_20240426103349_500.jpg/melon/resize/120/quality/80/optimize',
'SPOT! (feat. JENNIE)','지코 (ZICO)',58974
);

select * from melon;

delete melon;
commit;




