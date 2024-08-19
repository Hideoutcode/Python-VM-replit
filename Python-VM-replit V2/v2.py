import webbrowser
import tkinter as tk
import subprocess



#browserss

def browserss():
    webbrowser.open("https://www.google.com")


#edit
def edit():
    placeholder = 0

#customization
def tools():
    placeholder = 0

#notepad
def notepad():
    placeholder = "Notepad"

# calculator

def addition():
    global calc1, calc2, addprod
    try:
        calc1 = float(calc1.get())
        calc2 = float(calc2.get())
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return

    addprod = calc1 + calc2
    print(addprod)

def subtraction():
    global calc1, calc2, subprod
    try:
        calc1 = float(calc1.get())
        calc2 = float(calc2.get())
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return

    subprod = calc1 - calc2
    print(subprod)

def multiply():
    global calc1, calc2, prod
    try:
        calc1 = float(calc1.get())
        calc2 = float(calc2.get())
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return

    prod = calc1 * calc2
    print(prod)

def divide():
    global calc1, calc2, divprod
    try:
        calc1 = float(calc1.get())
        calc2 = float(calc2.get())
        if calc2 == 0:
            print("Error: Cannot divide by zero.")
            return
        divprod = calc1 / calc2
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return
    print(divprod)

def calc():
    global calc1, calc2
    calc = tk.Tk()
    calc.title("Calculator")
    calc.geometry("300x300")
    calc.configure(bg="gray")

    calc1 = tk.Entry(calc, width=10)
    calc1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    calc2 = tk.Entry(calc, width=10)
    calc2.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    # Center the buttons
    calc_add = tk.Button(calc, text="+", width=5, command=addition)
    calc_add.grid(row=2, column=0, padx=50, pady=20)  # Added padding for centering

    calc_sub = tk.Button(calc, text="-", width=5, command=subtraction)
    calc_sub.grid(row=2, column=1, padx=50, pady=20)  # Added padding for centering

    calc_mul = tk.Button(calc, text="*", width=5, command=multiply)
    calc_mul.grid(row=3, column=0, padx=50, pady=20)  # Added padding for centering

    calc_divide = tk.Button(calc, text="/", width=5, command=divide)
    calc_divide.grid(row=3, column=1, padx=50, pady=20)  # Added padding for centering

    # end calculator 




root = tk.Tk()
label = tk.Label(root, text='OS')
label.pack()
root.geometry("500x500")
root.title("OS")
root.configure(bg="skyblue")






menubar = tk.Menu(root)
#filemenu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
filemenu.add_command(label="browser", command=lambda: webbrowser.open("https://www.google.com"))
menubar.add_cascade(label="File", menu=filemenu)


# Create a new "Tools" menu
toolsmenu = tk.Menu(menubar, tearoff=0)
toolsmenu.add_command(label="Edit", command=edit)
toolsmenu.add_command(label="customization", command=tools)
menubar.add_cascade(label="Tools", menu=toolsmenu)

#calc
calculators = tk.Menu(menubar, tearoff=0)
calculators.add_command(label="Calculator", command=calc)
menubar.add_cascade(label="Calculator", menu=calculators)

#notepad
notepads = tk.Menu(menubar, tearoff=0)
notepads.add_command(label="Notepad", command=notepad)
menubar.add_cascade(label="Notepad", menu=notepads)


#browser
browsers = tk.Menu(menubar, tearoff=0)
browsers.add_command(label="Google", command=browserss)
browsers.add_cascade(label="Google Chrome" , menu=browsers)

root.config(menu=menubar)


root.mainloop()