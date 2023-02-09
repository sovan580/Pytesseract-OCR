# import tkinter import  all the functions and built-in modules in the tkinter library
from tkinter import *
  
# import filedialog module
from tkinter import filedialog

# Need to install opencv and pytesseract
import cv2                   # Import OpenCV
import pytesseract           # Import Pytesseract

# Path for the Tessseract-OCR in system files according to installation in system
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract' 

# Global variable for Image Path 
imagePath=''

# Function to browse for image files in system
def browseFiles():
    global imagePath
    imagePath = filedialog.askopenfilename(defaultextension="*.jpg", filetypes = (("JPG", "*.jpg"),("PNG","*.png")))
 
    browse_entry.delete(0, END)
    browse_entry.insert(0, imagePath) 

# Function for generation of text and writing it to a text file      
def generateText():
    #   Image Reading using OpenCv
    image = cv2.imread(imagePath)
   
    # Pre-processing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)        # Convert imgae to gray scale image
    gray = cv2.medianBlur(gray, 3)                        # Blur the image

    # Pass the image to Py-tesseract
    text = pytesseract.image_to_string(gray)

    # Write the text to a file named as Extracted.txt file
    file = open(r'C:\Users\Ankit\OneDrive\Desktop\OCR\Extracted.txt', 'w')
    file.write(text)
    file.close()
    print(text)    

##############################################################################################################################  
######################################################  Creation of GUI ######################################################   
##############################################################################################################################  
                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('OCR Converter')
  
# Set window size
window.geometry("300x300")
# set minimum window size value
window.minsize(400, 400)
 
# set maximum window size value
window.maxsize(400, 400)
  
#Set window background color
window.config(background = "white")
  
# Creating UI elements
label_file_explorer = Label(window,text = "OCR Using Tesseract",fg="#fff",bg = "#000",font='Arial 17 bold')    
button_browse = Button(window,text = "Browse Image Files",command = browseFiles,bg = "#0087D5",fg="#fff") 
button_generate = Button(window,text = "Generate Text File",command = generateText,bg = "#0087D5",fg="#fff")
select_label=Label(window,text="Select Image :", font=("Arial", 10), bg="#fff")
browse_entry=Entry(text="",width=30)

# UI elements placing
browse_entry.place(relx=0.35, rely=0.3,anchor=SW)
select_label.place(relx=0.08, rely=0.3, anchor=SW)
label_file_explorer.place(relx=0.5, rely=0.05, anchor=CENTER)
button_browse.place(relx=0.5, rely=0.5, anchor=CENTER)  
button_generate.place(relx=0.5, rely=0.7, anchor=CENTER)
  
# Let the window wait for any events
window.mainloop()