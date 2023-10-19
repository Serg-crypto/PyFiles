import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    password_entry.delete(0,END)

    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symb = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_abc = [random.choice(abc) for _ in range(random.randint(8,10))]
    password_num = [random.choice(num) for _ in range(random.randint(2,4))]
    password_simb = [random.choice(symb) for _ in range(random.randint(2,4))]

# Combine the list and shuffle the items
    PSW = password_abc + password_num + password_simb
    random.shuffle(PSW)
#Convert the elements of the list into a string
    PSW ="".join(PSW)
    #Insert the password into the field of our form
    password_entry.insert(0,PSW)
    pyperclip.copy(PSW)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    #Obtenemos los valores de los campos website, email y password
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    #Guardamos la información en un diccionario para posteriormente pasarla a un archivo JSON
    new_data = {
        website:{
                "email": email,
                "password":password
        },
    }

#Condicional para validar que todos los campos tengan la info requerida
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")

    else:
        #Probar si existe el archivo data.json abriendolo y guardandolo en la variable data
        try:
            with open("data.json", mode="r") as data_file:
            #Leer los datos ya existentes
                data = json.load(data_file)

        #En caso de que no exista el archivo se procede a crear un archivo data.json
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        #En caso de que sí exista el archivo entonces de procede a actualizarlo con la información de new_data
        else:
            # Actualizar con la información escrita en new_data
            data.update(new_data)
            #Escribir y guardar la información de new_data dentro del archivo data.json
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)




# ---------------------------- Find Password ------------------------------- #
def find_password():
    search_value = website_entry.get()
    try:
        with open("data.json",mode="r") as data_file:
            info = json.load(data_file)

            #Acceso a los valores dentro de la key buscada en el archivo JSON correspondiente al website el usuario busca
            email=info[search_value]["email"]
            password=info[search_value]["password"]

            #Se muestra al usuario los valores correspondientes dentro de una ventana
            tkinter.messagebox.showinfo(title=search_value,message=f'email:\n{email}\npassword:\n{password}')

    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Error", message='No Data File Found')
    except KeyError:
        tkinter.messagebox.showinfo(title="Error", message=f'Value not found for: {search_value}')



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
#Crear imagen en la posicion x,y establecida y utilizando el png que hemos indicado
canvas.create_image(100,112 , image=logo_img)
canvas.grid(column=1, row=0)

#LABELS--------------------------------------------------------------------------
text_website = Label(text="Website:", font=("Arial",12))
text_website.grid(column=0, row=1)

text_email = Label(text="Email/Username:", font=("Arial",12))
text_email.grid(column=0, row=2)

text_password = Label(text="Password:", font=("Arial",12))
text_password.grid(column=0, row=3)

#Entries-----------------------------------------------------------------------
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0,"example_zen@hotmail.com")
email_entry.grid(column=1,row=2, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(column=1,row=3)

generate_password_btn = Button(text="Generate Password",width=14, command=generatePassword)
generate_password_btn.grid(column=3, row=3)


search_btn=Button(text="Search", width=14, command=find_password)
search_btn.grid(column=3, row=1)

add_btn =Button(text="Add",width=30, command=savePassword)
add_btn.grid(column=1, row=4, columnspan=2)
window.mainloop()

