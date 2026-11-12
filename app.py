def FirstStep(a):
    rotazioni=[]
    bwr=a
    for i in range(len(a)-1):
        char=bwr[0:1]
        bwr=bwr[1:]+char
        rotazioni.append(bwr)
        
    
    print(rotazioni)
    SecondStep(rotazioni)

def SecondStep(b):

    b.sort()
    print(b)
    

    
          
          
          




parola_iniziale=input("Che parola vuoi comprimere?") 
parola_iniziale =  parola_iniziale + "$"
FirstStep(parola_iniziale)



