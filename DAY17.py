#Split the string into individual words using spaces
#Traverse each separated word one by one
#Reverse the characters of every word independently
#Store all reversed words while keeping the original word order same
#Join all reversed words together using spaces and return the final string

#USING MANUAL REVERSE LOOP
def reverse_words(s):
    if s=="":
        return ""
    words=s.split()
    result=[]
    for word in words:
        reversed_words=""
        #REVERSE MANUALLY
        for i in range(len(word)-1,-1,-1):
            reversed_words+=word[i]
        result.append(reversed_words)
    return " ".join(result)
print(reverse_words("I LOVE CODING"))

#USING SPLIT AND REVERSE METHOD
def reverse_words(s):
    if s=="":
        return ""
    words=s.split()
    result=[]
    #REVERSE EACH WORD
    for word in words:
        result.append(word[::-1])
    #JOIN ALL THE WORDS
    return " ".join(result)
print(reverse_words("I LOVE CODING"))

#USING SLACK METHOD
def reverse_words(s):
    if s=="":
        return ""
    stack=[]
    result=""
    #TRAVERSE THE CHARACTERS
    for char in s:
        #IF NOT SPACE
        if char!=" ":
            stack .append(char)
        #SPACE FOUND 
        else:
            #POP ALL TEH CHARACTERS 
            while stack:
                result+=stack.pop()
            #ADD SPACE
            result+=" "
    while stack:
        result+=stack.pop()
    return result
print(reverse_words("I LOVE CODING"))

#LONGEST PALINDROME OF SUBSTRING
#HERE WE CHECK ALL THE POSSIBLE SUBSTRINGS 
#NOW FOR THAT SUBSTRINGS WITH IS PALINDROMES 
#FROM AMONG ALL THE PALINDROMES WHICH IS TEH LONGEST
#THAT SUBSTRING IS CALLED AS LONGEST PALINDROME
#EDGE CASES :
             #FOR INPUT ""-> OUTPUT ""
             #SINGLE CHARACTER-> IT IS A PALINDROME
             #FOR NO LARGER PALINDROME :
                     #SINGLE CHARACTER BECOME PALINDROME
                     #EX: "ABC"->PALINDROME MAY BE A OR B OR C
             #PALINDROMES MAY BE EVEN OR ODD CENTER
             
#USING MANUAL PROCESS
def is_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        #NOT A PALINDROME THEN
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
        return True
def longest_palindrome(s):
    #EDGE CASE:
    if s=="":
        return ""
    longest=""
    n=len(s)
    #GENERATE SUBSTRINGS
    for i in range(n):
        for j in range(i,n):
            substring=s[i:j+1]
            #CHECK PALINDROME
            if is_palindrome(substring):
                #UPDATE LONGEST
                if len(substring)>len(longest):
                    longest=substring
    return longest
print(longest_palindrome("babad"))

#EXPAND AROUND CENTER METHOD 
def expand(s,left,right):
    while left>=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1
    return s[left+1:right]
def longest_palindrome(s):
    #EDGE CASE:
    if s=="":
        return ""
    longest=""
    #CHECK EVERY CENTER
    for i in range(len(s)):
        #ODD LENGTH
        odd=expand(s,i,i)
        #EVEN LENGTH
        even=expand(s,i,i+1)
        #UPDATE LONGEST
        if len(odd)>len(longest):
            longest=odd
        if len(even)>len(longest):
            longest=even
    return longest
print(longest_palindrome("babad"))