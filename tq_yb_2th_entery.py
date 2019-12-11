# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:49:03 2019

@author: tian
"""


from bs4 import BeautifulSoup
import requests

def to_utf8(deal_str):
    odom=deal_str.split()
    tmp_str = "".join(odom)
    result =  ' '.join(tmp_str.split())
    return result

year_list = []
month_list = []
month_links_list = []
last_3months_link_list = []

year_index = 0
month_index = 0

url_entry = 'http://www.tianqihoubao.com/lishi/'
city_link = 'http://www.tianqihoubao.com/lishi/guangzhou.html'
res_html = requests.get(city_link)
res_html_context = str(res_html.content,'GBK')
soup = BeautifulSoup(res_html_context, 'lxml')


#print(soup.prettify())  # 使用prettify()格式化显示输出
#print(soup.title.string)
h2_tags = soup.select('.wdetail h2')
for h2_child_tag in h2_tags:#
    year_list.append(h2_child_tag.string[:5])
#    print(h2_child_tag.string[:5])


div_tags = soup.select('.wdetail div')
for div_child_tag in div_tags:#
     uls = div_child_tag.select('ul')
     season_unit = []
     season_links_unit = []
     for ul in uls:
         li_tital = ul.find('li')
         for li_a in ul.find_all('a'):        
             print('\t', li_a.string[5:].split("月",1)[0] + "月", ':',url_entry[:-7] + li_a['href'])
             season_unit.append(li_a.string[5:].split("月",1)[0] + "月")
             season_links_unit.append( url_entry[:-7] + li_a['href'])
     month_list.append(season_unit)
     month_links_list.append(season_links_unit)
     print('\n')
     
year_index = len(year_list) - 1

if len(month_list[year_index]) > 2:
    month_index = len(month_list[year_index]) - 1 
    month_links_set = month_links_list[year_index]
    last_3months_link_list.append(month_links_set[month_index-2])
    last_3months_link_list.append(month_links_set[month_index-1])
    last_3months_link_list.append(month_links_set[month_index])
elif len(month_list[year_index]) == 2:
    month_index = len(month_list[year_index - 1]) - 1
    month_links_set = month_links_list[year_index - 1]
    last_3months_link_list.append(month_links_set[month_index])
    month_index = len(month_list[year_index]) - 1
    month_links_set = month_links_list[year_index - 1]    
    last_3months_link_list.append(month_links_set[0])
    last_3months_link_list.append(month_links_set[1])
else:
    month_index = len(month_list[year_index - 1]) - 1
    month_links_set = month_links_list[year_index - 1]
    last_3months_link_list.append(month_links_set[month_index-1])
    last_3months_link_list.append(month_links_set[month_index])
    month_index = len(month_list[year_index]) - 1
    month_links_set = month_links_list[year_index - 1]    
    last_3months_link_list.append(month_links_set[0])
    



