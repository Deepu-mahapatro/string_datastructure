#ISOMORPHIC STRING
#ISOMORPHIC MEANS 
#SAME STRUCTURE
#SAME REPETITION PATTERN
#CONSISTENT PATTERN 
#EX: FOR "EGG" AND "ADD"
#E->A,G->D,G->D HENCE CONSISTENT MAINTAINED 
#BECAUSE G->D AND G->D MAPPING IS CORRECT
#EX: FOR "FOO" AND "BAR" 
#F->B,O->A,O->R HENCE NO CONSISTENT
#BECAUSE O->R AND O->A DOES NOT MAP EACH OTHER
#WHICH MAPS CORRECTLY CALLED ISOMORPHIC STRING

#USING TWO DICTIONARIES
def isomorphic(s,t):
    if len(s)!=len(t):
        return False
    map_st={}
    map_ts={}
    for i in range(len(s)):
        ch1=s[i]
        ch2=t[i]
        if ch1 in map_st:
            if map_st[ch1]!=ch2:
                return False
        else:
            map_st[ch1]=ch2
        if ch2 in map_ts:
            if map_ts[ch2]!=ch1:
                return False
        else:
            map_ts[ch2]=ch1
    return True
print(isomorphic("egg","add"))
print(isomorphic("ag","foo"))

#USING PATTERN LIST METHOD
def pattern(word):
    mapping={}
    result=[]
    index=0
    for ch in word:
        if ch not in mapping:
            mapping[ch]=index
            index+=1
        result.append(mapping[ch])
    return result
def isomorphic(s,t):
    return pattern(s)==pattern(t)
print(isomorphic("egg","add"))
print(isomorphic("add","foo"))

#USING SETS METHOD
def isomorphic(s,t):
    if len(s)!=len(t):
        return False
    return (len(set(s))==len(set(t))==len(set(zip(s,t))))
print(isomorphic("add","egg"))
print(isomorphic("add","foo"))