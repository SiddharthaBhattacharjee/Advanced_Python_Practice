from tkinter import *

def rc(*args):
   print("Right click pressed")

def lc(*args):
   print("Left click pressed")

root = Tk()
root.geometry("500x500")
root.bind("<Button-1>",lc)
root.bind("<Button-3>",rc)
root.mainloop()
