from tkinter  import*
import time
import random

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restraurant management system")


Top = Frame(root, relief=SUNKEN,width=1600,bg="powder blue")
Top.pack(side=TOP)

f1 = Frame(root, relief=SUNKEN,width=1000,height=700,bg="grey")
f1.pack(side=LEFT)

f2 = Frame(root, relief=SUNKEN,width=300,height=700,bg="orange")
f2.pack(side=RIGHT)
text_input = StringVar()
operator = ""
'''lacal time generator '''
localtime = time.asctime(time.localtime(time.time()))
'''lable for the system'''
lableInfo = Label(Top, font=("arial",30,"bold"),text="    Restaurant  Management  System    ",anchor="w", fg="steel blue", bg="powder blue")
lableInfo.grid(row=0,column=0)

timeInfo = Label(Top, font=("arial",30,"bold"),text=localtime,anchor="w", fg="steel blue", bg="powder blue")
timeInfo.grid(row=1,column=0)
#================================calculator ============
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def clearBtn():
    global operator
    operator = ""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""
txtDisplay = Entry(f2, font=("arial",20,"bold"), text=text_input, bd=10,insertwidth=4,bg="powder blue",
 justify=CENTER)
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="7", bg="powder blue",
 command=lambda: btnClick(7)).grid(row=2,column=0)
btn8 = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="8", bg="powder blue",
 command=lambda: btnClick(8)).grid(row=2,column=1)
btn9 = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="9", bg="powder blue",
 command=lambda: btnClick(9)).grid(row=2,column=2)
btnPlus = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="+", bg="powder blue",
 command=lambda: btnClick("+")).grid(row=2,column=3)
btn4 = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="4", bg="powder blue",
 command=lambda: btnClick(4)).grid(row=3,column=0)
btn5 = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="5", bg="powder blue",
 command=lambda: btnClick(5)).grid(row=3,column=1)
btn6 = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="6", bg="powder blue",
 command=lambda: btnClick(6)).grid(row=3,column=2)
btnMinus = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="-", bg="powder blue",
 command=lambda: btnClick("-")).grid(row=3,column=3)
btn1 = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="1", bg="powder blue",
 command=lambda: btnClick(1)).grid(row=4,column=0)
btn2 = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="2", bg="powder blue",
 command=lambda: btnClick(2)).grid(row=4,column=1)
btn3 = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="3", bg="powder blue",
 command=lambda: btnClick(3)).grid(row=4,column=2)
btnTimes = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="*", bg="powder blue",
 command=lambda: btnClick("*")).grid(row=4,column=3)

btnZero = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="0", bg="powder blue",
 command=lambda: btnClick("0")).grid(row=5,column=0)

btnClear = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="C", bg="powder blue",
command=clearBtn).grid(row=5,column=1)

btnEquals = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="=", bg="powder blue",
command=btnEqualsInput).grid(row=5,column=2)

btnDivide = Button(f2, padx=16,font=("arial",15,"bold"), pady=16,bd=8,fg="black", text="/", bg="powder blue",
 command=lambda: btnClick("/")).grid(row=5,column=3)

#===========================================meals details======
rand = StringVar()
fries = StringVar()
burger = StringVar()
filet = StringVar()
subTotal = StringVar()
Total = StringVar()
Service_charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()



lblReference = Label(f1, font=("arial",15,"bold"),text="Reference",bd=10,fg="Black",bg="powder blue",anchor="w")
lblReference.grid(row=0,column=0)

txtReference = Entry(f1, state=DISABLED, font=("arial",15,"bold"),text=rand,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtReference.grid(row=0,column=1)

lblFries = Label(f1, font=("arial",15,"bold"),text="Large Fries",bd=10,fg="Black",bg="powder blue",anchor="w")
lblFries.grid(row=1,column=0)

txtFries = Entry(f1, font=("arial",15,"bold"),text=fries,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtFries.grid(row=1,column=1)

lblBurger = Label(f1, font=("arial",15,"bold"),text="Burger",bd=10,fg="Black",bg="powder blue",anchor="w")
lblBurger.grid(row=2,column=0)

txtBurger = Entry(f1, font=("arial",15,"bold"),text=burger,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtBurger.grid(row=2,column=1)

lblFilet = Label(f1, font=("arial",15,"bold"),text="Filet",bd=10,fg="Black",bg="powder blue",anchor="w")
lblFilet.grid(row=3,column=0)

txtFilet = Entry(f1, font=("arial",15,"bold"),text=filet,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtFilet.grid(row=3,column=1)

lblSubTotal = Label(f1, font=("arial",15,"bold"),text="Sub Total",bd=10,fg="Black",bg="powder blue",anchor="w")
lblSubTotal.grid(row=4,column=2)

txtSubTotal = Entry(f1, font=("arial",15,"bold"),text=subTotal,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtSubTotal.grid(row=4,column=3)

lblTotal = Label(f1, font=("arial",15,"bold"),text="Total",bd=10,fg="Black",bg="powder blue",anchor="w")
lblTotal.grid(row=5,column=2)

txtTotal = Entry(f1, font=("arial",15,"bold"),text=Total,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtTotal.grid(row=5,column=3)

lblService = Label(f1, font=("arial",15,"bold"),text="Service Charge",bd=10,fg="Black",bg="powder blue",anchor="w")
lblService.grid(row=2,column=2)

txtService = Entry(f1, font=("arial",15,"bold"),text=Service_charge,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtService.grid(row=2,column=3)

lblDrinks = Label(f1, font=("arial",15,"bold"),text=" Drinks ",bd=10,fg="Black",bg="powder blue",anchor="w")
lblDrinks.grid(row=0,column=2)

txtDrinks = Entry(f1, font=("arial",15,"bold"),text=Drinks,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtDrinks.grid(row=0,column=3)

lblTax = Label(f1, font=("arial",15,"bold"),text=" Tax ",bd=10,fg="Black",bg="powder blue",anchor="w")
lblTax.grid(row=3,column=2)

txtTax = Entry(f1, font=("arial",15,"bold"),text=Tax,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtTax.grid(row=3,column=3)

lblCost = Label(f1, font=("arial",15,"bold"),text=" Cost ",bd=10,fg="Black",bg="powder blue",anchor="w")
lblCost.grid(row=1,column=2)

txtCost = Entry(f1, font=("arial",15,"bold"),text=Cost,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtCost.grid(row=1,column=3)

lblChicken_Burger = Label(f1, font=("arial",15,"bold"),text="Chicken Burger",bd=10,fg="Black",bg="powder blue",anchor="w")
lblChicken_Burger.grid(row=4,column=0)

txtChicken_Burger = Entry(f1, font=("arial",15,"bold"),text=Chicken_Burger,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtChicken_Burger.grid(row=4,column=1)

lblCheese_Burger = Label(f1, font=("arial",15,"bold"),text="Cheese Burger",bd=10,fg="Black",bg="powder blue",anchor="w")
lblCheese_Burger.grid(row=5,column=0)

txtCheese_Burger = Entry(f1, font=("arial",15,"bold"),text=Cheese_Burger,bd=10,bg="powder blue",justify=RIGHT,insertwidth=4)
txtCheese_Burger.grid(row=5,column=1)

#========================== Buttons ================
def Ref():
    x = random.randint(10000,50000)
    randomRef = "x1x1z" +str(x)
    rand.set(randomRef)

    CoF = float(fries.get())
    CoB = float(burger.get())
    CoD = float(Drinks.get())
    CoCB = float(Chicken_Burger.get())
    CoCheeseB= float(Cheese_Burger.get())
    cost_of_fries = CoF * 2.3
    cost_of_burgers = CoB * 1.5
    cost_of_drinks = CoD * 2.1
    cost_of_chicken_bugers = CoCB * 3.1
    cost_of_cheese_bugers = CoCheeseB * 2.5

    cost_of_meal = "$ ", str("%.2f" % (cost_of_fries + cost_of_burgers + cost_of_drinks + cost_of_chicken_bugers + cost_of_cheese_bugers))

    PayTax = ((cost_of_fries + cost_of_burgers + cost_of_drinks + cost_of_chicken_bugers + cost_of_cheese_bugers) * 0.2)

    TotalCost = (cost_of_fries + cost_of_burgers + cost_of_drinks + cost_of_chicken_bugers + cost_of_cheese_bugers)

    Ser_Charge = ((cost_of_fries + cost_of_burgers + cost_of_drinks + cost_of_chicken_bugers + cost_of_cheese_bugers) / 99)

    Service = "$ ", str("%.2f" % Ser_Charge)

    OverAllCost = "$", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = "$ " , str('%.2f' % PayTax)

    subTotal.set(TotalCost)
    Service_charge.set(Service)
    Cost.set(cost_of_meal)
    Tax.set(PaidTax)
    Total.set(OverAllCost)

def Exit():
    root.destroy()

def Reset():
    rand.set("")
    fries.set("")
    burger.set("")
    filet.set("")
    subTotal.set("")
    Total.set("")
    Service_charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")

btnRef = Button(f1,bg="powder blue",font=("arial",15,"bold"),padx=16, pady=8, text=" Reference ", width=10,command=Ref ).grid(row=7,column=1)
btnTotal = Button(f1,bg="powder blue",font=("arial",15,"bold"),padx=16, pady=8, text=" Total ", width=10,command=Ref ).grid(row=7,column=2)
btnReset = Button(f1,bg="powder blue",font=("arial",15,"bold"),padx=16, pady=8, text=" Reset ", width=10,command=Reset ).grid(row=7,column=3)
btnExit = Button(f1,bg="powder blue",font=("arial",15,"bold"),padx=16, pady=8, text=" Exit ", width=10,command=Exit ).grid(row=7,column=4)



root.mainloop()