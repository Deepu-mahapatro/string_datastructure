#SORT CHARACTERS BY FREQUENCY 
#REARRANGING THE CHARACTERS OF A STRING SO THA CHARACTERS APPEARING MORE TIMES COME FIRST
#EX : FOR "TREE" -> "EETR" OR "EERT" 
#THE CHARACTER E APPEARS TWICE SO IT COMES FIRST
#COUNT HOW MANY TIMES EACH CHARACTER APPEARS
#ARRANGE CHARACTERS FORM HIGHEST FREQUENCY TO LOWEST FREQUENCY
#REPEAT EACH CHARACTER BASED ON ITS COUNT
#EDGE CASES: EMPTY STRING : "" -> OUTPUT ""
            #SINGLE CHARACTER "A" -> OUTPUT "A"
            #SAME CHARACTERS "AAA" -> OUTPUT "AAA"
            #UNIQUE CHARACTERS ANY ORDER IT MAY HAVE
            #SAME FREQUENCIES ANY ORDER MAY HAVE
#HENCE THE LOGIC IS TO COUNT->SORT->REBUILD

#USING FREQUENCY COUNT METHOD
#THIS METHOD USED TO SORT TEH TUPLES
def get_frequency(item):
    return item[1]
def frequency_sort(s):
    #EDGE CASE:
    if s=="":
        return ""
    #COUNT FREQUENCIES
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
        #SORT THE FREQUENCIES
        sorted_chars=sorted(freq.items(),key=get_frequency,reverse=True)
        #REBUILD RESULT
        result=""
        for ch,count in sorted_chars:
            result+=ch*count
    return result
print(frequency_sort("tree"))

#USING BUCKET METHOD 
def frequency_sort(s):
    #EDGE CASE: EMPTY STRING
    if s=="":
        return ""
    #COUNT
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    #CREATE BUCKETS: CREATES EMPTY BUCKETS WITH LIST
    #TO STORE THE COUNT FOR ALL CHARACTERS
    #IT CREATES TOTAL LEN + 1 EMPTY LIST BUCKETS
    buckets=[[] for _ in range(len(s)+1)]
    #NOW FOR TUPLES EACH COUNT THE VALUE IS GONE TO THAT BUCKET
    #SAME COUNT THE VALUES GOES
    for ch, count in freq.items():
        buckets[count].append(ch)
    #REBUILD RESULT
    result=""
    #TRAVERSE FROM HIGH TO LOW
    for count in range(len(buckets)-1,0,-1):
        for ch in buckets[count]:
            result+=ch*count
    return result
print(frequency_sort("tree"))

#USING COUNTER METHOD
from collections import Counter
def frequency_sort(s):
    # EDGE CASE
    if s == "":
        return ""
    # STEP 1: COUNT
    freq = Counter(s)
    # STEP 2: SORT
    sorted_items = sorted(freq.items(),
                          key=lambda item: item[1],
                          reverse=True)
    # STEP 3: BUILD RESULT
    result = ""
    for ch, count in sorted_items:
        result += ch * count
    return result
print(frequency_sort("tree"))
    
    
