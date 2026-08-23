def is_square(x1,y1,x2,y2,x3,y3,x4,y4):
    d1=(x1-x2)**2+(y1-y2)**2
    d2=(x2-x3)**2+(y2-y3)**2
    d3=(x3-x4)**2+(y3-y4)**2
    d4=(x4-x1)**2+(y4-y1)**2
    d5=(x1-x3)**2+(y1-y3)**2
    d6=(x2-x4)**2+(y2-y4)**2
    D=sorted([d1,d2,d3,d4,d5,d6])
    if D[0]==0:
        return False
    if not (D[0]==D[1]==D[2]==D[3]):
        return False
    if D[4]!=D[5]:
        return False
    if D[4]!=2*D[0]:
        return False
    return True