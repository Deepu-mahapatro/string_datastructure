# TODAY IS ABOUT PREFIX AND SUFFIX CONCEPT 
#PREFIX STARTS AT FIRST INDEX 0 ENDING CHANGES
#SUFFIX STARTS AT END -1 STARTING CHANGES

#LONGEST COMMON PREFIX
def longest_pref(strings):
    #ASSUME PREFIX AT START INDEX[0]
    prefix=strings[0]
    #COMPARE REMAINING STRINGS
    for word in strings[1:]:
        i=0
        while (
            i<len(strings)
            and i<len(word)
            and prefix[i]==word[i]
        ):
            i+=1
        prefix=prefix[:i]
        if prefix ==" ":
            return " "
    return prefix
strings=["flower","flow","flight"]
result=longest_pref(strings)
print(result)


#LONGEST COMMON SUFFIX
def longest_sff(strings):
    #ASSUME PREFIX AT START INDEX[0]
    suffix=strings[0]
    #COMPARE REMAINING STRINGS
    for word in strings[1:]:
        i=1
        while (
            i<=len(suffix)
            and i<=len(word)
            and suffix[-i]==word[-i]
        ):
            i+=1
        suffix=suffix[len(suffix)-(i-1):]
        if suffix=="":
            return ""
    return suffix
strings=['walking',"talking","barking"]
result=longest_sff(strings)
print(result)    

