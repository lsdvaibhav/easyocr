from flask import Flask, request, jsonify
#import easyocr
app = Flask(__name__)

@app.route("/im_size", methods=["POST"])
def process_image():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)
    #reader = easyocr.Reader(['en'])
    #output = reader.readtext('Image2.jpg')
    return jsonify({'msg': 'success', 'size': [img.width, img.height]})


if __name__ == "__main__":
    app.run(debug=True)
