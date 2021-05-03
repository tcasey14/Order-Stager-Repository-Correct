# Imports all from Tkinter GUI package
from tkinter import *

# Initialization
app = Tk()
ma = IntVar(None)
he = IntVar(None)
b = IntVar(None)


# Calculates the length times height and also weight with user-given data and puts merchandise in one of three staging locations (for the measurements I used approximate values that I thought would make sense from my experiences at work. )
def stage_product():
    try:
        re = float(mass.get()) 
        fe = float(height.get())
        b.set(re)
    except ZeroDivisionError:
        ma.set(None)
        he.set(None)
        b.set(None)
        return
    if re < 8:
        resLabelText.set("Stage product at Service Desk (SD-001-SD-010)")
    if 8 < re < 10:
        resLabelText.set("Stage product at Service Desk (SD-011-SD-020)")
    if 12 < re < 15:
        resLabelText.set("Stage product at Service Desk (SD-021-SD-030)")
    if 15 < re < 20:
        resLabelText.set("Stage product at Pro Desk (PD-001-PD-020)")
    if 20 < re < 25:
        resLabelText.set("Stage product at Pro Desk (PD-021-PD-040)")
    if 25 < re:
        resLabelText.set("Stage product at Back Wall (X1-001-100)")
    if 150 < fe:
        resLabelText.set("Stage product at Back Wall (X1-001-100)")
    if fe < 150:
        resLabelText.set("Stage product at Service Desk (SD-001-SD-030)")
    return


# Sets size and title
app.geometry("350x200+100+100")
app.title("Online Order Stager")

# Label and text box for length times height of merchandise
mLabelText = StringVar()
mLabelText.set("Enter the approximate merchandise length and height multiplied together in FT.: ")
massLabel = Label(app, textvariable=mLabelText)
massLabel.pack()

mass = Entry(app, textvariable=ma)
mass.pack()

# Label and text box for weight of merchandise
hLabelText = StringVar()
hLabelText.set("Enter your approximate merchandise weight in  LB. if over 150 pounds: ")
heightLabel = Label(app, textvariable=hLabelText)
heightLabel.pack()

height = Entry(app, textvariable=he)
height.pack()

# Buttons,labels,and textbox for Order Stager Function
button = Button(app, text="Stage Product", command=stage_product)
button.pack(padx=15, pady=15)
bmiLabelText = StringVar()
bmiLabelText.set("Stage product in: ")
bmiLabel = Label(app, textvariable=bmiLabelText)
bmiLabel.pack()

bmi = Entry(app, textvariable=b)
bmi.pack()
resLabelText = StringVar()
resLabelText.set("Stage the merchandise in:")
resLabel = Label(app, textvariable=resLabelText)
resLabel.pack()

#User input to ensure product can be staged properly
uLabelText = StringVar()
uLabelText = input("What location will the merchandise be staged in based on the app's prompt?(Also, type 'Too Small','Too Big','not enough space in assigned space' or nothing to get a different prompt.")
if uLabelText == "":
   print("Not a valid location, please enter the merchandise's measurements again")
elif uLabelText == "Too Big":
    print("Please stage somewhere on Back Wall")
elif uLabelText == "Too Small":
    print("Please stage somewhere at Service or Pro Desk")
elif uLabelText == "not enough space in assigned space":
    print("Try to stage in receiving or coordinate with management")
else:
    print("Order is staged in ", uLabelText)
    
# Starts the GUI
app.mainloop()

