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
