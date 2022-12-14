#Input list
lst = [80, 121, 116, 104, 111, 110]
 
# Printing initial list
print ("Input list", lst)
 
# Using chr() Method
res = ""
for i in lst:
    res = res + chr(i)
 
print ("String : ", str(res))
