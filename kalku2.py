import tkinter as tk
import customtkinter as ctk

jendela = ctk.CTk()
jendela.title("Kalkulator")
jendela.geometry("320x450")
jendela.configure(bg="#202124")

jendela.resizable(False, False)
#layar a    ngka
layar = ctk.CTkEntry(
    jendela,
    width=290,
    height=80,
    corner_radius=15,
    font=("Arial", 28),
    justify="right",
    fg_color="#303238",
    border_width=0
)

layar.pack(padx=12, pady=12)


# Teks pada layar

ekspresi = ""
angka_pertama = None
operator = None
angka_sekarang = "0"

#fungsi layar
def hasil() :
    global ekspresi
    
    if ekspresi[-1].isdigit() :
        if "÷" in ekspresi :
            ekspresi = ekspresi.replace("÷","/")
            hasil1 = eval(ekspresi)
            if hasil1.is_integer() : 
                hasil2 = int(hasil1)
                ekspresi = str(hasil2)
            else :            
                ekspresi = str(hasil1)
                
        else :
            hasil1 = eval(ekspresi)            
            if hasil1.is_integer() : 
                hasil2 = int(hasil1)
                ekspresi = str(hasil2)
            else :
                
                ekspresi = str(hasil1)
    
    else :
        ekspresi = ekspresi[:-1]
        hasil1 = eval(ekspresi)
        if hasil1.is_integer() : 
            hasil2 = int(hasil1)
            ekspresi = str(hasil2)
        else :            
            ekspresi = str(hasil1)
        
    
    layar.config(text=ekspresi)
    
def operator(op) :
    global ekspresi 
    operator = op
    
    if ekspresi[-1] in "+-x÷" :
        ekspresi = ekspresi[:-1]
        ekspresi += operator
    else :
        ekspresi += operator
        
    layar.config(text=ekspresi)
    
def tekan_angka(angka):
    global angka_sekarang
    global ekspresi
    if ekspresi == "":
        ekspresi = angka
    elif ekspresi == "0" :
        ekspresi = angka
    else:
        ekspresi += angka

    layar.config(text=ekspresi) 
    
def clear() :    
    global ekspresi
    ekspresi = "0"
    layar.config(text=ekspresi)
    
def delete():
    global ekspresi

    ekspresi = ekspresi[:-1]

    if ekspresi == "":
        ekspresi = "0"

    layar.config(text=ekspresi)
    
    
#tombol

tombol1 = tk.Frame(
    jendela,
    bg="#202124"
)
tombol1.pack(
    fill="both",
    expand=True,
    padx=12,
    pady=10
)
wadah_tombol = tk.Frame(
    tombol1,
    bg="#202124"
)
wadah_tombol.pack(anchor="center", expand=True)

tombol_7 = ctk.CTkButton(
    wadah_tombol,
    text="7",
    width=60,
    height=55,
    corner_radius=15,
    fg_color="#393B42",
    hover_color="#50535C",
    text_color="white",
    font=("Arial", 18)
)
tombol_7.grid(row=1, column=0)

tombol_8 = tk.Button(
    wadah_tombol,
    command=lambda : tekan_angka("8"),
    text="8",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_8.grid(row=1, column=1)

tombol_Clear = tk.Button(
    wadah_tombol,
    command=clear,
    text="C",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_Clear.grid(row=0, column=0)
                       
tombol_del = tk.Button(
    wadah_tombol,                                               
    command= delete,
    text="⌫",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_del.grid(row=0, column=1)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
tombol_perc = tk.Button(
    wadah_tombol,
    text="%",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_perc.grid(row=0, column=2)

tombol_divide = tk.Button(
    wadah_tombol,
    command= lambda : operator("÷"),
    text="÷",
    bg="orange",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_divide.grid(row=0, column=3)

tombol_9 = tk.Button(
    wadah_tombol,
    text="9",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_9.grid(row=1, column=2)

tombol_tim = tk.Button(
    wadah_tombol,
    text="x",
    bg="orange",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_tim.grid(row=1, column=3)

tombol_4 = tk.Button(
    wadah_tombol,
    text="4",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_4.grid(row=2, column=0)

tombol_5 = tk.Button(
    wadah_tombol,
    text="5",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_5.grid(row=2, column=1)

tombol_6 = tk.Button(
    wadah_tombol,
    text="6",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_6.grid(row=2, column=2)

tombol_min = tk.Button(
    wadah_tombol,
    command= lambda : operator("-"),
    text="-",
    bg="orange",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_min.grid(row=2, column=3)

tombol_1 = tk.Button(
    wadah_tombol,
    text="1",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_1.grid(row=3, column=0)

tombol_2 = tk.Button(
    wadah_tombol,
    text="2",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_2.grid(row=3, column=1)

tombol_3 = tk.Button(
    wadah_tombol,
    text="3",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_3.grid(row=3, column=2)

tombol_plus = tk.Button(
    wadah_tombol,
    command= lambda : operator("+"),
    text="+",
    bg="orange",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_plus.grid(row=3, column=3)

tombol_dot = tk.Button(
    wadah_tombol,
    text=".",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_dot.grid(row=4, column=1)

tombol_zero = tk.Button(
    wadah_tombol,
    text="0",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_zero.grid(row=4, column=0)

tombol_equal = tk.Button(
    wadah_tombol,
    command=hasil,
    text="=",
    bg="orange",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_equal.grid(row=4, column=2)

tombol_squared = tk.Button(
    wadah_tombol,
    text="n²",
    bg="#393B42",
    fg="white",
    font=("Arial", 16),
    width=5,
    height=2
)
tombol_squared.grid(row=4, column=3)

jendela.mainloop()

"""hasil = int(input("masukan angka : "));
while True :
    y = str(input("masukan operasi : "))
    if y == "=" :
        break
    elif y == "-" :
        pass
    elif y == "+" :
        pass
    else :
        hasil = "error"
        break

    x = int(input("masukan angka : "))
    
    if y == "+" :
        hasil += x
        
    elif y == "-" :
        hasil -= x

    else :
        hasil = "error"
        
        
print(hasil)
jendela.mainloop()
"""