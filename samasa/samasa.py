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
sys.path.append('../..')

from sly import Lexer, Parser

def d_to_v(input_string):
    scheme = detect.detect(input_string)
    print("input: " + input_string + " ---   encoding = " + str(scheme))
    if (str(scheme) == "Devanagari"):
      v_scheme_map = sanscript.SchemeMap(
                      sanscript.SCHEMES[sanscript.DEVANAGARI],
                      sanscript.SCHEMES[sanscript.VELTHUIS])
      output_string = sanscript.transliterate(input_string, scheme_map=v_scheme_map)
    else:
      output_string = input_string
      #print("please enter the input in devanagari")
    return output_string

def d_to_i(input_string):
    scheme = detect.detect(input_string)
    print("input: " + input_string + " ---   encoding = " + str(scheme))
    if (str(scheme) == "Devanagari"):
      v_scheme_map = sanscript.SchemeMap(
                      sanscript.SCHEMES[sanscript.DEVANAGARI],
                      sanscript.SCHEMES[sanscript.ITRANS])
      output_string = sanscript.transliterate(input_string, scheme_map=v_scheme_map)
    else:
      output_string = input_string
      #print("please enter the input in devanagari")
    return output_string    


def i_to_d(input_string):
    scheme = detect.detect(input_string)
    print("input: " + input_string + " ---   encoding = " + str(scheme))
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
      #print("please enter the input in devanagari")
    return output_string 

class SamasaGenerator():
    def a1(self,pp, up):
        sp =  "v6(" + up + ") f(" + pp + ")";
        return sp;  
    def a2(self,pp, up):
        sp =  "v3(" + pp + ") vipareetam vrittam";
        return sp; 
    def a3(self,pp, up):
        sp =  "v6(" + pp + ") v1(" + up + ") yasmin deshe";
        return sp;
    def a4(self,pp, up):
        sp =  "v6(" + pp + ") v6(" + up + ") samaharaha";
        return sp;
    def a5(self,pp, up):
        sp =  "v1(" + pp + ") v1(" + up + ") yasmin deshe";
        return sp;
    def a6(self,pp, up):
        sp =  "v6(" + pp + ") v6(" + up + ") samaharaha";
        return sp;
    def a7(self,pp, up):
        sp =  "v6(" + up + ") " + pp ;
        return sp;
    def t1(self,pp, up):
        sp =  "v1(" + pp + ") v6(" + up + ")";
        return sp;
    def t2(self,pp, up):
        sp =  "v2(" + pp + ") v1(" + up + ")";
        return sp;
    def t3(self,pp, up):
        sp =  "v3(" + pp + ") v1(" + up + ")";
        return sp;
    def t4(self,pp, up):
        sp =  "v4(" + pp + ") v1(" + up + ")";
        return sp;
    def t5(self,pp, up):
        sp =  "v5(" + pp + ") v1(" + up + ")";
        return sp;
    def t6(self,pp, up):
        sp =  "v6(" + i_to_d(pp) + ") v1(" + i_to_d(up) + ")";
        return sp;                                
    def t7(self,pp, up):
        sp =  "v7(" + pp + ") v1(" + up + ")";
        return sp; 
    def tn(self,pp, up):
        sp =  " न " + up;
        return sp; 
    def tds(self,pp, up):
        sp =  "v6(" + pp + ",ba) v1(" + up + ", ba) समाहारः";
        return sp; 
    def tdt(self,pp, up):
        sp =  "अष्ठसु v7(" + up + ", ba) संसृतः";
        return sp; 
    def tdu(self,pp, up):
        sp =  "tdu(" + pp + ", " + up + ")";
        return sp; 
    def tg(self,pp, up):
        sp =  "tg(" + pp + ", " + up + ")";
        return sp; 
    def tk(self,pp, up):
        sp =  "tk(" + pp + ", " + up + ")";
        return sp; 
    def tp(self,pp, up):
        sp =  "tp(" + pp + ", " + up + ")";
        return sp; 
    def tm(self,pp, up):
        sp =  "tm(" + pp + ", " + up + ")";
        return sp;
    def tb(self,pp, up):
        sp =  "tb(" + pp + ", " + up + ")";
        return sp;
    def U(self,pp, up):
        sp =  "U(" + pp + ", " + up + ")";
        return sp;
    def k1(self,pp, up):
        sp =  "k1(" + pp + ", " + up + ")";
        return sp;
    def k2(self,pp, up):
        sp =  "k2(" + pp + ", " + up + ")";
        return sp;
    def k3(self,pp, up):
        sp =  "k3(" + pp + ", " + up + ")";
        return sp;
    def k4(self,pp, up):
        sp =  "k4(" + pp + ", " + up + ")";
        return sp;
    def k5(self,pp, up):
        sp =  "k5(" + pp + ", " + up + ")";
        return sp;
    def k6(self,pp, up):
        sp =  "k6(" + pp + ", " + up + ")";
        return sp;
    def k7(self,pp, up):
        sp =  "k7(" + pp + ", " + up + ")";
        return sp;
    def km(self,pp, up):
        sp =  "km(" + pp + ", " + up + ")";
        return sp;
    def bs1(self,pp, up):
        sp =  "bs1(" + pp + ", " + up + ")";
        return sp;
    def bs2(self,pp, up):
        sp =  "bs2(" + pp + ", " + up + ")";
        return sp;
    def bs3(self,pp, up):
        sp =  "bs3(" + pp + ", " + up + ")";
        return sp;
    def bs4(self,pp, up):
        sp =  "bs4(" + pp + ", " + up + ")";
        return sp;
    def bs5(self,pp, up):
        sp =  "bs5(" + pp + ", " + up + ")";
        return sp;
    def bs6(self,pp, up):
        sp =  "bs6(" + pp + ", " + up + ")";
        return sp;
    def bs7(self,pp, up):
        sp =  "bs7(" + pp + ", " + up + ")";
        return sp;
    def bsd(self,pp, up):
        sp =  "bsd(" + pp + ", " + up + ")";
        return sp;
    def bsp(self,pp, up):
        sp =  "bsp(" + pp + ", " + up + ")";
        return sp;
    def bsg(self,pp, up):
        sp =  "bsg(" + pp + ", " + up + ")";
        return sp;
    def bsmn(self,pp, up):
        sp =  "bsmn(" + pp + ", " + up + ")";
        return sp;
    def bvp(self,pp, up):
        sp =  "bvp(" + pp + ", " + up + ")";
        return sp;
    def bss(self,pp, up):
        sp =  "bss(" + pp + ", " + up + ")";
        return sp;
    def bsu(self,pp, up):
        sp =  "bsu(" + pp + ", " + up + ")";
        return sp;
    def bv(self,pp, up):
        sp =  "bv(" + pp + ", " + up + ")";
        return sp;
    def bvs(self,pp, up):
        sp =  "bvs(" + pp + ", " + up + ")";
        return sp;
    def bvs_Caps(self,pp, up):
        sp =  "bvs_Caps(" + pp + ", " + up + ")";
        return sp;
    def bvu(self,pp, up):
        sp =  "bvu(" + pp + ", " + up + ")";
        return sp;
    def bb(self,pp, up):
        sp =  "bb(" + pp + ", " + up + ")";
        return sp;
    def di(self,pp, up):
        sp =  "di(" + pp + ", " + up + ")";
        return sp;
    def ds(self,pp, up):
        sp =  "ds(" + pp + ", " + up + ")";
        return sp;
    def E(self,pp, up):
        sp =  "E(" + pp + ", " + up + ")";
        return sp;
    def S(self,pp, up):
        sp =  "S(" + pp + ", " + up + ")";
        return sp;
    def d(self,pp, up):
        sp =  "d(" + pp + ", " + up + ")";
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
               WORD, HIPHEN, LPAREN, RPAREN, DANDA }
    ignore = ' \t'

    # Tokens

    HIPHEN   = r'-'
    LPAREN = r'<'
    RPAREN = r'>' 
    DANDA = r'\|'   
    TAG  = r'A[1-7]|Bs[2-7]|Bs[dgpsu]|Bsm[gn]|Bv[psSU]|B[bv]|D[is]|K[1-7]|Km|T[1-7]|T[bgmnpk]|Td[sut]'
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
    WORD = r'[a-zA-Z_]+'
    # Special symbols
    # Ignored pattern
    ignore_newline = r'\n+'

    literals = { '<', '>' }

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
        print("New Lquote" + str(self.nesting_level))
        return t

    @_(r'>')
    def rbrace(self, t):
        t.type = '>'      # Set token type to the expected literal
        self.lastTag = '>'
        self.nesting_level -=1
        print("End Lquote" + str(self.nesting_level))
        return t 
'''
    @_(r'E')
    def tag_E(self, t):
        if (self.lastTag == '>'):
            if (t.type == 'E'):
                print("Got " + t.type)        
                return t
        self.ESUTPrefix=t.value 
        self.lastTag = ''                
        return None

    @_(r'S')
    def tag_S(self, t):
        if (self.lastTag == '>'):
            if (t.type == 'S'):
                print("Got " + t.type)        
                return t
        self.ESUTPrefix=t.value 
        self.lastTag = ''                                
        return None

    @_(r'U')
    def tag_U(self, t):
        if (self.lastTag == '>'):
            if (t.type == 'U'):
                print("Got " + t.type)        
                return t   
        self.ESUTPrefix=t.value  
        self.lastTag = ''                    
        return None

    @_(r'd')
    def tag_d(self, t):
        print("11111111")
        if (self.lastTag == '>'):
            self.lastTag = '' 
            print("prefixed by >")
            if (t.type == 'd'):
                print("matched D token")                
                print("Got " + t.type)        
                return t
            else:
                print("not a D") 
        else:
            print("D not prefixed by >")                       
        self.ESUTPrefix=t.value
        print("Setting unused prefix and returning fail")                                  
        return None                

    @_(r'[a-zA-Z_]+')
    def any_word(self, t):
        if (self.ESUTPrefix != ''):
            print ("lex: prefixing " +  self.ESUTPrefix)
            new_t = t +  self.ESUTPrefix
            self.ESUTPrefix = ''
            return new_t
        else:
            return t; 
'''


class SamasaParser(Parser):
    tokens = SamasaLexer.tokens
    sg = SamasaGenerator();

    def __init__(self):
        self.compounds = { }



    @_('LPAREN component HIPHEN component RPAREN A1')
    def compound(self, p):
        print("New compond: Avyayi Bhava -> Avyaya Poorvapada")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.a1(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A2')
    def compound(self, p):
        print("New compond: Avyayi Bhava -> Avyaya Uttarapada")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.a2(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A3')
    def compound(self, p):
        print("New compond: Avyayi Bhava -> Tishtadgu Prabhrithi")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.a3(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A4')
    def compound(self, p):
        print("New compond: Avyayi Bhava -> Sankhya Poorvapada Nadyuttarapada")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.a4(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A5')
    def compound(self, p):
        print("New compond: Avyayi Bhava -> Nadyuttarapada, Anyapadarthe Samjnyaayaam")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.a5(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN A6')
    def compound(self, p):
        print("New compond: Avyayi Bhava -> Sankhya Poorvapada Vamshyotarapada")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.a6(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada        

    @_('LPAREN component HIPHEN component RPAREN A7')
    def compound(self, p):
        print("New compond: Avyayi Bhava -> Paare Madhye Poorvapada Shashtyuttarapada")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.a7(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN T1')
    def compound(self, p):
        print("New compond: Prathama Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.t1(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN T2')
    def compound(self, p):
        print("New compond: Dwiteeya Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.t2(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN T3')
    def compound(self, p):
        print("New compond: Triteeya Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.t3(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

                        
    @_('LPAREN component HIPHEN component RPAREN T4')
    def compound(self, p):
        print("New compond: Chathurthi Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.t4(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN T5')
    def compound(self, p):
        print("New compond: Panchami Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.t5(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada


    @_('LPAREN component HIPHEN component RPAREN T6')
    def compound(self, p):
        print("New compond: Shashti Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.t6(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN T7')
    def compound(self, p):
        print("New compond: Sapthami Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.t7(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TN')
    def compound(self, p):
        print("New compond: Nanj Tatpurusha")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.tn(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TDS')
    def compound(self, p):
        print("New compond: Samahara Dwigu")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.tds(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TDT')
    def compound(self, p):
        print("New compond: Taddhitartha Dwigu")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.tdt(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TDU')
    def compound(self, p):
        print("New compond: Uttarapada Dwigu")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.tdu(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TG')
    def compound(self, p):
        print("New compond: Gati Samasa")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.tg(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TK')
    def compound(self, p):
        print("New compond: KuSamasa")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.tk(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TP')
    def compound(self, p):
        print("New compond: Praadi Samasa")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.tk(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TM')
    def compound(self, p):
        print("New compond: Mayoora Vyamsakadi Samasa")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.tk(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TB')
    def compound(self, p):
        print("New compond: Bahupada Samasa")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.tb(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K1')
    def compound(self, p):
        print("New compond: Visheshana Poorvapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.k1(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K2')
    def compound(self, p):
        print("New compond: Visheshana Uttarapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.k2(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K3')
    def compound(self, p):
        print("New compond: Visheshana Ubhayapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.k3(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K4')
    def compound(self, p):
        print("New compond: Upamana Poorvapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.k4(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K5')
    def compound(self, p):
        print("New compond: Upamana Uttarapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.k5(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K6')
    def compound(self, p):
        print("New compond: Avadharana Poorvapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.k6(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN K7')
    def compound(self, p):
        print("New compond: Sambhavana Poorvapada Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.k7(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN KM')
    def compound(self, p):
        print("New compond: Madhyamapada Lopi Karmadharaya")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.km(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada        

    @_('LPAREN component HIPHEN component RPAREN BS2')
    def compound(self, p):
        print("New compond: DvitIyArtha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bs2(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada  

    @_('LPAREN component HIPHEN component RPAREN BS3')
    def compound(self, p):
        print("New compond: TritIyArtha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bs3(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada  

    @_('LPAREN component HIPHEN component RPAREN BS4')
    def compound(self, p):
        print("New compond: Chaturthyartha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bs4(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BS5')
    def compound(self, p):
        print("New compond: Panchamyartha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bs5(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BS6')
    def compound(self, p):
        print("New compond: Shashtyartha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bs6(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada         

    @_('LPAREN component HIPHEN component RPAREN BS7')
    def compound(self, p):
        print("New compond: Sapthamyartha BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bs7(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BSD')
    def compound(self, p):
        print("New compond: Digvachaka BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bsd(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BSP')
    def compound(self, p):
        print("New compond: Praharana Vishayaka BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bsp(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BSG')
    def compound(self, p):
        print("New compond: Grahana Vishayaka BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bsp(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BSMN')
    def compound(self, p):
        print("New compond: Asthyartha Madhyamapada Lopi BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bsmn(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada 

    @_('LPAREN component HIPHEN component RPAREN BVP')
    def compound(self, p):
        print("New compond: Pradi BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bvp(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BSS')
    def compound(self, p):
        print("New compond: Sankhyobhaya Pada BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bss(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BSU')
    def compound(self, p):
        print("New compond: Upamana PoorvaPada BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bsu(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BV')
    def compound(self, p):
        print("New compond: Vyadhikarana BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bv(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BVS')
    def compound(self, p):
        print("New compond: Sankhottarapada Vyadhikarana BahuvrIhi")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bvs(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BVSC')
    def compound(self, p):
        print("New compond: Sahaoorvapada Vyadhikarana BahuvrIhi")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bvs_Caps(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BVU')
    def compound(self, p):
        print("New compond: Upamanapoorvapada Vyadhikarana BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bvu(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN BB')
    def compound(self, p):
        print("New compond: Bahupada BahuvrIhi: Samanadhikarana")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.bb(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN DI')
    def compound(self, p):
        print("New compond: Itertara Dvandhva")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.di(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN DS')
    def compound(self, p):
        print("New compond: Samahara Dvandhva")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.ds(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN TAG')
    def compound(self, p):
        print("Unmatched Tag " + p.TAG)
        return ''

    @_('word')
    def component(self, p):
        print("Word as component:" + p.word)
        return p.word

    @_('compound')
    def component(self, p):
        print("Compound as component:" + p.compound)
        return p.compound

    @_('WORD')
    def word(self, p):
        print("Got a word " + p.WORD)        
        return p.WORD

    @_('component')
    def sentence(self, p):
        return p.component

    @_('component HIPHEN component')
    def sentence(self, p):
        return p.component0 + "-" + p.component1

    @_('compound component')
    def sentence(self, p):
        return p.compound + " " + p.component

    @_('sentence DANDA')
    def sentence(self, p):
        return p.sentence + "|" + p.DANDA        
'''
    @_('LPAREN component HIPHEN component RPAREN E')
    def compound(self, p):
        print("New compond: Ekakosha Dvandhva")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.E(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada        

    @_('LPAREN component HIPHEN component RPAREN S')
    def compound(self, p):
        print("New compond: Kevala Dvandhva")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.S(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada  

    @_('LPAREN component HIPHEN component RPAREN U')
    def compound(self, p):
        print("New compond: Upapada Samasa")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.U(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada

    @_('LPAREN component HIPHEN component RPAREN D')
    def compound(self, p):
        print("New compond: Dvirukthi Dvandhva")
        print("Poorvapada:" + p.component0)
        print("Poorvapada:" + p.component1)
        samasthaPada = self.sg.d(p.component0 , p.component1);
        print("Samasthapada:" + samasthaPada)
        return samasthaPada
'''

class compound_analyzer:
    def analyze(self,text):
        self.parser.parse(self.lexer.tokenize(text))

    def __init__(self):
        self.lexer = SamasaLexer()
        self.parser = SamasaParser()    





if __name__ == '__main__':
    ca = compound_analyzer()
    while True:
        try:
            input_text = input('samasa > ')
            translated_text = d_to_i(input_text)
            print(translated_text)
        except EOFError:
            break
        if translated_text:
            ca.analyze(translated_text)

