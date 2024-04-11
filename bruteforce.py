solution = []

def tous_differents(sol):
    for i in range(len(sol)):
        for j in range(len(sol)):
            if(sol[i] == sol[j]):
                return False
            
def calcul(sol):
    if ( (sol[0]*1000 + sol[1]*100 +sol[2]*10 + sol[3]) 
       + (sol[5]*1000 + sol[6]*100 + sol[7]*10 + sol[8])
       == (sol[10]*10000 + sol[11]*1000 + sol[12]*100 + sol[13]*10 + sol[14])
       ):
        return True

def brutality():
    
    #! coca + cola = pepsi
    #?caractère unique : c o a l p e s i
    
    for c in range(10):
        for o in range(10):
            for a in range(10):
                for l in range(10):
                    for p in range(10):
                        for e in range(10):
                            for s in range(10):
                                for i in range(10):
                                    print(c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i)
                                    if calcul([c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i]) and tous_differents([c,o,a,l,p,e,s,i]):
                                        solution.append([c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i])

def exec_brutality():
    brutality()
    print(solution)

exec_brutality()