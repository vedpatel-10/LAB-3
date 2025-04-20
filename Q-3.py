str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if str1 in str2:
    print("1st string is present in 2nd string")
elif str2 in str1:
    print("2nd string is present in 1st string")
else:
    print("None of the two string is present in other string")        

#OUTPUT:
# Enter first string: lion is the king of jungle
# Enter second string: lion is the king
# 2nd string is present in 1st string    
