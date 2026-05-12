#TOKENIZATION CONCEPTS
#tokenization is a concept of breaking a text into smaller parts called tokens.

#using split() method
s='python is easy to learn'
result=s.split()
print(result)

#list comprehension method
#shorter way of creating list
nums=[1,2,3,4,5]
s=[x*x for x in nums]
print(s)

#combining split + list comprehension
a=['greek for greeks','is','best','resource']
result=[x.split() for x in a]
print(result)

#using resplit() method
import re
s=['greek for greeks','is','best','resource']
result=[re.split(r'\s+',x) for x in s]
print(result)

#using map() method 
nums =[1,2,3]
result=map(str,nums)
print(list(nums))

#suing map() + split() method
s=['greek for greeks','best','resource'] 
result=map(str.split,s)
print(list(result))

#frequency count + hashing method 
s='banana'
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

#using collection.counter method
from collections import Counter
a='banana'
result=Counter(a)
print(result)

#using dict.get() method 
s='banana'
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
print(freq)

## lexicographical order method using operators
s1='python'
s2='java'
result=s1<s2
result1=s1>s2
result3=s1==s2
print(result)
print(result1)
print(result3)

#using different case letters and methods
s='A'
h='a'
result=s<h
result1=s>h
print(result)
print(result1)

#using sorting method 
s=['a','A','B','c']
s.sort()
print(s)
print(max(s))
print(min(s))
words=input().split()
words.sort()
print(words)
