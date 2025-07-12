import os
os.system("cls")

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}

def marca():
    marca = set()

    for marca in [productos][0]:
        pass   

def stock_marca(marca):
    pass

        
def busquedaprecio(pmin, pmax):
       precio = 0

       if pmin <= precio <= pmax:
             pass
      

def actualizar_precio(modelo,p):
       while True:
            if modelo in stock:
                return True
            else:
                   print("El modelo no existe")
                   return False
                   


def menu():
    while True:
            os.system("cls")
            print("=== Menu Principal === \n 1. Stock marca \n 2. Busqueda por precio \n 3. Actualizar precio \n 4. Salir")

            opcion = input("Elige una opcion: ")
            
            if opcion == "1":
                    marca = input("Introduce la marca a consultar: ")
            elif opcion == "2":
                while True:
                    os.system("cls")
                    try:
                        pmin = int(input("Introduce el precio minimo: "))
                        pmax = int(input("Introduce el precio maximo: "))
                        busquedaprecio(pmin,pmax)
                        break
                            
                    except ValueError:
                        input("Debe ingresar valores enteros!!")
            elif opcion == "3": 
                       
                modelo = input("Introduce el modelo a seleccionar: ")

            elif opcion == "4":
                        
                print("Programa finalizado.")
                break
            else:
                input("No se selecciono una opcion valida")
            
menu()