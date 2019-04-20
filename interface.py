from tkinter import *

#root = Tk() #importing a kinter class.. Basically creates a BLANK WINDOW with the constructor of the class
#theLabel = Label(root, text="Hello World!!!")
#theLabel.pack() #just pack it in the first place it fits
'''root.geometry("1350x750+0+0")
root.configure(background = "blue")

Tops = Frame(root, width = 1350, height = 100, bd=2, relief="raise")
Tops.pack(side=TOP)

FLeft = Frame(root, width = 900, height = 650, bd=1, relief="raise")
FLeft.pack(side=LEFT)

FRight = Frame(root, width = 440, height = 650, bd=1, relief="raise")
FRight.pack(side=RIGHT)'''

'''topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM) #Sets the container to the bottom of the window

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

#You have to pack the buttons to display them on the screen. Otherwise they wont be shown
button1.pack(side=LEFT) #put it as far left as possible
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)'''

'''one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X) #If the parent has his width changed, the two's width will change as well
three = Label(root, text="Three", bg="black", fg="white")
three.pack(side=LEFT, fill=Y)'''

#A way to organize widgets on the screen - GRID Layout

'''label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

entry_1 = Entry(root) #A simple input field
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E) #By default, the column is always equals to 0
label_2.grid(row=1, sticky=E) #Sticky : inside that container, you wanna to put it into the right
#OBS: E(EAST), W(WEST), N(NORTH), S(SOUTH)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2) #It takes 2 columns(or 2 cells)'''


#Binding a function to a widget
'''def printName():
    print("Hello, my name is Felipe")

button_1 = Button(root, text="Print my name", command=printName) #the command parameter says: when I click this button, call the function printName, for example
button_1.pack()'''

#Another way to do this
'''def printName(event):
    print("Hello, my name is Felipe")

button_1 = Button(root, text="Print my name") #the command parameter says: when I click this button, call the function printName, for example
button_1.bind("<Button-1>", printName)
button_1.pack()
'''

#Working with different types of events
'''def leftClick(event):
    print("Left")

def middleClick(event):
    print("Middle")

def rightClick(event):
    print("Right")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
#frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
#Left - 1; Midlle - 2; Right - 3
frame.pack()'''

#Using classes...
'''class DrawButtons:

    def __init__(self, master): #a special kind of function (constructor); The master parameter means the root or the mains window
        frame = Frame(master) #creating the frame in the main window
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit) #frame.quit brakes the main loop
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually worked!!!")


root = Tk()
b = DrawButtons(root)'''


#Creating Menus, Toolbars, StatusBar

'''def doNothing():
    print("ok, ok I won't...")

root = Tk()

#***** MainMenu *****
menu = Menu(root)
root.config(menu=menu)

#The tkinter already has the knowledge of how to make menus(Where to put them, ...)
#So it takes all the hard work for you

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu) #Adding a dropdown menu

subMenu.add_command(label="New project...", command=doNothing)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

#***** The Toolbar *****

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#***** Status Bar *****

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W) #bd stands for border
status.pack(side=BOTTOM, fill=X)
'''

#Message boxes
'''import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Monkeys can live up to 300 years.')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if (answer == 'yes'):
    print(" 8===D~" )'''

#Shapes and Graphics

'''root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50) #Starting x/y and Ending x/y
redLine = canvas.create_line(0, 100, 200, 50, fill="red")

greenBox = canvas.create_rectangle(25 , 25, 130, 60, fill="green")

#canvas.delete(redLine)
canvas.delete(ALL)'''

#Images and icons
#You have to display your images inside a label

def hello(event):
    print("Hello")

root = Tk()

photo = PhotoImage(file="Entrada1_cortada.png")
label = Label(root, image=photo)

label.bind("<Button-1>", hello)
label.pack()



root.mainloop() #keeps your GUI continuesly on the screen until you decide to close it out
