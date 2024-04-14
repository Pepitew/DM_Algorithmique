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

sol = [1,2,3,4,"",5,6,7,8,"",0,6,9,1,2]
print(tous_differents(sol))