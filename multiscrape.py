#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests

'''
Code based on wikisc.py, but built to handle multiple files stemming 
from one base file and a parallel language equivalent.

Not yet arranged into functions.
'''

url = 'https://simple.wikipedia.org/wiki/Category:Symptoms'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

simpends = []
englishends = []
for link in soup.find_all('a'):
    redirect = link.get("href","")
    if re.match("\/wiki/", redirect) and ":" not in redirect and "Main_Page" not in redirect:
        simpends.append("https://simple.wikipedia.org"+redirect)
        englishends.append("https://en.wikipedia.org"+redirect)

# for link in simpends: # change to englishends for en wikipedia
#     url = link
#     html = urlopen(url)
#     soup = BeautifulSoup(html, 'html.parser')
#     print(link) # for URLs above each article
#     for text in soup.find_all('p', limit=4):
#         article = text.get_text(' ',strip=True)
#         print(article)

for link in englishends: # change to simpends for simp wikipedia
    url = link
    try:
        html = urlopen(url)
    except:
        pass
    soup = BeautifulSoup(html, 'html.parser')
    print(link) # for URLs above each article
    for text in soup.find_all('p', limit=3):
        article = text.get_text(' ',strip=True)
        print(article)

