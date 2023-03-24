import io
import os
from google.cloud import vision

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
