# TWO POINTER CONCEPT IN STRINGS
#USES TWO POINTERS TO COMPARE OR DO OPERATION
#REDUCING NESTED LOOPS AND IMPROVE EFFICIENCY

#USING OPPOSITE DIRECTION METHOD(PALINDROME)
def is_palindrome(s):
    char=list(s)
    left=0
    right=len(char)-1
    while left<right:
        if char[left]!=char[right]:
            return "not a palindrome"
        left+=1
        right-=1
    return "palindrome"
print(is_palindrome("MADM"))


#USING SAME DIRECTION(REMOVE DUPLICATES)
def remove_dup(s):
    if len(s)==0:
        return ""
    char=list(s)
    left=0
    for right in range(1,len(char)):
        if char[right]!=char[left]:
            left+=1
            char[left]=char[right]
    return "".join(char[:left+1])
print(remove_dup("aabbcc"))    


#SWAP OR REVERSE ONLY VOWELS
def reverse_vow(s):
    char=list(s)
    vowels="aeiouAEIOU"
    left=0
    right=len(s)-1
    while left<right:
        #move left until vowel found
        while left<right and char[left] not in vowels:
            left+=1
        #move right until vowel found
        while left<right and char[right] not in vowels:
            right-=1
        #now swap both left and right
        char[left],char[right]=char[right],char[left]
        left+=1
        right-=1
    return "".join(char)
print(reverse_vow("hello"))



#REVERSE A STRING 
def reverse_str(s):
    left=0
    right=len(s)-1
    char=list(s)
    while left<right:
        char[left],char[right]=char[right],char[left]
        left+=1
        right-=1
    return "".join(char)
print(reverse_str("reversed"))
            