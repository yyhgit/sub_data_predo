# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:39:24 2017
将精准资助.test&train下的SCORE.txt文件通过python导入MySQL.world.score
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

f=csv.reader(file(r'E:\help\test\score_test.txt','rb'))
#count=0
for sc_0 in f:
#    print sc_0
#    count=count+1
#    if count>10:
#        break
    sc_1=sc_0[0]
    sc_2=sc_0[1]
    sc_3=int(sc_0[2])
    print sc_1,sc_2,sc_3
    sql_insert='insert into score(stu_id,dep,rank) values(%s,%s,%d)'%(sc_1,sc_2,sc_3)
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













#
#    word_list = s.split(' ')
#    print word_list
#    word_list = set(word_list)
#    to_w = ' '.join(word_list)
#    print word_list
#    f=open('file.txt','w')
#    f.write(to_w)
#    f.close()
#    
#w_s()
