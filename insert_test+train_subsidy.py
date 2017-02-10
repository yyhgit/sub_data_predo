# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:54:49 2017
将精准资助.test&train下的subsidy/studentID.txt文件通过python导入MySQL.world.subsidy/studentID
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

f=csv.reader(file(r'E:\help\train\subsidy_train.txt','rb'))
#count=0
for sub_0 in f:
#    print sub_0
#    count=count+1
#    if count>10:
#        break
    sub_1=sub_0[0]
    sub_2=int(sub_0[1])
    print sub_1,sub_2
    sql_insert='insert into subsidy(stu_id,sub_num) values(%s,%d)'%(sub_1,sub_2)
#    sql_insert='insert into score(stu_id,dep,rank) values(sc_1,sc_2,sc_3)'
    cursor.execute(sql_insert)
    conn.commit()

#sql_sel = 'select * from score'
#cursor.execute(sql_sel)
#rs=cursor.fetchall()
#for i in rs:
#    print i

conn.close()
cursor.close()