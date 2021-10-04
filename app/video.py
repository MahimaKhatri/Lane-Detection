import cv2
import numpy as np
from numpy.lib.polynomial import poly
from Lane.laneModule import LaneDetection

class Video(object):
    def __init__(self, path, display):
        self.video = cv2.VideoCapture(path)
        self.display = display
        self.model = LaneDetection()

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        ret, img = self.video.read()
        if ret:
            frame = img
            if self.display == 'org':
                ret, jpeg = cv2.imencode('.jpg', img)
                return jpeg.tobytes()

            elif self.display == 'grey':
                img = self.model.grayscale(img)
                ret, jpeg = cv2.imencode('.jpg', img)
                return jpeg.tobytes()

            elif self.display == 'Gaussian':
                img = self.model.gaussblur(img)
                ret, jpeg = cv2.imencode('.jpg', img)
                return jpeg.tobytes()
            
            elif self.display == 'Canny':
                img = self.model.canny(img)
                ret, jpeg = cv2.imencode('.jpg', img)
                return jpeg.tobytes()
            
            elif self.display == 'roi':
                img = self.model.canny(img)
                img = self.model.roi(img)
                ret, jpeg = cv2.imencode('.jpg', img)
                return jpeg.tobytes()
            
            elif self.display == 'lanes':
                img = self.model.hough(img, poly=False)
                ret, jpeg = cv2.imencode('.jpg', img)
                return jpeg.tobytes()

            elif self.display == 'lanes_with_path':
                img = self.model.hough(img, poly=True)
                ret, jpeg = cv2.imencode('.jpg', img)
                return jpeg.tobytes()

        else:
            r , jpeg = cv2.imencode('.jpg', np.zeros((img.shape[0],img.shape[1],3)))
            return jpeg.tobytes()