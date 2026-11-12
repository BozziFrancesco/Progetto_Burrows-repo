def FirstStep(a):
    rotazioni = []
    rotazioni.append(a)
    bwr = a
    for i in range(len(a) - 1):
        char = bwr[0:1]
        bwr = bwr[1:] + char
        rotazioni.append(bwr)
        
    print("\n--------PRIMO STEP-------\n")
    print(rotazioni)
    return SecondStep(rotazioni)

def SecondStep(b):
    b.sort()
    print("\n--------SECONDO STEP-------\n")
    print(b)
    return ThirdStep(b)

def ThirdStep(c):
    trasformata = ""
    for i in c:
        trasformata = trasformata + i[-1]

    print("\n--------TERZO STEP-------\n")
    return trasformata