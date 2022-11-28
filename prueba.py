row=([[1,2,3,4,5],[-1,-2,-3,-4,-5]])

for p in row:
    print(p[0],p[1],p[2],p[3],p[4])
    p[0]=p[0]+25

print(row)