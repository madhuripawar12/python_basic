a = [[12,7,3],[4 ,5,6],[7 ,8,9]]
transpose= [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
   for j in range(len(a[0])):
       transpose[i][j] = a[j][i]
for r in transpose:
   print(r)
