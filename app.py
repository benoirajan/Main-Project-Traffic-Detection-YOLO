from cProfile import label
from pyexpat.errors import messages
from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for, send_file, abort
from werkzeug.utils import secure_filename
import os
from yolov5.detect import run
from web import Traffic
from PIL import Image

app = Flask(__name__)


@app.route("/")
def FUN_root():
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("Glint.html")


@app.route("/testr")
def testr():
    return render_template("result.html")


@app.route('/image')
def get_image():
    if request.args.get('name') != '':
        filename = request.args.get('name')
    return send_file(filename, mimetype='image/jpg')


@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['image_file']
    maxdet = int(request.form.get('max_det'))
    confThresh = int(request.form.get('conf_thresh'))
    maxtime = int(request.form.get('mtime'))
    mintime = int(request.form.get('minTime'))
    filename = secure_filename(uploaded_file.filename)
    if filename == '':
        abort(400)
    
    file = "./upload/"
    if not os.path.exists(file):
        os.mkdir(file)
    file += filename
    if not os.path.exists(file):
        uploaded_file.save(file)

    dir, sums = getPrediction(maxdet, confThresh, file)
    time = Traffic.getGreenTime(sums, maxtime, maxdet)
    
    outfile = str(dir) + filename
    if sums > 0:
        time = mintime if time < mintime else time
    else:
        time = 0
    return render_template("result.html",
                           file=outfile,
                           sums=sums,
                           time=int(time))


def getPrediction(maxdet, confThresh, image):
    im = Image.open(image)
    (w, h) = im.size
    print("(w,h): ", w, h)
    out = './output/'
    m = int(max(w, h))
    lt = int(m/320)
    # print(maxdet,type(maxdet),confThresh,type(confThresh))
    # ncls=10
    ncls = run(weights='./weights/custom.pt', source=image, imgsz=(w, h), view_img=False, line_thickness=lt,
               project=out, max_det=maxdet, conf_thres=confThresh/100, name='webd', exist_ok=True)
    return out+"webd/", ncls


if __name__ == "__main__":
    app.run(debug=True,
            # host="0.0.0.0"
            )
