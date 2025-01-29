from tkinter import *
from tkinter import filedialog 
filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename 
    if filename is None:
        saveAs()
    else:
        t = text.get(0.0, END)
        with open(filename, 'w') as f:
            f.write(t)
    
def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if f is not None:
        t = text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title='Error', message='Failed to save the file')

def openFile():
    f = filedialog.askopenfile(mode='r')
    if f is not None:
        t = f.read()
        text.delete(0.0, END)
        text.insert(0.0, t)

def increase_font(event):
    current_size = text.cget("font").split()[-1]  # Get current font size
    new_size = int(current_size) + 2  # Increase font size by 2
    text.config(font=("Helvetica", new_size))  # Update font size

def decrease_font(event):
    current_size = text.cget("font").split()[-1]  # Get current font size
    new_size = int(current_size) - 2  # Decrease font size by 2
    if new_size > 10:  # Ensure font size doesn't go too small
        text.config(font=("Helvetica", new_size))  # Update font size

def quit():
    root.destroy()


root = Tk()
root.title('SNotes')
root.minsize(width=400,height=400)
root.maxsize(width=400,height=400)

text = Text(root, width=50, height=20, font=("Helvetica", 12), wrap=WORD, bg="#000000", fg="#00FFFF", insertbackground="#00FFFF")
text.pack()

# Create a vertical scrollbar
scrollbar = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Link the scrollbar to the Text widget
text.config(yscrollcommand=scrollbar.set)

menubar = Menu(root, background='#141414',fg = '#00FFFF', activebackground="#3b3b3b", activeforeground='#00FFFF')
filemenu = Menu(menubar, background='#141414', fg='#00FFFF')
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.configure(background='black')


root.bind("<Control-s>", lambda event: saveFile())

# Bind Ctrl + + to increase font size
root.bind("<Control-equal>", increase_font)

# Bind Ctrl + - to decrease font size
root.bind("<Control-minus>", decrease_font)

root.bind("<Control-q>", lambda event: quit())

root.mainloop()
