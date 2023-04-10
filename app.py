from receipt_ocr import get_receipt_text
from text_dection import detect_text

file_name = '/Users/chrisv/Desktop/CS 222/course-project-team95-billsplit/sample_receipt_1.jpg'
text = get_receipt_text(file_name)
print(text)

#detect_text(file_name)

