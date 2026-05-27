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
    
#ROTATE THE STRING
#A ROTATE STRING BEHAVE LIKE A CIRCULAR STRUCTURE
#AFTER THE LAST CHARACTER THE FIRST CHARACTER COMES AGAIN
#ROTATION DOES NOT REMOVE ANY CHARACTER AND DOES NOT ADD
#IT JUST CHANGE THE POSITION OF THE CHARACTER
#THERE ARE TWO TYPES OF ROTATION:
            #LEFT ROTATION: FRONT CHARACTERS MOVE TO END
            #RIGHT ROTATION: END CHARACTERS MOVE FRONT
#ROTATION MEANS SELECTING A DIFFERENT STARTING POINT IN THE SAME CIRCULAR SEQUENCE
#EDGE CASES: 
            # EMPTY STRING -> NO CHANGE
            #SINGLE CHARACTER -> NO CHANGE
            #SAME CHARACTERS -> UNCHANGED ROTATION
            #STRINGS WITH DIFFERENT LENGTHS CANNOT BE ROTATION

#USING SLICING METHOD(LEFT ROTATION)
def left_rotate(s,k):
    #EDGE CASE: EMPTY STRING
    if s=="":
        return ""
    #STRING LENGTH
    n=len(s)
    #EDGE CASE: HANDLE LARGE ROTATIONS
    k=k%n
    #EDGE CASE : ROTATION BY 0
    if k==0:
        return s
    #ROTATION PROCESS
    return s[k:]+s[:k]
print(left_rotate("abcde",2))

#USING SLICING METHOD(RIGHT ROTATION)
def right_rotate(s, k):
    #EDGE CASE 1: EMPTY STRING
    if s == "":
        return ""
    #STRING LENGTH
    n = len(s)
    #EDGE CASE 2: HANDLE LARGE ROTATIONS
    k = k % n
    #EDGE CASE 3: ROTATION BY 0
    if k == 0:
        return s
    #ROTATION
    return s[-k:] + s[:-k]
print(right_rotate("abcde", 2))

#USING REVERSAL METHOD
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
#LEFT ROTATION USING REVERSAL
def rotate_reversal(s, k):
    #EDGE CASE 1: EMPTY STRING
    if s == "":
        return ""
    arr = list(s)
    n = len(arr)
    #HANDLE LARGE ROTATIONS
    k = k % n
    #EDGE CASE 2: K = 0
    if k == 0:
        return s
    #STEP 1
    reverse(arr, 0, k - 1)
    #STEP 2
    reverse(arr, k, n - 1)
    #STEP 3
    reverse(arr, 0, n - 1)
    return "".join(arr)
#TEST
print(rotate_reversal("abcde", 2))

#USING LOOP METHOD CONCEPT(LEFT ROTATE)
def left_rotate_loop(s, k):
    #EDGE CASE 1: EMPTY STRING
    if s == "":
        return ""
    n = len(s)
    #HANDLE LARGE ROTATIONS
    k = k % n
    #CONVERT TO LIST
    s = list(s)
    #ROTATE ONE BY ONE
    for i in range(k):
        #STORE FIRST CHARACTER
        first = s[0]
        #SHIFT LEFT
        for j in range(n - 1):
            s[j] = s[j + 1]
        #PLACE FIRST AT END
        s[n - 1] = first
    return "".join(s)
#TEST
print(left_rotate_loop("abcde", 2))

#USING LOOP METHOD (RIGHT ROTATE)
def right_rotate_loop(s, k):
    #EDGE CASE 1: EMPTY STRING
    if s == "":
        return ""
    #STRING LENGTH
    n = len(s)
    #HANDLE LARGE ROTATIONS
    k = k % n
    #CONVERT STRING TO LIST
    s = list(s)
    #ROTATE ONE BY ONE
    for i in range(k):
        #STORE LAST CHARACTER
        last = s[n - 1]
        #SHIFT RIGHT
        for j in range(n - 1, 0, -1):
            s[j] = s[j - 1]
        #PLACE LAST CHARACTER AT FRONT
        s[0] = last
    #CONVERT BACK TO STRING
    return "".join(s)
#TEST
print(right_rotate_loop("abcde", 2))