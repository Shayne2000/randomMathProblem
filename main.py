import tkinter as tk
from heading import Heading as h
from tkinter import ttk
from formular import *


####### variable ##########

data_name = [['fraction to decimal','decimal to fraction',"fraction comparison"]
             ,["Factorization1","Factorization2","root2","root3","2variable equation"],3,
             ["parabola","circle","oval","synthetic division"],
             ["basic log1","basic log2"],6,
        ['plus-minus with variable']]
data_function = [[gen_fraction_to_decimal,gen_decimal_to_fraction,gen_comparison],
                 [gen_Factorization1,gen_Factorization2,gen_root2,gen_root3,gen_2variable_equation],3,
                 [gen_parabola,gen_circle,gen_oval,gen_syntheticdivision],
                 [gen_log_1,gen_log_2],6,[gen_plus]]

data_qTitle = [["decimal","fraction","operator"]
               ,["x","x","x","x","x , y"]
               ,3,["h , k , c" , "h , k , r","h , k , a , b","x"],
               ["x","x"],6,["x"]]

###### function #########


class MyButton (tk.Button) :
    def __init__ (self,screen,r,c) :
        tk.Button.__init__(self,screen,text="BUTTON",command=self.Myfunction)
        self.grid(row=r,column=c,padx=5,pady=5)
        self.row = r
        self.list_name = data_name[(r-1)]
        self.list_function = data_function[(r-1)]
        self.list_qTitle = data_qTitle[(r-1)]
    def Myfunction (self) :
        window = tk.Toplevel(screen)
        window.geometry('600x300')
        heading = h(window,("grade",self.row))
        
        self.Type = ttk.Combobox(window,values=self.list_name)
        self.Type.grid(row=1,column=0,padx=10,pady=10)
        
        self.Type.set(self.list_name[0])
        
        
        self.qTitle = tk.Label(window,text="find : "+self.list_qTitle[self.Type.current()])
        self.qTitle.grid(row=2,column=0,padx=5,pady=5,sticky = 'w')
        
        
        self.question = tk.Text(window,state='disabled',height=3,width=35)
        self.question.grid(row=3,column=0,padx=10,pady=10)
        

        self.button = tk.Button(window,text="generate",command=self.submit)
        self.button.grid(row=3,column=1,padx=10,pady=10)


        self.answer = ttk.Combobox(window,values="null",state="readonly")
        self.answer.grid(row=4,column=0,padx=10,pady=10)
        
         
    def submit (self) :
        
        self.qTitle["text"] = "find : "+self.list_qTitle[self.Type.current()]
        
        if self.question['state'] == "disabled" :
            self.question['state'] ='normal'
            
        value = self.list_function[self.Type.current()]()

        self.question.delete("1.0",'end')
        self.question.insert("1.0",value[0])
        self.question['state'] = 'disabled'
        
        
        self.answer["value"] = value[1]
        self.answer.set("Answer")
        



screen = tk.Tk()
screen.geometry('600x450')




###################


heading_text = tk.Label(screen,text="H O M E",font=("Tahoma",100,"bold"))
heading_text.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


###################


m1_text = tk.Label(screen,text="M1",bg="gray")
m1_text.grid(row=1,column=0,padx=5,pady=5,ipadx=100)


m1_button = MyButton(screen,1,1)

#m1_button = tk.Button(screen,text="BUTTON",command=)
#m1_button.grid(row=1,column=1,padx=5,pady=5)





####################


m2_text = tk.Label(screen,text="M2",bg="gray")
m2_text.grid(row=2,column=0,padx=5,pady=5,ipadx=100)

m2_button = MyButton(screen,2,1)


#####################


m3_text = tk.Label(screen,text="M3",bg="gray")
m3_text.grid(row=3,column=0,padx=5,pady=5,ipadx=100)

m3_button = MyButton(screen,3,1)


##################


m4_text = tk.Label(screen,text="M4",bg="gray")
m4_text.grid(row=4,column=0,padx=5,pady=5,ipadx=100)

m4_button = MyButton(screen,4,1)


###########################


m5_text = tk.Label(screen,text="M5",bg="gray")
m5_text.grid(row=5,column=0,padx=5,pady=5,ipadx=100)

m5_button = MyButton(screen,5,1)




m6_text = tk.Label(screen,text="M6",bg="gray")
m6_text.grid(row=6,column=0,padx=5,pady=5,ipadx=100)

m6_button = MyButton(screen,6,1)

test = tk.Label(screen,text="test",bg="gray")
test.grid(row=7,column=0,padx=5,pady=5,ipadx=100)

test_button = MyButton(screen,7,1)



screen.mainloop()