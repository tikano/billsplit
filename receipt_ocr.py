import io
import os
from google.cloud import vision
from PIL import Image;
import matplotlib.pyplot as plt
import numpy as np;
import cv2;

import keras_ocr;

model = keras_ocr.pipeline.Pipeline();


def get_text_from_file(file):
    """
    client = vision.ImageAnnotatorClient()

    content = file.read()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    text = response.text_annotations[0].description

    return text
    """
    newimage = file;
    
    
    with open("image.png", 'wb') as f:
        f = file;
    
    filearray = [newimage]
    prediction = model.recognize(filearray)
    print(prediction)
    
    filearray = [np.asarray(Image.open(file))];
    fig, axs = plt.subplots(nrows=len(filearray), figsize=(20, 20))
    axs = [axs]
    for ax, img, predictions in zip(axs, filearray, prediction):
        keras_ocr.tools.drawAnnotations(image=img, predictions=predictions, ax=ax)
    fig.savefig("plot.png")
    max = 0
    newstring = ""
    for word, box in prediction[0]:
        if (word == "total" or word == "amount") and box[0][1] > max:
            max = box[0][1]
    for word, box in prediction[0]:
        if abs(box[0][1] - max) < 20:
                if(word.isnumeric()):
                    newstring = newstring + word
                elif(word[1:].isnumeric()):
                    newstring = newstring + word[1:]
                          
    val = int(newstring)/100.0
        
    text = "The total bill is $" + str(val)
    return text
    

def get_receipt_text(file_name):
    """Extracts text from a receipt image using Google Cloud OCR API.
    Args:
        file_name: A string representing the file name (including path) of the receipt image.
    Returns:
        A string containing the extracted text from the receipt image.
    """
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Performs OCR on the image and extracts text
    response = client.text_detection(image=image)
    text = response.text_annotations[0].description

    return text
