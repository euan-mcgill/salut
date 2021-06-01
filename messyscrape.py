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

url = 'https://simple.wikipedia.org/wiki/Category:Pain'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
#%%

simpends = []
englishends = []
for link in soup.find_all('a'):
    redirect = link.get("href","")
    if re.match("\/wiki/", redirect) and ":" not in redirect and "Main_Page" not in redirect:
        simpends.append("https://simple.wikipedia.org"+redirect)
        englishends.append("https://en.wikipedia.org"+redirect)
    
#%%
# with loop to write directly to file?

with open('aligned-simple-pain.txt', 'w') as simpout:
    for link in simpends: # change to englishends for en wikipedia
        url = link
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        # print(link) # for URLs above each article
        for text in soup.find_all('p',limit=4):
            article = text.get_text(' ',strip=True)
            # print(article)
            simpout.write(article+'\n')
#%%
with open('aligned-english-pain.txt', 'w') as engout:
    for link in englishends: # change to simpends for simp wikipedia
        url = link
        try:
            html = urlopen(url)
        except:
            pass
        soup = BeautifulSoup(html, 'html.parser')
        # print(link) # for URLs above each article
        for text in soup.find_all('p', limit=3):
            article = text.get_text(' ',strip=True)
            # print(article)
            engout.write(article+'\n')

'''
English articles tend to be around 7x longer than Simple English
ones. Maybe we could just grab the first paragraph of the English
Wiki pages if the coverage tends to be the same as the whole simple
Wiki entry for a given subject
'''
