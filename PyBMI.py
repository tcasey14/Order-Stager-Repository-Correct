#Inports all from Tkinter GUI package
from Tkinter import *

#Calculates the BMI with user-given data and puts user in one of three categories
#Also checks if entered value for height is not zero
def calculateBMI():
	try:
		re = float(mass.get())/(float(height.get()) * float(height.get()))
		b.set(re)
	except ZeroDivisionError:
		ma.set(None)
		he.set(None)
		b.set(None)
		return
	if(re < 18.5): 
		resLabelText.set("and you are categorised as Underweight")
	if(re > 18.5 and re < 25): 
		resLabelText.set("and you are categorised as Normal")
	if(re > 25): 
		resLabelText.set("and you are categorised as Overweight")
	return

#Initializes GUI and sets size and title
app = Tk()
app.geometry("350x200+100+100")
app.title("PyBMI")

#Label and text box for mass
mLabelText = StringVar()
mLabelText.set("Enter your mass in kg:")
massLabel = Label(app, textvariable = mLabelText)
massLabel.pack()
ma = IntVar(None)
mass = Entry(app, textvariable = ma)
mass.pack()

#Label and text box for height
hLabelText = StringVar()
hLabelText.set("Enter your height in m")
heightLabel = Label(app, textvariable = hLabelText)
heightLabel.pack()
he = IntVar(None)
height = Entry(app, textvariable = he)
height.pack()

#Button and label and textbox for BMI calculation
button = Button(app, text="Calculate BMI", command = calculateBMI)
button.pack(padx = 15, pady = 15)
bmiLabelText = StringVar()
bmiLabelText.set("Your BMI is: ")
bmiLabel = Label(app, textvariable = bmiLabelText)
bmiLabel.pack()
b = IntVar(None)
bmi = Entry(app, textvariable = b)
bmi.pack()
resLabelText = StringVar()
resLabelText.set("and you are categorised as ")
resLabel = Label(app, textvariable = resLabelText)
resLabel.pack()

#Starts the GUI
app.mainloop()