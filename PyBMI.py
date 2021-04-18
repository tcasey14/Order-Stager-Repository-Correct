# Imports all from Tkinter GUI package
from tkinter import *

# Initialization
app = Tk()
ma = IntVar(None)
he = IntVar(None)
b = IntVar(None)


# Calculates the BMI with user-given data and puts user in one of three categories
# Also checks if entered value for height is not zero
def stage_product():
    try:
        re = float(mass.get()) + (float(height.get()))
        b.set(re)
    except ZeroDivisionError:
        ma.set(None)
        he.set(None)
        b.set(None)
        return
    if re < 25:
        resLabelText.set("Stage product at Service Desk (SD-001-SD-010")
    if 25 < re < 50:
        resLabelText.set("Stage product at Service Desk (SD-011-SD-020")
    if 50 < re < 100:
        resLabelText.set("Stage product at Service Desk (SD-021-SD-030")
    if 100 < re < 125:
        resLabelText.set("Stage product at Pro Desk (PD-001-PD-020")
    if 125 < re < 200:
        resLabelText.set("Stage product at Pro Desk (PD-021-PD-040)")
    if 200 < re:
        resLabelText.set("Stage product at Back Wall (X1-001-100")
    return


# Sets size and title
app.geometry("350x200+100+100")
app.title("Online Order Stager")

# Label and text box for mass
mLabelText = StringVar()
mLabelText.set("Enter the merchandise height in FT.: ")
massLabel = Label(app, textvariable=mLabelText)
massLabel.pack()

mass = Entry(app, textvariable=ma)
mass.pack()

# Label and text box for height
hLabelText = StringVar()
hLabelText.set("Enter your merchandise width in  FT.: ")
heightLabel = Label(app, textvariable=hLabelText)
heightLabel.pack()

height = Entry(app, textvariable=he)
height.pack()

# Button and label and textbox for BMI calculation
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


# Starts the GUI
app.mainloop()

