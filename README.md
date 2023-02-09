# Pytesseract-OCR (OpenCV Tkinter)

Allows upload of an image for OCR using Tesseract and deployed using Tkinter.  This uses Tkinter, a Python GUI framework based on Tcl/Tkl.   OpenCV is used to reduce noise in the image for better processing by pytesseract. Below are 3 images of a job posting taken on a Pixel 2XL phone, and reduced in size using Gimp by adjusting quality. 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
For Windows 10, Tesseract must be installed - you can find installer here:
* [Tesseract Window 10 Installers](https://github.com/UB-Mannheim/tesseract/wiki)


### Installing and Running
```
For ImageTk
$ sudo apt-get update
Install OpenCV
$ sudo apt-get install python3-pil.imagetk
$ pip install opencv-python 
$ pip install opencv-contrib-python
Install Tesseract/Pytesseract
$ sudo apt install tesseract-ocr
$ sudo apt install libtesseract-dev
$ pip install pytesseract
```


## Built With
```
Python
Tkinter
Pytesseract
OpenCV
```
