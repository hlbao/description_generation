# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:26:54 2020

@author: Honglin Bao
Department of Computer Science and Engineering
NSF BEACON Center for the Study of Evolution in Action
Michigan State University, East Lansing, MI, USA 48824
BAOHONGL@MSU.EDU
https://web.cse.msu.edu/person/3
"""
#!/usr/bin/python3
#Scraping a perticular link in wikipedia

import sys
import requests
import bs4
res = requests.get('https://es.wikipedia.org/wiki/Andorra/' + ' '.join(sys.argv[1:]))

res.raise_for_status()
#Just to raise the status code
wiki = bs4.BeautifulSoup(res.text,"lxml")
elems = wiki.select('p')
for i in range(len(elems)):
    print(elems[i].getText())
    
    