import Image, ImageTk
from Tkinter import *
import tkFileDialog
import tkMessageBox
import tkSimpleDialog


# function
root = Tk()
root.title("Notepad for python")

def About():
      tkMessageBox.showinfo(title='About', message='Notepad for python')

def Open():
      print( 'Ouvrir Fichier')
      myFormats =[
            ('Fichier Love','*.lov'),
            ('Fichier SHELL','*.py'),
             ('Fichier Document','*.doc'),
             ('Fichier Texte','*.txt'),
             ('All Files','*')
                         ]
      fileOpen = tkFileDialog.askopenfilename(parent=root,filetypes=myFormats,title='Choisir fichier')
      if fileOpen !='':
            T.delete(1.0,END)
            f =open(fileOpen, 'r+')
            T.insert(1.0, f.read())
            root.title(fileOpen)
            print('fichier ouvert')
      else:
            print('fichier non compatible')
            

def RightOpen(self):
            Open()

def Pyw():
      rep=tkMessageBox.askyesno("","Run ??")
      if rep:
             T.tag_add(SEL, "1.0",END)
             
def effacerZone():
      rep=tkMessageBox.askyesno("","nouveau??")
      if rep:
            T.delete(1.0,END)

             
def effaceron():
      rep=tkMessageBox.askyesno("","effacer??")
      if rep:
            T.delete(1.0,END)
            
def Save():
      tkMessageBox.showinfo('Sauvez fichier','Sauvez fichier')
      myFormats =[
            ('Fichier Love','*.lov'),
            ('Fichier SHELL','*.py'),
             ('Fichier Document','*.doc'),
             ('Fichier Texte','*.txt'),
            ('All Files','*')
                          ]
      fileName = tkFileDialog.asksaveasfilename(parent=root, filetypes=myFormats,title='Sauvez sous')
            
      if fileName !='':
            f=open(fileName, 'w')
            f.write(T.get(1.0,END))
            tkMessageBox.showinfo('Fichier sauver','Fichier sauvez')
      else:
            tkMessageBox.showinfo('not saved','not saved')
            
def RightSave(self):
            Save()

def SelAll(self):
            T.tag_add(SEL, "1.0",END)

def RightSelAll():
            T.tag_add(SEL, "1.0", END)

def Copy():
            T.event_generate('<Control-c')

def getText():
      w.OpenClipboard()
      d=w.GetClipboardData(win32con.CF_TEXT)
      w.CloseClipboard()


def setText(aType,aString):
      w.Open.Clipboard()
      w.emptyClipboard()
      w.setClipboardData(aType,aString)
      w.CloseClipboard()

def RightClickMenu(event):
            popup.tk_popup(event.x_root+42, event.y_root+10,0)
            popup.grab_release()
            st.config(cursor='hand2')
def main(event):
      st.config(cursor='hand2')
      
def Quitter():
      rep=tkMessageBox.askyesno("Confirmer","Voulez vous quitter ?")
      if rep:
            root.quit()
            
def comMenuAPropos():                                                                        ###
    tkMessageBox.showinfo(                                                                   ###
            "A propos de...",                                                                ###
            "     Notepad pour python\n\n" )
            
barreDeMenus = Menu(root)                                                             ###
root.config(menu = barreDeMenus)                                                      ###

menuFichier = Menu(barreDeMenus)                                                             ###
barreDeMenus.add_cascade(label="Fichier", menu=menuFichier)                                  ###

                      ###
menuFichier.add_command(label="Nouveau", command=effacerZone)
menuFichier.add_command(label="Ouvrir...", command=Open)                          ###
menuFichier.add_command(label="Enregistrer sous...", command=Save)
menuFichier.add_command(label="Enregistrer ", command=RightSave) ###
menuFichier.add_separator()                                                                  ###
menuFichier.add_command(label="Quitter", command=Quitter)
###
menuEdition = Menu(barreDeMenus)                                                             ###
barreDeMenus.add_cascade(label="Edition", menu=menuEdition)
menuEdition.add_command(label="copier", command=getText)
menuEdition.add_command(label="coller", command=setText)
menuEdition.add_command(label="selectionner tout", command=RightSelAll)

menuPython =Menu(barreDeMenus)
barreDeMenus.add_cascade(label="Pyshell", menu=menuPython)
menuPython.add_command(label="Run",command=Pyw)

menuAide = Menu(barreDeMenus)                                                                ###
barreDeMenus.add_cascade(label="Aide", menu=menuAide)                                        ###
menuAide.add_command(label="A propos", command=comMenuAPropos)

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
popup.add_command(label="tout effacer", command=effaceron)

root.bind('<Button-3>', RightClickMenu)
root.bind('<Control_L>'+'a',SelAll)
root.bind('<Control_L>'+'s',RightSave)
root.bind('<Control_L>'+'o',RightOpen)
root.bind('<Control_R>'+'a',SelAll)
root.bind('<Control_R>'+'s',RightSave)
root.bind('<Control_R>'+'o',RightOpen)

mainloop()
            

            

# main program


