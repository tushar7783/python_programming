a="tushar"
if("T"in a or "t" in a):#in finds the string is in parent string
    print("yes",end=",") #end="," will not change the line only if we have another print statement
b=a.isalpha()#Return True if the string is an alphabetic string, False otherwise.
print(b)
c=a.capitalize()#Return a capitalized version of the string.
print(c)
d=a.upper()
print(d)
e="TULLU"
f=e.lower()#Return a copy of the string converted to lowercase.
print(f)
g=e*5#replication
print(g)
l=a+e#concatenation
print(l)
v="tushar,is,a,good,boy"
h=v.split(",")
print(h)
print(v[::-1])#reverse the entire string
p=v.replace("tushar","tullu")
print(p)




