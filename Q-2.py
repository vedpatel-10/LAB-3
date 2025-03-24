def to_upper_case(s):
    result = ""
    for i in s:
        if (ord(i)>=65 and ord(i)<=90):
            result = result + i
        elif ord(i)>=97 and ord(i)<=122:
            result = result + chr(ord(i) - 32)
        else:
            result = result +i    

    return result

s = "My name is Xyz"
print(to_upper_case(s))        
     
