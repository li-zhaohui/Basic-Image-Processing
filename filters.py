import numpy as np
import cv2

class Filters(object):
    '''def __init__(self,filename,figure_size):
        self.filename = filename
        self.figure_size = figure_size
        self.image = cv2.imread(self.filename)'''

    def mean(self,image):
        new_image = cv2.blur(image,(5,5))
        cv2.imwrite("output/Mean.jpg",new_image)
        return new_image

    def gaussian(self,image):
        new_image = cv2.GaussianBlur(image, (5,5),0)
        cv2.imwrite("output/Gaussian.jpg",new_image)
        return new_image

    def median(self,image):
        new_image = cv2.medianBlur(image,5)
        cv2.imwrite("output/Median.jpg",new_image)
        return new_image

    def bilateral(self,image):
        bilateral = cv2.bilateralFilter(image, 15, 75, 75)
        cv2.imwrite("output/Bilateral.jpg",bilateral)
        return bilateral

    def averaging(self,image):
        blur = cv2.blur(image,(5,5))
        cv2.imwrite("output/Average.jpg",blur)
        return blur
    
if __name__=="__main__":
    filters = Filters()
    mean = filters.mean("1.jpg")
    gaus = filters.gaussian()
    med = filters.median()
    bil = filters.bilateral()
    ave = filters.averaging()
    cv2.imshow("Mean", mean)
    cv2.imshow("Gaussian", gaus)
    cv2.imshow("Median", med)
    cv2.imshow("Bilateral", bil)
    cv2.imshow("Averaging", ave)
    cv2.imshow("Original", filters.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
