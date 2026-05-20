#REMOVE OUTERMOST PARENTHESES

#FOR '(' FIRST IT IS OUTERMOST IT IS REMOVED AND DEPTH INCREASES BY 1
#FOR ')' FIRST IT IS OUTERMOST IT IS REMOVED AND DEPTH DECREASES BY 1
#FOR '('  IF DEPTH >0 THEN DEPTH INCREASES AND ADD TO RESULT
#FOR ')' DEPTH DECREASES THEN DEPTH >0  AND ADD TO RESULT

def remove_para(n):
    depth=0
    result=[]
    for i in n:
        if i=='(':
            if depth>0:
                result.append(i)
            depth+=1
        else:
            depth-=1
            if depth>0:
                result.append(i)
    return ''.join(result)
n="(()())(())"
print(remove_para(n))

#USING STACK METHOD 
def remove_para(n):
    stack=[]
    result=[]
    for i in n:
        #OPENING BRACKET
        if i=='(':
            if stack:
                result.append(i)
            stack.append(i)
    #CLOSING BRACKET
        else:
            stack.pop()
            if stack:
                result.append(i)
    return ''.join(result)
n="(()())(())"
print(remove_para(n))