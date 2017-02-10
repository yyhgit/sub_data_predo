# -*- coding: utf-8 -*-
"""
Spyder Editor
将精准资助.test+train数据导入到library表中
This is a temporary script file.
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


f=csv.reader(file(r'E:\help\test\library_test.txt','rb'))
#count=0
for lib_0 in f:
#    print lib_0
#    count=count+1
#    if count>10:
#        break
    lib_1=lib_0[0]
    m=lib_0[2]
    n=m.split(' ')
    lib_3=n[0] #.replace('/','-')
    lib_4=n[1]
#    print lib_1,lib_3
    lib_go="insert into library(stu_id,lib_date,lib_time)\
    values(%s,'%s','%s')"%(lib_1,lib_3,lib_4)
    
    cursor.execute(lib_go)
    conn.commit()
    
    
#lib_sql='select * from library'
#cursor.execute(lib_sql)
#lib_print=cursor.fetchall()
#for i in lib_print:
#    print i
    
conn.close
cursor.close
        