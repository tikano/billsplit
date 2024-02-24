## README

## Summary

We are Team 95 BillSplit. Our project is web app that allows you to upload an image of a receipt, the number of people involved in the tab, and their contacts. This app will automatically read your bill, split the bill, and notify through SMS message everyone how much they owe to who. 

Our project has two different versions as well: the main repository that uses Google OCR and a keras-version branch that uses Keras OCR.

For more details see project propsal: https://docs.google.com/document/d/1w41AvJ0Jwp_2t1rPL3KkX_QBVD7O9bImcilpwYTdDh8/edit?usp=sharing


## Installation Instructions

Clone the repo to your local.

First, create a virtual env folder by running `python -m venv env`

Then to activate the local environment run `source env/bin/activate`

Install the required packages by running `pip install -r requirements.txt`

To run the ocr library, you will need to follow authentication instructions found here: https://cloud.google.com/functions/docs/tutorials/ocr

Then start the backend server with `flask run`

Open `index.html` in your preferred browser and you will be able to interact with the application!

To run test cases, run `pytest test.py`

To switch to keras-verson use `git checkout keras-version`

## Group Members

Every one worked on both the front and back ends but here is something we all specifically took to do ourselves in addition to that.

Chris Varghese: Implemente google cloud vision

Chris Wang: Wireframe and test cases

Om Desai: Implementing Keras
