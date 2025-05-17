import tkinter as tk
from tkinter import ttk 
import logic

main_app = tk.Tk()
main_app.configure()
main_app.geometry("400x640")
main_app.resizable(False,False)
main_app.title("KALKULATOR")

# frame UI kalkulator
ui_frame = ttk.Frame(main_app)
ui_frame.pack(padx=10,pady=10,fill="x",expand=True)
empty_space = tk.Label(ui_frame, text="")
empty_space.grid(row=0, column=0, columnspan=4, pady=97) 

#frame output
output_var = tk.StringVar()
output = ttk.Entry(ui_frame, textvariable=output_var, font=("Arial", 24), justify='right')
output.grid(row=0, column=0, columnspan=5, sticky="nsew", pady=10, padx=10)

# Button nomor
button1 = tk.Button(ui_frame, text="1", width=12, height=6,command=lambda : logic.button_angka_click(1))
button1.grid(row=1, column=1)

button2 = tk.Button(ui_frame, text="2", width=12, height=6,command=lambda : logic.button_angka_click(2))
button2.grid(row=1, column=2)

button3 = tk.Button(ui_frame, text="3", width=12, height=6,command=lambda : logic.button_angka_click(3))
button3.grid(row=1, column=3)

button4 = tk.Button(ui_frame, text="4", width=12, height=6,command=lambda : logic.button_angka_click(4))
button4.grid(row=2, column=1)

button5 = tk.Button(ui_frame, text="5", width=12, height=6,command=lambda : logic.button_angka_click(5))
button5.grid(row=2, column=2)

button6 = tk.Button(ui_frame, text="6", width=12, height=6,command=lambda : logic.button_angka_click(6))
button6.grid(row=2, column=3)

button7 = tk.Button(ui_frame, text="7", width=12, height=6,command=lambda : logic.button_angka_click(7))
button7.grid(row=3, column=1)

button8 = tk.Button(ui_frame, text="8", width=12, height=6,command=lambda : logic.button_angka_click(8))
button8.grid(row=3, column=2)

button9 = tk.Button(ui_frame, text="9", width=12 ,height=6,command=lambda : logic.button_angka_click(9))
button9.grid(row=3, column=3)

button0 = tk.Button(ui_frame, text="0", width=12 ,height=6,command=lambda : logic.button_angka_click(0))
button0.grid(row=4, column=2)

#Tombol operasi
buttonhasil = tk.Button(ui_frame, text="=", width=12 ,height=6,command=lambda : logic.button_hasil(),bg="red")
buttonhasil.grid(row=4, column=1)

buttonclear = tk.Button(ui_frame, text="C", width=12 ,height=6,command=lambda : logic.clear())
buttonclear.grid(row=4, column=3)

buttontambah = tk.Button(ui_frame, text="+", width=12, height=6,command=lambda : logic.button_operasi_click("+"))
buttontambah.grid(row=1, column=4)

buttonkurang = tk.Button(ui_frame, text="-", width=12, height=6,command=lambda : logic.button_operasi_click("-"))
buttonkurang.grid(row=2, column=4)

buttonkali = tk.Button(ui_frame, text="X", width=12, height=6,command=lambda : logic.button_operasi_click("x"))
buttonkali.grid(row=3, column=4)

buttonkali = tk.Button(ui_frame, text="/", width=12, height=6,command=lambda : logic.button_operasi_click("/"))
buttonkali.grid(row=4, column=4)








