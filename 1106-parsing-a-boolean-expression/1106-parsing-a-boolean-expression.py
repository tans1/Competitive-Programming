class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operator = []
        openBracket = []
        boolean = []
        
        for i in range(len(expression)):
            if expression[i] in "&|!":
                operator.append(expression[i])
                
            elif expression[i] == "(":
                openBracket.append(len(boolean))
            
            elif expression[i] in 'ft':
                if expression[i] == 't':
                    boolean.append(True)
                else:
                    boolean.append(False)
                    
            elif expression[i] == ")":
                j = openBracket.pop()
                temp = boolean[j:]
                exp = operator.pop()
                
                if exp == "!":
                    for k in range(len(temp)):
                        temp[k] = not(temp[k])
                    
                    boolean = boolean[:j] + temp
                else:
                    if exp == "&":
                        temp2 = None
                        for x in temp:
                            if temp2 == None:
                                temp2 = x
                            else:
                                temp2 = temp2 and x
                            
                    elif exp == "|":
                        temp2 = None
                        for x in temp:
                            if temp2 == None:
                                temp2 = x
                            else:
                                temp2 = temp2 or x
                        
                    boolean = boolean[:j] + [temp2]

        return boolean[0]
