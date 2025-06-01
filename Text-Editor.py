# Text Editor Application
from tkinter import *
from tkinter import Menu 
from tkinter import filedialog as fd

def newFile():
    text_editor.delete("1.0", END)

def openFile():
    file_path = fd.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert(END, text)

def saveFile():
    global current_file_path
    if current_file_path:
        with open(current_file_path, "w") as file:
            text = text_editor.get("1.0", END)
            file.write(text)
    else:
        saveAs()

def saveAs():
    global current_file_path
    file_path = fd.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        current_file_path = file_path
        with open(file_path, "w") as file:
            text = text_editor.get("1.0", END)
            file.write(text)


# Initialize tkinter root and text editor
root = Tk()
text_editor = Text(root)
text_editor.pack()

# Initialize current file path
current_file_path = None

# Create menubar and file menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

# Add commands to file menu
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)

#similar to <hr> or <br>
filemenu.add_separator()       

filemenu.add_command(label="Quit", command=root.quit)
# Add file menu to menubar
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()
