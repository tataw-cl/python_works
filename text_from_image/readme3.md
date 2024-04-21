# Image to Text Converter

This is a simple Python program that converts an image into text using Optical Character Recognition (OCR).

## Dependencies

This program uses the following Python libraries:

- pytesseract: An OCR tool for Python that uses Tesseract.
- PIL (Pillow): A library for opening, manipulating, and saving many different image file formats.
  You also need to install Tesseract, which is the OCR engine used by pytesseract. You can download it from the [official website](https://github.com/UB-Mannheim/tesseract/wiki) and install it. After installation, you need to provide the path to the Tesseract executable in your script: should look something like this `pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"` //Replace the path with the correct path where you installed Tesseract.

## Installation

Before running the program, you need to install the required Python libraries. You can do this with pip:

```bash
pip install pytesseract pillow
```

```bash
  pip install opencv-python
```

## Usage

To use the program, you need to have an image file with some text on it. The image file should be in the same directory as the script, or you need to provide the full path to the image file.

Run the script in the terminal with: `python reader.py`
