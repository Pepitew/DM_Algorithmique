import time

solution = []

def tous_differents(sol):
    """
    Vérifie si tous les éléments dans la liste 'sol' sont différents les uns des autres.

    Args:
        sol (list): La liste contenant les éléments à vérifier.

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
    Vérifie si la somme des nombres formés par les éléments de la liste `sol` est égale au nombre formé par les éléments aux indices 10 à 14 de `sol`.

    Args:
        sol (list): Une liste contenant les chiffres nécessaires pour effectuer le calcul.

    Returns:
        bool: True si la somme est égale au nombre, False sinon.
    """
    if ( (sol[0]*1000 + sol[1]*100 +sol[2]*10 + sol[3]) 
       + (sol[5]*1000 + sol[6]*100 + sol[7]*10 + sol[8])
       == (sol[10]*10000 + sol[11]*1000 + sol[12]*100 + sol[13]*10 + sol[14])
       ):
        return True

def affiche(tab):
    """
    Affiche les éléments du tableau 'tab' de manière formatée.

    Args:
        tab (list): Le tableau contenant les éléments à afficher.

    Returns:
        None
    """
    print("c  o  c  a  |  c  o  l  a  |  p  e  p  s  i")
    for i in range(0, len(tab)):
        print(tab[i])
    
    
def brutality():
    """
    Cette fonction effectue une recherche exhaustive pour résoudre le problème de l'équation "coca + cola = pepsi".
    Elle génère toutes les combinaisons possibles de chiffres de 0 à 9 pour les lettres correspondantes dans l'équation.
    La fonction vérifie ensuite si la combinaison satisfait les contraintes de l'équation et si tous les chiffres sont différents.
    Les solutions valides sont stockées dans une liste.
    Enfin, le nombre de solutions trouvées est affiché.

    Args:
        None
    
    Returns:
        None

    """
    
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