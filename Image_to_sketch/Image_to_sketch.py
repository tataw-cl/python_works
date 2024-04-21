import cv2
# Ask the user for the image file name
#image_file = input("Please enter the image file name in this same location: ")
import tkinter as tk
from tkinter import filedialog
#Create a Tkinter root widget
root=tk.Tk()
root.withdraw()  #Hide the root widget

#open a file dialog and get the file name
image_file=filedialog.askopenfilename()

img = cv2.imread(image_file)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert_img = cv2.bitwise_not(grey_img)
blur_img = cv2.GaussianBlur(invert_img, (21,21),0)
inverted_blur = cv2.bitwise_not(blur_img)
sketch = cv2.divide(grey_img, inverted_blur, scale=256.0)
cv2.imwrite("your_pic.png", sketch)