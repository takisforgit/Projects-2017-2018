from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import win32clipboard

# function
root = Tk()
root.title("Simple Notepad with Python")

def About():
      messagebox.showinfo(title='About', message='Notepad for python')

def Open():
      print( 'Open File')
      myFormats =[
             ('Python files','*.py'),
             ('Word Document','*.doc'),
             ('Simple text','*.txt'),
             ('All Files','*')
                         ]
      fileOpen = filedialog.askopenfilename(parent=root,filetypes=myFormats,title='Choose file')
      if fileOpen !='':
            T.delete(1.0,END)
            f =open(fileOpen, 'r+')
            T.insert(1.0, f.read())
            root.title(fileOpen)
            print('File Open')
      else:
            print('File not compatible')
            

def RightOpen(self):
            Open()

def Pyw():
      rep=messagebox.askyesno("","Run ??")
      if rep:
             T.tag_add(SEL, "1.0",END)
             
def effacerZone():
      rep=messagebox.askyesno("Create New file","New??")
      if rep:
            T.delete(1.0,END)

             
def effaceron():
      rep=messagebox.askyesno("Delete All","Are you sure ?")
      if rep:
            T.delete(1.0,END)
            
def Save():
      messagebox.showinfo('Save file','Save file')
      myFormats =[
             ('Python files','*.py'),
             ('Word Document','*.doc'),
             ('Simple text','*.txt'),
             ('All Files','*')
                          ]
      fileName = filedialog.asksaveasfilename(parent=root, filetypes=myFormats,title='Save...')
            
      if fileName !='':
            f=open(fileName, 'w')
            f.write(T.get(1.0,END))
            messagebox.showinfo('File saved','File saved')
      else:
            messagebox.showinfo('NOT saved','File not saved')
            
def RightSave(self):
            Save()

def SelAll(self):
            T.tag_add(SEL, "1.0",END)

def RightSelAll():
            T.tag_add(SEL, "1.0", END)

def Copy():
            T.event_generate('<Control-c>')

def getText():
      win32clipboard.OpenClipboard()
      try:
            clip1 = win32clipboard.GetClipboardData()
            print(clip1)
      except TypeError:
            messagebox.showinfo('ATTENTION','Nothing exists in Clipboard !!!')
      win32clipboard.CloseClipboard()


def setText():
      win32clipboard.OpenClipboard()
      try:
            clip2 = win32clipboard.GetClipboardData()
            win32clipboard.SetClipboardText(clip2)
      except TypeError:
            messagebox.showinfo('ATTENTION','Nothing exists in Clipboard !!!')
      win32clipboard.EmptyClipboard()
      win32clipboard.CloseClipboard()
      

def RightClickMenu(event):
            popup.tk_popup(event.x_root+42, event.y_root+10,0)
            popup.grab_release()
##def main(event):
##      st.config(cursor='hand2')
##      
def Quitter():
      rep=messagebox.askyesno("Confirm","Really quit ?")
      if rep:
            root.quit()
            
def comMenuAPropos():                                                                        
    messagebox.showinfo(                                                                   
            "Just a ...",                                                                
            "     Notepad for python\n\n" )
            
MenuBar = Menu(root)                                                             
root.config(menu = MenuBar)                                                      

menuFichier = Menu(MenuBar)                                                             
MenuBar.add_cascade(label="File", menu=menuFichier)                                  

                      
menuFichier.add_command(label="New", command=effacerZone)
menuFichier.add_command(label="Open...", command=Open)                         
menuFichier.add_command(label="Save as...", command=Save)
menuFichier.add_command(label="Save ", command=RightSave) 
menuFichier.add_separator()                                                                  
menuFichier.add_command(label="Quit", command=Quitter)

menuEdition = Menu(MenuBar)                                                             
MenuBar.add_cascade(label="Edit", menu=menuEdition)
menuEdition.add_command(label="Copy", command=getText)
menuEdition.add_command(label="Paste", command=setText)
menuEdition.add_command(label="Select All", command=RightSelAll)

menuPython =Menu(MenuBar)
MenuBar.add_cascade(label="Pyshell", menu=menuPython)
menuPython.add_command(label="Run",command=Pyw)

menuAide = Menu(MenuBar)                                                                
MenuBar.add_cascade(label="Help", menu=menuAide)                                        
menuAide.add_command(label="About", command=comMenuAPropos)

s= Scrollbar(root)
T= Text(root, wrap=WORD)

T.focus_set()
s.grid(column =2, row=1, sticky = W+N+S)
T.grid(row=1, column=1)
s.config(command=T.yview)
T.config(yscrollcommand=s.set)

popup = Menu(root, tearoff=0)
popup.add_command(label="Select All", command =RightSelAll)
popup.add_command(label="Copy", command=Copy)
popup.add_command(label="Delete All", command=effaceron)

root.bind('<Button-3>', RightClickMenu)
root.bind('<Control_L>'+'a',SelAll)
root.bind('<Control_L>'+'s',RightSave)
root.bind('<Control_L>'+'o',RightOpen)
root.bind('<Control_R>'+'a',SelAll)
root.bind('<Control_R>'+'s',RightSave)
root.bind('<Control_R>'+'o',RightOpen)

mainloop()
            

            

# main program


