#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def plaintext(soup):
    '''
    Find section(s) common to all articles, get_text() method for these:
    '''
    # print(soup.get_text(strip=True)) # Plain text version of the entire page
    # print(soup.find_all('p', limit=10).get_text()) # gets first line of the article body cleaned, but still with refs
    # print(soup.find('p').get_text())
    for text in soup.find_all('p'):
        article = text.get_text(' ',strip=True)
    # Do some postprocessing here
    # return (article)
        print(article)

def getlinks(soup,simpends,englishends):
    '''
    Create a list of URL suffixes for wikipedia articles, append to both en. and simple. wikipedia URLs
    '''
    for link in soup.find_all('a'):
        redirect = link.get("href","")
        if re.match("\/wiki/", redirect) and ":" not in redirect and "Main_Page" not in redirect:
            simpends.append("https://simple.wikipedia.org"+redirect)
            englishends.append("https://en.wikipedia.org"+redirect)
    # return(simpends,englishends)
    # print(type(simpends[0]))

def main():
    # MAYBE USE REQUESTS INSTEAD TO OPEN MULTIPLE URLs
    url = 'https://simple.wikipedia.org/wiki/Coronavirus_disease_2019' # Base URL - should be the only thing we call that varies
    html = urlopen(url) # Open URL using library
    soup = BeautifulSoup(html, 'html.parser') # Parse HTML page with Beautiful Soup
    # print(soup.prettify()) # Print html to export to logs and invetigate
    simpends = []
    englishends = []
    plaintext(soup)
    getlinks(soup,simpends,englishends)

if __name__ == '__main__':
    main()
