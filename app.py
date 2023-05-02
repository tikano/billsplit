from receipt_ocr import get_receipt_text
from text_dection import detect_text
from flask import Flask, request

app = Flask(__name__)

file_name = '/Users/chrisv/Desktop/CS 222/course-project-team95-billsplit/sample_receipt_1.jpg'

@app.route('/')
def main():
    text = get_receipt_text(file_name)
    return text

#text = get_receipt_text(file_name)
#print(text)

#detect_text(file_name)

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if an image was uploaded
    if 'image' not in request.files:
        return 'No image file found', 400

    # Get the uploaded image file
    file = request.files['image']

    # TODO: Use Google OCR library to process the image
    text = get_receipt_text(file)
    return text, 200

    # Return a success response
    # return 'Image uploaded successfully', 200

if __name__ == '__main__':
    app.run(debug=True)

