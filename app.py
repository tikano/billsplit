from receipt_ocr import get_receipt_text
from text_dection import detect_text
from flask import Flask

app = Flask(__name__)

file_name = '/Users/chrisv/Desktop/CS 222/course-project-team95-billsplit/sample_receipt_1.jpg'

@app.route('/')
def main():
    text = get_receipt_text(file_name)
    return text

#text = get_receipt_text(file_name)
#print(text)

#detect_text(file_name)

