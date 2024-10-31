
from logging import root
from tkinter import*
from tkinter import messagebox



root=Tk()
root.geometry("240x100") 
root.title("Bank ATM Prototype") 


Label(root,text="Username:",font=("",10,"bold")).grid(row=0,column=0)

e1=Entry(root)
e1.grid(row=0, column=1)

Label(root,text="Password:",font=("",10,"bold")).grid(row=1,column=0)

e2=Entry(root ,show = '*')   ## hide password **
e2.grid(row=1, column= 1)

# credentials={"xyz":{"Password:":123}}

##---------------------
def Login():
    # for username input block
    User = e1.get().strip() 
    ## for password input block
    Password = e2.get().strip()  
    if User and Password :

        ###-------Merging line 
        window=Tk()
        # root.destroy()
        window.geometry("240x140") 

        Button(window, text="Balance", font=("", 10, "bold")).grid(row=0, column=0)
        Button(window, text="Deposit", font=("", 10, "bold")).grid(row=1, column=0)

        Button(window, text="Withdraw", font=("", 10, "bold")).grid(row=2, column=0)

        ### use Exit_COMMAND 
        Button(window, text="Log Out", command=exit, font=("", 10, "bold")).grid(row=3, column=0) 

    else:
        ## root.destroy()     ## not required code        
        messagebox.showerror("Error", "Invalid Credentials.")


Button(root, text="Login", command=Login, font=("", 10, "bold")).grid(row=7, column=1)
root.mainloop()





