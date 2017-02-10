create table Borrow
(
stu_id char(8) primary key,
borrow_date date,
book_title char(50),
book_number char(50)
);
--

create table Card
(
stu_id char(8) primary key,
con_cater char(10),
con_palace char(30),
con_pattern char(30),
con_date datetime,
con_money float,
con_left float
);
create table Dorm
(
stu_id char(8) primary key,
in_out_date datetime,
in_out  int
);
create table Library
(
stu_id char(8) primary key,
door char(4),
date datetime 
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
