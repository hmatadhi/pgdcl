#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import re
if (len(sys.argv) != 2):
    print ("USAGE: python lemma.py <arg>")
    print ("Arguments Given = " + str(sys.argv))
else:
    #print "Argument = " + sys.argv[1]
    input_word=sys.argv[1]
    #print (input_word)
    lemma_uri="https://sanskrit.inria.fr/cgi-bin/SKT/sktlemmatizer.cgi"
    lemma_params="lex=SH&q=" + input_word + "&t=VH&c=Noun"
    lemma_url = lemma_uri + "?" + lemma_params
    #print (lemma_url)
    params = {"lex": "SH", "q": input_word, "t":"VH", "c":"Noun"}
    s = requests.Session()
    #print ("session ready")
    data = s.get(lemma_url)
    #print("data = " + str(data.content))
    data.encoding = "UTF-8"
    soup = BeautifulSoup(data.text, "html.parser")
    lemma_tables = soup.find_all("table", class_="yellow_cent")
    if (lemma_tables):
       p = re.compile('\[(.*)\]\{(.*)\}', flags=re.LOCALE)
       for lemma_table in lemma_tables:  
           m = p.search(lemma_table.get_text())
           if (m):
               print(m.group())
