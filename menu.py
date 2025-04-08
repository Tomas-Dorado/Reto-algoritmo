import subprocess
import os



def menu():
    while True:
        print("\nMenú de Ejercicios")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Ejecutando el Ejercicio 1...")
            ruta_1 = os.path.join("Caballos", "lanzador.py")
            ruta_2 = os.path.join("Caballos", "Simulador.py")
            subprocess.run(["python", ruta_1])
            subprocess.run(["python", ruta_2])
        elif opcion == "2":
            print("Ejecutando el Ejercicio 2...")
            ruta = os.path.join("Reinas", "lanzador.py")
            subprocess.run(["python", ruta])
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")