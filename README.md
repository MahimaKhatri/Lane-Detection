# Lane-Detection

## Introduction
One of the most fundamental tasks in computer vision for autonomous driving is lane line detection on the road. Lane lines are painted for humans to see and follow while driving. In a very similar way, an autonomous vehicle that uses human designed infrastructure, needs to see the lane markings to steer accordingly and follow the road trajectory.

In this project, we will use Computer Vision to recognise lane lines in videos and pictures of roadways. One of the most essential traffic laws is to follow lane lines, therefore identifying them when developing models for autonomous vehicles is a crucial job. 

## Frontend

### Home Page
![alt text](https://github.com/MahimaKhatri/Lane-Detection/blob/master/Images/home.PNG)

### Developers Page
![alt text](https://github.com/MahimaKhatri/Lane-Detection/blob/master/Images/dev.png)

## Features

Computer Vision algorithm is used to detect straight lane markings on road using OpenCV Image Processing, Color Masks, Canny Edge Detection and Hough Transform.

### Original Image
![alt text](https://github.com/MahimaKhatri/Lane-Detection/blob/master/Images/test_image.jpg)

+ **GrayScale**

Grayscaling is the process of converting an image from other color spaces e.g. RGB, CMYK, HSV, etc. to shades of gray. It varies between complete black and complete white.

![alt text](https://github.com/MahimaKhatri/Lane-Detection/blob/master/Images/test_imagegray.jpg)

+ **Gaussian Blur**

In image processing, a Gaussian blur (also known as Gaussian smoothing) is the result of blurring an image by a Gaussian function (named after mathematician and scientist Carl Friedrich Gauss).In Gaussian Blur operation, the image is convolved with a Gaussian filter instead of the box filter. The Gaussian filter is a low-pass filter that removes the high-frequency components.

![alt text](https://github.com/MahimaKhatri/Lane-Detection/blob/master/Images/test_imagegauss.jpg)

+ **Canney Edge**

Canny Edge Detection is used to detect the edges in an image. It accepts a gray scale image as input and it uses a multistage algorithm.

![alt text](https://github.com/MahimaKhatri/Lane-Detection/blob/master/Images/test_imagecanny.jpg)

+ **Hough Transform**

The Hough transform is a feature extraction technique used in image analysis, computer vision, and digital image processing. The purpose of the technique is to find imperfect instances of objects within a certain class of shapes by a voting procedure. This voting procedure is carried out in a parameter space, from which object candidates are obtained as local maxima in a so-called accumulator space that is explicitly constructed by the algorithm for computing the Hough transform.

![alt text](https://github.com/MahimaKhatri/Lane-Detection/blob/master/Images/test_imagehough.jpg)

![alt text](https://github.com/MahimaKhatri/Lane-Detection/blob/master/Images/test_imagehough_path.jpg)

### Video Demo

## Tech Stack

+ Html
+ CSS
+ Flask
+ OpenCV

## Running Instructions
Open the terminal and type the following 
```
$ git clone https://github.com/MahimaKhatri/Lane-Detection.git
$ cd Lane-Detection
$ python3 -m venv lane-env
$ source lane-env/bin/activate
$ pip3 install -r requirements.txt
$ python3 run.py
```

### Requirements


## Developers

<table>
<tr align="center">


<td>

Mudit Jindal 

<p align="center">
<img src = "https://avatars.githubusercontent.com/u/60563356?s=400&u=09a4f1f24803e0bd5cdc674e0fa021ca791fe126&v=4"  height="120"
alt="Mudit Jindal">
</p>
<p align="center">
<a href = "https://github.com/mudit14224" target="_blank"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/mudit-jindal-40521a18b/" target="_blank">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>






<td>

Mahima Khatri

<p align="center">
<img src = "https://avatars.githubusercontent.com/u/77387745?v=4"  height="120"
alt="Mahima Khatri">
</p>
<p align="center">
<a href = "https://github.com/MahimaKhatri" target="_blank"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/mahima-khatri-434a3b193/" target="_blank">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>
</tr>
</table>




