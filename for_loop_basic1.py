def basico():
    for i in range(0,151):
        print(i)

def multiplos():
    i=5
    while i<1001:
        print(i)
        i+=5
        

def dojo_way():
    for n in range(1,101):
        if(n%10==0):
            print("Coding Dojo")
        elif(n%5==0):
            print("Coding")
        else:
            print(n)

def big_add():
    sum=0
    n=0
    while n<500000:
        sum+=n
        n+=2
    print("La suma es:",sum)    

def regresivo_4():
    init= 2018
    end=0
    while init > end:
        print(init)
        init-=4


def count_flex(lowNum, highNum, mult):
    init= lowNum
    end=highNum
    result=""
    while init <= end:
        if(init%3==0):
            result+=str(init)+","
        init+=1    
    return result[0:len(result)-1]

def primo(n):    
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def n_primos():
    for i in range(2,1000):
        if primo(i)==True:
            print(i)

#basico()
#multiplos()
#dojo_way()
#big_add()
#regresivo_4()
#x= count_flex(2, 9, 3)
#print(x)
#print(primo(7))
n_primos()