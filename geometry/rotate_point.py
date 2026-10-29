from math import radians,sin,cos

# 点(x,y)を, 点(cx,cy)を中心に d 度回転させたときの座標を出力
# d>0:反時計回り, d<0:時計回り
def rotate_point(x,y,cx,cy,d):
    x-=cx
    y-=cy
    d=radians(d)
    X,Y=x*cos(d)-y*sin(d),y*cos(d)+x*sin(d)
    X+=cx
    Y+=cy
    return (X,Y)