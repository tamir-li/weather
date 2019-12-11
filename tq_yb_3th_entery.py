# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:15:15 2019

@author: tian
"""


from bs4 import BeautifulSoup
import requests
import os
import csv
#import re

def to_utf8(deal_str):
    odom=deal_str.split()
    tmp_str = "".join(odom)
    result =  ' '.join(tmp_str.split())
    return result



headers=[]
tinqi_data = []

url_entry = 'http://www.tianqihoubao.com/lishi/'
tianqi_entry = 'http://www.tianqihoubao.com/lishi/guangzhou/month/201907.html'
res_html = requests.get(tianqi_entry)
res_html_context = str(res_html.content,'GBK')

soup = BeautifulSoup(res_html_context, 'lxml')


#print(soup.prettify())  # 使用prettify()格式化显示输出

print(soup.title.string)
h1_tags = soup.select('div#content h1')
print(h1_tags[0].string)

tables_tags = soup.select('div#content table')
#print(str(tables_tags[0].find_all('tr')))

row_index = 0
for tr_child_tag in tables_tags[0].find_all('tr'):#   
     tds = tr_child_tag.select('td')
     tb_row = []
     if row_index > 0:
         print('\t', to_utf8(tds[0].a.string), '\t', to_utf8(tds[1].string), '\t', to_utf8(tds[2].string), '\t', to_utf8(tds[3].string))
         tb_row.append(to_utf8(tds[0].a.string))
         tb_row.append(to_utf8(tds[1].string))
         tb_row.append(to_utf8(tds[2].string))
         tb_row.append(to_utf8(tds[3].string))
         tinqi_data.append(tb_row)
         row_index += 1;
         continue
     else:
         print('\t', to_utf8(tds[0].b.string), '\t', to_utf8(tds[1].b.string), '\t', to_utf8(tds[2].b.string), '\t', to_utf8(tds[3].b.string))
         headers.append(to_utf8(tds[0].b.string))
         headers.append(to_utf8(tds[1].b.string))
         headers.append(to_utf8(tds[2].b.string))
         headers.append(to_utf8(tds[3].b.string))
         row_index += 1;
         continue
     
        
file_path = os.getcwd() + '\\tianqi.csv'

try:
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
 
        if headers is not None:
            writer.writerow(headers)
 
        for row in tinqi_data:
            writer.writerow(row)
 
        print("Write a CSV file to path %s Successful." % file_path)
except Exception as e:
    print("Write an CSV file to path: %s, Case: %s" % (file_path, e))

