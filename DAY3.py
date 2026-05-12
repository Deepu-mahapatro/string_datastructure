# ANAGRAM CONCEPT
# BOTH STRINGS CALLED ANAGRAM IF THEY CONTAIN SAME CHARACTERS 
#WITH SAME FREQUENCY COUNT BUT ORDER CNA BE DIFFERENT

#ANAGRAM USING FREQUENCY COUNT METHOD
s1=input("enter a string")
s2=input("enter a string")
freq1={}
freq2={}
for i in s1:
    freq1[i]=freq1.get(i,0)+1
for i in s2:
    freq2[i]=freq2.get(i,0)+1
if freq1==freq2:
    print("ANAGRAM")
else:
    print("NOT AN ANAGRAM")
    
    
#USING GROUP ANAGRAM
words=["eat","ate","tea","tan"]
groups={}
for i in words:
    key=''.join(sorted(i))
    if key not in groups:
        groups[key]=[]
    groups[key].append(i)
print(groups)


#USING CONDITION AS ALL TRUE
s1=input("enter a string")
s2=input("enter a string")
freq={}
for i in s1:
    freq[i]=freq.get(i,0)+1
print("after first string")
print(freq)
for i in s2:
    freq[i]=freq.get(i,0)-1
print("after second string")
print(freq)
result=all(value==0 for value in freq.values())
print(result)