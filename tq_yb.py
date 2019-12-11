#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author;Tsukasa


from bs4 import BeautifulSoup
import requests


url_entry = 'http://www.tianqihoubao.com/lishi/'
province_list = []
citys_list = []
city_links_list = []

province_index = 0
city_index = 0

res_html = requests.get(url_entry)
res_html_context = str(res_html.content,'GBK')
soup = BeautifulSoup(res_html_context, 'lxml')
dl_tags = soup.select('.citychk dl')
for dl_child_tag in dl_tags:#,string='更多'
     dt = dl_child_tag.dt
     for dt_a in dt.find_all('a'):      
 #        print(dt.string, ':', dt_a['href'])
         city_unit = []
         city_link_unit = []
         dd = dl_child_tag.dd
         for dd_a in dd.find_all('a'):
             city_unit.append(dd_a.string)
             city_link_unit.append(url_entry[:-7] + dd_a['href'])
#             print('\t', dd_a.string, ':', url_entry[:-7]+ dd_a['href'])
        
         province_list.append(dt.string)
         citys_list.append(city_unit)
         city_links_list.append(city_link_unit)
         
city_sets = city_links_list[province_index]
city_link = city_sets[city_index]
print(city_link)    
#print(province_list[province_index])    

