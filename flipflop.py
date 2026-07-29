def palindr(r):
    e = len(r)-1
    s = 0
    while s<e:
        if r[s] != r[e]:
            return False
        s = s+1 
        e = e-1
    return True
r = (1,2,2,3,3,2,2,1)
if palindr(r):
    print("Turple is flip flop.")
else:
    print("Not a flip flop. ")
    