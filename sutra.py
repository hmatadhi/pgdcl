import csv
import codecs
# include standard modules
import getopt, sys

def convert(s): 
    # initialization of string to "" 
    new = "".encode('utf-8') 
    # traverse in the string  
    for x in s: 
        new += x  
    # return string  
    return new 

def remove_zws(utf_str1):
    no_zws_str1 = []
    for i in range(0, len(utf_str1)-1):
        if ((utf_str1[i] == 0xe2) and (utf_str1[i+1] == 0x80) and (utf_str1[i+2] == 0x8C)):
            i = i + 3
        else:
            no_zws_str1.append(utf_str1[i])
    no_zws_str1.append(0xC0)
    no_zws_str1.append(0x80)
    return convert(no_zws_str1)

def print_unicode_array(hdr, utf_str1):
    print("unicode_str: " + hdr + "[" + utf_str1 + "]")
    my_list=[]
    for c in utf_str1:
        my_list.append(c)
    print("[" + str(my_list) + "]")    

def unicode_compare(utf_str1, utf_str2):
    print("unicode_compare: " + utf_str1 + " " + utf_str2)
    print(utf_str1)    
    for c in utf_str1:
        print(c)
    print(utf_str2)    
    for c in utf_str2:
        print(c)

    if (type(utf_str1) != type(utf_str2)):
        print("type mismatch: " + str(type(utf_str1)) + " " + str(type(utf_str2)))
        return False
    len1 = len(utf_str1)
    len2 = len(utf_str2)
    if (len1 != len2):
        print("len mismatch: " + str(len1) + " " + str(len2))
        return False
    for i in range(0, len1, 1):
        print("character mismatch @: " + str(i) + " " + utf_str1[i] + " " + utf_str2[i])
        if (utf_str1[i] != utf_str2[i]):
            return False
    return True

class psutra:
  def __init__(self, sindex, sks, stype, sterm, stext, spcheda):
    self.sindex = sindex  
    self.sks = sks
    self.stype = unicode(stype.replace('\xe2\x80\x8c', ''), "utf-8")
    self.sterm = unicode(sterm.replace('\xe2\x80\x8c', ''), "utf-8")
    self.stext = unicode(stext.replace('\xe2\x80\x8c', ''), "utf-8")
    self.spcheda = unicode(spcheda.replace('\xe2\x80\x8c', ''), "utf-8")
    #print_unicode_array("new word unicode:", self.sterm);
    #print_unicode_array("new word unicode replace zwx:", self.sterm.replace('\u200c', ''));
  def display(self):
      print(str(self.sindex) + " " + self.sks + " " + self.stype + " " + self.sterm + " " + self.stext)
  
class plist_db:
  def __init__(self, verbose):
      self.verbose = verbose
      self.plist = []
      self.plist2 = []
      self.read_file()
  def read_file(self):
    with open('sutra.csv', 'rb') as f:
        reader = csv.reader(f)
        sutras = list(reader)
    # getting length of list 
    no_of_sutras = len(sutras)
    if (self.verbose == 1): 
        print ("No of Sutras = " + str(no_of_sutras))
    for sutra_index in range(no_of_sutras): 
        if (sutra_index > 1):
            s = psutra(sutra_index, 
                   self.get_sks(sutras[sutra_index][0]),
                   sutras[sutra_index][3],
                   sutras[sutra_index][4],
                   sutras[sutra_index][5],
                   sutras[sutra_index][6],
                   )
            self.plist.append(s)
  def get_sks(self, num):
    adhyaya = str(num[0])
    patha   = str(num[1:2])
    sutra   = str(num[2:])
    return (adhyaya + "." + patha + "." + sutra)
  def compare_sutra_param(self, str1, str2):
    if ((str1 == str2) or (str2 == u"all".encode("utf-8"))):
        if (self.verbose == 1):
            print("check passed: in list=" + str1 + "\n given = " + str2)
        return True
    else:
        return False
  def compare_sutra_param2(self, str1, str2):
    if (unicode_compare(str1,str2) or (str2 == u"all".encode("utf-8"))):
        if (self.verbose == 1):
            print("check passed: in list=" + str1 + "\n given = " + str2)
        return True
    else:
        return False
  def search_sutra(self, name, stype):
    uni_name = unicode(name.replace('\xe2\x80\x8c', ''), "utf-8")  
    uni_stype = unicode(stype.replace('\xe2\x80\x8c', ''), "utf-8")  
    if (self.verbose == 1):  
        print("Search Request:\n Name=" + uni_name + "\n" + " Type=" + uni_stype)
    for s in self.plist:
        if (self.verbose == 1):
            print("check 1: " + s.sks + " in list=" + s.stype + "\n given = " + uni_stype)
            print("check 2: " + s.sks + " in list=" + s.sterm.encode('utf-8') + "\n given = " + uni_name.encode('utf-8'))
        if (self.compare_sutra_param(s.stype,uni_stype)):
            if (self.compare_sutra_param(s.sterm,uni_name)):
                s.display()

# read commandline arguments, first
unixOptions = "ht:n:v"
gnuOptions = ["help", "type=", "name=", "verbose"]        
fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]
try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)

# evaluate given options
stype = "all"
name = "all"
verbose = 0
helpasked = 0
for currentArgument, currentValue in arguments:
    if currentArgument in ("-v", "--verbose"):
        verbose = 1
    elif currentArgument in ("-h", "--help"):
        helpasked = 1
    elif currentArgument in ("-t", "--type"):
        stype = currentValue    
    elif currentArgument in ("-n", "--name"):
        name = currentValue    

if (helpasked):        
        print (unixOptions + "\n" + str(gnuOptions))
else:
    db = plist_db(verbose)
    db.search_sutra(name, stype)


        
