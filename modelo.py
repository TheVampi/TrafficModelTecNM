import random
import tkinter as tk
import csv
import time

carrosArray = []
personasArray = []
bicicletasArray=[]
indice_actual = 0

def escrituraArchivo():
    with open(r'C:\Users\luisi\Desktop\DataStructures-TecNM\Python\lab08Semaforo\valores.csv', 'w+', newline='') as file:
        file.write('valor1' + "|" + 'valor2' + '\n')
        writer = csv.writer(file, delimiter='|', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for i in range(20):
            carros = random.randint(1, 20)
            personas = random.randint(1, 10)
            bicicletas=random.randint(1,10)
            writer.writerow([carros, personas,bicicletas])

escrituraArchivo()

def leerArchivo():
    with open(r'C:\Users\luisi\Desktop\DataStructures-TecNM\Python\lab08Semaforo\valores.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        next(reader)  # Saltar la primera fila
        for row in reader:
            carros = int(row[0])
            personas = int(row[1])
            bicicletas= int(row[2])
            carrosArray.append(carros)
            personasArray.append(personas)
            bicicletasArray.append(bicicletas)

leerArchivo()

print("Valores de carrosArray:", carrosArray)
print("Valores de personasArray:", personasArray)
print("Valores de bicicletasArray:", bicicletasArray)

def leer_valores():
    global indice_actual
    if indice_actual < 20:
        valor1 = carrosArray[indice_actual]
        valor2 = personasArray[indice_actual]
        valor3= bicicletasArray[indice_actual]
        print('Valor1: ' + str(valor1))
        print('Valor2: ' + str(valor2))
        print('Valor3: ' + str(valor3) )
        label.config(text=f"Carros: {valor1}, Personas: {valor2}, Bicicletas: {valor3}")

        #Prioridad a personas
        if valor1<15 and valor2+valor3<10:
            mover_rectangulo_morado()
            mover_rectangulo_verde()
            print('pasan primero carros')
        else:
            if (valor1<15 and valor2+valor3>=10):
                mover_rectangulo_rojo()
                mover_rectangulo_azul()
                print('pasan primero personas')
            else:
                mover_rectangulo_morado()
                mover_rectangulo_verde()
                print('pasan primero carros')

        indice_actual += 1

def mover_rectangulo_rojo():
    move_rectangulo_abajo()

def move_rectangulo_abajo():
    coords = canvas.coords(rectangulo)
    y1 = coords[1]  # Coordenada y de la parte superior
    y2 = coords[3]  # Coordenada y de la parte inferior
    if y2 < 400:
        canvas.move(rectangulo, 0, 2)
        root.after(10, move_rectangulo_abajo)
    else:
        canvas.coords(rectangulo, 175, 0, 225, 50)
        ##leer_valores()  # Llamar a leer_valores después de mover el rectángulo

# AZUL
def mover_rectangulo_azul():
    move_rectangulo_abajoB()

def move_rectangulo_abajoB():
    coords = canvas.coords(rectangulo4)
    y1 = coords[1]  # Coordenada y de la parte superior
    y2 = coords[3]  # Coordenada y de la parte inferior
    if y2 < 400:
        canvas.move(rectangulo4, 0, 2)
        root.after(10, move_rectangulo_abajoB)
    else:
        canvas.coords(rectangulo4, 110, 0, 160, 50)
        leer_valores()  # Llamar a leer_valores después de mover el rectángulo

def move_rectangulo_abajo_decisionB():
    coords = canvas.coords(rectangulo4)
    y1 = coords[1]  # Coordenada y de la parte superior
    y2 = coords[3]  # Coordenada y de la parte inferior
    if y2 < 400:
        canvas.move(rectangulo, 0, 2)
        root.after(10, move_rectangulo_abajoB)
    else:
        canvas.coords(rectangulo, 110, 0, 160, 50)
        #leer_valores()  # Llamar a leer_valores después de mover el rectángulo

##VERDE
def mover_rectangulo_verde():
    move_rectangulo_derecha()

def move_rectangulo_derecha():
    coords = canvas.coords(rectangulo3)
    x1 = coords[0]  # Coordenada x de la parte izquierda
    x2 = coords[2]  # Coordenada x de la parte derecha
    if x2 < 400:
        canvas.move(rectangulo3, 2, 0)  # Mover hacia la derecha
        root.after(10, move_rectangulo_derecha)
    else:
        canvas.coords(rectangulo3, 0, 200, 50, 250)
        leer_valores()  # Llamar a leer_valores después de mover el rectángulo verde

def mover_rectangulo_morado():
    move_rectangulo_izquierda()  # Llamar al movimiento del rectángulo morado


def move_rectangulo_izquierda():
    coords = canvas.coords(rectangulo2)
    x1 = coords[0]  # Coordenada x de la parte izquierda
    x2 = coords[2]  # Coordenada x de la parte derecha
    if x1 > 0:
        canvas.move(rectangulo2, -2, 0)  # Mover hacia la izquierda
        root.after(10, move_rectangulo_izquierda)
    else:
        canvas.coords(rectangulo2, 350, 300, 400, 350)
        ##leer_valores()  # Llamar a leer_valores después de mover el rectángulo morado


root = tk.Tk()
root.title("Laboratorio 07")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Creación de los rectángulos
rectangulo = canvas.create_rectangle(175, 0, 225, 50, fill="red")
rectangulo2 = canvas.create_rectangle(350, 300, 400, 350, fill="purple")
rectangulo3 = canvas.create_rectangle(0, 200, 50, 250, fill="green")
rectangulo4 = canvas.create_rectangle(110, 0, 160, 50, fill="blue")

# Creación del label
label = tk.Label(root, text="")
label.pack()

leer_valores()

root.mainloop()