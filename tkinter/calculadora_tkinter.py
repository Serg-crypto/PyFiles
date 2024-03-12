import tkinter as tk


root = tk.Tk()
root.title("Test")
root.geometry("400x400")

n1 = tk.StringVar()
n2 = tk.StringVar()
r = tk.StringVar()


def sumar():
    r.set( float(n1.get()) + float(n2.get()))

def restar():
    r.set( float(n1.get()) - float(n2.get()) )

def multiplicar():
    r.set( float(n1.get()) * float(n2.get()) )


first_number = tk.Label(root, text="Number 1:")
first_number.grid(row = 0, column = 0, sticky = "w", padx = 2, pady = 2)


entry_n1 = tk.Entry(root,justify = "center", textvariable = n1)
entry_n1.grid(row = 0, column = 1, padx = 2, pady = 2)


second_number = tk.Label(root, text="Number 2:")
second_number.grid(row = 1, column = 0, sticky = "w", padx = 2, pady = 2)


entry_n2 = tk.Entry(root, justify = "center", textvariable = n2)
entry_n2.grid(row = 1, column = 1, padx = 2, pady = 2)

btn_sumar = tk.Button(root, text="Sumar", command = sumar)
btn_sumar.grid(row = 2, column = 0)

btn_restar = tk.Button(root, text="Restar", command = restar)
btn_restar.grid(row = 2, column = 1)

btn_producto = tk.Button(root, text="Multiplicar", command = multiplicar)
btn_producto.grid(row = 2, column = 2)


entry_result = tk.Entry(root, justify = "center", textvariable = r, state = "disabled")
entry_result.grid(row = 3 , column = 1, padx = 5, pady = 5)
root.mainloop()

