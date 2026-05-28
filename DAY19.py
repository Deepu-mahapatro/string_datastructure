#COUNT NUMBER OF SUBSTRINGS 
#A SUBSTRING MEANS A CONTINUOUS PART OF A STRING
#CHOOSE A STARTING INDEX AND ENDING INDEX
#EVERY EXPANSION CREATES ONE SUBSTRING
#COUNT IT CONTINUE UNTIL END OF THE STRING
#MOVE THE STARTING INDEX FORWARD ANS REPEAT THE PROCESS
#STOP WHEN ALL STARTS ARE COMPLETED 
#EDGE CASE:
           #FOR EMPTY STRING NO SUBSTRINGS->0
           #FOR A SINGLE CHARACTER "A"-> SUBSTRING IS "A"
           #FOR SAME CHARACTERS "AAA"-> SUBSTRING 3 ("A","A","A")

#USING BRUTE FORCE METHOD
def count_sub(s):
    #EDGE CASE: EMPTY STRING
    if s=="":
        return ""
    #STORE TOTAL COUNT
    count=0
    #OUTER LOOP->START INDEX
    for start in range(len(s)):
        #INNER LOOP->ENDING INDEX
        for end in range(start,len(s)):
            count+=1
    return count
s="abcd"
print(count_sub(s))

#GENERATE ACTUAL SUBSTRING USING SLICING AND NESTED LOOPS
def count_sub(s):
    #EDGE CASE: EMPTY STRING
    if s=="":
        return ""
    #STORE ALL SUBSTRING
    sub_string=[]
    #CHOOSE START INDEX
    for start in range(len(s)):
        #CHOOSE END INDEX
        for end in range(start,len(s)):
            #CREATE SUBSTRING
            current=s[start:end+1]
            #STORE SUBSTRING
            sub_string.append(current)
    return len(sub_string)
s="abcd"
print(count_sub(s))

#USING MATHEMATICAL FORMULA
def count_sub(s):
    n=len(s)
    #APPLY FORMULA
    return (n*(n+1)//2)
s="abcd"
print(count_sub(s))

#USING RECURSION METHOD
def count_sub(s,start=0):
    #BASE CASE : IF START REACHES STRING END
    if start==len(s):
        return 0
    #SUBSTRINGS FROM CURRENT START
    current_count=len(s)-start
    #RECURSIVE COUNT SUBSTRING 
    return current_count+count_sub(s,start+1)
s="abcd"
print(count_sub(s))


#CONVERT ROMAN TO INTEGER
#HERE THE INPUT IS GIVEN AS "XIV"
#WE NEED TO CONVERT INTO INTEGER AS 15
#COMMON ROMAN NUMBERS ARE 
    #  I->1
    #  V->5
    #  X->10
    #  L->50
    #  C->100
    #  D->500
    #  M->1000
#START READING FROM LEFT SIDE
#ONE ROMAN AT A TIME AND CONVERT INTO VALUE
#NOW MOVE TO NEXT SYMBOL AND CHECK VALUE
#NOW COMPARE BOTH IF CURRENT VALUE IS SMALLER THAN NEXT VALUE
#THEN SUBTRACT IT OR LESE ADD NOW MOVE TO NEXT
#REPEAT THIS PROCESS UNTIL ALL SYMBOLS ARE FINISHED
#EDGE CASE:
        # FOR SINGLE CHARACTER -> JUST ADD 
        #LAST SYMBOL ALWAYS GET ADDED AS THERE IS NO EXISTS FOR COMPARISON
        ##EVERY NEXT SYMBOL IS SMALLER THEN ADD ALL

#USING LEFT TO RIGHT COMPARISON METHOD
def roman_to_integer(s):
    #EDGE CASE: EMPTY STRING
    if s=="":
        return 0
    #STORE ROMAN VALUES
    roman={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    #STORE FINAL ANSWER 
    total=0
    #TRAVERSE STRING
    for i in range(len(s)):
        #CURRENT VALUE
        current=roman[s[i]]
        #CHECK NEXT VALUE EXISTS
        if i+1<len(s):
            #NEXT VALUE
            next_value=roman[s[i+1]]
            #SUBTRACTION CASE
            if current<next_value:
                total-=current
            #ADDITION CASE
            else:
                total+=current
        else:
            #LAST CHARACTER ALWAYS ADDED
            total+=current
    return total
print(roman_to_integer("XIV"))

#USING RIGHT TO LEFT COMPARISON METHOD
def roman_to_integer(s):
    #EDGE CASE: EMPTY STRING
    if s=="":
        return 0
    #ROMAN VALUES
    roman={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    #STORE FINAL ANSWER
    total=0
    #STORE PREVIOUS VALUE
    prev=0
    #TRAVERSE RIGHT TO LEFT
    for char in reversed(s):
        #CURRENT VALUE
        current=roman[char]
        #SUBTRACTION CASE
        if current<prev:
            total-=current
        #ADDITION CASE
        else:
            total+=current
        #UPDATE PREVIOUS
        prev=current
    return total
print(roman_to_integer("XIV"))

#USING SIMPLE METHOD
def roman_to_integer(s):
    #EDGE CASE: EMPTY STRING
    if s=="":
        return 0
    #ROMAN VALUES
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    #EDGE CASE
    if not s:
        return 0
    #FINAL ANSWER
    total=0
    for i in range(len(s)-1):
        current=roman[s[i]]
        next_value=roman[s[i+1]]
        #ADD OR SUBTRACT
        if current<next_value:
            total-=current
        else:
            total+=current
    #ADD LAST CHARACTER ALWAYS ADD
    total+=roman[s[-1]]
    return total
print(roman_to_integer("XIV"))