from tkinter import *
root=Tk()
root.geometry("1000x500")
root.title("KAATHI HOUSE")
root.resizable(False,False)

def Reset():
    entry_Kaathiroll.delete(0,END)
    entry_Paratha.delete(0,END)
    entry_CholeB.delete(0,END)
    entry_chillipotato.delete(0,END)
    entry_KHWrap.delete(0,END)
    entry_Vanila.delete(0,END)
    entry_pavbhaji.delete(0,END)
    Total_bill.set("")
    txt.delete('1.0',END)
#######################################################################

    

##################################################################
def Total():
    try:a1=int(Kaathiroll.get())
    except:a1=0

    try:a2=int(Paratha.get())
    except:a2=0

    try:a3=int(CholeB.get())
    except:a3=0

    try:a4=int(chillipotato.get())
    except:a4=0

    try:a5=int(pavbhaji.get())
    except:a5=0

    try:a6=int(KHWrap.get())
    except:a6=0

    try:a7=int(Vanila.get())
    except:a7=0

    #define cost of each item per quantity
    c1=65*a1
    c2=55*a2
    c3=75*a3
    c4=70*a4
    c5=90*a5
    c6=100*a6
    c7=200*a7




    txt.delete('1.0',END)
    txt.insert(END,"       Welcome To KAATHI ROLL\n")
    txt.insert(END,"\n==================================")
    txt.insert(END,"\nProduct          Qty         Price")
    txt.insert(END,"\n==================================")

#######################################################################################################

        
    if Kaathiroll.get() !="":
        txt.insert(END,f"\nKaathiroll         {int(Kaathiroll.get())}          {c1}")
    if Paratha.get() != "":
        txt.insert(END,f"\nParatha            {int(Paratha.get())}           {c2}")
    if CholeB.get() != "":
        txt.insert(END,f"\nCholeB             {int(CholeB.get())}             {c3}")
    if chillipotato.get() != "":
        txt.insert(END,f"\nchillipotato       {int(chillipotato.get())}       {c4}")
    if pavbhaji.get() != "" :
        txt.insert(END,f"\npavBhaji           {int(pavbhaji.get())}           {c5}")
    if KHWrap.get() != "":
        txt.insert(END,f"\nKhWrap             {int(KHWrap.get())}             {c6}")
    if Vanila.get() != "":
        txt.insert(END,f"\nVanila             {int(Vanila.get())}             {c7}")
    txt.insert(END,"\n==================================")

 ##############################################################################

    lbl_total=Label(f2,font=("aria",10,"bold"),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=70,y=295)

    entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="beige")
    entry_total.place(x=20,y=320)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f'%totalcost)
    Total_bill.set(string_bill)
Label(text="KAATHI HOUSE",bg="lightblue",fg="black",font=("Times",33,"bold"),width="300",height="2").pack()
#Menu Card
f=Frame(root,bg="beige",highlightbackground="black",highlightthickness=4,width=300,height=370)
f.place(x=10,y=118)
Label(f,text="Menu",font=("Times",28,"bold","underline"),fg="black",bg="beige",justify=CENTER).place(x=80,y=5)
Label(f,font=("Times",17,),text="Kathi Roll-Rs.65   ",fg="black",bg="beige",justify=CENTER).place(x=40,y=80)
Label(f,font=("Times",17),text="Paratha-Rs.55    ",fg="black",bg="beige",justify=CENTER).place(x=40,y=110)
Label(f,font=("Times",17),text="Chole Bhature-Rs.75 ",fg="black",bg="beige",justify=CENTER).place(x=40,y=140)
Label(f,font=("Times",17),text="Chilli Potato-Rs.70   ",fg="black",bg="beige",justify=CENTER).place(x=40,y=170)
Label(f,font=("Times",17),text="Pav bhaji-Rs.90    ",fg="black",bg="beige",justify=CENTER).place(x=40,y=200)
Label(f,font=("Times",17),text="KH Wrap-Rs.100",fg="black",bg="beige",justify=CENTER).place(x=40,y=230)
Label(f,font=("Times",17,),text="Vanila Cake-Rs.200",fg="black",bg="beige",justify=CENTER).place(x=40,y=260)

#BILL
f2=Frame(root,bg="white",highlightbackground="black",highlightthickness=1)
f2.place(x=690,y=118,width=300,height=370)

Bill=Label(f2,text="Bill Area",font=("Times",20,"bold"),bd=7,relief=GROOVE)
Bill.pack(fill=X)
scroll_y=Scrollbar(f2,orient=VERTICAL)
txt=Text(f2,yscrollcommand=scroll_y.set) 
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=txt.yview)
txt.pack(fill=BOTH,expand=1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       


#Entry Work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Kaathiroll=StringVar()
Paratha=StringVar()
CholeB=StringVar()
chillipotato=StringVar()
pavbhaji=StringVar()
KHWrap=StringVar()
Vanila=StringVar()
Total_bill=StringVar()

#Label

lbl_Kaathiroll=Label(f1,font=("Times", 20, 'bold'), text="Kathi Roll", width=12,fg="Black")
lbl_Paratha=Label(f1,font=("Times", 20, 'bold'), text="Paratha", width=12,fg="black")
lbl_CholeB=Label(f1,font=("Times", 20, 'bold'), text="Chole Bhature", width=12,fg="black")
lbl_chillipotato=Label(f1,font=("Times", 20, 'bold'), text="Chilli Potato", width=12,fg="black")
lbl_pavbhaji=Label(f1,font=("Times", 20, 'bold'), text="Pav bhaji", width=12,fg="black")
lbl_KHWrap=Label(f1,font=("Times", 20, 'bold'), text="KH Wrap", width=12,fg="black")
lbl_Vanila=Label(f1,font=("Times", 20, 'bold'), text="Vanila Cake", width=12,fg="black")

lbl_Kaathiroll.grid(row=1, column=0)
lbl_Paratha.grid(row=2, column=0)
lbl_CholeB.grid(row=3, column=0)
lbl_chillipotato.grid(row=4, column=0)
lbl_pavbhaji.grid(row=5, column=0)
lbl_KHWrap.grid(row=6, column=0)
lbl_Vanila.grid(row=7, column=0)
#Entry
entry_Kaathiroll=Entry (f1, font=("Times", 20, 'bold'),justify=CENTER, textvariable=Kaathiroll,bd=6, width=8, bg="Grey")
entry_Paratha=Entry (f1, font=("Times", 20, 'bold'), justify=CENTER, textvariable=Paratha,bd=6, width=8, bg="beige")
entry_CholeB=Entry (f1, font=("Times", 20, 'bold'), justify=CENTER, textvariable=CholeB,bd=6, width=8, bg="Grey")
entry_chillipotato=Entry (f1, font=("Times", 20, 'bold'), justify=CENTER, textvariable=chillipotato,bd=6, width=8, bg="beige")
entry_pavbhaji=Entry (f1, font=("Times", 20, 'bold'), justify=CENTER,textvariable=pavbhaji,bd=6, width=8, bg="grey")
entry_KHWrap=Entry (f1, font=("Times", 20, 'bold'),justify=CENTER, textvariable=KHWrap,bd=6, width=8, bg="beige")
entry_Vanila=Entry (f1, font=("Times", 20, 'bold'),justify=CENTER, textvariable=Vanila,bd=6, width=8, bg="grey")

entry_Kaathiroll.grid(row=1, column=1)
entry_Paratha.grid(row=2, column=1)
entry_CholeB.grid(row=3, column=1)
entry_chillipotato.grid(row=4, column=1)
entry_pavbhaji.grid(row=5, column=1)
entry_KHWrap.grid(row=6, column=1)
entry_Vanila.grid(row=7, column=1)

#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("Times",16,'bold'),width=10,text='Reset',command=Reset)
btn_reset.grid(row=8,column=0)


btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("Times",16,'bold'),width=9,text="Total",command=Total)
btn_total.grid(row=8,column=1)



root.mainloop()
