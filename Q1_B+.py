import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
#from google.colab.patches import cv2_imshow
class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
def gDiff(img,PointC,tmpPoint):
    return abs(int(img[PointC.x,PointC.y]) - int(img[tmpPoint.x,tmpPoint.y]))
def selectConnects(p):
    if p != 0:
        connects = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0), Point(1, 1), \
                    Point(0, 1), Point(-1, 1), Point(-1, 0)]
    else:
        connects = [ Point(0, -1),  Point(1, 0),Point(0, 1), Point(-1, 0)]
    return connects
 
 
def regionGrow(img,seeds,thresh,p = 1):
    height, weight = img.shape
    seedMark = np.ones(img.shape)
    seedList = []
    for seed in seeds:
        seedList.append(seed)
    label = 0
    connects = selectConnects(p)
    while(len(seedList)>0):
        PointC = seedList.pop(0)
 
        seedMark[PointC.x,PointC.y] = label
        for i in range(len(connects)):
            Xt = PointC.x + connects[i].x
            YT = PointC.y + connects[i].y
            if Xt < 0 or YT < 0 or Xt >= height or YT >= weight:
                continue
            Diff = gDiff(img,PointC,Point(Xt,YT))
            if Diff <= thresh and seedMark[Xt,YT] == 1:
                seedMark[Xt,YT] = label
                seedList.append(Point(Xt,YT))
    return seedMark
img = np.array(Image.open("B+.png").convert("L"))

seeds = [Point(50,10),Point(50,50),Point(100, 50)]
#modifier
 
Img = regionGrow(img,seeds,thresh=30, p=1)
plt.imshow(Img, cmap='gray')
plt.show()