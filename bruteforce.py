solution = []
def contraintes_unicités(sol):
    for i in range(10):
    if(sol[i] != sol[i+1] and
       sol[i] != sol[2] and
       sol[i] != sol[3] and
       sol[i] != sol[4] and
       sol[i] != sol[5] and
       sol[i] != sol[6] and
       sol[i] != sol[7] and
       sol[i] != sol[8] and
       sol[i] != sol[9] and
       ):
def contraintes(sol):
    if ( (sol[0]*1000 + sol[1]*100 +sol[2]*10 + sol[3]) 
       + (sol[5]*1000 + sol[6]*100 + sol[7]*10 + sol[8])
       == (sol[10]*10000 + sol[11]*1000 + sol[12]*100 + sol[13]*10 + sol[14])
       ):
        return True

def brutality():
    
    #! coca + cola + pepsi
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
                                    if contraintes([c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i]):
                                        solution.append([c,o,c,a,"|",c,o,l,a,"|",p,e,p,s,i])

def exec_brutality():
    brutality()
    print(solution)

exec_brutality()