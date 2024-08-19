import webbrowser
import tkinter as tk
import subprocess



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

button1 = tk.Button(root, text="🧭", command=lambda: webbrowser.open("https://www.google.com"), width=1, height=1)
button1.pack(side="bottom")
button2 = tk.Button(root, text="🖩", command=calc, width=1, height=1)
button2.pack(side="bottom")

button3 = tk.Button(root, text="📝", command=notepad, height=1, width=1)
button3.pack(side="bottom")


root.mainloop()