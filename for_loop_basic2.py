def countdown(p_desde):    
    result=[]
    for i in range(p_desde,-1,-1):
        result.append(i)
    return result    

def PrintAndReturn(p_lista):
    print(p_lista[0])
    return(p_lista[1])

def FirstAndLen(p_lista):
    return(p_lista[0]+len(p_lista))

def gtSecond(p_lista):
    v_result=[]
    if len(p_lista)>3:
        for val in p_lista:
            if(val>p_lista[1]):
                v_result.append(val)
        print(len(v_result))
        return v_result
    else:
        return False

def ThisLonThatVal(p_size,p_val):
    v_result=[]
    for indice in range(0,p_size):
        v_result.append(p_val)
    return v_result
#print(countdown(2))

#print(PrintAndReturn([1,2]))

#print(FirstAndLen([1,2,3,4,5]))

#print(gtSecond([5,2,3,2,1,4]))

#print(gtSecond([5]))

#print(ThisLonThatVal(7,4))