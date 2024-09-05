from tkinter import *



root=Tk()
root.title("Login")
root.geometry("1000x630")

#=============================================DETAILS==============================================================================

pwd=StringVar()
name=StringVar()
cls=StringVar()
sec=StringVar()
rn=StringVar()

#==================================================Exit=============================================================================
def qexit():
    root.destroy()
#==================================================Check Score======================================================================
i1=StringVar()
i2=StringVar()
i3=StringVar()
i4=StringVar()
i5=StringVar()
i6=StringVar()


def check():
    a1=int(i1.get())
    a2=int(i2.get())
    a3=int(i3.get())
    a4=int(i4.get())
    a5=int(i5.get())
    a6=int(i6.get())
    
    if a1==2:
        r1=4
    else:
        r1=0
        
    if a2==1:
        r2=4
    else:
        r2=0    
    if a3==2:
        
        r3=4
    else:
        r3=0
    if a4==1:
        
        r4=4
    else:
        r4=0
    if a5==2:
        r5=4
    else:
        r5=0
    if a6==1:
        
        r6=4
    else:
        r6=0
    sc1=r1+r2+r3+r4+r5+r6    
    pts=str(r1+r2+r3+r4+r5+r6)
    
    sco=open("score.txt","w")
    finalmarks="Your Score is ="+pts
    sco.write(finalmarks)

#====================================================Pie Chart====================================================================    
    import matplotlib.pyplot as plt
    labels = 'Correct','Incorrect'
    sizes = [sc1/4,6-sc1/4]
    colors = ['gold', 'yellowgreen']
    explode = (0.1, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()

#===================================================Start Quiz======================================================================
def startquiz():
    nam=name.get()
    cla=cls.get()
    sect=sec.get()
    roll=rn.get()
    f=open("info.txt","w")
    det="Name:"+nam+",Class:"+cla+"-"+sect+",Roll Number:"+roll
    f.write(det)
    
    quiz=Toplevel()
    quiz.title("Let's Play")
    quiz.geometry("1200x650")
    labelquiz=Label(quiz,text=("Quiz" ),font=( 'TechHaus' ,60 ),fg="grey",bd=10,anchor='w')
    labelquiz.pack(side=TOP)
    labeldet=Label(quiz,text=("Name: "+nam+" Class: "+cla+"-"+sect+" Roll Number: "+roll+"") ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    labeldet.pack()
    f1 = Frame(quiz,width = 1200,height=1000,relief=SUNKEN)
    f1.pack(side=LEFT)
    f2 = Frame(quiz,width = 600,height=1000,relief=SUNKEN)
    f2.pack(side=RIGHT)


#=======================================QUESTIONS 1======================================================================================    
    
    q1=Label(f1,text=("Q.1.IC chips used in computers are usually made of?") ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    q1.pack()
    o11=Radiobutton(f1,text="Lead",variable=i1,value=1)
    o11.pack()
    o12=Radiobutton(f1,text="Silicon",variable=i1,value=2)
    o12.pack()
    o13=Radiobutton(f1,text="Chromium",variable=i1,value=3)
    o13.pack()
    o14=Radiobutton(f1,text="Gold",variable=i1,value=4)
    o14.pack()
#==========================================QUESTIONS 2====================================================================================    
    q2=Label(f1,text=("Q.2.When was First GTA game released?") ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    q2.pack()
    o21=Radiobutton(f1,text="1997",variable=i2,value=1)
    o21.pack()
    o22=Radiobutton(f1,text="2004",variable=i2,value=2)
    o22.pack()
    o23=Radiobutton(f1,text="2001",variable=i2,value=3)
    o23.pack()
    o24=Radiobutton(f1,text="1985",variable=i2,value=4)
    o24.pack()
#===========================================QUESTIONS 3===================================================================================
    q3=Label(f1,text=("Q.3.Which is the First Programming Language?") ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    q3.pack()
    o31=Radiobutton(f1,text="Python",variable=i3,value=1)
    o31.pack()
    o32=Radiobutton(f1,text="Plankalkül",variable=i3,value=2)
    o32.pack()
    o33=Radiobutton(f1,text="Ruby on Rails",variable=i3,value=3)
    o33.pack()
    o34=Radiobutton(f1,text="Javascript",variable=i3,value=4)
    o34.pack()
#============================================QUESTIONS 4==================================================================================
    q4=Label(f2,text=("Q.4.Which supercomputer is developed by the Indian Scientists?") ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    q4.pack()
    o41=Radiobutton(f2,text="Param",variable=i4,value=1)
    o41.pack()
    o42=Radiobutton(f2,text="Super 301",variable=i4,value=2)
    o42.pack()
    o43=Radiobutton(f2,text="Compaq Presario",variable=i4,value=3)
    o43.pack()
    o44=Radiobutton(f2,text="CRAY YMP",variable=i4,value=4)
    o44.pack()
#===========================================QUESTIONS 5===================================================================================    
    q5=Label(f2,text=("Q.5.In binary code, the number 7 is written as?") ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    q5.pack()
    o51=Radiobutton(f2,text="110",variable=i5,value=1)
    o51.pack()
    o52=Radiobutton(f2,text="111",variable=i5,value=2)
    o52.pack()
    o53=Radiobutton(f2,text="101",variable=i5,value=3)
    o53.pack()
    o54=Radiobutton(f2,text="100",variable=i5,value=4)
    o54.pack()
#============================================QUESTIONS 6=====================================================================================    
    q6=Label(f2,text=("Q.6.When was First Mario game released?") ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    q6.pack()
    o61=Radiobutton(f2,text="1985",variable=i6,value=1)
    o61.pack()
    o62=Radiobutton(f2,text="1965",variable=i6,value=2)
    o62.pack()
    o63=Radiobutton(f2,text="1975",variable=i6,value=3)
    o63.pack()
    o64=Radiobutton(f2,text="1989",variable=i6,value=4)
    o64.pack()
    
    btnexit=Button(f2,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Exit", bg="grey",command=qexit)
    btnexit.pack(side=BOTTOM)
    btncheck=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Check Score", bg="grey",command=check)
    btncheck.pack(side=BOTTOM)

#==============================================RESET=======================================================================================
def reset():
    name.set(" ")
    cls.set(" ")
    sec.set(" ")
    rn.set(" ")

#==============================================Registration=================================================================================
def registration():
    reg=Toplevel()
    reg.title("REGISTRATION")
    reg.geometry("1000x700")
    labelreg=Label(reg,text="REGISTRATION" ,font=( 'TechHaus' ,60 ),fg="grey",bd=10,anchor='w')
    labelreg.pack()
    label1=Label(reg,text="CREATED AND DEVELOPED BY RITICK KUMAR" ,font=( 'brushield' ,16),fg="grey",bd=10,anchor='w')
    label1.pack()
    label1=Label(reg,text="NAME" ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    label1.pack()
    entryname= Entry(reg,font=('ariel' ,20,'bold'), textvariable=name , bd=6,insertwidth=4,bg="white" ,justify='right')
    entryname.pack()
    label1=Label(reg,text="CLASS" ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    label1.pack()
    entrycls= Entry(reg,font=('ariel' ,20,'bold'), textvariable=cls, bd=6,insertwidth=4,bg="white" ,justify='right')
    entrycls.pack()
    label1=Label(reg,text="SECTION" ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    label1.pack()
    entrysec= Entry(reg,font=('ariel' ,20,'bold'), textvariable=sec, bd=6,insertwidth=4,bg="white" ,justify='right')
    entrysec.pack()
    label1=Label(reg,text="ROLL NUMBER" ,font=( 'ariel',16,'bold'),fg="grey",bd=10,anchor='w')
    label1.pack()
    entryrolln= Entry(reg,font=('ariel' ,20,'bold'), textvariable=rn, bd=6,insertwidth=4,bg="white" ,justify='right')
    entryrolln.pack()
    btnreg=Button(reg,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="REGISTER", bg="grey",command=startquiz)
    btnreg.pack()

    btnreset=Button(reg,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="grey",command=reset)
    btnreset.pack()
   

    




#==============================================LOGIN=====================================================================================
def login():
    password=pwd.get()
    if password=="vi":
        registration()
    else:
        root.destroy()

 
#===============================================LOGIN PANEL===============================================================================
photo=PhotoImage(file="1.png")
img=Label(image=photo)
img.pack()

a1= Entry(root,font=('ariel' ,20,'bold'), textvariable=pwd ,show="*", bd=6,insertwidth=10,bg="yellow" ,justify='right')
a1.pack()
btnlogin=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="LOGIN", bg="grey",command=login)
btnlogin.pack()



mainloop()
