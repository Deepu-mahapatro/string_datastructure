# SLIDING WINDOW CONCEPT 

#FIXED SIZE SLIDING WINDOW 
#MAXIMUM NUMBER OF VOWELS IN A SUBSTRING OF (COUNT)
s="abciiidef"
vowels="aeiou"
k=3
count=0
#FOR FIRST WINDOW
for i in range(k):
    if s[i] in vowels:
        count+=1
max_count=count
#FOR NEXT SLIDE WINDOWS
for i in range(k,len(s)):
    #REMOVE LEFT CHARACTER
    if s[i-k] in vowels:
        count-=1
    #ADD RIGHT CHARACTER
    if s[i] in vowels:
        count+=1
    max_count=max(max_count,count)
print(max_count)



#VARIABLE SIZE SLIDING WINDOW
#LONGEST SUBSTRING WITHOUT REPEATING 
s="abcabcbb"
result=set()
left=0
max_length=0
for right in range(len(s)):
    while s[right] in result:
        result.remove(s[left])
        left+=1
    result.add(s[right])
    current_length=right-left+1
    max_length=max(max_length,current_length)
    