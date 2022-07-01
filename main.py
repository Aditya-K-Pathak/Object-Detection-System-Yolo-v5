# Inbuilt Libraries =============================
import os
from tkinter import *
from tkinter import messagebox as tmsg
from PIL import Image, ImageTk

# User defined Libraries =============================
import command as cmd
import Image_Window as NewWin
import Voice_Assistance as Va
import speech

# Function Definition For Image Window File =============================
def find():
    root.destroy()
    NewWin.create()


# Function Definition For Voice Command File =============================
def listen():
    root.destroy()
    Va.listen()

# Function to open File Explorer =====================
def open_explorer():
    import easygui
    easygui.fileopenbox()


# Function to stop program ===================
def exit():
    root.destroy()

# Function for help button ====================
def help():
    tmsg.showinfo()
    content = ""
    with open("help.txt") as file:
        content += file.read()
    speech.speak(content)

# Function to respond on clicking info Button =============================
def show():
    try:
        speech.speak("Opening Information of Project")
        res = ""
        with open("About.txt") as abt:
            res += abt.read()
            speech.speak(res)
    except:
        tmsg.showerror("Network Connection Error", 
        "Please Check your Internet Connection...")
    os.system("ABOUT.pdf")


root = Tk()
# Main screen Adjustment =============================
root.title("Object Detection System")  # Title of main window
root.geometry("1104x615")  # Dimension of main windows

# Fixing dimension of main windows
root.minsize(1104, 615)
root.maxsize(1104, 615)

# Window's Icon ======================
root.iconbitmap('Resources/icon.ico')

# Background Image for main window=============================
image = Image.open("Resources/bg.jpg")
pic = ImageTk.PhotoImage(image)
label = Label(image=pic)
label.place(x=0, y=0)

# Button for live or Real_Time_Object_Detection file=============================
B1 = Button(text=" Live Object Detection", 
    width=30, command=cmd.start_webcam)
B1.place(x=786, y=424)

# Button for Image_Window file=============================
B2 = Button(text="Image Based Object Detection",
    width=30, command=find)
B2.place(x=786, y=545)

# Button for Voice_Assistance file=============================
B3 = Button(text="   🎙️", font=("Helvetica", 20), command=listen)
B3.place(x=40, y=350)

# Info Button ==========================
info_button = Image.open("Resources/info.png")
info_button_ = ImageTk.PhotoImage(info_button)
Button(image = info_button_, command = show).place(x=1050, y=50)

# Menubar ============================
mbar=Menu(root)
m1=Menu(mbar)
m1.add_command(label="Open file", command = open_explorer)
m1.add_command(label="Exit", command = exit)
root.config(menu=mbar)
mbar.add_cascade(label="File",menu=m1)

m2=Menu(mbar)
m2.add_command(label="Help",command=help)
root.config(menu=mbar)
mbar.add_cascade(label="Help",menu=m2)

# Welcome Note ==========================
try:
    speech.speak("Welcome to Voice Command based Object Detection System...")
except Exception as e:
    tmsg.showerror("Network Connection Error",
        f"Please Check your Internet Connection...\nDetail: {e}")
    # root.destroy()

root.mainloop()
