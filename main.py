import tkinter as tk
import random


# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.title("🎲 Adivina el Número")
ventana.geometry("600x500")
ventana.config(bg="#2C3E50")
ventana.resizable(False, False)

# VARIABLES
numero_secreto = 0
intentos = 0
jugador = ""

# FUNCIÓN PARA LIMPIAR LA VENTANA
def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()


# MENÚ PRINCIPAL
def menu_principal():
    limpiar_ventana()
    titulo = tk.Label(
        ventana,
        text="🎲 ADIVINA EL NÚMERO 🎲",
        font=("Arial",24,"bold"),
        bg="#2C3E50",
        fg="#F1C40F"
    )
    titulo.pack(pady=40)
    tk.Button(
        ventana,
        text="Iniciar Juego",
        font=("Arial",14),
        width=20,
        bg="#3498DB",
        fg="white",
        command=ventana_juego
    ).pack(pady=10)
    tk.Button(
        ventana,
        text="Resultados",
        font=("Arial",14),
        width=20,
        bg="#3498DB",
        fg="white",
        command=resultados
    ).pack(pady=10)
    tk.Button(
        ventana,
        text="Instrucciones",
        font=("Arial",14),
        width=20,
        bg="#3498DB",
        fg="white",
        command=instrucciones
    ).pack(pady=10)
    tk.Button(
        ventana,
        text="Salir",
        font=("Arial",14),
        width=20,
        bg="#E74C3C",
        fg="white",
        command=ventana.destroy
    ).pack(pady=10)

# PANTALLA DEL JUEGO
def ventana_juego():

    limpiar_ventana()
    
    global lbl_animacion
    global entrada_nombre
    global boton_comenzar

    titulo = tk.Label(
        ventana,
        text="Nuevo Juego",
        font=("Arial",22,"bold"),
        bg="#2C3E50",
        fg="#F1C40F"
    )
    titulo.pack(pady=20)
    tk.Label(
        ventana,
        text="Nombre del jugador",
        bg="#2C3E50",
        fg="white",
        font=("Arial",13)
    ).pack()
    entrada_nombre = tk.Entry(
        ventana,
        font=("Arial",14),
        justify="center"
    )
    entrada_nombre.pack(pady=10)
    boton_comenzar = tk.Button(
        ventana,
        text="Comenzar",
        bg="#27AE60",
        fg="white",
        font=("Arial",13),
        command=iniciar_juego
    )
    boton_comenzar.pack(pady=10)
    lbl_animacion = tk.Label(
        ventana,
        text="",
        font=("Arial",15,"bold"),
        bg="#2C3E50",
        fg="white"
    )
    lbl_animacion.pack(pady=25)

    tk.Button(
        ventana,
        text="← Volver",
        command=menu_principal,
        bg="#E67E22",
        fg="white",
        font=("Arial",12)
    ).pack(side="bottom", pady=20)

# ANIMACIÓN
def iniciar_juego():
    global jugador
    jugador = entrada_nombre.get().strip()
    if jugador == "":
        lbl_animacion.config(
            text="Ingrese su nombre.",
            fg="red"
        )
        return
    entrada_nombre.config(state="disabled")
    boton_comenzar.config(state="disabled")
    animacion(0)

def animacion(paso):

    puntos = "." * (paso % 4)

    lbl_animacion.config(
        text="Generando número" + puntos,
        fg="white"
    )

    if paso < 12:
        ventana.after(250, lambda: animacion(paso + 1))
    else:
        comenzar_partida()

# GENERAR NÚMERO
def comenzar_partida():

    global numero_secreto
    global intentos
    numero_secreto = random.randint(1,100)
    intentos = 0
    mostrar_interfaz_juego()

# INTERFAZ DEL JUEGO
def mostrar_interfaz_juego():
    limpiar_ventana()
    tk.Label(
        ventana,
        text=f"Jugador: {jugador}",
        font=("Arial",16,"bold"),
        bg="#2C3E50",
        fg="#F1C40F"
    ).pack(pady=15)

    tk.Label(
        ventana,
        text="Ingrese un número entre 1 y 100",
        font=("Arial",14),
        bg="#2C3E50",
        fg="white"
    ).pack()

    tk.Label(
        ventana,
        text="(Aquí irá la lógica del juego)",
        font=("Arial",15),
        bg="#2C3E50",
        fg="#58D68D"
    ).pack(pady=50)

# RESULTADOS
def resultados():

    limpiar_ventana()

    tk.Label(
        ventana,
        text="RESULTADOS",
        font=("Arial",22,"bold"),
        bg="#2C3E50",
        fg="#F1C40F"
    ).pack(pady=30)

    tk.Label(
        ventana,
        text="Aún no hay resultados.",
        bg="#2C3E50",
        fg="white",
        font=("Arial",14)
    ).pack()

    tk.Button(
        ventana,
        text="Volver",
        command=menu_principal
    ).pack(pady=20)

# INSTRUCCIONES

def instrucciones():

    limpiar_ventana()
    texto = """
1. Escriba su nombre.

2. El sistema generará
un número del 1 al 100.

3. Intente adivinarlo.

4. Si el número es mayor muestra la pista:
'Muy Alto'

5. Si es menor muestra la pista:
'Muy Bajo'

6. Gana cuando acierte.
"""

    tk.Label(
        ventana,
        text="INSTRUCCIONES",
        font=("Arial",22,"bold"),
        bg="#2C3E50",
        fg="#F1C40F"
    ).pack(pady=20)
    tk.Label(
        ventana,
        text=texto,
        bg="#2C3E50",
        fg="white",
        font=("Arial",13),
        justify="left"
    ).pack()
    tk.Button(
        ventana,
        text="Volver",
        command=menu_principal
    ).pack(pady=20)

menu_principal()

ventana.mainloop()