import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from tkinter import ttk


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("NOTEPAD INFO", "NOTEPAD FOR ALL: THIS NOTEPAD IS CREATED FOR PYTHON PROJECT AND IS QUITE EASY TO USE.IT IS CREATED KEEPING IN MIND THAT ANY USER CAN USE IT (: WITHOUT ANY ISSUE")
if __name__ == '__main__':
    #tkinter setup
    root = Tk()
    root.title("NOTEPAD FOR ALL")
    root.geometry("800x750")

    #Add TextArea
    TextArea = Text(root,fg='green')                                                 #alert:here remove -- font option in Fg you can add further color
    file = None
    TextArea.pack(expand=True, fill=BOTH)
    TextArea.configure(font=("Arial", 16,"italic"))                       #alert:harshit add this line
 
    # creating a menubar
    MenuBar = Menu(root)

    #File Menu Starts(creating one object of menu-- as Filemenu)
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Undo", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Redo", command=paste)
    #to add font withsubmenu (--remark here font is inheriting editmenu)--added by me    add in yours as well
    def type1():                                                   #FUNCTIONS FOR FONT OPTIONS
        TextArea.configure(font=("Impact",18))
    def type2():
        TextArea.configure(font=("Calibri",18))
    def type3():
        TextArea.configure(font=("Courier",18))
    def type4():
        TextArea.configure(font=("lucida 13",18))
    
    Font=Menu(EditMenu,tearoff=0)
    Font.add_command(label='impact',command=type1)
    Font.add_command(label='calibri',command=type2)
    Font.add_command(label='courier',command=type3)
    Font.add_command(label='lucida',command=type4)
    EditMenu.add_cascade(label="Font", menu = Font)   

    MenuBar.add_cascade(label="Edit", menu = EditMenu)               #font size adding
    def size1():
        TextArea.configure(font=(0,16))
    def size2():
        TextArea.configure(font=(0,24))
    def size3():
        TextArea.configure(font=(0,48))
    def size4():
        TextArea.configure(font=(0,64))


    size=Menu(EditMenu,tearoff=0)         #adding font size
    size.add_command(label='16',command=size1)
    size.add_command(label='24',command=size2)
    size.add_command(label='48',command=size3)
    size.add_command(label='64',command=size4)
    EditMenu.add_cascade(label="Font size", menu = size)
    

    #CALCULATOR
    #yeah functions entrybox me expression ko enter kaarwane me madad karenge"inko thoda dekhna 
    # expression to access among all the functions
    expression = ""
    # functions
    def input_number(number, equation):
        # accessing the global expression variable
        global expression
        # concatenation of string
        expression = expression + str(number)
        equation.set(expression)
    def clear_input_field(equation):
        global expression
        expression = ""
        # setting empty string in the input field
        equation.set("Enter the expression")
    def evaluate(equation):
        global expression
        # trying to evaluate the expression
        try:
            result = str(eval(expression))
            # showing the result in the input field
            equation.set(result)
            # setting expression to empty string
            expression = ""
        except:
            # some error occured
            # showing it to t he user equation.set("Enter a valid expression")
            expression = ""
    # creating the calculators gui
    
    def main():
         window=Toplevel(root)                   #yehi toplevel apni calculaor ki window open karta hai yeah root ko inherit kar rha hai
        
         # setting the title of GUI window
         window.title("Calculator")
         # set the configuration of GUI window
         window.geometry("325x175")
         # varible class instantiation
         equation = StringVar()
         # input field for the expression
         input_field = Entry(window, textvariable=equation)
         input_field.place(height=100)
         # we are using grid position
         # for the arrangement of the widgets
         input_field.grid(columnspan=4, ipadx=100, ipady=5)
         # settin the placeholder message for users
         equation.set("Enter the expression")
         # creating buttons and placing them at respective positions
         B1 = Button(window, text='1', fg='red', bg='black', bd=0, command=lambda: input_number(1, equation), height=2, width=7)
         B1.grid(row=2, column=0)
         B2 = Button(window, text='2', fg='red', bg='black', bd=0, command=lambda: input_number(2, equation), height=2, width=7)
         B2.grid(row=2, column=1)
         B3 = Button(window, text='3', fg='red', bg='black', bd=0, command=lambda: input_number(3, equation), height=2, width=7)
         B3.grid(row=2, column=2)
         B4 = Button(window, text='4', fg='red', bg='black', bd=0, command=lambda: input_number(4, equation), height=2, width=7)
         B4.grid(row=3, column=0)
         B5 = Button(window, text='5', fg='red', bg='black', bd=0, command=lambda: input_number(5, equation), height=2, width=7)
         B5.grid(row=3, column=1)
         B6 = Button(window, text='6', fg='red', bg='black', bd=0, command=lambda: input_number(6, equation), height=2, width=7)
         B6.grid(row=3, column=2)
         B7 = Button(window, text='7', fg='red', bg='black', bd=0, command=lambda: input_number(7, equation), height=2, width=7)
         B7.grid(row=4, column=0)
         B8 = Button(window, text='8', fg='red', bg='black', bd=0, command=lambda: input_number(8, equation), height=2, width=7)
         B8.grid(row=4, column=1)
         B9 = Button(window, text='9', fg='red', bg='black', bd=0, command=lambda: input_number(9, equation), height=2, width=7)
         B9.grid(row=4, column=2)
         B10 = Button(window, text='0', fg='red', bg='black', bd=0, command=lambda: input_number(0, equation), height=2, width=7)
         B10.grid(row=5, column=0)
         plus = Button(window, text='+', fg='red', bg='black', bd=0, command=lambda: input_number('+', equation), height=2, width=7)
         plus.grid(row=2, column=3)
         minus = Button(window, text='-', fg='red', bg='black', bd=0, command=lambda: input_number('-', equation), height=2, width=7)
         minus.grid(row=3, column=3)
         multiply = Button(window, text='*', fg='red', bg='black', bd=0, command=lambda:  input_number('*', equation), height=2, width=7)
         multiply.grid(row=4, column=3)
         divide = Button(window, text='/', fg='red', bg='black', bd=0, command=lambda: input_number('/', equation), height=2, width=7)
         divide.grid(row=5, column=3)
         equal = Button(window, text='=', fg='red', bg='black', bd=0, command=lambda: evaluate(equation), height=2, width=7)
         equal.grid(row=5, column=2)
         clear = Button(window, text='Clear', fg='red', bg='black', bd=0, command=lambda: clear_input_field(equation), height=2, width=7)
         clear.grid(row=5, column=1)
   # showing the CALCULATOR
         window.mainloop()
        
        
            
   
       
   # adding calculator
    calc=Menu(MenuBar,tearoff=0)
    calc.add_command(label="calculator",command=main)
    MenuBar.add_cascade(label="CALC", menu = calc)
   #calulator ended

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu = HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar
    Scroll = Scrollbar(TextArea,bg='red',)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    #adding background color and text color bar
    from tkinter import colorchooser as cc
    def bg_color():
        clr=cc.askcolor(title="select color")
        TextArea.configure(background=clr[1])
    def text_color():
        color=cc.askcolor()
        colorHex=color[1]
        TextArea.config(fg=color[1])
        
        
    def f_and_r(): 
        import tkinter as tk 
        r1=tk.Tk()
        l1=Label(r1,text="find")
        l1.grid(row=0,column=1)
        edit=Entry(r1)
        edit.grid(row=0,column=2)
        Find=Button(r1,text="Find")
        Find.grid(row=0,column=3)
        l2=Label(r1,text="REPLACE WITH")
        l2.grid(row=0,column=4)
        edit2=Entry(r1)
        edit2.grid(row=0,column=5)
        replace=Button(r1,text="Find and replace")
        replace.grid(row=0,column=6)
        def find():
            TextArea.tag_remove("found","1.0",END)
            s=edit.get()
            if (s):
                idx='1.0'
                while 1:
                    idx=TextArea.search(s,idx,nocase=1,stopindex=END)
                    if not idx: break
                    lastidx="%s+%dc"%(idx,len(s))
                    TextArea.tag_add("found",idx,lastidx)
                    idx=lastidx
                TextArea.tag_config("found",foreground="red")

            edit.focus_set()
        def find_and_replace():
            TextArea.tag_remove("found","1.0",END)
            s=edit.get()
            r=edit2.get()
            if (s and r):
                idx="1.0"
                while 1:
                    idx=TextArea.search(s,idx,nocase=1,stopindex=END)
                    if not idx: break
                    lastidx="%s+%dc"%(idx,len(s))
                    TextArea.delete(idx,lastidx)
                    TextArea.insert(idx,r)
                    lastidx="%s+%dc"%(idx,len(r))
                    TextArea.tag_add("found",idx,lastidx)
                    idx=lastidx
                TextArea.tag_config("found",foreground="green",background="yellow")
            edit.focus_set()
        Find.configure(command=find)
        replace.config(command=find_and_replace)
        r1.mainloop()
    EditMenu.add_command(label="background colour",command=bg_color)
    EditMenu.add_command(label="Text colour",command=text_color)
    
    EditMenu.add_command(label="find and replace",command=f_and_r)

    root.mainloop()
    
###-------------coding----------------ended----------------------------------###
 
