import tkinter as tk



class Heading (tk.Label) :
    def __init__(self,SCREEN,TEXT) :
        tk.Label.__init__(self,SCREEN,text=TEXT,font=("Tahoma",50,"bold"))
        self.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#heading_text = tk.Label(screen,text="H O M E",font=("Tahoma",100,"bold"))
#heading_text.grid(row=0,column=0,columnspan=4,padx=10,pady=10)