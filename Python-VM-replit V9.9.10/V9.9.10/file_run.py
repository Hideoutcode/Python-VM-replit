import webbrowser
import tkinter as tk
import time
import subprocess








#shell 


def exec(command_input):
    command = command_input.get()
    print(command)
    commanddata = ["> Tk.Show.User", "> Tk.Exit", "> Tk.Notepad", "> Tk.Version", "> Tk.Help"]
    if command in commanddata:
        if command == "> Tk.Show.User":
            users = "> Commercial User --- Admin \n FALSE"
            command_input.delete(0, tk.END)
            command_input.insert(tk.END, users)



        elif command == "> Tk.Exit":
            exit()
        elif command == "> Tk.Notepad":
            shell1.destroy()
            notepad()

        elif command == "> Tk.Version":
            version = "> Python-VM-Replit V 0.7.12"
            command_input.delete(0, tk.END)
            command_input.insert(tk.END, version)

        elif command == "> Tk.Help":
            command_input.delete(0, tk.END)
            command_input.insert(tk.END, commanddata)



def shell():
    global command_input, shell1
    shell1 = tk.Toplevel()
    shell1.title(">_")
    shell1.geometry("300x300")
    shell1.configure(bg="steelblue4")
    command_input = tk.Entry(shell1, width=50, bg="steelblue3")
    command_input.pack(pady=10)
    command_input.insert(0, "> ")
    execute = tk.Button(shell1, text="EXEC",bg="red", command=lambda: exec(command_input))
    execute.pack(side="bottom", pady = 5)
   #end shell  


#savefile

def saves(filename):
    global file_content
    with open(filename, "a") as thefile:
        thefile.write(file_content)
        thefile.close()




def savefile(Filename, file_cont):
    global file_entry, file_content
    filename = Filename
    file_content = file_entry.get("1.0", tk.END)
    saves(filename.get())


#openfile





# file_cont = file_entry.get("1.0", tk.END)

def openfile(Filename):
    filename = Filename.get() #file name
    with open(filename, "r") as thefile:

        if filename != "user.py" and  filename != "main.py" and filename != "file_run.py":
         content =  thefile.read()
         file_entry.insert( tk.END, content)
         thefile.close()

        if filename == "user.py":
            forb = "Error 314 Forbidden file"
            file_entry.insert(tk.END, forb + "\n")
            

        if filename == "main.py":
            forb = "Error 314 Forbidden file"
            file_entry.insert(tk.END, forb + "\n")

        if filename == "file_run.py":
            forb = "Error 314 Forbidden file"
            file_entry.insert(tk.END, forb + "\n")
        # end file Open()




#notepad
def notepad():
    global file_entry, Filename, file_cont
    notepad = tk.Tk()
    notepad.title("Notepad")
    notepad.geometry("400x400")
    notepad.resizable(False, False)
    
    #save file 
    button12 = tk.Button(notepad, text="Save File", command=lambda: savefile(Filename, file_cont))

    #openfile 
    button12.pack(side="right")
    button13 = tk.Button(notepad, text="Open File", command=lambda: openfile(Filename))
    button13.pack(side="left")

    #file entry
    file_entry = tk.Text(notepad, width=60, height=23)
    file_entry.pack(pady = 3)
    file_label = tk.Label(notepad, text="File Name").pack()
    #filename 
    Filename = tk.Entry(notepad)
    Filename.pack()
    file_cont = file_entry.get("1.0", tk.END)






#time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

#bCKGROUND
def background():
    global root, color_entry
    bg = tk.Tk()
    bg.geometry("200x100")
    bg.title("Background")
    label = tk.Label(bg, text="Background Color")
    label.pack()
    color_entry = tk.Entry(bg, width = 20)
    color_entry.pack()
    submit = tk.Button(bg, text="Submit", command= submits)
    submit.pack()

def submits():
    global color
    color = color_entry.get()
    root.configure(bg=color)
    

   
    
       
                
        
        
              

   
    


#browserss

def browserss():
    root.destroy()
    subprocess.call(["python", "search_engine.py"])


#edit
def edit():
    placeholder = 0

#customization
def tools():
    placeholder = 0






# calculator, do not edit or modify

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

    # end calculator, do not edit or modify

def out():
    root.destroy()
    subprocess.call(["python","Intro.py"])






root = tk.Tk()
root.geometry("500x500")
root.title("Python-VM-TK-Replit    v0.7.13")
root.configure(bg="skyblue")







#time lael
time_label = tk.Label(root, text="", font=("Arial", 12))
time_label.pack(side="bottom")
update_time()


menubar = tk.Menu(root)

#filemenu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New File", command=notepad)
filemenu.add_command(label="Open File", command=notepad)
filemenu.add_command(label="Exit", command=out)
menubar.add_cascade(label="File", menu=filemenu)


# Tools menu
toolsmenu = tk.Menu(menubar, tearoff=0)
toolsmenu.add_command(label="Edit", command=edit)
toolsmenu.add_command(label="customization", command=tools)
toolsmenu.add_command(label=">_", command=shell)
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
browsers.add_command(label="BROWSER", command=browserss)
menubar.add_cascade(label="Browser (SCRAPE)" , menu=browsers)


#settings
settings = tk.Menu(menubar, tearoff=0)
settings.add_command(label="Set Background", command=background)
settings.add_command(label="Sign Out", command=out)
menubar.add_cascade(label="Settings", menu=settings)





root.config(menu=menubar)


root.mainloop()

# Made by Zach H. 2024