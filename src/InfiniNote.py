#Main Imports
import tkinter
from tkinter import *
import os
#Space for message
from tkinter.messagebox import *
#Dialog Box
from tkinter.filedialog import *

#!/C:/User/garitbibbs/AppData/Local/Programs/Python/Python37/python.exe

class Notepad:
    __root = Tk()
    __root.geometry('500x600')
#Menu
    __thisWidth = 500
    __thisHeight = 600
    __MenuBar = Menu(__root)
    __TextArea = Text(__root)
    __FileMenu = Menu(__MenuBar, tearoff=0)
    __InfoMenu = Menu(__MenuBar, tearoff=0)
    __SettingsMenu = Menu(__MenuBar, tearoff=0)
    __ColorMenu = Menu(__SettingsMenu, tearoff=0)

    #Scrollbar
    __Scrollbar = Scrollbar(__TextArea)
    __Scrollbar.config(bg= '#8A8E8E', activebackground= '#8A8E8E')
    __file = None

    

    def __init__(self, **kwargs):
        
        #Future Update Set Icon
        #Title
        self.__root.title("Untitled - InfiniNote")
        self.__TextArea['bg']='#8A8E8E'
        self.__TextArea['font']='Times'
        self.__MenuBar['font']='Times'

         # Center the window 
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight() 
      
        # For left-alling 
        left = (screenWidth / 2) - (self.__thisWidth / 2)  
          
        # For right-allign 
        top = (screenHeight / 2) - (self.__thisHeight /2)  
          
        # For top and bottom 
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              left, top))

        #Realignment
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        
        #Add Controls
        self.__TextArea.grid(sticky = N + E + S + W)
        self.__Scrollbar.pack(side=RIGHT, fill=Y)
        self.__root.config(menu = self.__MenuBar)
        self.__MenuBar.add_command(label="Info",
        command=self.__ShowInfo)
        #Save a File
        self.__FileMenu.add_command(label="Save",
        command=self.__SaveFile)
        #open a file
        self.__FileMenu.add_command(label="Open",
        command=self.__OpenFile)
        #New File
        self.__FileMenu.add_command(label="New",
        command=self.__NewFile)
        self.__FileMenu.add_command(label="Clear",
        command=self.__Clear)
        
        

        #Line in the Dialog
        self.__FileMenu.add_separator()                                          
        self.__FileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.__MenuBar.add_cascade(label="File", 
                                        menu=self.__FileMenu)
    def __SaveFile(self):
        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("Text Files [*.txt]","*.txt"), 
                                                ("HTML Files [*.html, *.htm]", "*.html"),
                                                ("Python Files [*.py]", "*.py"),
                                                ("CSS Files [*.css]", "*.css"),
                                                ("C++ Files [*.cpp]", "*.cpp")]) 
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                # Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.__TextArea.get(1.0,END)) 
                file.close() 
                  
                # Change the window title 
                self.__root.title(os.path.basename(self.__file) + " - InfiniNote") 
                  
              
        else: 
            file = open(self.__file,"w") 
            file.write(self.__TextArea.get(1.0,END)) 
            file.close()
    def __OpenFile(self):
        self.__file = askopenfilename(defaultextension=".txt",
        filetypes=[("Text Files [*.txt]", "*.txt"),
        ("Python Files [*.py]", "*.py")])
        if self.__file == "":
            #No File To Open
            self.__file == None
        else:
                #Set the name of the file as the title
            self.__root.title(os.path.basename(self.__file) + "- InfiniNote")
            self.__TextArea.delete(1.0, END)

            #Try to open the file

            file = open(self.__file, "r")
            lines = file.read()
            self.__TextArea.insert('1.0', chars=lines)
            file.close()
            
    def __quitApplication(self):
        self.__root.destroy()
        #exit
    def __NewFile(self):
        self.__root.title("Untitled - InfiniNote")
        self.__file = None
        self.__TextArea.delete(1.0, END)
    def __ShowInfo(self):
        showinfo("InfiniNote", "Version-0.2 \n Reid Powell")
    def __Clear(self):
        self.__TextArea.delete(1.0, END)
    def run(self):
        self.__root.mainloop()

#Run
notepad = Notepad(width=500, height=600)
notepad.run()