import pyautogui as pag
from tkinter import *
import time 
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
def takeScreenshot ():
    
    myScreenshot = pag.screenshot()
    myScreenshot.save(r'C:\Users\manav\Desktop\test.png')
    time.sleep(1)
    file=open("test.txt","w")
    file.write(ocr_core(r'C:\Users\manav\Desktop\test.png'))
    file.close()


  


root= Tk()
root.title("Copy It!")

myButton = Button(root,text='Take Screenshot', command=takeScreenshot, bg='red',fg='white',font= 10)
myButton.pack()


root.mainloop()