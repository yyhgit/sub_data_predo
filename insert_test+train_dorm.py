# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:48:54 2017
在 dorm表格中插入数据
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


f=csv.reader(file(r'E:\help\train\dorm_train.txt','rb'))
#count=0
for dorm_0 in f:
#    print dorm_0
#    count=count+1
#    if count>10:
#        break
    dorm_1=dorm_0[0]
    m=dorm_0[1]
    n=m.split(' ')
    dorm_2=n[0]
    dorm_3=n[1]
#    dorm_4=int(dorm_0[2])
#    print dorm_1,dorm_2,dorm_3
    dorm_5='insert into dorm(stu_id,in_out_date,in_out_time) \
    values(%s,\'%s\',\'%s\')'%(dorm_1,dorm_2,dorm_3)
    
    cursor.execute(dorm_5)
    conn.commit()
#dorm_6='select * from dorm'
#cursor.execute(dorm_6)
#dorm_7=cursor.fetchall()
#for i in dorm_7:
#    print i
conn.close()
cursor.close()