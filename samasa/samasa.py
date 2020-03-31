# -----------------------------------------------------------------------------
# calc.py
# -----------------------------------------------------------------------------
#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import re
from indic_transliteration import sanscript
from indic_transliteration import detect
from bs4 import BeautifulSoup
import sys
import json

sys.path.append('../..')

from sly import Lexer, Parser



class subanta:
    gen = { 'male': 0, 'female' : 1, 'neuter' : 2 }
    vachana = {'eka':1, 'dvi':2, 'bahu':3}    
    vibhakthi = { 'prathama':2,'dvitiya':3,'tritiya':4,'chaturthi':5,\
                  'panchami':6,'shashti':7,'sapthami':8,'sambhodana':9}

    tables=[]                   
    def __init__(self, pratipadika):

         self.pratipadika = pratipadika

         self.get_sup_tables();

    def get_table(self, data, class_=""):
        #data.encoding = "UTF-8"
        #print("data = " + str(data.content))    
        soup = BeautifulSoup(data.text, features="html.parser")
        #class_="inflexion"
        lemma_tables = soup.find_all("table",class_=class_)
        table_data = [];
        for lemma_table in lemma_tables:
            #print(lemma_table.prettify())
            if (len(lemma_table.get_text())):
                #print("->" +lemma_table.get_text()+ "->\n") 
                table_data = list()
                for tr in lemma_table.find_all('tr'):
                    row_data = list()
                    for th in tr.find_all('th'):
                        row_data.append(d_to_v(th.text))
                    for td in tr.find_all('td'):
                        row_data.append(d_to_v(td.text))                        
                    table_data.append(row_data)
        return table_data

    def get_sup_tables(self):
        self.tables = []
        input_word = self.pratipadika
        #print("get_sup_tables for " + input_word)
        if ("[" in input_word) or  (" " in input_word):
            input_word = "tad"
            self.with_pronoun = True;
            lexid = "pron"
            class_ = ""
            lemma_uri="https://sanskritlibrary.org/cgi-bin/cgi-skt/decl"
            lemma_params_m="stem=" + input_word + "&gender=m&lexid=" + lexid + "&filter=SktDevaUnicode"
            lemma_params_f="stem=" + input_word + "&gender=f&lexid=" + lexid + "&filter=SktDevaUnicode"
            lemma_params_n="stem=" + input_word + "&gender=n&lexid=" + lexid + "&filter=SktDevaUnicode"            
        else: 
            self.with_pronoun = False;
            lexid = ""
            class_ = "inflexion"            
            lemma_uri="https://sanskrit.inria.fr/cgi-bin/SKT/sktdeclin.cgi"
            lemma_params_m="lex=SH&q=" + input_word + "&t=VH&g=Mas&font=roma"
            lemma_params_f="lex=SH&q=" + input_word + "&t=VH&g=Fem&font=roma"
            lemma_params_n="lex=SH&q=" + input_word + "&t=VH&g=Neu&font=roma"

        #lemma_uri="http://tdil-dc.in/cgi-bin/skt_gen/noun/noun_gen.cgi"
        #lemma_params_f="encoding=SLP&rt=" + input_word + "&gen=%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A5%80"
        #lemma_params_n="encoding=SLP&rt=" + input_word + "&gen=%E0%A4%A8%E0%A4%AA%E0%A5%81%E0%A4%82"
        #lemma_params_m="encoding=SLP&rt=" + input_word + "&gen=%E0%A4%AA%E0%A5%81%E0%A4%82"


        sess = requests.Session()
        data_m = sess.get(lemma_uri + "?" + lemma_params_m)
        data_f = sess.get(lemma_uri + "?" + lemma_params_f)
        data_n = sess.get(lemma_uri + "?" + lemma_params_n)

        table_m = self.get_table(data_m,class_=class_)
        self.tables.append(table_m) 
        table_f = self.get_table(data_f,class_=class_) 
        self.tables.append(table_f) 
        table_n = self.get_table(data_n,class_=class_) 
        self.tables.append(table_n)         
        return self.tables



    def get_subantha(self, g,n,v):
        try:
            flag = self.tables[0][0][1]
            #print("flag=[" + flag  + "]")
            #print("g=" + str(g) )
            #print("n=" + str(n) )
            #print("v=" + str(v) )  
            if (flag == 's'):
                if (v > 1):
                    v = v + 1
            #print("updated v=" + str(v) )                                          
            #print(str(self.tables[g]))
            #print(str(self.tables[g][v]))  
            #print(str(self.tables[g][v][n])) 
            strRet = self.tables[g][v][n]
        except:
            #print("Index error")
            strRet = ""
        return strRet

    def v(self, vibhakthiStr, num="eka"):
        vstrList = [] 
        #print ("self.with_pronoun=" + str(self.with_pronoun))
        vstr_m = self.get_subantha(self.gen['male'], self.vachana[num], self.vibhakthi[vibhakthiStr]) 
        vstr_f = self.get_subantha(self.gen['female'], self.vachana[num], self.vibhakthi[vibhakthiStr])  
        vstr_n = self.get_subantha(self.gen['neuter'], self.vachana[num], self.vibhakthi[vibhakthiStr]) 
        if (self.with_pronoun):
             vstr_m = self.pratipadika + " " + vstr_m
             vstr_f = self.pratipadika + " " + vstr_f
             vstr_n = self.pratipadika + " " + vstr_n
        if (vstr_m and (vstr_m not in vstrList)):
            vstrList.append(vstr_m)  
        if (vstr_f and (vstr_f not in vstrList)):
            vstrList.append(vstr_f)   
        if (vstr_n and (vstr_n not in vstrList)): 
            vstrList.append(vstr_n) 
        if (len(vstrList) == 1):
            vStr =  vstrList[0]
        else:
            vStr = str(vstrList)                             
        return  str(vstrList)

    vibhakthi = { 'prathama':2,'dvitiya':3,'tritiya':4,'chaturthi':5,\
                  'panchami':6,'shashti':7,'sapthami':8,'sambhodana':9}
    def v1(self):
        return  self.v("prathama")

    def v2(self):
        return  self.v("dvitiya")

    def v3(self):                            
        return  self.v("tritiya")

    def v4(self):
        return  self.v("chaturthi")

    def v5(self):
        return  self.v("panchami")

    def v6(self, num="eka"):                            
        return  self.v("shashti", num)

    def v7(self):
        return  self.v("sapthami")

    def v8(self):                            
        return  self.v("sambhodana")
        

def d_to_v(input_string):
    scheme = detect.detect(input_string)
    #print("input: " + input_string + " ---   encoding = " + str(scheme))
    if (str(scheme) == "Devanagari"):
      v_scheme_map = sanscript.SchemeMap(
                      sanscript.SCHEMES[sanscript.DEVANAGARI],
                      sanscript.SCHEMES[sanscript.VELTHUIS])
      output_string = sanscript.transliterate(input_string, scheme_map=v_scheme_map)
      #print("Ascii translation for tokenization:\n")
      scheme = detect.detect(output_string)
      #print("input: " + output_string + " ---   encoding = " + str(scheme))
    else:
      output_string = input_string
      #print("please enter the input in devanagari")
    return output_string

def v_to_d(input_string):
    scheme = detect.detect(input_string)
    if (str(scheme) == "Velthuis"):
      v_scheme_map = sanscript.SchemeMap(
                      sanscript.SCHEMES[sanscript.VELTHUIS],
                      sanscript.SCHEMES[sanscript.DEVANAGARI])
      output_string = sanscript.transliterate(input_string, scheme_map=v_scheme_map)
      scheme = detect.detect(output_string)
    else:
      output_string = input_string
    return output_string    

def d_to_i(input_string):
    scheme = detect.detect(input_string)
    #print("input: " + input_string + " ---   encoding = " + str(scheme))
    if (str(scheme) == "Devanagari"):
      v_scheme_map = sanscript.SchemeMap(
                      sanscript.SCHEMES[sanscript.DEVANAGARI],
                      sanscript.SCHEMES[sanscript.ITRANS])
      output_string = sanscript.transliterate(input_string, scheme_map=v_scheme_map)
      #print("Ascii translation for tokenization:")
      scheme = detect.detect(output_string)
      #print("output: " + output_string + " ---   encoding = " + str(scheme))      
    else:
      output_string = input_string
      #print("please enter the input in devanagari")
    return output_string    


def i_to_d(input_string):
    scheme = detect.detect(input_string)
    if (str(scheme) == "ITRANS"):
        inputSchemeIndex = sanscript.ITRANS
    elif   (str(scheme) == "HK"):  
        inputSchemeIndex = sanscript.HK
    if ((str(scheme) == "ITRANS") or (str(scheme) == "HK")):            
      v_scheme_map = sanscript.SchemeMap(
                      sanscript.SCHEMES[inputSchemeIndex],
                      sanscript.SCHEMES[sanscript.DEVANAGARI])
      output_string = sanscript.transliterate(input_string, scheme_map=v_scheme_map)
    else:
      output_string = input_string
    return output_string 

class SamasaGenerator():
    def f_a1(self, pp):
        if (pp == "upa"):
            return d_to_v("समीपं")
        else:
            return (pp)

    def f_tp(self, pp):
        if (pp == "pra"):
            return d_to_v("प्रकृष्टः")
        else:
            return pp

    def f_U(self, pp):
        if (pp == "kara.h"):
            return d_to_v("करोति")
        else:
            return pp

    def f_bsmn(self, pp):
        if (pp == "a"):
            return d_to_v("अविद्यमानः")
        else:
            return pp

    def a1(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v6() + self.f_a1(pp);
        return sp;  
    def a2(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v3() + d_to_v(" विपरीतं वृत्तं");
        return sp; 
    def a3(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v6() + " " + sub_up.v1() + d_to_v("यस्मिन् देशे");
        return sp;
    def a4(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v6() + " " + sub_up.v6() + d_to_v("समाहारः");
        return sp;
    def a5(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() + " " + d_to_v("यस्मिन् देशे");
        return sp;
    def a6(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v6() + " " + sub_up.v6() + " " + d_to_v("समाहारः");
        return sp;
    def a7(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_up.v6() + " " +  pp ;
        return sp;
    def t1(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v6() + " ";
        return sp;
    def t2(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v2() + " " +  up ;
        return sp;
    def t3(self,pp, up):
        sub_pp =subanta(pp)         
        sp =  sub_pp.v3()  + " " + up ;
        return sp;
    def t4(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp = sub_pp.v4() + " " +  up ;
        return sp;
    def t5(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp = sub_pp.v5() + " " + up ;
        return sp;
    def t6(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp = sub_pp.v6()  + " " + up ;
        return sp;                                
    def t7(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)     
        sp = sub_pp.v7() + " " + up ;
        return sp; 
    def tn(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  " न " + up;
        return sp; 
    def tds(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp = sub_pp.v6("bahu") + " " + sub_up.v6("bahu") + d_to_v(" समाहारः");
        return sp; 
    def tdt(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  d_to_v("अष्ठसु ") + sub_up.v7("bahu") + d_to_v(" संसृतः");
        return sp; 
    def tdu(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + up;
        return sp; 
    def tg(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  pp + up;
        return sp; 
    def tk(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  pp + up;
        return sp; 
    def tp(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  self.f_tp(pp) + " " + up;
        return sp; 
    def tm(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  pp + " " + up;
        return sp;
    def tb(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp = sub_pp.v1() + " " + sub_up.v1(up);
        return sp;
    def U(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp = sub_pp.v2() + " " + self.f_U(up);
        return sp;
    def k1(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)  
        sp =   sub_pp.v1() + d_to_v("तत्") + sub_up.v1() + d_to_v("च");
        return sp;
    def k2(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + d_to_v(" च ") + sub_up.v1() + d_to_v("च");
        return sp;
    def k3(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + d_to_v(" च असौ ") + sub_up.v1() + d_to_v("च");
        return sp;
    def k4(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + d_to_v(" इव ") + sub_up.v1() ;
        return sp;
    def k5(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() + d_to_v(" इव ");
        return sp;
    def k6(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + d_to_v(" एव ") + sub_up.v1() ;
        return sp;
    def k7(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + d_to_v(" इति ") + sub_up.v1() ;
        return sp;
    def km(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + d_to_v(" प्रियः ") + sub_up.v1() ;
        return sp;
    def bs2(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() + d_to_v(" यम्") ;
        return sp;
    def bs3(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() + d_to_v(" येन ") ;
        return sp;
    def bs4(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() + d_to_v(" यस्मै ")  ;
        return sp;
    def bs5(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() + d_to_v(" यस्मात् ")  ;
        return sp;
    def bs6(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() + d_to_v(" यस्य ") ;
        return sp;
    def bs7(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() + d_to_v(" यस्मिन् ") ;
        return sp;
    def bsd(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v6() + d_to_v(" च ") + sub_up.v6() + d_to_v(" च यदन्तरालं ");
        return sp;
    def bsp(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + d_to_v(" च ") + sub_up.v3() + d_to_v(" च प्रहृत्य इदं युद्धं प्रवृत्तं ");
        return sp;
    def bsg(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v7() + d_to_v(" च ") + sub_up.v7() + d_to_v(" च गृहीत्वा इदं युद्धं प्रवृत्तं  ");
        return sp;
    def bsmn(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  self.f_bsmn(pp) + " " + sub_up.v1() + d_to_v(" यस्य ") ;
        return sp;
    def bvp(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() ;
        return sp;
    def bss(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + d_to_v(" वा ") + sub_up.v1() + d_to_v(" यस्य ") ;
        return sp;
    def bsu(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + d_to_v(" इव ") + sub_up.v1() + d_to_v(" यस्य ") ;
        return sp;
    def bv(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() ;
        return sp;
    def bvs(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_up.v6() + " " + up + d_to_v(" यस्य ");
        return sp;
    def bvs_Caps(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v3() + d_to_v(" सह ") ;
        return sp;
    def bvu(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v6() + d_to_v(" इव ") + up + d_to_v(" यस्य ");
        return sp;
    def bb(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() ;
        return sp;
    def di(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + d_to_v(" च ") + sub_up.v1() + d_to_v(" च ") ;
        return sp;
    def ds(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp = sub_pp.v1() + d_to_v(" च ") + sub_up.v1() + d_to_v(" च " );
        return sp;
    def E(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v2("dvi") ;
        return sp;
    def S(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_up.v1() + " " + sub_pp.v1() ;
        return sp;
    def d(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() ;
        return sp;
    def K(self,pp, up):
        sub_pp =subanta(pp)  
        sub_up =subanta(up)         
        sp =  sub_pp.v1() + " " + sub_up.v1() ;
        return sp;

class SamasaLexer(Lexer):
    tokens = { TAG,\
               A1, A2, A3, A4, A5, A6,A7, \
               BS2,BS3,BS4,BS5,BS6,BS7,\
               BSD,BSG,BSP,BSS,BSU,\
               BSMN,BVP,\
               BVS,BVSC,BVU,\
               BB,BV,\
               DI,DS,\
               K1,K2,K3,K4,K5,K6,K7,\
               KM,\
               T1,T2,T3,T4,T5,T6,T7,\
               TB,TG,TM,TN,TP,TK,\
               TDS,TDU,TDT,\
#               E,S,U,D,\
               WORD, HIPHEN, LPAREN, RPAREN, DANDA, PLUS, NUMBER }
    ignore = ' \t'

    # Tokens
    HIPHEN   = r'-'
    LPAREN = r'<'
    RPAREN = r'>' 
    DANDA = r'\|'
    PLUS = r'\+'
    TAG  = r'A[1-7]|Bs[2-7]|Bs[dgpsu]|Bsm[gn]|Bv[psSU]|B[bv]|D[is]|K[1-7]|Km|T[1-7]|T[bgmnpk]|Td[sut]|[KU]'
    #TAG  = r'A[1-6]|Bs[2-7]|Bs[dgpsu]|Bsm[gn]|Bv[sSU]|B[bv]|D[is]|K[1-5]|Km|T[1-7]|T[bgmnp]|Tds|[ESUd].'
    TAG['A1'] = A1
    TAG['A2'] = A2
    TAG['A3'] = A3
    TAG['A4'] = A4
    TAG['A5'] = A5
    TAG['A6'] = A6
    TAG['A7'] = A7    
    TAG['Bs2'] = BS2
    TAG['Bs3'] = BS3
    TAG['Bs4'] = BS4
    TAG['Bs5'] = BS5
    TAG['Bs6'] = BS6
    TAG['Bsd'] = BSD
    TAG['Bsg'] = BSG
    TAG['Bsp'] = BSP
    TAG['Bss'] = BSS
    TAG['Bsu'] = BSU
    TAG['Bsmn'] = BSMN
    TAG['Bvp'] = BVP    
    TAG['Bvs'] = BVS
    TAG['BvS'] = BVSC
    TAG['BvU'] = BVU
    TAG['Bb'] = BB
    TAG['Bv'] = BV
    TAG['Di'] = DI
    TAG['Ds'] = DS
    TAG['K1'] = K1
    TAG['K2'] = K2
    TAG['K3'] = K3
    TAG['K4'] = K4
    TAG['K5'] = K5
    TAG['K6'] = K6
    TAG['K5'] = K5
    TAG['Km'] = KM
    TAG['T1'] = T1
    TAG['T2'] = T2
    TAG['T3'] = T3
    TAG['T4'] = T4
    TAG['T5'] = T5
    TAG['T6'] = T6
    TAG['Tb'] = TB
    TAG['Tg'] = TG
    TAG['Tm'] = TM
    TAG['Tn'] = TN
    TAG['Tp'] = TP
    TAG['Tk'] = TK  
    TAG['Tdu'] = TDU 
    TAG['Tds'] = TDS 
    TAG['Tdt'] = TDT               
    #TAG['E.'] = E
    #TAG['S.'] = S
    #TAG['U.'] = U
    #TAG['d.'] = D
    WORD = r'[a-z_~\.\"|]+'
    NUMBER = r'[0-9]+'
    # Special symbols
    # Ignored pattern
    ignore_newline = r'\n+'

    literals = { '<', '>'}

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

    def __init__(self):
         self.nesting_level = 0

    @_(r'<')
    def lbrace(self, t):
        t.type = '<'      # Set token type to the expected literal
        self.lastTag = '<'
        self.nesting_level += 1
        #print("New Lquote" + str(self.nesting_level))
        return t

    @_(r'>')
    def rbrace(self, t):
        t.type = '>'      # Set token type to the expected literal
        self.lastTag = '>'
        self.nesting_level -=1
        #print("End Lquote" + str(self.nesting_level))
        return t 

class SamasaParser(Parser):
    tokens = SamasaLexer.tokens
    sg = SamasaGenerator();

    def __init__(self):
        self.compounds = { }

    @_('optcompound')
    def sentence(self, p):
        return p.optcompound

    @_('compoundgroup empty')
    def optcompound(self, p):
        return p.compoundgroup

    @_('')
    def empty(self, p):
        pass

    @_('compound')
    def compoundgroup(self, p):
        return p.compound

    @_('sentence shlokaend')
    def sentence(self, p):
        samasthaPada = p.sentence + " " + p.shlokaend
        print("Sentence: Shloka Completion:" + samasthaPada)          
        return samasthaPada

    @_('sentence DANDA')
    def sentence(self, p):
        samasthaPada = p.sentence + " " + p.DANDA
        print("Sentence: Completion:" + samasthaPada)          
        return samasthaPada

    @_('sentence compound')
    def compoundgroup(self, p):
        samasthaPada = p.sentence + " " + p.compound
        print("Sentence: Compound Group:" + samasthaPada)          
        return samasthaPada

    @_('compound word')
    def sentence(self, p):
        samasthaPada = p.compound + " " + p.word
        print("Sentence: Simple Join:" + samasthaPada)            
        return samasthaPada

    @_('word PLUS compound')
    def sentence(self, p):
        samasthaPada = p.word + "+" + p.compound
        print("Sentence: Sandhi Join:" + samasthaPada)        
        return  samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A1')
    def compound(self, p):
        print("Compound: Avyayi Bhava -> Avyaya Poorvapada")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.a1(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A2')
    def compound(self, p):
        print("Compound: Avyayi Bhava -> Avyaya Uttarapada")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.a2(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A3')
    def compound(self, p):
        print("Compound: Avyayi Bhava -> Tishtadgu Prabhrithi")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.a3(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A4')
    def compound(self, p):
        print("Compound: Avyayi Bhava -> Sankhya Poorvapada Nadyuttarapada")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.a4(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A5')
    def compound(self, p):
        print("Compound: Avyayi Bhava -> Nadyuttarapada, Anyapadarthe Samjnyaayaam")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.a5(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A6')
    def compound(self, p):
        print("Compound: Avyayi Bhava -> Sankhya Poorvapada Vamshyotarapada")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.a6(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada        

    @_('LPAREN component HIPHEN component RPAREN A7')
    def compound(self, p):
        print("Compound: Avyayi Bhava -> Paare Madhye Poorvapada Shashtyuttarapada")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.a7(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN T1')
    def compound(self, p):
        print("Compound: Prathama Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.t1(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN T2')
    def compound(self, p):
        print("Compound: Dwiteeya Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.t2(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN T3')
    def compound(self, p):
        print("Compound: Triteeya Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.t3(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

                        
    @_('LPAREN component HIPHEN component RPAREN T4')
    def compound(self, p):
        print("Compound: Chathurthi Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.t4(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN T5')
    def compound(self, p):
        print("Compound: Panchami Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.t5(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada


    @_('LPAREN component HIPHEN component RPAREN T6')
    def compound(self, p):
        print("Compound: Shashti Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.t6(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN T7')
    def compound(self, p):
        print("Compound: Sapthami Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.t7(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TN')
    def compound(self, p):
        print("Compound: Nanj Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.tn(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TDS')
    def compound(self, p):
        print("Compound: Samahara Dwigu")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.tds(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TDT')
    def compound(self, p):
        print("Compound: Taddhitartha Dwigu")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.tdt(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TDU')
    def compound(self, p):
        print("Compound: Uttarapada Dwigu")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.tdu(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TG')
    def compound(self, p):
        print("Compound: Gati Samasa")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.tg(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TK')
    def compound(self, p):
        print("Compound: KuSamasa")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.tk(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TP')
    def compound(self, p):
        print("Compound: Praadi Samasa")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.tk(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TM')
    def compound(self, p):
        print("Compound: Mayoora Vyamsakadi Samasa")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.tk(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TB')
    def compound(self, p):
        print("Compound: Bahupada Samasa")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.tb(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K1')
    def compound(self, p):
        print("Compound: Visheshana Poorvapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.k1(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K2')
    def compound(self, p):
        print("Compound: Visheshana Uttarapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.k2(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K3')
    def compound(self, p):
        print("Compound: Visheshana Ubhayapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.k3(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K4')
    def compound(self, p):
        print("Compound: Upamana Poorvapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.k4(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K5')
    def compound(self, p):
        print("Compound: Upamana Uttarapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.k5(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K6')
    def compound(self, p):
        print("Compound: Avadharana Poorvapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.k6(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K7')
    def compound(self, p):
        print("Compound: Sambhavana Poorvapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.k7(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN KM')
    def compound(self, p):
        print("Compound: Madhyamapada Lopi Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.km(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada        

    @_('LPAREN component HIPHEN component RPAREN BS2')
    def compound(self, p):
        print("Compound: DvitIyArtha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bs2(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada  

    @_('LPAREN component HIPHEN component RPAREN BS3')
    def compound(self, p):
        print("Compound: TritIyArtha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bs3(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada  

    @_('LPAREN component HIPHEN component RPAREN BS4')
    def compound(self, p):
        print("Compound: Chaturthyartha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bs4(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BS5')
    def compound(self, p):
        print("Compound: Panchamyartha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bs5(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BS6')
    def compound(self, p):
        print("Compound: Shashtyartha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bs6(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada         

    @_('LPAREN component HIPHEN component RPAREN BS7')
    def compound(self, p):
        print("Compound: Sapthamyartha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bs7(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BSD')
    def compound(self, p):
        print("Compound: Digvachaka BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bsd(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BSP')
    def compound(self, p):
        print("Compound: Praharana Vishayaka BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bsp(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BSG')
    def compound(self, p):
        print("Compound: Grahana Vishayaka BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bsp(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BSMN')
    def compound(self, p):
        print("Compound: Asthyartha Madhyamapada Lopi BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bsmn(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BVP')
    def compound(self, p):
        print("Compound: Pradi BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bvp(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BSS')
    def compound(self, p):
        print("Compound: Sankhyobhaya Pada BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bss(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BSU')
    def compound(self, p):
        print("Compound: Upamana PoorvaPada BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bsu(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BV')
    def compound(self, p):
        print("Compound: Vyadhikarana BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bv(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BVS')
    def compound(self, p):
        print("Compound: Sankhottarapada Vyadhikarana BahuvrIhi")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bvs(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BVSC')
    def compound(self, p):
        print("Compound: Sahaoorvapada Vyadhikarana BahuvrIhi")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bvs_Caps(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BVU')
    def compound(self, p):
        print("Compound: Upamanapoorvapada Vyadhikarana BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bvu(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BB')
    def compound(self, p):
        print("Compound: Bahupada BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.bb(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN DI')
    def compound(self, p):
        print("Compound: Itertara Dvandhva")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.di(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN DS')
    def compound(self, p):
        print("Compound: Samahara Dvandhva")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.ds(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TAG')
    def compound(self, p):
        if (p.TAG == "E"):
            samasthaPada = self.compound_E(p)
        elif (p.TAG == "U"):
            samasthaPada = self.compound_U(p)
        elif (p.TAG == "S"):
            samasthaPada = self.compound_S(p)
        elif (p.TAG == "K"):
            samasthaPada = self.compound_K(p) 
        elif (p.TAG == "d"):
            samasthaPada = self.compound_d(p) 
        else:                      
            samasthaPada = "Unmatched Tag:" + p.TAG + "(" + p.component0 + "," + p.component1 + ")"
        return samasthaPada

    @_('compound PLUS word')
    def compoundgroup(self, p):
        samasthaPada = p.compound + "+" + p.word
        print("Compound: Compound and Word (Sandhi):" + samasthaPada)        
        return  samasthaPada

    @_('word PLUS word')
    def compoundgroup(self, p):
        samasthaPada = p.word0 + "+" + p.word1
        print("Compound: Wordgroup (Sandhi):" + samasthaPada)        
        return  samasthaPada

    @_('word HIPHEN word')
    def compoundgroup(self, p):
        samasthaPada = p.word0 + "-" + p.word1
        print("Compound: Wordgroup(Samasa, Missing Tag)" + samasthaPada)        
        return  samasthaPada

    @_('sentence word')
    def compoundgroup(self, p):
        samasthaPada = p.sentence + " " + p.word
        print("Compound: Wordgroup(Samasa, Word)" + samasthaPada)        
        return  samasthaPada

    @_('compoundgroup PLUS word')
    def compoundgroup(self, p):
        samasthaPada = p.compoundgroup + "+" + p.word
        print("Compound: Wordgroup (Sandhi):" + samasthaPada)        
        return  samasthaPada

    @_('word word')
    def compoundgroup(self, p):
        samasthaPada = p.word0 + "-" + p.word1
        print("Compound: Wordgroup(Words)" + samasthaPada)        
        return  samasthaPada

    @_('word')
    def component(self, p):
        #print("Word as component:" + p.word)
        return p.word

    @_('compound')
    def component(self, p):
        #print("Compound as component:" + p.compound)
        return p.compound

    @_('WORD')
    def word(self, p):
        #print("Got a word " + p.WORD)        
        return p.WORD
 
    @_('DANDA DANDA NUMBER DANDA DANDA')
    def shlokaend(self, p):
        #print("Got a word " + p.WORD)        
        return '||' + p.NUMBER + '||'


    def compound_E(self, p):
        print("Compound: Ekakosha Dvandhva")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.E(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada        

    def compound_S(self, p):
        print("Compound: Kevala Dvandhva")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.S(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada  

    def compound_U(self, p):
        print("Compound: Upapada Samasa")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.U(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    def compound_d(self, p):
        print("Compound: Dvirukthi Dvandhva")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.d(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    def compound_K(self, p):
        print("Compound: Upapada Samasa")
        print("Poorvapada:" + p.component0)
        print("Uttarapada:" + p.component1)
        samasthaPada = self.sg.K(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada        
'''

    @_('ANYCHARACTER')
    def compoundgroup(self, p):
        return p.ANYCHARACTER 

    @_('compound ANYCHARACTER')
    def compoundgroup(self, p):
        return p.compound + " " + p.ANYCHARACTER

    @_('compound compound')
    def compoundgroup(self, p):
        return p.compound0 + " " + p.compound1


'''

class compound_analyzer:
    def analyze(self,text):
        outStr = self.parser.parse(self.lexer.tokenize(text))
        return outStr
    def __init__(self):
        self.lexer = SamasaLexer()
        self.parser = SamasaParser()    




if __name__ == '__main__':
    print("\nWelcome to samasa tag analyzer.\n") 
    print("Author: Harsha M.\n\n") 
    ca = compound_analyzer()
    while True:
        try:
            input_text = input('samasa_tagged > ')
            translated_text = d_to_v(input_text)
        except EOFError:
            break
        if translated_text:
            outStr = ca.analyze(translated_text)
            print("outStr=" + v_to_d(outStr))

