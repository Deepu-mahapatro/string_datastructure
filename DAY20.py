#LONGEST COMMON PREFIX

#THE PURPOSE OF LONGEST COMMON PREFIX IS:
#TO FIND THE LONGEST STARTING PART (PREFIX) THAT IS COMMON IN ALL STRINGS.

#PROCESS:
#TAKE THE FIRST STRING AS REFERENCE.
#TRAVERSE CHARACTER BY CHARACTER FROM LEFT TO RIGHT.
#COMPARE THE CURRENT CHARACTER WITH THE SAME POSITION IN ALL OTHER STRINGS.
#IF ALL CHARACTERS MATCH:
    #CONTINUE TO NEXT POSITION.
#IF ANY CHARACTER MISMATCHES:
    #STOP IMMEDIATELY.
#RETURN THE PREFIX FOUND SO FAR.
#RESULT BECOMES THE LONGEST COMMON PREFIX.

#FORMULA:
    #LONGEST COMMON PREFIX =
    #ALL MATCHING CHARACTERS FROM INDEX 0
    #UNTIL THE FIRST MISMATCH.

#CONDITION:
    #EVERY STRING MUST HAVE THE SAME CHARACTER
    #AT THE CURRENT POSITION.

#IMPORTANT RULES:
    #PREFIX ALWAYS STARTS FROM INDEX 0.
    #COMPARISON IS DONE POSITION BY POSITION.
    #FIRST MISMATCH STOPS THE PROCESS.
    #ANYTHING AFTER A MISMATCH CANNOT BE PART OF THE PREFIX.
    #THE ANSWER CAN NEVER BE LONGER THAN THE SHORTEST STRING.

#IF NO COMMON PREFIX EXISTS:
    #RETURN ""

#WHY THIS WORKS:
    #A PREFIX MUST START FROM THE BEGINNING OF EVERY STRING.
    #THE FIRST DIFFERENT CHARACTER DEFINES THE MAXIMUM POSSIBLE PREFIX.
    #CHECKING EACH POSITION GUARANTEES THE CORRECT ANSWER.

#EDGE CASES:
    #EMPTY ARRAY -> RETURN ""
    #SINGLE STRING -> RETURN THE ENTIRE STRING
    #NO COMMON PREFIX -> RETURN ""
    #ALL STRINGS SAME -> RETURN THE ENTIRE STRING
    #ONE STRING EMPTY -> RETURN ""
    #SHORTEST STRING ENDS FIRST -> PREFIX CANNOT GROW FURTHER

#FINAL IDEA:
#COMPARE CHARACTERS FROM THE START OF ALL STRINGS.
#KEEP MOVING FORWARD WHILE ALL CHARACTERS MATCH.
#STOP AT THE FIRST MISMATCH.
#THE MATCHED PART BEFORE THE MISMATCH IS THE LONGEST COMMON PREFIX.

#BRUTE FORCE APPROACH
def longestCommonPrefix(s):
    #EDGE CASE: EMPTY STRING
    if not s:
        return ""
    prefix=""
    first=s[0]
    for i in range(len(first)):
        current_prefix=first[:i+1]
        for word in s:
            if not word.startswith(current_prefix):
                return prefix
        prefix=current_prefix
    return prefix
s=["flower","flight","flow"]
print(longestCommonPrefix(s))

#VERTICAL SCANNING
def longestCommonPrefix(s):
    #EDGE CASE:EMPTY STRING
    if not s:
        return ""
    first=s[0]
    for i in range(len(first)):
        char=first[i]
        for word in s[1:]:
            #EDGE CASE:
            if i>=len(word):
                return first[:i]
            if word[i]!=char:
                return first[:i]
    return first
s=["flower","flow","flight"]
print(longestCommonPrefix(s))

#HORIZONTAL SCANNING
def longestCommonPrefix(s):
    #EDGE CASE:EMPTY STRING
    if not s:
        return ""
    prefix=s[0]
    for word in s[1:]:
        while not word.startswith(prefix):
            prefix=prefix[:-1]
            #EDGE CASE:
            if prefix=="":
                return ""
    return prefix
s=["flower","flow","flight"]
print(longestCommonPrefix(s))

#BEST OPTIMAL METHOD
def longestCommonPrefix(s):
    #EDGE CASE: EMPTY STRING
    if not s:
        return ""
    first=s[0]
    for i in range(len(first)):
        for word in s[1:]:
            if i>=len(word) or word[i]!=first[i]:
                return first[:i]
    return first
s=["flower","flow","flight"]
print(longestCommonPrefix(s))


#CHECK TWO STRINGS ARE ANAGRAM OF EACH OTHER OR NOT

#THE PURPOSE OF ANAGRAM IS:
#TO CHECK WHETHER TWO STRINGS CONTAIN
#THE SAME CHARACTERS WITH THE SAME FREQUENCIES.

#PROCESS:
#FIRST CHECK LENGTH OF BOTH STRINGS.
#IF LENGTHS DIFFER:
    #RETURN FALSE.
#COUNT FREQUENCY OF EACH CHARACTER.
#COMPARE FREQUENCIES OF BOTH STRINGS.
#IF ALL FREQUENCIES MATCH:
    #RETURN TRUE.
#ELSE:
    #RETURN FALSE.

#CONDITION:
    #EVERY CHARACTER MUST APPEAR
    #THE SAME NUMBER OF TIMES IN BOTH STRINGS.

#IMPORTANT RULES:
    #ORDER DOES NOT MATTER.
    #FREQUENCY MATTERS.
    #SAME LENGTH DOES NOT GUARANTEE ANAGRAM.
    #ALL CHARACTER COUNTS MUST MATCH.

#IF NOT POSSIBLE:
    #RETURN FALSE.

#WHY THIS WORKS:
    #ANAGRAMS CONTAIN THE SAME LETTERS.
    #EQUAL FREQUENCIES GUARANTEE SAME LETTER DISTRIBUTION.
    #COMPARING COUNTS ENSURES CORRECTNESS.

#EDGE CASES:
    #DIFFERENT LENGTHS -> FALSE
    #BOTH EMPTY -> TRUE
    #ONE EMPTY -> FALSE
    #SAME STRING -> TRUE
    #REPEATED CHARACTERS -> CHECK COUNTS
    #DIFFERENT FREQUENCIES -> FALSE
    #CASE SENSITIVE CHARACTERS -> HANDLE CAREFULLY
    #SPACES/SPECIAL CHARACTERS -> DEPENDS ON PROBLEM

#FINAL IDEA:
#AN ANAGRAM IS NOT ABOUT ORDER.
#IT IS ABOUT HAVING EXACTLY THE SAME CHARACTERS
#WITH EXACTLY THE SAME FREQUENCIES.

#BRUTE FORCE METHOD
def is_anagram(s1,s2):
    #EDGE CASE 
    if len(s1)!=len(s2):
        return False
    s2=list(s2)
    for char in s1:
        if char in s2:
            s2.remove(char)
        else:
            return False
    return True
print(is_anagram("listen","silent"))

#SORTING APPROACH
def is_anagram(s1,s2):
    #EDGE CASE
    if len(s1)!=len(s2):
        return False
    return sorted(s1)==sorted(s2)
print(is_anagram("listen","silent"))

#HASHMAP/DICTIONARY APPROACH
def is_anagram(s1,s2):
    #EDGE CASE:
    if len(s1)!=len(s2):
        return False
    count1={}
    count2={}
    for ch in s1:
        count1[ch]=count1.get(ch,0)+1
    for ch in s2:
        count2[ch]=count2.get(ch,0)+1
    return count1==count2
print(is_anagram("listen","silent"))

#OPTIMAL METHOD
def is_anagram(s1,s2):
    #EDGE CASE
    if len(s1)!=len(s2):
        return False
    count={}
    #INCREASE COUNTS
    for ch in s1:
        count[ch]=count.get(ch,0)+1
    #DECREASE COUNTS
    for ch in s2:
        if ch not in count:
            return False
        count[ch]-=1
    #VERIFY ALL BECOMES ZERO
    for value in count.values():
        if value!=0:
            return False
    return True
print(is_anagram("silent","listen"))