# Inbuilt Libraries =============================
from tkinter import *
import speech
from tkinter import messagebox as tmsg
from PIL import Image, ImageTk

# User defined Libraries =============================
import command as cmd


def create():
    root1 = Tk()
    # Window's Detailing ============================= 
    root1.title("Image Based Object Detection")
    root1.geometry("1104x615")
    root1.minsize(1104, 615)
    root1.maxsize(1104, 615)

    # forward function invoked whenever "Find" Button is pressed
    def forward():
        path = e1.get()
        try:
            # try block to check if file is present
            cmd.start_scan(path)
        except:
            # shows file not found Error if no file is found
            tmsg.showerror("File Not Foud", f"No such file exist in path\n{path}")
        root1.destroy  # Destroys the window even if file is found or not

    # Function to open File Explorer =====================
    def open_explorer():
        import easygui
        easygui.fileopenbox()


    # Function to stop program ===================
    def exit():
        root1.destroy()


    def help():
        tmsg.showinfo()
        content = ""
        with open("help.txt") as file:
            content += file.read()
        speech.speak(content)

    # Adds Frame for easy updating =============================
    C1 = LabelFrame(root1, background="black", width=1104, height=615)
    C1.place(x=0, y=0)

    # Background Image =============================
    image = Image.open("Resources/object_background.jpg")
    pic = ImageTk.PhotoImage(image)
    Label(C1, image=pic).place(x=0, y=0)

    # Entry Box =============================
    e1 = StringVar()
    a = Entry(textvariable=e1, width=50)
    a.place(x=786, y=424)
    a.insert(0, "File Path")

    # Find Button to check for file =============================
    Button(C1, text="Find", command=forward).place(x=900, y=444)

    mbar=Menu(root1)
    m1=Menu(mbar)
    m1.add_command(label="Open file", command = open_explorer)
    m1.add_command(label="Exit", command = exit)
    root1.config(menu=mbar)
    mbar.add_cascade(label="File",menu=m1)

    m2=Menu(mbar)
    m2.add_command(label="Help",command=help)
    root1.config(menu=mbar)
    mbar.add_cascade(label="Help",menu=m2)

    root1.mainloop()
