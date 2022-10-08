from tkinter import *
import tkinter as tk
import threading
from PIL import ImageTk, Image
from playsound import playsound
root = tk.Tk()
root.geometry('700x300')
root.title("piano")
root.maxsize(700,335)
root.minsize(700,335)
root['bg']="white"
icon = ImageTk.PhotoImage(Image.open('piano.png'))
icon_label = Label(root,image=icon)
icon_label.place(x=295,y=10)
icon_label.pack()
frame1 = Frame(root,width=700,height=198,highlightbackground="blue",highlightthickness=5)
frame1.place(x=0,y=100)
class piano():
        def PianoSound(self,sound):
                store=f'Piano{sound}.mp3'
                text = Label(root, text=f'Tune : {store}',background="white",width=20)
                text.place(x=280,y=70)
                playsound(store)
        def __init__(self,index):
                self.index = index
                if self.index%2 != 0:
                        Button(frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=3,command=lambda:threading.Thread(target=self.PianoSound,args=[self.index]).start(),cursor="hand2").grid(row=0,column=self.index)
                else:
                        Button(frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=2,command=lambda:threading.Thread(target=self.PianoSound,args=[self.index]).start(),cursor="hand2").grid(row=0,column=self.index)

if __name__ == '__main__':
        for i in range(1,24):
                piano(i)

root.mainloop()    
    



