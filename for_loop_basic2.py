def biggie_size (p_lista):
    for v_indice in range(len(p_lista)):
        if(p_lista[v_indice]  >0):
            p_lista[v_indice]='BIG'
    return p_lista

def count_positives(p_lista):
    v_nPositivos=0
    for v_elementos in p_lista:
        if v_elementos>0:
            v_nPositivos+=1
    p_lista[len(p_lista)-1]=v_nPositivos
    return p_lista

def sum_total(p_lista):
    v_suma=0
    for v_elementos in p_lista:
        v_suma+=v_elementos
    return v_suma

def promedio(p_lista):    
    return sum_total(p_lista)/len(p_lista)

def longitud(p_lista):
    return len(p_lista)

def minimo(p_lista):
    if len(p_lista) > 0 :
        v_minimo=p_lista[0]
        for v_elemento in p_lista:
            if v_elemento < v_minimo:
                v_minimo=v_elemento
        return v_minimo
    else:
        return False

def maximo(p_lista):
    if len(p_lista) >0:
        v_maximo=p_lista[0]
        for v_elemento in p_lista:
            if v_elemento < v_maximo:
                v_maximo=v_elemento
        return v_maximo
    else:
        return False

def ultimate_analysis(p_lista):
     return 'total:'+ str(sum_total(p_lista)) + ', promedio:'+ str(promedio(p_lista))+ ', minimo:' + str(minimo(p_lista))+ ', maximo:'+str(maximo(p_lista)) + ', longitud:'+ str(longitud(p_lista))
    

#print(biggie_size([- 1, 3, 5, -5]))
#print(count_positives ([- 1,1,1,1]))
#print(sum_total ([1,2,3,4]))
#print(promedio ([1,2,3,4]) )
#print(longitud ([37,2,1, -9]))
#print( minimo ([37,2,1, -9]))
#print(maximo ([37,2,1, -9]))
print(ultimate_analysis ([37,2,1, -9]) )