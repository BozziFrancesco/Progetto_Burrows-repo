def FirstStep(a):
     
    bwr=a
    for i in a:
        char=a[0:0]
        bwr=bwr+char
        SecondStep(bwr)
    
    print(bwr)

def SecondStep(b):
    
          
          
          




parola_iniziale=input("Che parola vuoi comprimere?") 
parola_iniziale =  parola_iniziale + "$"
FirstStep(parola_iniziale)



