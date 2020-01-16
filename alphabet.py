#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
virama='्';
implicita='अ';
barematras={
  'sk' : {'', 'ा', 'ि', 'ी', 'ु', 'ू',
          'ृ', 'ॄ', 'ॢ', 'ॣ',
          'े', 'ै',
          'ो', 'ौ'}
};
vowels = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ',
              'ऋ', 'ॠ', 'ऌ', 'ॡ',
              'ए', 'ऐ', 'ओ', 'औ'];
symbols = ['ं', 'ः', 'ऽ', '।', '॥',
               '०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];
noncons = len(vowels) + len(symbols)
print("vowels length=" + str(len(vowels)))
print("constant length=" + str(len(symbols)))

consonants = ['क', 'ख', 'ग', 'घ', 'ङ',
                  'च', 'छ', 'ज', 'झ', 'ञ',
                  'ट', 'ठ', 'ड', 'ढ', 'ण',
                  'त', 'थ', 'द', 'ध', 'न',
                  'प', 'फ', 'ब', 'भ', 'म',
                  'य', 'र', 'ल', 'व',
                  'श', 'ष', 'स', 'ह'];
varnamala = []
varnamala.extend(vowels)
varnamala.extend(symbols)
varnamala.extend(consonants)

alphabets = {

'sk': varnamala,

'hardkyoto':['a', 'A', 'i', 'I', 'u', 'U',
              'R', 'RR', 'lR', 'lRR',
              'e', 'ai', 'o', 'au',

              'M', 'H', '\'', '.', '..',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

              'k', 'kh', 'g', 'gh', 'G',
              'c', 'ch', 'j', 'jh', 'J',
              'T', 'Th', 'D', 'Dh', 'N',
              't', 'th', 'd', 'dh', 'n',
              'p', 'ph', 'b', 'bh', 'm',
              'y', 'r', 'l', 'v',
              'z', 'S', 's', 'h'],

'itrans':     ['a', ['aa','A'], 'i', ['ii','I'], 'u', ['uu','U'],
              ['RRi','R^i'], ['RRI','R^I'], ['LLi','L^i'], ['LLI','L^I'],
              'e', 'ai', 'o', 'au',

              'M', 'H', '\'', '|', '||',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

              'k', 'kh', 'g', 'gh', ['~N','N^'],
              'ch', 'Ch', 'j', 'jh', ['~n','JN'],
              'T', 'Th', 'D', 'Dh', 'N',
              't', 'th', 'd', 'dh', 'n',
              'p', 'ph', 'b', 'bh', 'm',
              'y', 'r', 'l', ['v','w'],
              'sh', 'Sh', 's', 'h'],

'velthius':   ['a', 'aa', 'i', 'ii', 'u', 'uu',
              '.r', '.rr', '.l', '.ll',
              'e', 'ai', 'o', 'au',

               '.m', '.h', '\'', '|', '||',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

              'k', 'kh', 'g', 'gh', '"n',
              'c', 'ch', 'j', 'jh', '~n',
              '.t', '.th', '.d', '.dh', '.n',
              't', 'th', 'd', 'dh', 'n',
              'p', 'ph', 'b', 'bh', 'm',
              'y', 'r', 'l', 'v',
               '"s', '.s', 's', 'h'],

'iast':          ['a', 'ā', 'i', 'ī', 'u', 'ū',
                'ṛ', 'ṝ', 'ḷ', 'ḹ',
                'e', 'ai', 'o', 'au',

              'ṃ', 'ḥ', '\'', '|', '||',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

                'k', 'kh', 'g', 'gh', 'ṅ',
                'c', 'ch', 'j', 'jh', 'ñ',
                'ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ',
                't', 'th', 'd', 'dh', 'n',
                'p', 'ph', 'b', 'bh', 'm',
                'y', 'r', 'l', 'v',
                'ś', 'ṣ', 's', 'h'],

'IAST':          ['A', 'Ā', 'I', 'Ī', 'U', 'Ū',
                'Ṛ', 'Ṝ', 'Ḷ', 'Ḹ',
                'E', 'Ai', 'O', 'Au',

                  'Ṃ', 'Ḥ', '\'', '|', '||',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

                'K', 'Kh', 'G', 'Gh', 'Ṅ',
                'C', 'Ch', 'J', 'Jh', 'Ñ',
                'Ṭ', 'Ṭh', 'Ḍ', 'Ḍh', 'Ṇ',
                'T', 'Th', 'D', 'Dh', 'N',
                'P', 'Ph', 'B', 'Bh', 'M',
                'Y', 'R', 'L', 'V',
                'Ś', 'Ṣ', 'S', 'H'],

'kannada':       ['ಅ', 'ಆ', 'ಇ', 'ಈ', 'ಉ', 'ಊ',
                  'ಋ', 'ೠ', 'ಌ', 'ೡ',
                  'ಏ', 'ಐ', 'ಓ', 'ಔ',
                  'ಂ', 'ಃ',

                  'ಕ', 'ಖ', 'ಗ', 'ಘ', 'ಙ',
                  'ಚ', 'ಛ', 'ಜ', 'ಝ', 'ಞ',
                  'ಟ', 'ಠ', 'ಡ', 'ಢ', 'ಣ',
                  'ತ', 'ಥ', 'ದ', 'ಧ', 'ನ',
                  'ಪ', 'ಫ', 'ಬ', 'ಭ', 'ಮ',
                  'ಯ', 'ರ', 'ಲ', 'ವ',
                  'ಶ', 'ಷ', 'ಸ', 'ಹ'],

'ipa':           ['ɐ', 'ɑː', 'i', 'iː', 'u', 'uː',
                  'ɻ', 'ɻː', 'ɭ', 'ɭː',
                  'eː', 'əi', 'oː', 'əu',

                  '[anusa]', '[visarga]', '[elided a]', '', '',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

                  'k', 'kʰ', 'g', 'gʱ', 'ŋ',
                  #'c͡ç', 'c͡çʰ', 'ɟ͡ʝ', 'ɟ͡ʝʱ', 'ɲ',
                  'c', 'cʰ', 'ɟ', 'ɟʱ', 'ɲ',
                  'ʈ', 'ʈʰ', 'ɖ', 'ɖʱ', 'ɳ',
                  't̪', 't̪ʰ', 'd̪', 'd̪ʱ', 'n̪',
                  'p', 'pʰ', 'b', 'bʱ', 'm',

                  'j', 'r', 'l', 'ʋ',
                  'ɕ', 'ʂ', 's̪', 'ɦ']
};

transList = [itrans:'', harvardkyoto:'', velthius:'', IAST:'', iast:'', ipa:'']

def convert(s, trie):
    out = '';
    where = trie;
    d = 0;
    a = '';
    b = 0;
    i = 0;
    while (i < s.length):
        c = s[i];
        i = i + 1;
        d = d + 1;
        b = b + 1;
        if (where[c] != None): 
            where = where[c];
            if (where.label != None):
                a = where.label; b = 0;
        else:                  
            if (b==d):
                a = s[i-b];
                b = b - 1;
            out = out + a;
            i = i - b;
            where = trie;
            d = 0;
            a = '';
            b = 0;
    out += a+s.substr(i-b);
    return out;
        


def maketrie(table):
    root = [];
    for  s in table:
        where = root;
        for i in range(0, s.length):
            if (where[s[i]] == None):
                where[s[i]] = [];
            where = where[s[i]];
        where.label = table[s];
    return root;

def to_sk(alphabet): 
    ret = [];
    for i in alphabet: 
        rhs = alphabets['sk'][i] + (i>=noncons ? virama : '');
        if (type(alphabet[i]) == str):
            ret[alphabet[i]] = rhs;
        else:
            for c in alphabet[i]:
               ret[alphabet[i][c]] = rhs;
    return ret;
        

def from_sk(alphabet):
    ret = [];
    for i in alphabet:
        lhs = alphabets['sk'][i] + (i>=noncons ? virama : '');
        if (type(alphabet[i]) == str):
            ret[lhs] = alphabet[i];
        else:
            ret[lhs] = alphabet[i][0];
            
    return ret;


def make_trans(f):
    t = maketrie(to_sk(alphabets[f]));
    u = maketrie(from_sk(alphabets[f]));
    
def make_transList():
    for  f in transList:
        make_trans(f)

print(sys.argv[1]);
