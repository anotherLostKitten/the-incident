class Img:
    def __init__(self,r,c):
        self.c=c
        self.r=r
        self.img=[0 for i in range(r*c)]
    def s(self,r,c,v):
        self.img[c+r*self.c]=v
    def ln(self,rs,cs,rf,cf,v):
        dr=abs(rf-rs)
        dc=abs(cf-cs)
        if rs>rf if dr<dc else cs>cf:
            self.ln(rf,cf,rs,cs,v)
        elif dr<dc:
            rr=2*dr-dc
            for c in range(cs,cf-1 if cs>cf else cf+1,-1 if cs>cf else 1):
                self.s(rs,c,v)
                rs+=1 if rr>0 else 0
                rr+=2*dr-2*dc if rr>0 else 2*dr
        else:
            rr=2*dc-dr
            for r in range(rs,rf-1 if rs>rf else rf+1,-1 if rs>rf else 1):
                self.s(r,cs,v)
                cs+=1 if rr>0 else 0
                rr+=2*dc-2*dr if rr>0 else 2*dc
    def __str__(self):
        txt = "P3 "+str(self.c)+" "+str(self.r)+" 255\n"
        for i in self.img:
            txt+=str(i/65536)+" "+str(i/256%256)+" "+str(i/256)+" "
        return txt
if __name__ == "__main__":
    img=Img(500,500)
    pts=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2))
    for i in range(len(pts)):
        for j in range(i,len(pts)):
            if i<8 or ((i!=8 or j!=15) and j!=i+1):
                img.ln(250+100*pts[i][0],250+100*pts[i][1],250+100*pts[j][0],250+100*pts[j][1],16777215)
    f=open("things.ppm","w")
    f.write(str(img))
    f.close()
