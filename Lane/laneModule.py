import cv2
import numpy as np
from numpy.lib.polynomial import poly
from numpy.lib.type_check import imag


class LaneDetection():
    # Converting the image to grayscale
    def grayscale(self, img):
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return gray_img

    # Applying Gaussian blur to the image
    def gaussblur(self, img):
        gray = self.grayscale(img)
        gb = cv2.GaussianBlur(gray, (5, 5), 0)
        return gb

    # Using the Canny edge detector to detect the edges
    def canny(self, img):
        gauss = self.gaussblur(img)
        canny = cv2.Canny(gauss, 50, 150)
        return canny
    
    # finding lane lines region of interest
    def roi(self, canny_img):
        height = canny_img.shape[0]
        polygons = np.array([[(200, height), (1100, height), (550, 250)]])
        mask = np.zeros_like(canny_img)
        cv2.fillPoly(mask, polygons, 255)
        # use the bitwise and operation to apply the mask on the image to obtain the region of interest
        roi = cv2.bitwise_and(canny_img, mask)
        return roi

    # Generate the coordinates for the lines using slope and intercept of the averaged lines
    def make_coordinates(self, img, line_params):
        slope, intercept = line_params
        y1 = img.shape[0]
        y2 = int(y1*(3/5))
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
        return np.array([x1, y1, x2, y2])

    # Find the avg slope and intercept of the lines and return the coordinates of the averaged lines
    def avg_slope_intercept(self, img, lines):
        left_fit = []
        right_fit = []

        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            # Fit a 1D polynomial to find the slope and the intercept of the line from the line coordinates
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope, intercept = parameters[0], parameters[1]
            if slope<0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))

        # Take the avg slope and intercept of the lines
        left_fit_avg = np.average(left_fit, axis=0)
        right_fit_avg = np.average(right_fit, axis=0)
        left_line = self.make_coordinates(img, left_fit_avg)
        right_line = self.make_coordinates(img, right_fit_avg)

        return np.array([left_line, right_line])

    # Display the lane lines on the image
    def display_lines(self, img, lines, poly=False):
        edges = []
        line_img = np.zeros_like(img)
        line_img = cv2.cvtColor(line_img, cv2.COLOR_GRAY2BGR)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                edges.append(line)
                cv2.line(line_img, (x1, y1), (x2, y2), color=(255, 0, 0), thickness=10)
        if poly:
            points = np.array([[edges[0][2], edges[0][3]], [edges[0][0], edges[0][1]], [edges[1][0], edges[1][1]], [edges[1][2], edges[1][3]]])
            cv2.fillPoly(line_img, pts=[points], color=(0,256,0))
        return line_img

    def hough(self, img, poly=False):
        canny_img = self.canny(img)
        roi_img = self.roi(canny_img)
        # Find the lane lines using Hough transform
        lines = cv2.HoughLinesP(roi_img, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
        avg_lines = self.avg_slope_intercept(img, lines)
        line_img = self.display_lines(roi_img, avg_lines, poly=poly)
        combo_image = cv2.addWeighted(img, 0.9, line_img, 1, 1)
        return combo_image

    




    


