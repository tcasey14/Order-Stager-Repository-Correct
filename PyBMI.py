# Imports all from Tkinter GUI package
from tkinter import *

# Initialization
app = Tk()
ma = IntVar(None)
he = IntVar(None)
b = IntVar(None)
us = StringVar(None)

# Calculates the length times height and also weight with user-given data and puts merchandise in one of three staging locations (for the measurements I used approximate values that I thought would make sense from my experiences at work. )
def stage_product():
    try:
        re = float(mass.get()) 
        fe = float(height.get())
        b.set(re)
        us = str(user.get())
        
    except ZeroDivisionError:
        ma.set(None)
        he.set(None)
        b.set(None)
        us.set(None)
        return
        #if statements
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
    if us == "quit":
        resLabelText.set("Not a valid location, please enter the merchandise's measurements again")
    if us == "Too Big":
        resLabelText.set("Please stage somewhere on Back Wall")
    if us == "Too Small":
        resLabelText.set("Please stage somewhere at Service or Pro Desk")
    if us == "not enough space in assigned space":
        resLabelText.set("Try to stage in receiving or coordinate with management")
    return  
# Sets size and title
app.geometry("350x200+100+100")
app.title("Home Depot Online Order Stager")

# Label and text box for length times height of merchandise
mLabelText = StringVar()
mLabelText.set("Welcome to The Home Depot Online Order Stager! Enter the approximate merchandise length and height multiplied together in FT.: ")
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
#User input to ensure product can be staged properly
uLabelText = StringVar()
uLabelText.set("What location will the merchandise be staged in based on the app's prompt?(Also, type 'Too Small','Too Big','not enough space in assigned space' or 'quit' to get a different prompt.)")
userLabel = Label(app, textvariable=uLabelText)
userLabel.pack()

user = Entry(app, textvariable=us)
user.pack()

# Buttons,labels,and textbox for Order Stager Function
button = Button(app, text="Stage Product", command=stage_product)
button.pack(padx=15, pady=15)
bmiLabelText = StringVar()
bmiLabelText.set("Stage product in: ")


bmi = Entry(app, textvariable=b)
bmi.pack()
resLabelText = StringVar()
resLabelText.set("Stage the merchandise in:")
resLabel = Label(app, textvariable=resLabelText)
resLabel.pack()

button = Button(app, text="Final Stage", command=stage_product)
button.pack(padx=15, pady=15)
bmiLabelText = StringVar()
bmiLabelText.set("Product is staged in:")
bmiLabelText
bmiLabel = Label(app, textvariable=bmiLabelText)
bmiLabel.pack()
user = Entry(app, textvariable=us)
user.pack()


# Starts the GUI
app.mainloop()


