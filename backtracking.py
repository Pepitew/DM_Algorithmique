global COMPTEUR_EXEC
COMPTEUR_EXEC = 0
import time

def tous_differents(sol):
    for i in range(len(sol)):
        for j in range(i+1,len(sol)):
            if(sol[i] == sol[j]):
                return False
    return True
            
def calcul(sol):
    [A, I, C, L, S, O, P, E] = sol
    if ( (C*1000 + O*100 +C*10 + A) +
         (C*1000 + O*100 + L*10 + A) == 
         (P*10000 + E*1000 + P*100 + S*10 + I)
       ):
        return True
    
def affiche(tab):
    [A, R1, I, C, L, R2, S, O, R3, P, E] = tab
    
    n1 = int(str(C) + str(O) + str(C) + str(A))
    n2 = int(str(C) + str(O) + str(L) + str(A))
    res = int(str(P) + str(E) + str(P) + str(S) + str(I))
    
    print("solution : coca + cola = pepsi ==>", n1, "+", n2, "=", res)
        
def est_solution(sol):
    global COMPTEUR_EXEC
    [A, R1, I, C, L, R2, S, O, R3, P, E] = sol
    if(tous_differents([A,I,C,L,S,O,P,E]) and calcul([A,I,C,L,S,O,P,E])):
        COMPTEUR_EXEC += 1
        affiche(sol)
        return True
    return False

#!###############################################################
#? [0, 1,2,3,4, 5,6,7,8, 9,10]
#?  A R1 I C L R2 S O R3 P E

#!###############################################################

def ajout_possible(sol):
    if(len(sol) == 3):
        if(sol[0]*2 == 10* sol[1] + sol[2]):
            return True
        else:
            return False
        
    if(len(sol) == 7):
        if(sol[3]+sol[4]+sol[1] == 10*sol[5]+sol[6]):
            return True
        else:
            return False
        
    if(len(sol) == 10):
        if(sol[7]*2 + sol[5] == 10*sol[8]+sol[9]):
            return True
        else:
            return False    
    if(len(sol) == 11):
        if(2*sol[3] + sol[8] == 10*sol[9] + sol[10]): 
            return True
        else:
            return False
    return True


def backtracking(sol):
    
    if(len(sol) == 11):
        est_solution(sol)
    else:
        for val in range (10):
            sol.append(val)
            if(ajout_possible(sol)):
                backtracking(sol)
            sol.pop()
            
def exec_backtracking():
    global COMPTEUR_EXEC
    debut = time.time()
    backtracking([])
    fin = time.time()
    temps_ecoule = fin - debut
    print("nombre de solutions : "+ str(COMPTEUR_EXEC))
    print("temps écoulé =",temps_ecoule, "secondes")
    
exec_backtracking()