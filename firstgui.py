# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:06:31 2019

@author: INDERSINGH
"""

#GUI PROJECT
import tkinter as Tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import os
global filename
#import color2
global brown_c
import cv2
import datetime
import sys
import time
import subprocess
import numpy as np
from skimage import *
from scipy import ndimage
from scipy.ndimage import *
import array
from scipy import asarray, ones, vstack, hstack
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
os.remove("report.txt")
f= open("report.txt","w+")
f.write("This is automatically generated report of grain analyser\n\n")
currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M")
f.write("Date and time:"+str(currentdate)+"\n\n")
f.close()
def click():
    #win2 = Toplevel()
   # win2.geometry("600x250")
    #Label (win2, text = "Please connect webcam",bg="white",fg="black",font="none 14 bold") .grid(row=0,column=0,sticky=W)
    #os.system('python captureoriginalimage.py')
    #DATE=$(/date +"%Y-%m-%d_%H%M%S")
    #now = datetime.datetime.now()
    
    #fswebcam -r 1280x720 --no-banner /home/pi/Desktop/MEproject/captureimages/image.jpg
    #chmod +x webcam.sh
    #./webcam.sh
    #fswebcam image.jpg
    # read the absolute path
    script_dir = os.path.dirname(os.path.abspath(__file__))
# call the .sh to capture the image
    #chmod +x webcam.sh
    os.system('./webcam.sh')
#get the date and time, set the date and time as a filename.
    currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
# create the real path
    rel_path = currentdate +".jpg"
#  join the absolute path and created file name
    abs_file_path = os.path.join(script_dir, rel_path)
    print (abs_file_path)
    
    class App(Frame):
        def __init__(self, master):
            Frame.__init__(self, master)
            self.grid(row=0)
            self.columnconfigure(0,weight=1)
            self.rowconfigure(0,weight=1)
            self.original = Image.open(abs_file_path)
            resized = self.original.resize((300, 200),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized) # Keep a reference, prevent GC
            self.display = Label(self, image = self.image)
            self.display.grid(row=0)
    #img = ImageTk.PhotoImage(Image.open('snapshot100.png'))      
   # Label (root, image=img) .grid(row=0,column=1,sticky=E)    
    #mainloop()
    root = Toplevel()
    app = App(root)
    app.mainloop()
    
    
    #img111 = ImageTk.PhotoImage(Image.open(abs_file_path))      
    #Label (win2, image=img111) .grid(row=0,column=0,sticky=E)    
    #label1 = Label(image=img111)
    #label1.image = img111 # keep a reference!
    #label1.pack()
    #fswebcam image10.jpg
    mainloop()
def load():
    global filename
    
    #win3.geometry("600x250")
    
    #pathlabel.pack()
    
    filename = filedialog.askopenfilename(filetypes =(("Files","*.*"),))
    img = cv2.imread(filename)
    cv2.imwrite('selected.png',img)
    #win3 = Toplevel()
   # pathlabel = Label(win3)
   # pathlabel.config(text=filename) 
    #filename = filenam
    #self.controller = filenam
   
    class App(Frame):
        def __init__(self, master):
            Frame.__init__(self, master)
            self.grid(row=0)
            self.columnconfigure(0,weight=1)
            self.rowconfigure(0,weight=1)
            self.original = Image.open(filename)
            resized = self.original.resize((300, 200),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized) # Keep a reference, prevent GC
            self.display = Label(self, image = self.image)
            self.display.grid(row=0)
    #img = ImageTk.PhotoImage(Image.open('snapshot100.png'))      
   # Label (root, image=img) .grid(row=0,column=1,sticky=E)    
    #mainloop()
    root = Toplevel()
    app = App(root)
    app.mainloop()
    
   
   
   # img222 = ImageTk.PhotoImage(Image.open(filename))      
   # Label (win3, image=img222) .grid(row=0,column=0,sticky=E)    
   # label1 = Label(image=img222)
   # label1.image = img222 # keep a reference!
    #label1.pack()
    img = cv2.imread(filename)
    cv2.imwrite('selected.png',img)
    mainloop()
def view():
    global filename
    #root = Toplevel()
    #root.geometry("1280x720")
    
    class App(Frame):
        def __init__(self, master):
            Frame.__init__(self, master)
            self.grid(row=0)
            self.columnconfigure(0,weight=1)
            self.rowconfigure(0,weight=1)
            self.original = Image.open(filename)
            resized = self.original.resize((300, 200),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized) # Keep a reference, prevent GC
            self.display = Label(self, image = self.image)
            self.display.grid(row=0)
    #img = ImageTk.PhotoImage(Image.open('snapshot100.png'))      
   # Label (root, image=img) .grid(row=0,column=1,sticky=E)    
    #mainloop()
    root = Toplevel()
    app = App(root)
    app.mainloop()
    
   
    
    #img = ImageTk.PhotoImage(Image.open(filename))      
   # Label (root, image=img) .grid(row=0,column=1,sticky=E)    
    mainloop() 
def landw():
    #
    os.system('python leng_wid.py')
    win10 = Toplevel()
    #win10.geometry('%sx%s' % (width, height))
    f2= open("lengthwidth.txt","r")
    arg=f2.read()
    f2.close()
    Label (win10, text = arg ,bg="white",fg="black",font="none 7 ") .grid(row=0,column=0,sticky=W+E)
    #scrollbar = Scrollbar(win10)
    #scrollbar.grid( side = RIGHT )
def colourcal():
    
    global filename
    os.system('python color2.py')
    f2= open("colourinfo.txt","r")
    arg=f2.read()
    f2.close()
    win11 = Toplevel()
    Label (win11, text = arg,bg="white",fg="black",font="none 7") .grid(row=0,column=0,sticky=W+E)

def gradeassign():
    win12 = Toplevel()
    global var1 
    global var2
    global var3
    global var4
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    Label (win12, text = "Select the Standard",bg="white",fg="black",font="none 14 bold") .grid(row=0,column=0,sticky=W)
    c1 = Checkbutton(win12, text = "DMI", variable=var1) .grid(column=0, row=1, sticky=W)
    c2 = Checkbutton(win12, text = "Cambodia", variable=var2) .grid(column=0, row=2, sticky=W)
    c3 = Checkbutton(win12, text = "ARSO", variable=var3) .grid(column=0, row=3, sticky=W)
    c4 = Checkbutton(win12, text = "CODEX", variable=var4) .grid(column=0, row=4, sticky=W)
    Button(win12, text = "Submit", command=mget) .grid(column=0, row=5, sticky=E)
def mget():
    global brown_c
    global var1
    global var2
    global var3
    global var4
    global a_length
    a_length = list()
    img = "bw_image.png"
    bw = cv2.imread(img, True)
    labeled, n = label(bw)
    ndimage.find_objects(labeled, max_label=n)
    for i in range (n):
        props = measure.regionprops(labeled)
    props = iter(props)
    next(props)
    for prop in props:
        a_len = prop.major_axis_length/10.31
        a_length.append(a_len)
    #print(var1.get(),var2.get(),var3.get())
    if (var1.get() == 1):
        #global brown_c
        print("DMI CLASSIFICATION")
        f= open("report.txt","a+")
        f.write("\n\n -----DMI CLASSIFICATION-----  \n")
        

        broken_b = 0
        brown_c = 0
        B_mean1 = list()
        G_mean1 = list()
        R_mean1 = list()
        for i in range (len(a_length)):
            if (0 < a_length[i] < 7.5):
                    broken_b = broken_b + 1
        print("number of broken seeds less than 7.5",broken_b)
        bro_per = (broken_b/(len(a_length)))*100
        print("Percentage of Broken Seeds:",bro_per)
        f.write("\n Percentage of Broken Seeds:"+str(bro_per)+"\n")
        for i in range (len(a_length)):
            if (i > 0):
                rel_path = "c" + str(i) + ".png"
                re_img1 = cv2.imread(rel_path)
                b, g, r = cv2.split(re_img1)
                ttl = re_img1.size 
                imge1 = Image.open(rel_path)
                pix_val = list(imge1.getdata())
                pix_val_flat = [x for sets in pix_val for x in sets]
                for k in range (len(pix_val_flat)):
                    if (pix_val_flat[k] == 0):
                        ttl = ttl - 1
                B = float(np.sum(b)) / ttl #convert to float, as B, G, and R will otherwise be int
                G = float(np.sum(g)) / ttl
                R = float(np.sum(r)) / ttl
                B_mean1.append(B)
                G_mean1.append(G)
                R_mean1.append(R)
        for m in range (len(B_mean1)):
            if (B_mean1[m] > 56): #78
                rel_path_colour = "seed no." + str(m+1) + ":white"
               # print(rel_path_colour)
            else:
                rel_path_colour = "seed no." + str(m+1) + ":brown"
                brown_c = brown_c + 1
        dis_colo_perc = (brown_c/(len(a_length)))*100
        print("Percentage of discolored grain:",dis_colo_perc)
        f.write("\n Percentage of discolored grain:"+str(dis_colo_perc)+"\n")

        if (bro_per < 5 and dis_colo_perc < 2.5):
            print("Result : Raw milled grade I")
            f.write("\n Result : Raw milled grade I")
        elif (bro_per < 10 and dis_colo_perc < 5):
            print("Result : Raw milled grade II")
            f.write("\n Result : Raw milled grade II")
        elif (bro_per < 15 and dis_colo_perc < 10):
            print("Result : Raw milled grade III")
            f.write("\n Result : Raw milled grade III")
        elif (bro_per < 25 and dis_colo_perc < 40):
            print("Result : Raw milled grade IV")
            f.write("\n Result : Raw milled grade IV")
        elif (dis_colo_perc < 50 and bro_per > 60 ):
            print("Result : Broken Basmati Grade I")
            f.write("\n Result : Broken Basmati Grade I")
        elif (dis_colo_perc < 70 and bro_per > 60 ):
            print("Result : Broken Basmati Grade II")
            f.write("\n Result : Broken Basmati Grade II")
        elif (dis_colo_perc < 100 and bro_per < 60 ):
            print("Broken Basmati Grade III")
            f.write("\n Result : Broken Basmati Grade III")
        else:
            print("No grade is assigned")
            f.write("\n Result : SAMPLE REJECTED AND NO GRADE IS ASSIGNED")
        f.close()
    if (var2.get() == 1):
        f= open("report.txt","a+")
        f.write("\n\n\n -----CAMBODIA CLASSIFICATION-----  \n")
        print("CAMBODIA CLASSIFICATION")
       # i = 0
        whole = 0
        head = 0
        broken = 0
        for i in range (len(a_length)):
            if (9 < a_length[i] < 200):
                whole = whole +1
                #i = i + 1
            elif (8 < a_length[i] < 9):
                head = head + 1
                #i = i + 1
            else:
                broken = broken + 1
                #i = i + 1
        print("No. of Whole Seeds:",whole)
        f.write("No. of Whole Seeds:"+str(whole)+"\n")
        print("No. of Head Seeds:",head)
        f.write("No. of Head Seeds:"+str(head)+"\n")
        print("No. of Broken Seeds:",broken)
        f.write("No. of Broken Seeds:"+str(broken)+"\n")
        f.close()
        #m = 0
        #for prop in props:
           # print('Label: {} >> Seed Area: {} >> Length: {} >> Width: {}'.format(m+1,(prop.major_axis_length/10.31)*(prop.minor_axis_length/10.31)  , prop.major_axis_length/10.31, prop.minor_axis_length/10.31))
        #print(broken)
 
    if (var3.get() == 1):
        print("ARSO CLASSIFICATION")
        f= open("report.txt","a+")
        f.write("\n\n -----ARSO CLASSIFICATION-----  \n")
        whole = 0
        head = 0
        lbroken = 0
        mbroken = 0
        sbroken = 0
        for i in range (len(a_length)):
            if (9 < a_length[i] < 200):
                whole = whole +1
                #i = i + 1
            elif (7.5 < a_length[i] < 9):
                head = head + 1
                #i = i + 1
            elif (5 < a_length[i] < 7.5):
                lbroken = lbroken + 1
            elif (2.5 < a_length[i] < 5):
                mbroken = mbroken + 1
            else:
                sbroken = sbroken + 1
                #i = i + 1
        print("No. of Whole Seeds:",whole)
        f.write("No. of Whole Seeds:"+str(whole)+"\n")

        print("No. of Head Seeds:",head)
        f.write("No. of Head Seeds:"+str(head)+"\n")

        print("No. of Large Broken Seeds:",lbroken)
        f.write("No. of Large Broken Seeds:"+str(lbroken)+"\n")

        print("No. of Medium Broken Seeds:",mbroken)
        f.write("No. of Medium Broken Seeds:"+str(mbroken)+"\n")

        print("No. of Small Broken Seeds:",sbroken)
        f.write("No. of Small Broken Seeds:"+str(sbroken)+"\n")

        f.close()
    if (var4.get() == 1):
        print("CODEX CLASSIFICATION")
        f= open("report.txt","a+")
        f.write("\n\n -----CODEX CLASSIFICATION-----  \n")
        long = 0
        medium = 0
        short = 0
        for i in range (len(a_length)):
            if (6.6 < a_length[i] < 200):
                long = long +1
                #i = i + 1
            elif (6.2 < a_length[i] < 6.6):
                medium = medium + 1
                #i = i + 1
            else:
                short = short + 1
        print("No. of long Seeds:",long)
        f.write("No. of long Seeds:"+str(long)+"\n")

        print("No. of medium Seeds:",medium)
        f.write("No. of medium Seeds:"+str(medium)+"\n")
        
        print("No. of short Seeds:",short)
        f.write("No. of short Seeds:"+str(short)+"\n")
        f.close()
def e_mail():
    os.system('python mailsec.py')
def identify():
    os.system('python co_ordinate.py')
def viewresult():
    win13 = Toplevel()
    f5= open("report.txt","r")
    arg=f5.read()
    f5.close()
    Label (win13, text = arg,bg="white",fg="black",font="none 7") .grid(row=0,column=0,sticky=W+E)
def transferim():
    win16 = Toplevel()
    Label (win16, text = "Use VNC file transfer function",bg="white",fg="black",font="none 10") .grid(row=0,column=0,sticky=W+E)
    
def capturemulti():
    win15 = Toplevel()
    Label (win15, text = "Please Wait!!!",bg="white",fg="red",font="none 10") .grid(row=0,column=0,sticky=W+E)
    os.system('python motor_1.py')
    Button(win15, text = "Transfer images",width=50, command=transferim) .grid(column=0, row=0, sticky=E)
def VisualSFMproce():
    win18 = Toplevel()
    f7= open("visualpro.txt","r")
    visualpr=f7.read()
    f7.close()
    Label (win18, text = visualpr,bg="white",fg="black",font="none 10") .grid(row=1,column=0,sticky=W)
def Meshlabproce():
    win19 = Toplevel()
    f8= open("meshlabpro.txt","r")
    meshlabpr=f8.read()
    f8.close()
    Label (win19, text = meshlabpr,bg="white",fg="black",font="none 10") .grid(row=1,column=0,sticky=W)

def steps3d():
    win17 = Toplevel()
    Label (win17, text = "For detailed procedure of VisualSFM and Meshlab Click following buttons:",bg="white",fg="black",font="none 10") .grid(row=0,column=0,sticky=W+E)
    Button(win17, text = "VisualSFM Steps",width=52, command=VisualSFMproce) .grid(column=0, row=1, sticky=W)
    Button(win17, text = "Meshlab Steps",width=52, command=Meshlabproce) .grid(column=0, row=2, sticky=W)
def meshresult():
    #root = Toplevel()
    #photologo = PhotoImage(file="logo3.GIF")
    class App(Frame):
        def __init__(self, master):
            Frame.__init__(self, master)
            self.grid(row=0)
            self.columnconfigure(0,weight=1)
            self.rowconfigure(0,weight=1)
            self.original = Image.open('snapshot100.JPG')
            resized = self.original.resize((300, 200),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized) # Keep a reference, prevent GC
            self.display = Label(self, image = self.image)
            self.display.grid(row=0)
    #img = ImageTk.PhotoImage(Image.open('snapshot100.png'))      
   # Label (root, image=img) .grid(row=0,column=1,sticky=E)    
    #mainloop()
    root = Toplevel()
    app = App(root)
    app.mainloop()
    #root.destroy()
    
def reconstructfunc():
    win14 = Toplevel()
    Button(win14, text = "Capture Multiple Images",width=50, command=capturemulti) .grid(column=0, row=0, sticky=E)
    Button(win14, text = "Build 3D",width=50, command=steps3d) .grid(column=0, row=1, sticky=E)
    Button(win14, text = "View Final output",width=50, command=meshresult) .grid(column=0, row=2, sticky=E)

def analyze():
    win4 = Toplevel()
    Button(win4, text = "Run Preprocessing Algorithm",width=50, command=preprocess) .grid(column=0, row=0, sticky=E)
    Button(win4, text = "Calculate Length and Width",width=50, command=landw) .grid(column=0, row=1, sticky=E)
    Button(win4, text = "Estimate Colour",width=50, command=colourcal) .grid(column=0, row=2, sticky=E)
    Button(win4, text = "Check Grade",width=50, command=gradeassign) .grid(column=0, row=3, sticky=E)
    Button(win4, text = "View Results",width=50, command=viewresult) .grid(column=0, row=4, sticky=E)
    Button(win4, text = "Identify position of brown grain ",width=50, command=identify) .grid(column=0, row=6, sticky=E)
    Button(win4, text = "Send an E-mail ",width=50, command=e_mail) .grid(column=0, row=5, sticky=E)
    Button(win4, text = "3D Reconstruction",width=50, command=reconstructfunc) .grid(column=0, row=7, sticky=E)

def preprocess():
    win5 = Toplevel()
    Button(win5, text = "View Original Image",width=15, command=ogclick) .grid(columnspan=2, rowspan=2, sticky=E+W)
    Button(win5, text = "View Gray Scale Image",width=15, command=inclick) .grid(columnspan=2, rowspan=2, sticky=E+W)
    #Button(win5, text = "View Improved Contrast Image",width=20, command=conclick) .grid(columnspan=2, rowspan=2, sticky=E+W)
    Button(win5, text = "View Binary Image",width=25, command=biclick) .grid(columnspan=2, rowspan=2, sticky=E+W)
def ogclick():
    #win6 = Toplevel()
    global filename
    
    class App(Frame):
        def __init__(self, master):
            Frame.__init__(self, master)
            self.grid(row=0)
            self.columnconfigure(0,weight=1)
            self.rowconfigure(0,weight=1)
            self.original = Image.open(filename)
            resized = self.original.resize((300, 200),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized) # Keep a reference, prevent GC
            self.display = Label(self, image = self.image)
            self.display.grid(row=0)
    #img = ImageTk.PhotoImage(Image.open('snapshot100.png'))      
   # Label (root, image=img) .grid(row=0,column=1,sticky=E)    
    #mainloop()
    root = Toplevel()
    app = App(root)
    app.mainloop()
    
    
    #img = ImageTk.PhotoImage(Image.open(filename))      
    #Label (win6, image=img) .grid(row=0,column=0,sticky=E)    
    #label1 = Label(image=img)
    #label1.image = img # keep a reference!
    #label1.pack()

def inclick():
    global filename
    #win7 = Toplevel()
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img1 = cv2.imread(img)
    #equ = cv2.equalizeHist(gray)
    #intens = np.hstack((gray,equ)) #stacking images side-by-side
    cv2.imwrite('intansity.png',gray)
    
    class App(Frame):
        def __init__(self, master):
            Frame.__init__(self, master)
            self.grid(row=0)
            self.columnconfigure(0,weight=1)
            self.rowconfigure(0,weight=1)
            self.original = Image.open('intansity.png')
            resized = self.original.resize((300, 200),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized) # Keep a reference, prevent GC
            self.display = Label(self, image = self.image)
            self.display.grid(row=0)
    #img = ImageTk.PhotoImage(Image.open('snapshot100.png'))      
   # Label (root, image=img) .grid(row=0,column=1,sticky=E)    
    #mainloop()
    root = Toplevel()
    app = App(root)
    app.mainloop()
    
    
    #intens = PhotoImage(file="intansity.png")
    #Label (win7, image=intens) .grid(row=1,column=1,sticky=W)    
    #label2 = Label(image=intens)
    #label2.image = intens # keep a reference!
    #label2.pack()
def conclick():
    win8 = Toplevel()
    hicon = ImageTk.PhotoImage(Image.open("High_contrast.jpg"))      
    Label (win8, image=hicon) .grid(row=0,column=0,sticky=E)    
    label3 = Label(image=hicon)
    label3.image = hicon # keep a reference!
    label3.pack()
def biclick():
    #win9 = Toplevel()
    im_gray = cv2.imread('intansity.png', cv2.IMREAD_GRAYSCALE)
    (thresh, biimg) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    #biimg = ImageTk.PhotoImage(Image.open("binary_image.jpg"))      
    cv2.imwrite('bw_image.png', biimg)
    
    class App(Frame):
        def __init__(self, master):
            Frame.__init__(self, master)
            self.grid(row=0)
            self.columnconfigure(0,weight=1)
            self.rowconfigure(0,weight=1)
            self.original = Image.open('bw_image.png')
            resized = self.original.resize((300, 200),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized) # Keep a reference, prevent GC
            self.display = Label(self, image = self.image)
            self.display.grid(row=0)
    #img = ImageTk.PhotoImage(Image.open('snapshot100.png'))      
   # Label (root, image=img) .grid(row=0,column=1,sticky=E)    
    #mainloop()
    root = Toplevel()
    app = App(root)
    app.mainloop()
    #root.destroy()
    
    #biimg = PhotoImage(file="bw_image.png")
    #Label (win9, image=biimg) .grid(row=0,column=0,sticky=E)    
    #label4 = Label(image=biimg)
    #label4.image = biimg # keep a reference!
    
    #label4.pack()
 # main
window = Tk()
window.title("Rice Quality Analyser")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry('%sx%s' % (width, height))
#window.geometry("900x250")
window.configure(background = "white")
#Text
Label (window, text = "WELCOME TO RICE QUALITY ANALYZER",bg="white",fg="black",font="none 11 bold") .grid(row=0,column=0,sticky=W)
# logo
#PhotoImage.zoom(25,35)
photologo = PhotoImage(file="logo3.GIF")

Label (window, image=photologo) .grid(row=0,column=1,sticky=E)
#l.pack()

##CREATE A BUTON
Button(window, text = "Capture Image",width=15, command=click) .grid(row=2, column=0, sticky=W)
Button(window, text = "Load Image",width=15, command=load) .grid(row=2, column=1, sticky=E)
Button(window, text = "View Loaded Image",width=20, command=view) .grid(row=4, column=1, sticky=E)
Button(window, text = "Run Analyzer",width=25, command=analyze) .grid(columnspan=2, rowspan=2, sticky=E+W)

mainloop()