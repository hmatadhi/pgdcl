#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import re
from indic_transliteration import sanscript
from indic_transliteration import detect
from bs4 import BeautifulSoup


def check_dvitiiya(input_word):
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
       p = re.compile('\[(.*)\]\{(.*)\}', flags=re.UNICODE)
       for lemma_table in lemma_tables:  
           m = p.search(lemma_table.get_text())
           if (m):
               print(m.group())
               p2 = re.compile('du', flags=re.UNICODE)
               m2 = p2.search(m.group())
               if (m2):
                   print(m2.group())
                   return True
    return False
               
print("input:" + sys.argv[1])
scheme = detect.detect(sys.argv[1])
output=""
print("input: " + sys.argv[1] + " ---   encoding = " + str(scheme))
if (str(scheme) == "Devanagari"):
    v_scheme_map = sanscript.SchemeMap(
                    sanscript.SCHEMES[sanscript.DEVANAGARI],
                    sanscript.SCHEMES[sanscript.VELTHUIS])
    output = sanscript.transliterate(sys.argv[1], scheme_map=v_scheme_map)
else:
    print("please enter the input in devanagari")

l = len(output)
last_token2=output[l-2:]
last_token1=output[l-1:]

print(output)
print(last_token2)
print(last_token1)

s_1_1_11_ending_check=((last_token2 == "ii") or (last_token2 == "uu")
      or (last_token1 == "e"))

s_1_1_11_dvitiiya_check  = check_dvitiiya(output)

print("s_1_1_11 पदान्त  ईदूदेद् check =" + str(s_1_1_11_ending_check))
print("s_1_1_11  द्विवचनं check = " + str(s_1_1_11_dvitiiya_check))

if (s_1_1_11_ending_check and s_1_1_11_dvitiiya_check):
    print("s_1_11 ईदूदेद् and  द्विवचनं both true,  hence प्रगृह्यम् = True")
elif(s_1_1_11_ending_check):
    print("s_1_11 ईदूदेद् True but द्विवचनं is False,  hence प्रगृह्यम् = False")    
elif(s_1_1_11_dvitiiya_check):
    print("s_1_1_11  द्विवचनं True but ईदूदेद् False,  hence प्रगृह्यम् = False")    
else:    
    print("s_1_1_11 Both  द्विवचनं  and ईदूदेद् False, hence  प्रगृह्यम् = False")

