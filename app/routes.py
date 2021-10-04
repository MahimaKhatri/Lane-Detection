from flask import Flask, render_template, request, Response
from werkzeug.utils import secure_filename
import os
from os.path import isfile, join
import cv2
from Lane.laneModule import LaneDetection
from app.video import Video
from app import app

def gen(camera):
    while camera:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route("/", methods =["GET", "POST"])
def home_page():
    path = None
    choice = None
    if request.method == "POST":
        choice = request.form.get("IV")
        if choice == "Image":
            f = request.files['file']
            filename = secure_filename(f.filename)
            org_path = "Images/Original/" + filename
            path = os.path.join(app.config['UPLOAD_PATH'], org_path)
            f.save(path)
            display = request.form.get("dis")
            if display == 'org':
                path = 'static/uploads' + '/Images/Original/' + filename
                print(path)

            elif display == 'grey':
                img = cv2.imread(path)
                model = LaneDetection()
                gray_img = model.grayscale(img)
                file_name = filename[:-4] + "gray.jpg"
                gray_path = "Images/Gray/" + file_name
                path = os.path.join(app.config['UPLOAD_PATH'], gray_path)
                cv2.imwrite(path, gray_img)
                path = 'static/uploads/' + gray_path

            elif display == 'Gaussian':
                img = cv2.imread(path)
                model = LaneDetection()
                gauss_img = model.gaussblur(img)
                file_name = filename[:-4] + "gauss.jpg"
                gray_path = "Images/Gaussian/" + file_name
                path = os.path.join(app.config['UPLOAD_PATH'], gray_path)
                cv2.imwrite(path, gauss_img)
                path = 'static/uploads/' + gray_path

            elif display == 'Canny':
                img = cv2.imread(path)
                model = LaneDetection()
                canny_img = model.canny(img)
                file_name = filename[:-4] + "canny.jpg"
                gray_path = "Images/Canny/" + file_name
                path = os.path.join(app.config['UPLOAD_PATH'], gray_path)
                cv2.imwrite(path, canny_img)
                path = 'static/uploads/' + gray_path

            elif display == 'roi':
                img = cv2.imread(path)
                model = LaneDetection()
                canny_img = model.canny(img)
                roi_img = model.roi(canny_img)
                file_name = filename[:-4] + "roi.jpg"
                gray_path = "Images/ROI/" + file_name
                path = os.path.join(app.config['UPLOAD_PATH'], gray_path)
                cv2.imwrite(path, roi_img)
                path = 'static/uploads/' + gray_path
            
            elif display == 'lanes':
                img = cv2.imread(path)
                model = LaneDetection()
                hough_img = model.hough(img, poly=False)
                file_name = filename[:-4] + "hough.jpg"
                gray_path = "Images/hough/" + file_name
                path = os.path.join(app.config['UPLOAD_PATH'], gray_path)
                cv2.imwrite(path, hough_img)
                path = 'static/uploads/' + gray_path

            elif display == 'lanes_with_path':
                img = cv2.imread(path)
                model = LaneDetection()
                hough_img = model.hough(img, poly=True)
                file_name = filename[:-4] + "hough_path.jpg"
                gray_path = "Images/hough_path/" + file_name
                path = os.path.join(app.config['UPLOAD_PATH'], gray_path)
                cv2.imwrite(path, hough_img)
                path = 'static/uploads/' + gray_path

        if choice == 'Video':
            f = request.files['file']
            filename = secure_filename(f.filename)
            org_path = "Videos/Original/" + filename
            path = os.path.join(app.config['UPLOAD_PATH'], org_path)
            f.save(path)
            display = request.form.get('dis')
            return Response(gen(Video(path, display=display)), mimetype='multipart/x-mixed-replace; boundary=frame')

    return render_template("index.html", path=path, choice=choice)

@app.route("/dev")
def dev_page():
    return render_template("dev.html")

if __name__ == "__main__":
    app.run(debug=True)
