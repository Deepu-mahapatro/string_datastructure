#lenght of string
s="pyton"
print(len(s))

#string traversal
s="python"
for i in s:
    print(i)
    
#string comaparision
s1="python"
s2="Python"
print(s1==s2)
print(s1!=s2)
print(s1<s2)
print(s1>s2)

#string concatenation
s1="python"
s2="programming"
print(s1+s2)

#swapcase method
s="python"
print(s.swapcase())

#case conversion
s="python"
print(s.upper())

s="PYTHON"
print(s.lower())

#string reverse
s="python"
print(s[::-1])

#slicing and substring
s="Python programming"
print(s[2:6:2])

#search for a substring
s="python programming"
print(s.find("pro"))
print('g' in s)

#insert a char in string
s="pthon"
s1=s[:1]+"y"+s[1:]
print(s1)

#delete char form a string
s="pthon"
s1=s[:1]+s[1:]
print(s1)

#rotate string
s="python"
s1=s[1:]+s[0]
print(s1)

s2=s[-1:]+s[:-1]
print(s2)
