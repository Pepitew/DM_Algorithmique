import time

solution = []

def tous_differents(sol):
    for i in range(len(sol)):
        for j in range(i+1,len(sol)):
            if(sol[i] == sol[j]):
                return False
    return True
            
def calcul(sol):
    if ( (sol[0]*1000 + sol[1]*100 +sol[2]*10 + sol[3]) 
       + (sol[5]*1000 + sol[6]*100 + sol[7]*10 + sol[8])
       == (sol[10]*10000 + sol[11]*1000 + sol[12]*100 + sol[13]*10 + sol[14])
       ):
        return True

def affiche(tab):
    print("c  o  c  a  |  c  o  l  a  |  p  e  p  s  i")
    for i in range(0, len(tab)):
        print(tab[i])
    
    
def brutality():
    
    #! coca + cola = pepsi
    #?caractère unique : c o a l p e s i
    compteur = 0
    sol_char_unique = []
    for c in range(10):
        for o in range(10):
            for a in range(10):
                for l in range(10):
                    for p in range(10):
                        for e in range(10):
                            for s in range(10):
                                for i in range(10):
                                                            
                                    #* print(c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i)
                                    if calcul([c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i]) and tous_differents([c,o,a,l,p,e,s,i]):
                                        solution.append([c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i])
                                        compteur=compteur + 1
    
    print("nombre de solution = ", compteur)
    
    
def exec_brutality():
    debut = time.time()
    brutality()
    affiche(solution)
    fin = time.time()
    temps_ecoule = fin - debut
    print("temps écoulé =",temps_ecoule, "secondes")
    
    
exec_brutality()