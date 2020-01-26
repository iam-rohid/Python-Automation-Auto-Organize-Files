import os
import time
import tkinter as tk
from tkinter import filedialog, Text



root = tk.Tk()
root.title("Organize Your Files")
root.resizable(0, 0)




isfileSelected = False
canvasWidth = 600
canvasHeight = 300
canvasColor = "#272727"
Button1text = "Select Folder"
Button2text = "Organize"


Dir = ""
Audios      =   ["mp3", "wav", "flac", "aac", "aa", "aax", "awb", "dvf", "ogg", "oga", "mpgg", "vox", "wma", "wv", "webm", "pcm", "ac3", "eac3"]
Videos      =   [".mkv", "mp4", "m4a", "m4v", "f4v", "f4a", "m4b", "m4r", "f4b", "mov", "3gp", "3gp2", "3g2", "3gpp", "3gpp2", "ogg", "oga", "ogv", "ogx", "wmv", "wma", "webm", "flv", "vob", "vob"]
Images      =   ["png", "jpg", "jpeg", "svg", "riff"]
Softwares   =   ["exe", "msi", "pkg", "dmg"]
ISO_Files   =   ["iso"]
Compressed_Files   =   ["zip","rar","7z","tar"]
def Button1(text):
    Button1 = tk.Button(frame, text=text, command = SelectFolder, bd=0, bg="#fff", padx = 10, pady = 5, fg = "#414141", font=("none", 12, "normal"), highlightcolor = "#f1f1f1", state = "normal")
    Button1.place(anchor = "n",width = 300, height = 50, relx=0.5, y = 150)

def Button2(text,state,command):
    Button2 = tk.Button(frame, text=text, command = command, bd=0, bg="#fff", padx = 10, pady = 5, fg = "#414141", font=("none", 12, "normal"), highlightcolor = "#f1f1f1", state = state)
    Button2.place(anchor = "n",width = 300, height = 50, relx=0.5, y = 220)

def FileLinkText(text):
    FileLink = tk.Label(frame, text=text, font=("none", 14), fg="#fff", bg = canvasColor)
    FileLink.place(anchor = "n", width=canvasWidth, relx=0.5, y = 70)


def SelectFolder():
    Dir  = ""
    Dir = tk.filedialog.askdirectory(initialdir="C:/", title="Select Folder")
    if(Dir != ""):
        FileLinkText("Folder Name " + (Dir.split("/"))[-1])
        Button1("Select Again")
        Button2("Organize","active",Organize)
        os.chdir(Dir)
        Audios.append(Dir + "/Audio")
        Videos.append(Dir +"/Videos")
        Images.append(Dir +"/Images")
        Softwares.append(Dir +"/Softwares")
        ISO_Files.append(Dir +"/ISO_Files")
        Compressed_Files.append(Dir +"/Compressed_Files")
    elif(Dir == ""):
        FileLinkText("Please select the directory you want me to organize!")
        Button2("Organize","disable",Organize)


def CloseProgram():
    exit()


def Organize():     
    for filename in os.listdir(os.getcwd()):
        if len(filename.split('.')) != 1:
            extention = filename.split('.')[-1]
            if extention in Audios:
                if "Audios" not in os.listdir():
                    os.mkdir("Audios")

                folder_dest = Audios[-1]

            elif extention in Videos:
                if "Videos" not in os.listdir():
                    os.mkdir("Videos")

                folder_dest = Videos[-1]
                
            elif extention in Images:
                if "Images" not in os.listdir():
                    os.mkdir("Images")

                folder_dest = Images[-1]
                
            elif extention in Softwares:
                if "Softwares" not in os.listdir():
                    os.mkdir("Softwares")

                folder_dest = Softwares[-1]
                
            elif extention in ISO_Files:
                if "ISO_Files" not in os.listdir():
                    os.mkdir("ISO_Files")

                folder_dest = ISO_Files[-1]
                
            elif extention in Compressed_Files:
                if "Compressed_Files" not in os.listdir():
                    os.mkdir("Compressed_Files")

                folder_dest = Compressed_Files[-1]

            else:
                if "Others" not in os.listdir():
                    os.mkdir("Others")
                    
                folder_dest = os.curdir + "/Others"

            oldFileName = filename
            while filename in os.listdir(folder_dest):
                filenamearry = filename.split('.')
                filename = filename[0:filename.index('.')] +  " - Copy." + filenamearry[-1]
            
            src = os.getcwd() + '/' + oldFileName
            new_dest = folder_dest + "/" + filename
            os.rename(src, new_dest)
    Button2("Done", "active", CloseProgram)

    


tk.Canvas(root, height=canvasHeight, width=canvasWidth).pack()

frame = tk.Frame(root, bg=canvasColor)
frame.place(relwidth = 1, relheight = 1)

HeaderText = tk.Label(frame, text="Organize Your Files", font=("none", 20, "bold"), fg="#fff", bg = canvasColor)
HeaderText.place(anchor = "n", relx=0.5, y = 20)

Button1("Select Folder")

FileLinkText("Choose a Diractory which you want to organize")

Button2("Organize","disable", Organize)

root.mainloop()