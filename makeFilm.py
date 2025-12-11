#!/usr/bin/env python
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wand.display import display
import subprocess

class film :
    pts = [(60,190), (640,114), (640,334), (60,280)]
    
    def __init__(self,backgroundImageFile="papyrusKerouac.jpg"):
        self.fileName=backgroundImageFile
        self.xmi = min(map(lambda x:x[0],self.pts))
        self.xma= max(map(lambda x:x[0],self.pts))
        self.ymi = min(map(lambda x:x[1],self.pts))
        self.yma= max(map(lambda x:x[1],self.pts))

    def makeImage(self,x0,x1,showIt=False,saveIt=False):
        """
        construit l'image où le trapèze de bord certical x0 et x1
        et le trapèze de bord vertical x2et x3
        la valeur -1 indique le plus grand x possible
        """
        if x0>self.xma or x0==-1 :x0=self.xma
        if x1>self.xma or x1==-1 :x1=self.xma
        if x0<self.xmi:x0=self.xmi
        if x1<self.xmi:x1=self.xmi
        if not (x0<=x1):
            print(f"{x0=} and {x1=} must be in increasing order")
            return
        self.img = Image(filename=self.fileName)
        self.draw = Drawing()
        self.draw.stroke_color = Color('black')
        self.draw.stroke_width = 1
        self.draw.fill_color = Color('transparent')  # pas de remplissage
        self.draw.polygon(self.pts)
        self.draw(self.img)
        self.go(self.xmi,x0)
        self.go(x1,self.xma)
        if showIt:
            display(self.img)
        if saveIt:
            fileName=f"image_{x0}_{x1}.jpg"
            self.img.save(filename=fileName)
            print(f"{fileName} saved")
            return fileName
        
    def droiteVertical(self,P1,P2,x):
        """
        retourne ordonnée de l'intersection droite passant par P1 et P2 (2-uples) et // à Oy
        """
        x0=P1[0];y0=P1[1]
        x1=P2[0];y1=P2[1]
        return (y1-y0)/(x1-x0)*(x-x0)+y0

    def rectangle(self,a,b):
        """
        retourne le trapèze dont les verticales ont pour abscisse X1 et X2
        """
        x0 = a
        y0 = self.droiteVertical(self.pts[0],self.pts[1],x0)
        x1 = b
        y1 = self.droiteVertical(self.pts[0],self.pts[1],x1)
        x2 = b
        y2 = self.droiteVertical(self.pts[2],self.pts[3],x2)
        x3 = a
        y3 = self.droiteVertical(self.pts[2],self.pts[3],x3)
        return [(x0,y0),(x1,y1),(x2,y2),(x3,y3)]

    def go(self,x1,x2):
        """
        dessine le polygone avec abscisse x1 et x2, et sauve l'image  'image%d'%n
        """
        global draw,img
        newPts = self.rectangle(x1,x2)
        self.draw.stroke_color = Color('blue')
        self.draw.fill_color = Color('black')  
        self.draw.polygon(newPts)
        self.draw(self.img)

    def go2(self,X1,X2):
        """
        dessine avec deux masques (60,X1) et (X2,640)
        """
        self.go(xmi,X1)
        self.go(X2,xma)

    def display(self):
        display(self.img)

film=film()
nIm=10
dx = (640-60-40)/nIm
fichiers=[]
for i in range(nIm):
    x0=60+i*dx
    x1= x0+50
    name = film.makeImage(x0,x1,showIt=False,saveIt=True)
    fichiers.append(name)

################################################
#                                           MONTAGE                                                              #
################################################
tmpFile = open("liste.txt","w")
for f in fichiers:
    tmpFile.writelines(f"file '{f}'\n")
    tmpFile.writelines(f"duration 0.2\n")
tmpFile.close()
cmd = 'ffmpeg -f concat -i liste.txt -vf "scale=iw-mod(iw\,2):ih-mod(ih\,2)"  -fps_mode vfr -pix_fmt yuv420p  film.mp4'
print(cmd)
subprocess.run(["rm", "-f", "film.mp4"], check=True)
resultat = subprocess.run(
    cmd,
    shell=True,
    capture_output=True,    # récupère stdout et stderr
    text=True                       # renvoie des chaînes plutôt que des bytes
)
print(resultat.stdout)
print(resultat.stderr)

subprocess.run(["mplayer","film.mp4"])
   
