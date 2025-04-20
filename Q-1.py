input = input("Enter a string: ")
count = 0

for i in input:
    if i == 'a' or i == 'e' or i == 'i' or i =='o' or i =='u':
        count = count + 1

print("Total vowels in the given string are: " + str(count))     

#OUTPUT:
# Enter a string: my name is ved patel
# Total vowels in the given string are: 6
