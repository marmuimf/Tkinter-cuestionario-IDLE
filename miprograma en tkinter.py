##interfaz de usuario libre en Tk en una ventana raiz.

import tkinter as tk

def salir():
    raiz.destroy()#salgo del programa

raiz = tk.Tk() ##identificamos el tk para llamarlo despues

#definicion Ventana
raiz.title("Cuestionario de satisfaccion")
raiz.geometry("600x550+100+100")#margenes ventana
raiz.iconbitmap("logo.ico")


##MENU
barramenu= tk.Menu(raiz)
#elemento menu: Archivo
raiz.config(menu=barramenu)
archivo = tk.Menu(barramenu,tearoff=0)#tearoff=1 sacar barra de herramientas
barramenu.add_cascade(label="Arhivo",menu=archivo)
#añado comandos de menu: Archivo
archivo.add_command(label="Nuevo")
archivo.add_command(label="Abrir")
archivo.add_command(label="Guardar")
archivo.add_command(label="Salir",command=salir)
#elemento menu: Ayuda
ayuda = tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Ayuda",menu=ayuda)
#añado comandos de menu: Archivo
ayuda.add_command(label="Ayuda")
ayuda.add_command(label="Documentación en linea")
ayuda.add_command(label="Acerca de ...")
ayuda.add_command(label="Soporte")


##WIDGETS
# etiqueta
tk.Label(raiz,text="Escribe tu nombre:").pack(padx=10,pady=5)
#entradas de texto
tk.Entry(raiz).pack(padx=10,pady=5)


tk.Label(raiz,text="Indica cuanto te gusta el modulo:").pack(padx=5,pady=5)
#rango horiz
tk.Scale(raiz,from_=0,to=10,orient=tk.HORIZONTAL).pack(padx=5,pady=10)

#botones de seleccion multiple-cuadrados
tk.Checkbutton(raiz, text="Marca esta casilla si se lo recomendarias a un amigo.").pack(padx=10,pady=10)


tk.Label(raiz,text="Cuantas asignaturas tienes?").pack(padx=10,pady=10)
#selector de valores numericos
tk.Spinbox(raiz,from_=0,to=10).pack(padx=5,pady=5)


tk.Label(raiz,text="Comentarios:").pack(pady=10)
#area de texto
area_texto = tk.Text(raiz, width=30, height=5)
area_texto.pack()


tk.Label(raiz,text="Cuado hayas terminado pulsa el boton:").pack(padx=10,pady=20)
#boton con comando
tk.Button(raiz,text="Salir",command=salir).pack(padx=10,pady=5)


raiz.mainloop()#captura el bucle para que se abra la ventana para el usuario
