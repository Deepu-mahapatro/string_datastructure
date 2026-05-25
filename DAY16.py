#MAXIMUM NESTING DEPTH OF PARENTHESIS
#PARENTHESIS ARE NESTED WHEN ONA PAIR COMES INSIDE THE ANOTHER PAIR
#EX: (()) HERE OUTER PAIR: () AND INNER PAIR:()
#HANCE THE DEPTH OF THIS BECOMES 2
#THE MAXIMUM NESTING DEPTH MEANS:
         #THE LARGEST NUMBER OF OPEN PARENTHESIS ACTIVE AT SAME TIME
#FOR EDGE CASES:
             #EMPTY STRING : "" MAX_DEPTH=0
             #FOR NO PARENTHESIS : A+B+C123 MAX_DEPTH=0
             #FOR SEQUENTIAL PARENTHESIS :()()() MAX_DEPTH=1
             #FOR INVALID CASE : )( MAX_DEPTH=-1
             #FOR A VALID PARENTHESIS DEPTH>=0
             #AND FINAL_DEPTH=0
#FINAL PROCESS:
# ( always increases nesting level
# ) always decreases nesting level
#Current depth represents active nested layers
#Maximum active layers = maximum nesting depth
#Valid strings never go below zero
#Valid strings end at zero depth
#CONCLUSION: MAX_DEPTH MEANS HIGHEST NUMBER
            # OF OPENING BRACKETS

#USING BRUTE FORCE METHOD:
def maxDepth(s):
    current_depth=0
    max_depth=0
    for i in s:
        #OPENING BRACKET
        if i=='(':
            current_depth+=1
            #UPDATE MAXIMUM
            if current_depth>max_depth:
                max_depth=current_depth
        #CLOSING BRACKET
        elif i==')':
            current_depth-=1
    return max_depth
print(maxDepth("(1+(2*3)+((8)/4))+1"))

#USING STACK METHOD
def maxDepth_stack(s):
    stack = []
    max_depth = 0
    for char in s:
        # Opening bracket
        if char == '(':
            stack.append(char)
            # Update maximum depth
            if len(stack) > max_depth:
                max_depth = len(stack)
        # Closing bracket
        elif char == ')':
            if stack:
                stack.pop()
    return max_depth
print(maxDepth_stack("(1+(2*3)+((8)/4))+1"))

#USING PYTHONIC SHORT METHOD
def maxDepth_pythonic(s):
    depth = 0
    maximum = 0
    for char in s:
        if char == '(':
            depth += 1
            maximum = max(maximum, depth)
        elif char == ')':
            depth -= 1
    return maximum
print(maxDepth_pythonic("(1+(2*3)+((8)/4))+1"))


            