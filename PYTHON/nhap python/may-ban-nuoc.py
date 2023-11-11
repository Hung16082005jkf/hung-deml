l = {}
q = [] 
def hung(a): 
    j = 0   
    for i in range(1,a):
        d = a%i
        if d == 0:
            j = j + i
    if j == a:
        return True
    if j != a:
        return False
for i in range(0,900):
    hung(i)
    if hung(i) == True:
        l[i] = hung(i)
print(l)


        
    
