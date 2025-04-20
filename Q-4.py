def str_remover_1(str1,str2):
    newstr = str2.replace(str1,"")
    return newstr

def str_remover_2(str2,str1):
    newstr = str1.replace(str2 , "")
    return newstr

str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")

if str1 in str2:
    print(str_remover_1(str1,str2))
elif str2 in str1 :
    print(str_remover_2(str2,str1))
else:
    print("There is no string which is present in another !")

#OUTPUT:
# Enter 1st string: Ved is studying in EE-DIV3
# Enter 2nd string: studying 
# Ved is  in EE-DIV3    
