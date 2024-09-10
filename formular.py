import tkinter as tk
from tkinter import ttk
import random

def change (x,y) : #ทำเศษส่วนเป็นรูปอย่างง่าย
    for i in range(abs(x),0,-1) :
        if ((abs(y) % i) == 0) and ((abs(x) % i) == 0):
            y = y/i
            x = x/i
    if y < 0 and x < 0 :
        x = x*-1
        y = y*-1
    return x,y



def r (x=-10,y=10,z=None) : #easy random
    a = random.randint(x,y)
    while a == z :
        a = r(x,y,z)
    return a

def myfunction (x) : #สัญลักษณ์หน้าตัวเลข
        if x >= 0 :
            o = '+'
        elif x < 0 :
            o = ''
        return o
    

################################################################


def gen_plus () :
    x = r()
    y = r()
    l1 =[x,y,"x"]
    random.shuffle(l1)
    q = (l1[0],random.choice(["+","-"]),l1[1],'=',l1[2])
    
    if q[1] == "+" :
        if l1[2] == 'x':
            a = x+y
        elif l1[1] == 'x' :
            a = l1[2]-l1[0]
        elif l1[0] == 'x' :
            a = l1[2]-l1[1]
    elif q[1] == "-" :
        if l1[2] == 'x':
            a = l1[0]-l1[1]
        elif l1[1] == 'x':
            a = l1[0]-l1[2]
        elif l1[0] == 'x' :
            a = x+y
    return q,a
        
def gen_Factorization1 () :
    x = r(z=0)
    y = r(z=0)
    
    f1 = myfunction(x+y)
    f2 = myfunction(x*y)
    
    q = ["x^2 {}{}x {}{} = 0".format(f1,x+y,f2,x*y)]
    
    a = ["x = {},{}".format(x*-1,y*-1)]
    
    return q,a
        
def gen_Factorization2 () :
    w = r(z=0)
    x = r(z=0)
    y = r(z=0)
    z = r(z=0)
    
    xw = change(x,w)
    zy = change(z,y)
    f1 = myfunction((x*y)+(w*z))
    f2 = myfunction(x*z)
    
    q = ["{}x^2 {}{}x {}{} = 0".format(w*y,f1,(x*y)+(w*z),f2,x*z)]
    a = ["x = {}/{} , {}/{}".format(int(xw[0])*-1,int(xw[1]),int(zy[0])*-1,int(zy[1]))]
    
    return(q,a)


def gen_parabola () :
    h = r()
    k = r()
    c = r()
    
    direction = random.choice(['x','y'])
    
    answer = ['h = {}  k = {}  c = {}'.format(h,k,c)]
    
    
    f1 = myfunction(2*k)
    f2 = myfunction((k**2)*-1 + (c*h*-4))
    f3 = myfunction(-2*h)
    f4 = myfunction((h**2)+(4*c*k))
    
    
    if direction == 'x' :
        question = ["y^2 = {}x {} {}y {} {}".format((c*4),f1,2*k,f2,(k**2)*-1 + (c*h*-4))]
    elif direction == 'y' :
        question = ['y = ( x^2 {}{}x {} {} ) / {}'.format(f3,(-2*h),f4,((h**2)+(4*c*k)),4*c)]
        
    return question,answer



def gen_circle () :
    h = r()
    k = r()
    R = r()
    
    f1 = myfunction(2*h)
    f2 = myfunction(2*k)
    f3 = myfunction(h**2+k**2-R**2)
    
    question = 'x^2 + y^2 {}{}x {}{}y {}{} = 0'.format(f1,2*h,f2,2*k,f3,h**2+k**2-R**2)
    
    
    return question,['h = {} , k = {} , r = {}'.format(h,k,R)]



def gen_oval () :
    h = r()
    k = r()
    a = r(z=0)
    b = r(z=0)
    while a == b :
        b = r(z=0)
    
    if a > b :
        answer = ['h = {}  k = {}  a = {}  b = {}'.format(h,k,a,b)]
    elif b > a :
        answer = ['h = {}  k = {}  a = {}  b = {}'.format(h,k,b,a)]
    
    question = ['{}x^2 {}{}y^2 {}{}x {}{}y {}{} = 0'.format(b,myfunction(a),a,myfunction(-2*b*h),-2*b*h,myfunction(-2*a*k),-2*a*k,myfunction((h**2*b)+(k**2*a)-(a*b)),(h**2*b)+(k**2*a)-(a*b))]
    
    
    
    return question,answer
    



def gen_2variable_equation () :
    x = r()
    y = r()
    fx1 = r()
    fy1 = r()
    fx2 = r()
    fy2 = r()
    
    
    question = ["{}x {}{}y = {}\n{}x {}{}y = {}".format(fx1,myfunction(fy1),fy1,(fx1*x+fy1*y),fx2,myfunction(fy2),fy2,(fx2*x+fy2*y))]
    
    answer = ['x = {}  y = {}'.format(x,y)]
    
    return question,answer


def gen_root2 () :
    x = random.randint(0,20)
    
    question = ["if y = {} and x is root2 of y \nwhat is x".format(x**2)]
    
    answer = ['x = {}'.format(x,x)]
    return question,answer

def gen_root3 () :
    x = r()
    
    question = ["if y = {} and x is root3 of y \nwhat is x".format(x**3)]
    
    answer = ['x = {}'.format(x,x)]
    return question,answer



def gen_fraction_to_decimal () :
    x1 = r()
    x2 = random.random()
    
    x = x1+round(x2,2)
    y = x*100
    z = 100
    
    for i in range(100,0,-1) :
        if ((y % i) == 0) and ((z % i) == 0):
            y = y/i
            z = z/i
    
    q = ['change {}/{} to decimal'.format(int(round(y,0)),int(round(z,0)))]
    
    
    return q,x



def gen_decimal_to_fraction () :
    x = r()
    y = r(z=0)
    
    xy = change(x,y)
    
    a = ["{}/{}".format(int(xy[0]),int(xy[1]))]
    
    q = [round(x/y,3)]
    
    return q,a
            
            
def gen_comparison () :
    x1 = r()
    x2 = r(z=0)
    y1 = r()
    y2 = r(z=0)
    
    x = x1/x2 
    y = y1/y2
    
    if x1 < 0 and x2 < 0 :
        x1 = x1*-1
        x2 = x2*-1
    if y2 < 0 and y1 < 0 :
        y1 = y1*-1
        y2 = y2*-1
    
    if x == y :
        o = "="
    elif x > y :
        o = ">"
    elif x < y :
        o = "<"
            
    a = ["{}/{} {} {}/{}".format(x1,x2,o,y1,y2)]
    
    q = ["{}/{} is... to {}/{}".format(x1,x2,y1,y2)]
    
    return q,a


def gen_log_1 () :
    n = r(x=2)
    x = r(0,4)
    xa = n**x
    
    q = ["log base {} of x = {}".format(n,x)]
    
    return q,xa

def gen_log_2 () :
    b = random.choice([2,3,5])
    p1 = r(-5,5,0)
    p2 = r(-5,5,0)
    
    def f (x,y=b) :
        if x < 0 :
            return "1/{}".format(y**-x)
        elif x > 0 :
            return y**x
    
    c = change(p2,p1)
    
    q = ["x = log base {} of {}".format(f(p1),f(p2))]
    a = ["x = {}/{}".format(int(c[0]),int(c[1]))]
    
    return q,a

def gen_syntheticdivision () :
    x = r(z=0)
    y = r(z=0)
    z = r(z=0)
    
    fx2 = (x*y)+(x+y)*z
    f1 = myfunction(x+y+z)
    f2 = myfunction(fx2)
    f3 = myfunction(x*y*z)
    
    q = ["x^3 {}{}x^2 {}{}x {}{} = 0".format(f1,x+y+z,f2,fx2,f3,x*y*z)]
    
    a = ["x = {},{},{}".format(x*-1,y*-1,z*-1)]
    
    return q,a

def gen_arcs_end_point_coordinate1 () :
    x = r(x=1,y=2)
    y = random.choice([1,2])
    
    q = "p({}pi/{})".format(x,y)
    
    
    x1,x2 = change(x,y)
    
    
    x1 = x1%2
    
    
    a = ""
    
    return q,a

def gen_trigonometric_functions () :
    x = [0,30,45,60]
    x1 = random.choice(x)
    y = random.choice([0,90,180,270])
    z = random.choice([y+x1,y-x1])
    f = random.choice([("sin","","","-","-"),("cos","",'-','-',""),("tan",'','-','','-'),
                       ("csc",'','','-','-'),("sec",'','-','-',''),("cot",'','-','','-')])
    
    q = "{}{}".format(f[0],z)
    
    if z > 270 :
        Q = 4
    elif z > 180 :
        Q = 3
    elif z > 90 :
        Q = 2
    else :
        Q = 1
        
    a = "{}".format(f[Q])
    
gen_trigonometric_functions()