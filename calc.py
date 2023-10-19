from tkinter import *
import ttkbootstrap as ttk

def button_click(number):
	if number=="^":
		number="**"
	current_text = eqn.get()
	eqn.set(current_text + str(number))

def clear():
    eqn.set("")
    
def back():
	val=''
	temp=list(eqn.get())
	temp.pop(-1)
	for l in temp:
		val+=l
	eqn.set(str(val))
    
def calculate():
    try:
        result = eval(eqn.get())
        eqn.set(str(result))
    except:
        eqn.set("Error")

root = Tk()
root.geometry('400x450')
root.title("Basic Calculator")
style = ttk.Style(theme='darkly')
style.configure('.', font=('TkDefaultFont', 20))
eqn = ttk.StringVar()
prev=ttk.StringVar()
lbl = ttk.Label(root, textvariable=prev, font=('Calibri', 20, 'bold'))
lbl.grid(row=0, columnspan=4, pady=10, padx=3)
entry = ttk.Entry(root, textvariable=eqn, font=('Calibri', 20, 'bold'))
entry.grid(row=1, columnspan=4, pady=10, padx=3)

button_width = 10  # Adjust the width as needed

buttons = [
    ["C","%","^","<"],
    [1, 2, 3, "+"],
    [4, 5, 6, "-"],
    [7, 8, 9, "*"],
    [0, ".", "=", "/"]
    
]

for i in range(5):
    for j in range(4):
        if buttons[i][j] == "=":
            button = ttk.Button(root, text=f"{buttons[i][j]}", bootstyle='warning', command=calculate)
        elif buttons[i][j] == "C":
            button = ttk.Button(root, text=f"{buttons[i][j]}", bootstyle='danger', command=clear)
        elif buttons[i][j] == "<":
            button = ttk.Button(root, text=f"{buttons[i][j]}", bootstyle='info', command=back)
        else:
            button = ttk.Button(root, text=f"{buttons[i][j]:^3}", bootstyle='success', command=lambda num=buttons[i][j]: button_click(num))
        button.grid(row=i + 2, column=j, padx=0, pady=10, ipadx=button_width)

root.mainloop()

