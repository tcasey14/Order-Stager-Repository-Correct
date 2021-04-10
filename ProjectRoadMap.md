Project Road Map for Order Stager
For project in IS 3020
The best example of code that could relate to what I am doing for this project was a BMI calculator. For the project, I want to change it to be able to enter height,length, and potentially weight of an object and then prompt the user where merchandise should be displayed.Ideally, I also want to have a set number each area can have merchandise staged in, so that areas do not get merchandise in them that are already filled. The code base is similar to a calculator, so the main thing that will be changed is the output going from spitting out numbers to arbitrary locations of a store. 



# Imports all from Tkinter GUI package
from tkinter import *

# Initialization
app = Tk()
ma = IntVar(None)
he = IntVar(None)
b = IntVar(None)


# Calculates the BMI with user-given data and puts user in one of three categories
# Also checks if entered value for height is not zero
def calculate_bmi():
    try:
        re = float(mass.get()) / (float(height.get()) * float(height.get()))
        b.set(re)
    except ZeroDivisionError:
        ma.set(None)
        he.set(None)
        b.set(None)
        return
    if re < 18.5:
        resLabelText.set("and you are categorised as Underweight!")
    if 18.5 < re < 25:
        resLabelText.set("and you are categorised as Normal!")
    if re > 25:
        resLabelText.set("and you are categorised as Overweight!")
    return


# Sets size and title
app.geometry("350x200+100+100")
app.title("PyBMI")

# Label and text box for mass
mLabelText = StringVar()
mLabelText.set("Enter your mass in kg: ")
massLabel = Label(app, textvariable=mLabelText)
massLabel.pack()

mass = Entry(app, textvariable=ma)
mass.pack()

# Label and text box for height
hLabelText = StringVar()
hLabelText.set("Enter your height in m: ")
heightLabel = Label(app, textvariable=hLabelText)
heightLabel.pack()

height = Entry(app, textvariable=he)
height.pack()

# Button and label and textbox for BMI calculation
button = Button(app, text="Calculate BMI", command=calculate_bmi)
button.pack(padx=15, pady=15)
bmiLabelText = StringVar()
bmiLabelText.set("Your BMI is: ")
bmiLabel = Label(app, textvariable=bmiLabelText)
bmiLabel.pack()

bmi = Entry(app, textvariable=b)
bmi.pack()
resLabelText = StringVar()
resLabelText.set(" and you are categorised as: ")
resLabel = Label(app, textvariable=resLabelText)
resLabel.pack()

# Starts the GUI
app.mainloop()
