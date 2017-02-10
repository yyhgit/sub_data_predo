--
drop table borrow;
create table Borrow
(
stu_id char(8), 
bw_time date,
book_number char(30)
);

drop table Card;
create table Card
(
stu_id char(8) ,
con_cater char(10),
con_palace char(30),
con_pattern char(30),
con_date date,
con_date time,
con_money float,
con_left float
);


drop table dorm;
create table Dorm
(
stu_id char(8), 
in_out_date date,
in_out_time time
);



create table Library
(
stu_id char(8), --primary key,
--door char(4),
lib_date date,
lib_time time
);

create table Library
(
stu_id char(8), 
lib_date date,
lib_time time
);



create table Score
(
stu_id char(8) primary key,
dep char(20),
rank int
);


create table Subsidy
(
stu_id char(8) primary key,
sub_num int
);


create  table department
(
stu_id char(8) primary key,
dep_1 int,
dep_2 int,
dep_3 int,
dep_4 int,
dep_5 int,
dep_6 int,
dep_7 int,
dep_8 int,
dep_9 int,
dep_10 int,
dep_11 int,
dep_12 int,
dep_13 int,
dep_14 int,
dep_15 int,
dep_16 int,
dep_17 int,
dep_18 int,
dep_19 int
);