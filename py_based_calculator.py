from tkinter import *

# init values
exp = ""

def click(val):
    global exp
    exp += str(val)
    data.set(exp)

def clear():
    global exp
    exp = ""
    data.set("")

def back():
    global exp
    exp = exp[:-1]
    data.set(exp)

def solve():
    global exp
    try:
        res = str(eval(exp))
        data.set(res)
        exp = res
    except:
        data.set("Error")
        exp = ""

# main window
win = Tk()
win.title("Calc - Basic")
win.geometry("300x400")
win.config(bg="lightblue")

data = StringVar()

# input box
entry = Entry(win, textvariable=data, font=("Arial", 18), bd=5, relief=RIDGE, justify=RIGHT)
entry.pack(expand=True, fill="both")

# frame 1
f1 = Frame(win)
f1.pack(expand=True, fill="both")

Button(f1, text="7", font=("Arial", 15), command=lambda: click(7)).pack(side=LEFT, expand=True, fill="both")
Button(f1, text="8", font=("Arial", 15), command=lambda: click(8)).pack(side=LEFT, expand=True, fill="both")
Button(f1, text="9", font=("Arial", 15), command=lambda: click(9)).pack(side=LEFT, expand=True, fill="both")
Button(f1, text="/", font=("Arial", 15), command=lambda: click("/")).pack(side=LEFT, expand=True, fill="both")

# frame 2
f2 = Frame(win)
f2.pack(expand=True, fill="both")

Button(f2, text="4", font=("Arial", 15), command=lambda: click(4)).pack(side=LEFT, expand=True, fill="both")
Button(f2, text="5", font=("Arial", 15), command=lambda: click(5)).pack(side=LEFT, expand=True, fill="both")
Button(f2, text="6", font=("Arial", 15), command=lambda: click(6)).pack(side=LEFT, expand=True, fill="both")
Button(f2, text="*", font=("Arial", 15), command=lambda: click("*")).pack(side=LEFT, expand=True, fill="both")

# frame 3
f3 = Frame(win)
f3.pack(expand=True, fill="both")

Button(f3, text="1", font=("Arial", 15), command=lambda: click(1)).pack(side=LEFT, expand=True, fill="both")
Button(f3, text="2", font=("Arial", 15), command=lambda: click(2)).pack(side=LEFT, expand=True, fill="both")
Button(f3, text="3", font=("Arial", 15), command=lambda: click(3)).pack(side=LEFT, expand=True, fill="both")
Button(f3, text="-", font=("Arial", 15), command=lambda: click("-")).pack(side=LEFT, expand=True, fill="both")

# frame 4
f4 = Frame(win)
f4.pack(expand=True, fill="both")

Button(f4, text="C", font=("Arial", 15), bg="red", fg="white", command=clear).pack(side=LEFT, expand=True, fill="both")
Button(f4, text="0", font=("Arial", 15), command=lambda: click(0)).pack(side=LEFT, expand=True, fill="both")
Button(f4, text=".", font=("Arial", 15), command=lambda: click(".")).pack(side=LEFT, expand=True, fill="both")
Button(f4, text="+", font=("Arial", 15), command=lambda: click("+")).pack(side=LEFT, expand=True, fill="both")

# frame 5
f5 = Frame(win)
f5.pack(expand=True, fill="both")

Button(f5, text="⌫", font=("Arial", 15), bg="orange", fg="white", command=back).pack(side=LEFT, expand=True, fill="both")
Button(f5, text="=", font=("Arial", 15), bg="green", fg="white", command=solve).pack(side=LEFT, expand=True, fill="both")

# run loop
win.mainloop()
