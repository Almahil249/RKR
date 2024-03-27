import re
#AHmed alaa 20210885
#Ahmed sahal 20210921
def eliminate_implication(expression):
    ra = []
    if(re.search('\(\w+[|,]\w+\) -> \w+',expression) != None):
        print(1)
        imp = re.findall(r'\(\w+[|,]\w+\) -> \w+',expression)
        
        for w in imp:
            w = '~'+w
            ra.append(re.sub(r'->','|',w))
    elif(re.search('\w+ ->',expression) != None):
        imp = re.findall(r'\w+ -> \w+',expression)
        for w in imp:
            w = '~'+w
            ra.append(re.sub(r'->','|',w)) 
    elif(re.search('\(\w+[|,]\w+\) -> \(',expression) != None):
        imp = re.findall(r'\(\w+[|,]\w+\) -> \(\w+[|,]\w+\)',expression)
        for w in imp:
            w = '~'+w
            ra.append(re.sub(r'->','|',w)) 
    elif(re.search('\(\w+\([a-z]\)[|,]\w+\([a-z]\)\) -> ',expression) != None):
        imp = re.findall(r'\(\w+\([a-z]\)[|,]\w+\([a-z]\)\) -> \w+',expression)
        for w in imp:
            w = '~'+w
            ra.append(re.sub(r'->','|',w)) 
    elif(re.search('\w+\([a-z]\) ->',expression) != None):
        imp = re.findall(r'\w+\([a-z]\) -> \w+\([a-z]\)',expression)
        for w in imp:
            w = '~'+w
            ra.append(re.sub(r'->','|',w)) 
    elif(re.search('\(\w+\([a-z]\)[|,]\w+\([a-z]\)\) -> \(',expression) != None):
        imp = re.findall(r'\(\w+\([a-z]\)[|,]\w+\([a-z]\)\) -> \(\w+\([a-z]\)[|,]\w+\([a-z]\)\)',expression)
        print(imp)
        for w in imp:
            w = '~'+w
            ra.append(re.sub(r'->','|',w))
    newstr = ""
    for r in ra:
          newstr = newstr + r
    return(newstr) 
      
def move_negation_inward(expression):
    i = 0
    negation = []
    newex = re.split(r' [|,] ',expression)
    newexp = ""
    #print(newex)
    for i in newex:
         newexp = newexp + " "+ i
    print(newexp)
    if(re.search(r'\~\(\w+ \w+\)',newexp) != None):
            print(2)
            noL =  re.findall(r'\~\(\w+[,|]\w+',newexp)
            newexpression = ""
            for no in noL:
                if(re.search(r'\|',no) == None and re.search(r'FA [a-z]',no) == None):
                        newexpression = expression.replace((re.search(r'~\(\w+,\w+\)',expression)).group(),(re.split(r'~',re.sub(r',','|',no)+')')[1]))
                        return(newexpression)
                elif(re.search(r'\|',no) != None and re.search(r'FA [a-z]',no) == None):
                        newexpression = expression.replace((re.search(r'~\(\w+\|\w+\)',expression)).group(),(re.split(r'~',re.sub(r'\|',',',no)+')')[1]))
                        return(newexpression)
                    #negation.append(re.sub(r'\|',',',negation[0]))
                    #negation.append(re.sub(r'FAX','TEX',negation[0]))
                    #negation.append(re.sub(r'TEX','FAX',negation[1]))
            print(newexpression)
    elif(re.search(r'\~\(\w+\([a-z]\)[,|]\w+\([a-z]\)\)',expression) != None):
        noL =  re.findall(r'\~\(\w+\([a-z]\)[,|]\w+\([a-z]\)\)',newexp)
        newexpression = ""
        for no in noL:
            if(re.search(r'\|',no) == None):
                        expression =  expression.replace((re.search(r'~\(\w\([a-z]\)+,\w\([a-z]\)+\)',expression)).group(),(re.split(r'~',re.sub(r',','|',no)+')')[1]))
                        Lop = re.findall(r'\w+\([a-z]\)',expression)
                        for L in Lop:
                            newexpression = expression.replace(re.search(L[0]+r'\([a-z]\)',expression).group(),'~'+L[0]+re.search(r'\([a-z]\)',expression).group())
                        return(newexpression)
            elif(re.search(r'\|',no) != None ):
                        newexpression = expression.replace((re.search(r'~\(\w+\([a-z]\)\|\w+\([a-z]\)\)',expression)).group(),(re.split(r'~',re.sub(r'\|',',',no)+')')[1]))
                        return(newexpression)
    elif(re.search(r'~FA [a-z]\(\w+\([a-z]\)[,|]\w+\([a-z]\)\)',expression) != None):
            noL =  re.findall(r'~FA [a-z]\(\w+\([a-z]\)[,|]\w+\([a-z]\)\)',newexp)
            print(noL)
            newexpression = ""
            for no in noL:
                    if(re.search(r'\|',no) == None and re.search(r'FA [a-z]',no) != None):
                                expression =  expression.replace((re.search(r'~FA [a-z]\(\w\([a-z]\)+,\w\([a-z]\)+\)',expression)).group(),(re.split(r'~',re.sub(r',','|',no)+')')[1]))
                                newexpression = re.sub('FA','TE',expression)
                                return(newexpression)
                    elif(re.search(r'\|',no) != None and re.search(r'FA [a-z]',no) != None):
                                expression = expression.replace((re.search(r'~FA [a-z]\(\w+\([a-z]\)\|\w+\([a-z]\)\)',expression)).group(),(re.split(r'~',re.sub(r'\|',',',no)+')')[1]))
                                newexpression = re.sub('FA','TE',expression)
                                return(newexpression)
    elif(re.search(r'~TE [a-z]\(\w+\([a-z]\)[,|]\w+\([a-z]\)\)',expression) == None):
            noL =  re.findall(r'~FA [a-z]\(\w+\([a-z]\)[,|]\w+\([a-z]\)\)',newexp)
            newexpression = ""
            for no in noL:
                    if(re.search(r'\|',no) == None and re.search(r'FA [a-z]',no) != None):
                                expression =  expression.replace((re.search(r'~TE [a-z]\(\w\([a-z]\)+,\w\([a-z]\)+\)',expression)).group(),(re.split(r'~',re.sub(r',','|',no)+')')[1]))
                                newexpression = re.sub('TE','FA',expression)
                                return(newexpression)
                    elif(re.search(r'\|',no) != None and re.search(r'FA [a-z]',no) == None):
                                expression = expression.replace((re.search(r'~TE [a-z]\(\w+\([a-z]\)\|\w+\([a-z]\)\)',expression)).group(),(re.split(r'~',re.sub(r'\|',',',no)+')')[1]))
                                newexpression = re.sub('TE','FA',expression)
                                return(newexpression)


        
         

def remove_double_not(expression):
    return re.split(r'~~',expression)[1]
def standardize_variable_scope(expression):
    ListOfletters = []
    newlist = []
    newX = ['x0','x1','x2','x3','x4','x5']
    i = 0
    Qf = re.search(r' [|,] ',expression).group()
    splited = re.split(r' [|,] ',expression)
    print(splited)
    for str in splited:
        dop =  re.search(r'(TE [a-z]\(\w+\([a-z]\)[|,->]\w+\([a-z]\)\)|FA [a-z]\(\w+\([a-z]\)[|,->]\w+\([a-z]\)\))',str).group()
        if(dop[3] in ListOfletters):
            newlist.append(dop.replace(dop[3],newX[i]))
            i =+1
        else:
            newlist.append(dop)
            ListOfletters.append(dop[3])
    newstr = ""
    count = 0
    for i in newlist:
          
          if (count == len(newlist)-1):
                newstr = newstr + i
          else:
                newstr = newstr + i + Qf
          count =+1
    return newstr
    pass

def skolemization(expression):
            print(type(expression))
            ListOfletters = []
            newlist = []
            newX = ['A','B','C','D','E']
            i = 0
            splited = re.split(r' [|,]',expression)
            print(splited)
            for str in splited:
                dop =  re.search(r'(TE [a-z]\(\w+\([a-z]\)[|,->]\w+\([a-z]\)\))',str)
                if(dop != None):
                    dop = dop.group()
                    newdop = dop.replace(dop[3],newX[i])
                    expression = expression.replace(re.search(r'(TE [a-z]\(\w+\([a-z]\)[|,->]\w+\([a-z]\)\))',str).group(),newdop)
                    expression = expression.replace(r"TE","")
                    expression = expression.replace(newX[i],"",2)
                    i =+1
    
            return expression
def move_quantifiers_left(expression):
    LQ = ""
    nop = re.findall('FA [a-z]\(',expression)
    #print(nop)
    listofletters = []
    for i in nop:
         listofletters.append(i[3])
         pass
    #print(listofletters)
    newexp = expression.replace(re.search('FA [a-z]',expression).group(), "")
    for x in listofletters:
        LQ = 'FA ' + x +' ' + LQ
    newexp = LQ + newexp
    return newexp
def eliminate_universal_quantifiers(expression):
    newexp = expression.replace(re.search('FA [a-z]',expression).group(), "")
    return newexp
def distribution(expression):
    if(re.search(r'\w+\([a-z]\) \| \(',expression) != None):
         exp = re.findall(r'\w+\([a-z]\) \| \(\w+\([a-z]\),\w+\([a-z]\)',expression)
         print(exp)
         for ex in exp:
            Twopart = re.split(r' \| ',ex)
            newexp = re.split(r',',Twopart[1])
            nop = '('+Twopart[0]+'|'+newexp[0]+') ,'+'( '+Twopart[0]+'|'+newexp[1]+')'
            return nop
    elif(re.search(r'\w+ \| \(',expression) != None):
        exp = re.findall(r'\w+ \| \(\w+,\w+\)',expression)
        print(exp)
        for ex in exp:
            Twopart = re.split(r' \| ',ex)
            newexp = re.split(r',',Twopart[1])
            nop = '('+Twopart[0]+'|'+newexp[0]+')) ,'+'('+Twopart[0]+'|'+'('+newexp[1]+')'
            return nop
    elif(re.search(r'\(\w+,\w+\) \| \(',expression) != None):
        exp = re.findall(r'\(\w+,\w+\) \| \(\w+,\w+\)',expression)
        print(exp)
        for ex in exp:
            Twopart = re.split(r' \| ',ex)
            Onepart = re.split(r',',Twopart[0])
            newexp = re.split(r',',Twopart[1])
            nop = '('+Onepart[0]+'|'+newexp[0]+')) ,'+'('+Onepart[0]+'|'+'('+newexp[1]+')'+', '+Onepart[1]+'|'+newexp[0]+')) ,'+'('+Onepart[1]+'|'+'('+newexp[1]+')'
            return nop
    elif(re.search(r'\(\w+\([a-z]\),\w+\([a-z]\)\) \| \(',expression) != None):
         exp = re.findall(r'\(\w+\([a-z]\),\w+\([a-z]\)\) \| \(\w+\([a-z]\),\w+\([a-z]\)',expression)
         print(exp)
         for ex in exp:
            Twopart = re.split(r' \| ',ex)
            Onepart = re.split(r',',Twopart[0])
            newexp = re.split(r',',Twopart[1])
            nop = '('+Onepart[0]+'|'+newexp[0]+') ,'+' ('+Onepart[0]+'|'+'('+newexp[1]+')'+', ('+Onepart[1]+'|'+newexp[0]+') ,'+' ('+Onepart[1]+'|'+'('+newexp[1]+')'
            return nop
    else:
          return expression
def clauses_from_conjunctions(expression):
    return re.split(',',expression)

#####form:FA x(p(x) -> a(x)) | TE x(p(x) -> a(X))
L = []
eliminate_implication('p(x) -> a(x)')
