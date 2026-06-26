#1.concatination
#=====================================
# num=1
# letter="A"
# print(str(num)+letter)
# ------------------------------

#2.repetaion
# print("hi"*3)  # actully concatination happning here like hi+hi+hi

#-------------------------------------------------------------------

#3.SLICING
#==================================
text="pythonclass"
#print(text[:])
# print(text[:3]) #==>pyt 
# print(text[:5]) #==>python
# print(text[6:])   #==>class
#
# print(text[-1,-5,1]) #NO PRINTS



# print(dir(str))
# fuctions in string 
# ===========================================================================
#                           string functions                                ||
#                            ---------------                                || 
#'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',         ||
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',         ||
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',  ||
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',      ||
# 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',     ||
# 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',      ||
#  'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',        ||
#  'swapcase', 'title', 'translate', 'upper', 'zfill']                      ||
#============================================================================
# print("i LOVE python".capitalize())   #out =====> I love python

# print("i LOVE python".title())        #out =====> I love Python

# print("vivek".upper())                #out =====> VIVEK

# print("VIVEK".lower())                #out =====> vivek  #only applicable in Standers english
#print("i LOVE python".casefold())      #out =====> i love python  # applicable for all languages
#print("i LOVE python".find("p"))       #out =====> idex 7
# print("i LOVE python".find("x"))      #out =====> idex -1
# print("i LOVE python".index("x"))       #out =====> idex -1
#----------------------------------------------------------------------
# usage of count(),lower(),strip(),replace()
# s=input("enter a string:")
# c=input("what you want to count in this string:")
# s=s.strip()
# s=s.lower()
# print(f"this sentance has {s.count(c)}:{c} ")
# s=s.replace(c," ")
# print(s)
# #---------------------------------------------------------------------

#----zfill() function------------*
# a="100"                         #|
# b="200"                         #|
# c=int(a)+int(b)                 #|
# print(str(c).zfill(7))          #|
#--------------------------------*
#============================ ****FIND AN USER ENTERD WORD AND REPLACE WITH WHAT HE WANT WITH **** =====================*
#FIND AN USER ENTERD WORD AND REPLACE WITH WHAT HE WANT WITH                                                           #|
# def re_place(s,f,r):                                                                                                   #|
#     s=s.replace(f,r)                                                                                                   #|
#     return s                                                                                                           #|
# while True:                                                                                                             #|
#     s=input("enter the sentance:").lower()                                                                               #|
#     print(s.upper())                                                                                                       #|
#     f=input("enter what you want to replace:")                                                                             #|
#     r=input("with what:")                                                                                                  #|
#     print(re_place(s,f,r)) 
#     repeat=input("do you have any other words to replace:")
#     if repeat.lower()!="y" or "yes" or "ofcourese" or "yah":
#         break                                                                                                           #|
#========================================================= end end end end =============================================*
#zfill FUNCTION
#----------------
# number = "23"
# print(number.zfill(8)) # Output: -0000290
# number = "+290"
# print(number.zfill(8)) # Output: +0000290

#strip() FUNCTION
#--------------------------------------------==================================
# x="        vivek         "
# print(x.strip())    # =====>vivek
# print(x.lstrip())   # =====>vivek   right space exist left space remove
# print(x.rstrip())   # =====>vivek   lest space exist right side space remove
# ---------------------------------END --------------------------------------------

#      *swapcase()*
#--------------------------
# t="     vivek"
# print(t.title())
# print(t.lower())
# print(t.strip())
# t=t.replace("v","b")
# print(t)
# print(t.index("b"))
#_______________________________
#upper(),lower(),casefold(),title(),strip(),swapcase()
# t="     vivek"
# t=t.strip()
# print(t.title())
# print(t.lower())
# print(t.upper())
# print(t.casefold())
# print("vIvEk".swapcase()) #==> it swap the case, means it convert lower case to upper and upper to lower in the word
#out like: ViVeK

#isalpha(): #check charectors only
# name="vivek"
# print(name.isalpha()) # =====>true
# name="vivek123"
# print(name.isalpha()) # =====>False
# --------------------------------------------
#isdigit()
#************
# x="12"
# print(x.isdigit())      #======>true  
# x="12e"
# print(x.isdigit())      #======>false
# x="python"
# print(x.isdigit())      #======>false
# #----------------------------------------------

#isalnm()
#************
# name="vivek"
# print(name.isalnum()) # =====>true
# name="vivek123"
# print(name.isalnum()) # =====>true
# name="123445555"
# print(name.isalnum())   # =====>true

# x=3.14
# y=str(x)
# print(y.isdecimal())
# print(y.isdigit())
# print(y.isnumeric())

#count
# p="kannan"
# print(p.count("n"))    #====> 3
# print(p.count("a"))    #====> 2
# #------------------------------------
# #endswith
# p="kannan"
# print(p.endswith("n"))    #====> True
# print(p.endswith("k"))    #====> False
# #-------------------------------------

#x=["a","b","c"]
# print(" @ ".join(x))

# x=["a","b","c"]
# print(" ! ".join(x))


#split()
#----------------------------------
# p="i love.python"
# print(p.split())


# p="i.love.pyt.ho.n"
# p.replace("."," ")
# print(p.split())
  
x="18A65934"
# print(x.isdecimal())
# print(x.isdigit())
# print(x.isnumeric())
# print(x.count("1"))
# print(x.find("A"))
# x=x.replace("A","xxxxx")


