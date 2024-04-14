global COMPTEUR_EXEC
COMPTEUR_EXEC = 0
import time

def tous_differents(sol):
    """
    Vérifie si tous les éléments dans la liste 'sol' sont différents les uns des autres.

    Args:
        sol (list): Une liste d'éléments.

    Returns:
        bool: True si tous les éléments sont différents, False sinon.
    """
    for i in range(len(sol)):
        for j in range(i+1,len(sol)):
            if(sol[i] == sol[j]):
                return False
    return True
            
def calcul(sol):
    """
    Calcule si la solution donnée est valide.

    Args:
        sol (list): Une liste contenant les valeurs des variables A, I, C, L, S, O, P, E.

    Returns:
        bool: True si la solution est valide, False sinon.
    """
    [A, I, C, L, S, O, P, E] = sol
    if ( (C*1000 + O*100 +C*10 + A) +
         (C*1000 + O*100 + L*10 + A) == 
         (P*10000 + E*1000 + P*100 + S*10 + I)
       ):
        return True
    
def affiche(tab):
    """
    Affiche la solution du problème de l'équation coca + cola = pepsi.

    Args:
        tab (list): Une liste contenant les valeurs des lettres correspondantes aux chiffres de l'équation.

    Returns:
        None
    """
    [A, R1, I, C, L, R2, S, O, R3, P, E] = tab
    
    n1 = int(str(C) + str(O) + str(C) + str(A))
    n2 = int(str(C) + str(O) + str(L) + str(A))
    res = int(str(P) + str(E) + str(P) + str(S) + str(I))
    
    print("solution : coca + cola = pepsi ==>", n1, "+", n2, "=", res)



def est_solution(sol):
    """
    Vérifie si la solution donnée est une solution valide.

    Args:
        sol (list): La solution à vérifier.

    Returns:
        bool: True si la solution est valide, False sinon.
    """
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
    """
    Vérifie si une solution partielle peut être ajoutée à la solution complète.

    Args:
        sol (list): La solution partielle à vérifier.

    Returns:
        bool: True si la solution partielle peut être ajoutée, False sinon.
    """
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
    """
    Effectue une recherche en profondeur avec retour en arrière (backtracking) pour trouver une solution.

    Args:
        sol (list): La solution partielle actuelle.

    Returns:
        None
    """
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
    print("le nombre de solutions est : ", COMPTEUR_EXEC)
    print("le temps d'execution est : ", temps_ecoule)

################################ TESTS ################################

assert tous_differents([1, 2, 3, 4, 5]) == True
assert tous_differents([1, 2, 3, 3, 4]) == False
assert tous_differents([5, 4, 3, 2, 1]) == True
assert tous_differents([1, 1]) == False
assert tous_differents([]) == True

#Inutile de tester les fonctions calcul et affiche


exec_backtracking()