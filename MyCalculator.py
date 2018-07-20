from tkinter import *

root=Tk()
root.title("MyCalculator(MYVIRUSKING)")
root.resizable(width = False, height = False)


#Display Entry widget-------------------------------------------------------------
text_input=StringVar()
e=Entry(root,bd=30,relief=RIDGE,width=24,bg="lightblue",font=('times',25,'bold'),fg='black',justify=RIGHT,textvariable=text_input).grid(columnspan=4)

    

#Button with Command-------------------------------------------------------------
operator=""
def btnclick(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)

def clearbtn():
    global operator
    operator=""
    text_input.set("")


def equalbtn():
    try:
        global operator
        result=str(eval(operator))
        text_input.set(result)
        operator=result
    except SyntaxError:
        operator=""
        error="Invalid Syntax!"
        text_input.set(error)
        
    
    
   

#Display All Buttons widgets------------------------------------------------------
btn7=Button(root,text="7",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick(7)).grid(row=1,column=0)
btn6=Button(root,text="8",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick(8)).grid(row=1,column=1)
btn9=Button(root,text="9",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick(9)).grid(row=1,column=2)
btn_div=Button(root,text="/",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick('/')).grid(row=1,column=3)

btn4=Button(root,text="4",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick(4)).grid(row=2,column=0)
btn5=Button(root,text="5",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick(5)).grid(row=2,column=1)
btn6=Button(root,text="6",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick(6)).grid(row=2,column=2)
btn_mul=Button(root,text="*",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick('*')).grid(row=2,column=3)

btn1=Button(root,text="1",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick(1)).grid(row=3,column=0)
btn2=Button(root,text="2",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick(2)).grid(row=3,column=1)
btn3=Button(root,text="3",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick(3)).grid(row=3,column=2)
btn_sub=Button(root,text="-",width=9,height=4,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick('-')).grid(row=3,column=3)

btn0=Button(root,text="0",width=9,height=7,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick(0)).grid(row=4,column=0)
btnc=Button(root,text="C",width=9,height=7,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=clearbtn).grid(row=4,column=1)
btn_eql=Button(root,text="=",width=9,height=7,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=equalbtn).grid(row=4,column=2)
btn_add=Button(root,text="+",width=9,height=7,bd=15,relief=RAISED,bg="lightblue",fg='black',font=('times,20,bold'),command=lambda : btnclick('+')).grid(row=4,column=3)


root.mainloop()


