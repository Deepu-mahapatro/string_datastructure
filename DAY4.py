#RABIN_KARP ALGORITHM
#USED TO FIND A PATTERN IN THE STRING
#IT USES HASHING SLIDING WINDOW ROLLING HASHING

#USING ALL METHODS 
def rabin_karp(text,pattern):
    n=len(text)
    m=len(pattern)
    pattern_hash=hash(pattern)
    for i in range(n-m+1):
        window=text[i:i+m]
        window_hash=hash(window)
        if pattern_hash==window_hash:
            if window==pattern:
                return i
text="ABCDEFGH"
pattern="DEF"
result=rabin_karp(text,pattern)
print(result)


#TO FIND A HASH FUNCTION
def hash_func(s):
    total=0
    for i in s:
        total+=ord(i)
    return total%10
s="ABCDE"
result=hash_func(s)
print(result)


#USING ROLLING HASHING
def calculate_hash(s):  #TO CALCULATE HASH FUNCTION
    total=0
    for i in s:
        total+=ord(i)
    return total
def rollin_hash(old_hash,old_char,new_char):  #ROLLING HASHING LOGIC
    old_hash=old_hash-ord(old_char)
    old_hash=old_hash+ord(new_char)
    return old_hash
def process_hash(text,window_size):  #FOR FIRST WINDOW
    window=text[:window_size]
    current_hash=calculate_hash(window)
    print(window,current_hash)
    for i in range(window_size,len(text)):
        current_hash=rollin_hash(current_hash,text[i-window_size],text[i])
        new_window=text[i-window_size+1:i+1]
        print(new_window,current_hash)
process_hash("ABCDEFG",3)