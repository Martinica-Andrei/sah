import tkinter as tk

sah_marime = 8

ecran = tk.Tk()

for i in range(sah_marime):
    for j in range(sah_marime):
        buton = tk.Button(ecran, text='', width=5,height=5, highlightthickness=0, padx=0, pady=0)
        buton.grid(row=i, column=j)

ecran.mainloop()