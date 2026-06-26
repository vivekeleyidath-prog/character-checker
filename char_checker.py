#1 # CHATGPT CODING CHALLENGE 
# Write a Python program that counts:
# *Total uppercase letters*
# *Total lowercase letters*
# ~~~~~~~~~~~~~~~~~~~~~~~CODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# s=input("enter the string:")  #   chatGPT RATE 9 OUT OF 10  ****    
# tup=td=tlw=sp=al=spc=0
# for ch in s:
#     if ch.isupper():
#         tup+=1
#     elif ch.islower():
#         tlw+=1
#     if ch.isalpha():
#         al+=1
#     elif ch.isdigit():
#         td+=1
#     elif ch.isspace():
#         sp+=1
#     else:
#         spc+=1
# print("TOTAL UPPER CASE LETTERS IN STRING:",tup)
# print("TOTAL LOWER CASE LETTERS IN STRING:",tlw)
# print("TOTAL            DIGITS  IN STRING:",td)
# print("TOTAL             SPACE  IN STRING:",sp)
# print("TOTAL SPECIAL CHARECTERS IN STRING:",spc)
# print("TOTAL         ALPHABETS  IN STRING:",al)
# =-------------------------------------------------------- END -----------------------------------------------
#2 # CHATGPT CODING CHALLENGE 
#Write a program to find the second largest number in a list without using
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
numbers = [-5, -2, -10]
largest=numbers[0]
sec_large=numbers[0]
if largest==sec_large and len(numbers)>1:
    sec_large=numbers[1]
for i in numbers:
    if i>largest:
        largest=i
for i in numbers:
    if i>sec_large and i<largest:
        sec_large=i
print(numbers)
print("THE LARGEST IN THIS LIST IS        :",largest)    
print("THE SECOND LARGEST IN THIS LIST IS :",sec_large)  
