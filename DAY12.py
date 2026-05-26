#REVERSE WORDS IN A STRING
#FIRST IDENTIFY THE STRING
#NOW SPLIT TEH STRINGS ACCORDING TO SPACES
#NOW REVERSE THE WORDS USING REVERSE KEYWORD
#NOW JOIN WITH ADDING THE SPACES BETWEEN THE WORDS
#FINALLY THE OUTPUT SHOULD TEH REVERSE OF INPUT

#USING REVERSE + SPLITTING METHOD
def reverse_split(s):
    word=s.split() 
    word=word[::-1]
    return ' '.join(word)
result=reverse_split("I LOVE PYTHON")
print(result)

#USING REVERSE() METHOD
def reverse_split(s):
    word=s.split()
    word.reverse()
    return ' '.join(word)
result=reverse_split("I LOVE PYTHON")
print(result)

#USING LOOP FORM BACKWARD
def reverse_split(s):
    words=s.split()
    result=[]
    n=len(words)
    for i in range(n-1,-1,-1):
        result.append(words[i])
    return ' '.join(result)
print(reverse_split("I LOVE PYTHON"))

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



#LARGEST ODD NUMBER IN A STRING 
#TAKING THE DIGITS AS STRING LIKE S="12345"
#NOW CONTINUE TO CHECK WHETHER IT IS ODD OR EVEN BY LAST NUMBER
#IF LAST IS ODD TEH IT IS ODD NUMBER
#IF LAST IS EVEN THEN IT IS EVEN NUMBER
#INSTEAD OF CHECKING FORM FRONT TO AVOID DIGITS 
#WE CHECK FROM LAST AND REMOVE IT 
# IF LAST IS EVEN REMOVE UNTIL TEH ODD GET
#WHEN THE ODD GET THAT POINT IS THE LARGEST ODD SUBSTRING 

#BRUTE FORCE APPROACH
def largest_dig(s):
    largest=""
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            substring=s[i:j]
            if int(substring[-1])%2!=0:
                if int(substring)>int(largest or 0):
                    largest=substring
    return largest
s="126450"
print(largest_dig(s)) 

#SCAN FORM LEFT
def largest_dig(s):
    largest=""
    n=len(s)
    for i in range(n):
        if int(s[i])%2!=0:
            largest=s[:i+1]
    return largest
s="3456270"
print(largest_dig(s))

#SCAN FORM RIGHT
def largest_dig(s):
    n=len(s)
    for i in range(n-1,-1,-1):
        if int(s[i])%2!=0:
            return s[:i+1]
    return ""
s="345250"
print(largest_dig(s))