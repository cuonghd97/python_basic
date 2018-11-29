from tkinter import *

root=Tk()#tao 1 cua so
root.title("Sinionth")
root.geometry("400x400+150+150")
def Clicked():
    print("Clicked!")
btn=Button(root,text='Click here!',command=Clicked)
btn.pack(side=TOP)#giong add cua java

root.mainloop()



