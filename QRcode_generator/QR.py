from _tkinter import *
from tkinter import Entry,Button, Label, Tk
import qrcode


def generate_qr():
    link=entry.get()
    QR=qrcode.QRCode(
        version=15,
        box_size=10,
        border=5
    )
    QR.add_data(link)
    QR.make(fit=True)
    img=QR.make_image(fill="black", back_color="white")
    img.save("test1.png")

root = Tk()

label = Label(root, text="Enter the link:")
label.pack()

entry = Entry(root, bg="lightgrey", fg="black", font=("Arial", 12))
entry.pack()

button = Button(root, text="Generate QR Code", command=generate_qr, bg="green", fg="white", font=("Arial", 12), padx=20, pady=10, border=5)
button.pack()

root.mainloop()

#Alternative way without GUI


#import qrcode
# import image
# QR=qrcode.QRCode(
#     version=15, #To signify the version of the QRCode. Higher versions ==ability to make more complex images
#     box_size=10, #size of box of QRcode
#     border=5 #for the images' white border 
# )
# link=input("Please enter the link to convert") #include any path of your choice which you want to become a QRcode
# QR.add_data(link)
# QR.make(fit=True)
# img =QR.make_image(fill="black", back_color ="white")
# img.save("test.png")