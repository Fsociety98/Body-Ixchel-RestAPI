import numpy as np
#import cv2
from cv2 import *
from matplotlib import pyplot as plt


class MastografiaAnomaliaDetector():
    def __init__(self, modelSource, imgSourceRoute, rectangleLabel):
        self.modelSource = str(modelSource)
        self.imgSourceRoute = str(imgSourceRoute)
        self.rectangleLabel = str(rectangleLabel)

    def analize(self):
        #clasificador
        self.anomalias_cascade=cv2.CascadeClassifier(self.modelSource)

        self.imgSource = cv2.imread(self.imgSourceRoute)
        self.gray = cv2.cvtColor(self.imgSource,cv2.COLOR_BGR2GRAY)
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.anomalias = self.anomalias_cascade.detectMultiScale(self.gray,1.9,5,75)

        for (self.x, self.y, self.w, self.h) in self.anomalias:
            self.imgResult = cv2.rectangle(self.imgSource,(self.x, self.y),(self.x + self.w, self.y + self.h),(0,255,0),2)
            cv2.putText(self.imgResult,self.rectangleLabel,( self.x, self.y), self.font,0.9,(0,255,0),2)

        
        self.p ,self.l, self.m = cv2.split(self.imgResult)
        self.imgResult = cv2.merge([self.m, self.l, self.p])

        return self.imgResult

    def saveImage(self, img, route):
        #self.resultImagePath = '{0}{1}.jpg'.format(route, name)
        self.resultImagePath = route
        cv2.imwrite(self.resultImagePath, img)

    def getResultImagePath(self):
        return self.resultImagePath


