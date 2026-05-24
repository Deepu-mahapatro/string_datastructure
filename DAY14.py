#STRING TO INTEGER(ATOI)
#EXTRACT A VALID INTEGER CAREFULLY FROM A MESSY STRING
#BY FOLLOWING THE CONDITIONS
#IGNORE LEADING SPACES
#ONLY ONE SIGN ALLOWED
#READING TEH DIGITS IN A CONTINUES MANNER
#STOPS AT INVALID CHARACTER
#HANDLE THE OVERFLOW
#RETURN FINAL INTEGER

#USING NORMAL METHOD
def myAtoi(s):
    i=0
    n=len(s)
    #SKIP LEADING SPACES
    while i<n and s[i]==" ":
        i+=1
    #EDGE CASE: EMPTY STRING OR ONLY SPACES
    if i==n:
        return 0
    #HANDLE THE SIGN
    sign=1
    if s[i]=='-':
        sign=-1
        i+=1
    elif s[i]=='+':
        i+=1
    #READ DIGITS
    result=0
    while i<n and s[i].isdigit():
        digit=int(s[i])
        #CONTROL OVERFLOW
        if result>(2147483647 -digit)//10:
            if sign==1:
                return 2147483647
            else:
                return -2147483648
        result=result*10+digit
        i+=1
    #APPLY SIGN
    return sign*result
print(myAtoi("    123"))