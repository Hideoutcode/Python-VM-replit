import subprocess
import tkinter as tk
import smtplib
import ssl
from email.message import EmailMessage
import os


#automated emailing service

def send_email():
  email_sender = 'emailhere'
  email_password = 'email app password here or env variable'
  email_receiver = 'email reciever here must be also yours'
  body = message
  em = EmailMessage()
  em['From'] = email_sender
  em['to'] = email_receiver
  em.set_content(body)

  context = ssl.create_default_context()
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())







#after login is successful 






def worked():
    login_window.destroy()
    root.destroy()
    subprocess.call(["python", "file_run.py"])
    
    
#message creator 

def message_creater():
    global entry9, entry8, message_screen
    message_screen = tk.Tk()
    message_screen.geometry("500x500")
    message_screen.title("Reset Password")
    label8 = tk.Label(message_screen, text="Username and email", bg="gray")
    label8.pack(pady =5 )
    entry8 = tk.Entry(message_screen, bg="white")
    entry8.pack(padx = 10, pady = 10)
    label9 = tk.Label(message_screen, text="New Password", bg="gray")
    label9.pack(pady= 10, padx = 10)
    entry9 = tk.Entry(message_screen, bg="gray",)
    entry9.pack()
    button8 = tk.Button(message_screen, text="Reset", bg="red", command=send_c)
    button8.pack()


#send email here

def send_c():
  global message, user_email
  message = entry9.get()
  user_email = entry8.get()
  send_email()
  message_screen.destroy()




#admin

def back():
    admin1.destroy()
    subprocess.call(["python", "main.py" ])
    
    


def data():
   with open("user.py", "r") as thefile:
     files = thefile.read()
     untitled.get("1.0", tk.END)
     untitled.insert(tk.END, files)
     thefile.close()


def admin():
  global admin1, untitled
  login_window.destroy()
  root.destroy()
  admin1 = tk.Tk()
  admin1.geometry("300x350")
  admin1.title("Admin")
  admin1.configure(bg="dimgray")
  buttonb = tk.Button(admin1, text="Data", bg="red", height = 2, width = 15,  command=data)
  buttonb.pack(padx = 20, pady = 20)
  buttonc = tk.Button(admin1, text="Exit", bg="red", height = 2, width = 15, command=back)
  buttonc.pack(padx = 20, pady = 20)
  untitled = tk.Text(admin1, width = 30, height = 10)
  untitled.pack()
  




#login window made here in module

def logib():
   global entry1, entry2, username, login_window
   login_window = tk.Tk()
   login_window.title("Sign In VM OS")
   login_window.geometry("500x500")
   login_window.configure(bg="gray")
   label5 = tk.Label(login_window, text="Username: ")
   label5.pack(pady=20)
   entry1 = tk.Entry(login_window)
   entry1.pack(pady=0)
   label6 = tk.Label(login_window, text="Password: ")
   label6.pack(pady=20)
   entry2 = tk.Entry(login_window, show="*")
   entry2.pack(pady=0)
   submit_button = tk.Button(login_window, text="Submit", command=submit_form)
   submit_button.pack(pady=15)
   

#readlines to authenticate password and username 

def submit_form():
  global entry1, entry2, username, login_window
  if entry1 and entry2:
      username = entry1.get()
      password = entry2.get()
      with open('user.py', 'r') as file:
          lines = file.readlines()
          stored_users = [lines[i].strip() for i in range(0, len(lines), 2)]
          stored_passwords = [lines[i].strip() for i in range(1, len(lines), 2)]


          if username in stored_users and password == stored_passwords[stored_users.index(username)]:

            worked()

          else:
            tko = tk.Toplevel()
            tko.overrideredirect(True)
            tkl = tk.Label(tko, text="Invalid username or password", bg="red")
            tkl.pack(side="bottom")
            tko.after(700, tko.destroy)

          if username == "admin" and password =="admin":
            admin()

           
          
           

         







      #start after completing sign up. 



  #user sign up window here 


def signub():
   global user1, passw2, signup_window
   
   signup_window = tk.Tk()
   signup_window.title("Create Account")
   signup_window.geometry("500x500")
   signup_window.configure(bg="white")
   agree = tk.Label(signup_window, text="By signing up, you agree to our terms and conditions", bg="gray")
   agree.pack(side="bottom")
   label1 = tk.Label(signup_window, text="Username: ")
   label1.pack(pady=20)
   user1 = tk.Entry(signup_window)
   user1.pack(pady=0)
   label2 = tk.Label(signup_window, text="Password: ")    
   label2.pack(pady=20)
   passw2 = tk.Entry(signup_window, show="*")
   passw2.pack(pady=0)
   submit_sign = tk.Button(signup_window, text="Submit", command=submit_sign_form)
   submit_sign.pack(pady=15)

#append password and username to a file.
def submit_sign_form():
    global user1, passw1
    if user1 and passw2:
      username1 = user1.get()
      password1 = passw2.get()
      with open('user.py', 'a') as file1:
        file1.write( username1 + "\n" + password1 + "\n")
      signup_window.destroy()
      logib()

   



def info():
  info = tk.Tk()
  info.title("ERROR")
  info.geometry("500x500")
  label = tk.Label(info, text="Error Info not Found code: 9920746", bg="red")
  






#This is the home page window and directs to other windows 
root = tk.Tk()
root.configure(bg="LightGray")
root.geometry( "500x500")
root.title("Python-VM-Replit")
label = tk.Label(root, text="Python  VM  OS     V 0.5.12", bg="gray")
label.pack(side="bottom")
button1 = tk.Button(root, text="Sign In", command=logib, width=20, height=2)
button1.pack(pady=15)
button2 = tk.Button(root, text="Create Account", command=signub, width=20, height=2)
button2.pack(pady=15)
button3 = tk.Button(root, text="Forgot Password", width=15, height=1, bg="red",  command=message_creater)
button3.pack(pady=15)



root.mainloop()



#Made By Zach H. YTvariety122@gmail.com
#2024