ls1=[[2,6],[10,1]]
ls2=[[3,5],[7,9]]
r1=len(ls1)
r2=len(ls2)
c1=len(ls1[-1])
c2=len(ls2[-1])
out=[[0]*c2 for i in range(r1)]
if c1==r2:
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                out[i][j]+=ls1[i][k]*ls2[k][j]
for ele in out:
    print(*ele)
