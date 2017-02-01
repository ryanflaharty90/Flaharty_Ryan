import math
class Distance:
    def init(self,x1,y1,x2,y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.YTwo = y2
        self.distance = 0

    def setValues(self,newX1,newY1,newX2,newY2):
        self.xOne = newX1
        self.yOne = newY1
        self.xTwo = newX2
        self.yTwo = newY2
        self.distance = 0

    def getMPH(self):
        self.distance = Math.sqrt((xTwo-xOne)*(xTwo-xOne)+(yTwo-yOne)*(yTwo-yOne));
        


    
