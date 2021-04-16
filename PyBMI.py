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
        re = float(mass.get()) / (float(height.get()) * float(height.get()))
        b.set(re)
    except ZeroDivisionError:
        ma.set(None)
        he.set(None)
        b.set(None)
        return
    if re < 50:
        resLabelText.set("Stage product at Service Desk (SD-001-050)")
    if 50 < re < 150:
        resLabelText.set("Stage product at Pro Desk (PD-001-050")
    if re > 150:
        resLabelText.set("Stage product along Back Wall or outside (BW-001 or X1-001)")
    return


# Sets size and title
app.geometry("350x200+100+100")
app.title("Online Order Stager")

# Label and text box for mass
mLabelText = StringVar()
mLabelText.set("Enter the merchandise weight in LB.: ")
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

