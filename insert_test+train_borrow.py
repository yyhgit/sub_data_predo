# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:43:04 2017
将精准资助.test&train下的borrow.txt文件通过python导入MySQL.world.borrow
@author: zmb
"""
import csv
import MySQLdb
conn=MySQLdb.connect(
                     host='localhost',
                     port=3306,
                     user='root',
                     passwd='root',
                     db='world',
                     charset='utf8'
                     )

cursor=conn.cursor()

f=csv.reader(file(r'E:\help\test\borrow_test.txt','rb'))
count=0
for bw_0 in f:
    print bw_0
    count=count+1
    if count>10:
        break
    bw_1=bw_0[0]
    bw_2=bw_0[1]
#    bw_3=bw_0[2]
    bw_4=bw_0[3]
    print bw_1,bw_2,bw_4
    sql_insert='insert into score(stu_id,borrow_date,book_number) values(%s,\'%s\',%s)'%(bw_1,bw_2,bw_4)

    cursor.execute(sql_insert)
    conn.commit()

    
#sql_sel = 'select * from score'
#cursor.execute(sql_sel)
#rs=cursor.fetchall()
#for i in rs:
#    print i

conn.close()
cursor.close()
