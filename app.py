from flask import Flask, request, render_template, send_file
from PIL import Image, ImageEnhance
from io import BytesIO
import io
from werkzeug.datastructures import FileStorage
# from skimage import io
# from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    title = 'This is Fix Image App!!'
    
    if request.method == 'GET':
        return render_template('index.html', title=title)
    # else:
    #     f = request.files['file']
    #     print("f is :"+ str(f))
    #     img_bright = f.point(lambda x:x*1.8)
        
    #     return send_file(img_bright,
    #         attachment_filename=f.filename,
    #         as_attachment=True)
    else:
        f = request.files['file']
        buf = io.BytesIO()
        # adjust_contrast(f, buf, 1.7)
        adjust_bright(f, buf, 1.7)
        buf.seek(0)

        return send_file(buf,
            attachment_filename=f.filename,
            as_attachment=True)
    
# def adjust_contrast(input_image, output_image, factor):
#     image = Image.open(input_image)
#     enhancer_object = ImageEnhance.Contrast(image)
#     out = enhancer_object.enhance(factor)
#     out.save(output_image, 'JPEG')

def adjust_bright(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Brightness(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image, 'JPEG')

if __name__ == '__main__':
    app.run(debug=True)