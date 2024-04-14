import time
solution = []
            
def calcul(sol):
    """
    Vérifie si la somme des nombres formés par les éléments de la liste `sol` est égale au nombre formé par les éléments aux indices 10 à 14 de `sol`.

    Args:
        sol (list): Une liste contenant les éléments nécessaires pour effectuer le calcul.

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
    Affiche les éléments d'un tableau.

    Args:
        tab (list): Le tableau à afficher.

    Returns:
        None
    """
    for i in range(0, len(tab)):
        print(tab[i])
    
    
def brutality():
    """
    Cette fonction effectue une recherche exhaustive pour résoudre le problème suivant :
    Trouver les valeurs des variables c, o, a, l, p, e, s, i qui satisfont l'équation coca + cola = pepsi.
    Chaque variable doit prendre une valeur différente parmi les chiffres de 0 à 9.
    
    La fonction utilise des boucles imbriquées pour générer toutes les combinaisons possibles des variables.
    Chaque combinaison est vérifiée en appelant la fonction calcul pour vérifier si elle satisfait l'équation.
    Les solutions valides sont stockées dans la liste solution.
    
    À la fin de l'exécution, la fonction affiche le nombre de solutions trouvées.

    Args:
        None

    Returns:
        None
    """
    
    #! coca + cola = pepsi
    #?caractère unique : c o a l p e s i
    compteur = 0
    
    for c in range(10):
        for o in range(10):
            if(o!=c):
                for a in range(10):
                    if(a!=c and a!=o):
                        for l in range(10):
                            if(l!=c and l!=o and l!=a):
                                for p in range(10):
                                    if(p!=c and p!=o and p!=a and p!=l):
                                        for e in range(10):
                                            if(e!=c and e!=o and e!=a and e!=l and e!=p):
                                                for s in range(10):
                                                    if(s!=c and s!=o and s!=a and s!=l and s!=p and s!=e):
                                                        for i in range(10):
                                                            if(i!=c and i!=o and i!=a and i!=l and i!=p and i!=e and i!=s):
                                                            
                                                                #print(c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i)
                                                                if calcul([c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i]):
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