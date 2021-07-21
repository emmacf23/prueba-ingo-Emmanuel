
import tkinter as tk
from tkinter import messagebox
from timeConvertion import dateToString


window= tk.Tk() # Se crea la ventana
window.title('Redactando la Hora')

canvas = tk.Canvas(window, width = 400, height = 250,  relief = 'raised') #Se definen sus dimensiones
canvas.pack()

title = tk.Label(window, text='Redactando la Hora') # Se crea el titulo
title.config(font=('helvetica', 14))
canvas.create_window(200, 25, window=title)

labelInput = tk.Label(window, text='Escriba una hora, por favor(hh:mm am/pm):') #Se crea el label del input
labelInput.config(font=('helvetica', 10))
canvas.create_window(200, 100, window=labelInput)

entryTime = tk.Entry (window) # Se crea el input
canvas.create_window(200, 140, window=entryTime)

def getDateToString ():
    valueFromInput = entryTime.get()
    answer = dateToString(valueFromInput) #Ejecutamos la función de conversión
    if(answer['error']): #Validamos que no haya ocurrido un error
        messagebox.showerror(title="Error", message=answer['text'])
    else:        
        messagebox.showinfo(title="Respuesta", message=answer['text'])
    
button = tk.Button(text='Calcular', command=getDateToString, bg='navy', fg='white', font=('helvetica', 9, 'bold'))
canvas.create_window(200, 180, window=button)

window.mainloop()


