#SUM OF BEAUTY OF ALL SUBSTRINGS
#FOR EVERY POSSIBLE SUBSTRING IN A STRING:
    #COUNT THE FREQUENCY OF EACH CHARACTER
    #FIND:
        #MAXIMUM FREQUENCY 
        #MINIMUM FREQUENCY(ONLY AMONG CHARACTERS THAT APPEARS)
<<<<<<< HEAD
    #B
    # BEAUTY OF SUBSTRING=
=======
    #BEAUTY OF SUBSTRING:
>>>>>>> 64edbf3a184d929fe4abd86df349748776955141
                         #MAX FREQUENCY-MIN FREQUENCY
#NOW ADD ALL THE BEAUTY VALUES OF ALL SUBSTRINGS 
#BEAUTY MEANS:HOW UNEVEN THE CHARACTER DISTRIBUTION IS INSIDE A SUBSTRING
#THIS TELLS HOW FAR THE SUBSTRING IS FORM BEING BALANCED
#IF ALL CHARACTERS APPEAR SAME NUMBER OF TIMES BEAUTY : 0
#IF ONE CHARACTER APPEARS MUCH MORE: BEAUTY BECOMES LARGER
#MAX FREQUENCY=HIGHEST OCCURRING CHARACTER COUNT
#MIN FREQUENCY=SMALLEST NON ZERO OCCURRING COUNT

#USING BRUTE FORCE APPROACH
def beautySum(s):
    n = len(s)
    total_beauty = 0
    # Generate all substrings
    for i in range(n):
        for j in range(i, n):
            # Frequency map for current substring
            freq = {}
            # Build substring frequency
            for k in range(i, j + 1):
                char = s[k]
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            # Find max and min frequency
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            # Add beauty
            total_beauty += (max_freq - min_freq)
    return total_beauty
print(beautySum("aba"))

#USING DICTIONARY METHOD
def beautySum(s):
    n = len(s)
    total_beauty = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            char = s[j]
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            total_beauty += (max_freq - min_freq)
    return total_beauty
print(beautySum("aba"))

#USING COUNTER METHOD
from collections import Counter
def beautySum(s):
    n = len(s)
    total_beauty = 0
    for i in range(n):
        current = ""
        for j in range(i, n):
            current += s[j]
            freq = Counter(current)
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            total_beauty += (max_freq - min_freq)
    return total_beauty
print(beautySum("aba"))
