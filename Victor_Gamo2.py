productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
# opcion 1 stock por la marca
def stock_marca(marca):
    for modelo, datos in productos.items():
        if datos [0].lower() == marca.lower():
            print(f"{modelo}: {stock[modelo][1]} Unidades")


def busqueda_de_precio(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except:
        print("Debes ingresar un numero entero porfavor")
        return
    
    Resultados = []
    for modelo, (precio, unidades) in stock.items():
        if unidades > 0 and p_min <= precio <= p_max:
            marca = productos[modelo][0]
            Resultados.append(f"{marca} - {modelo}")
    
    if Resultados:
        Resultados.sort()
        for r in Resultados:
            print(r)
    else:
        print("No hay notebooks en ese rango de precio.")

def actualizar_precio(modelo, nuevo_precio):
    if modelo not in stock:
        return False
    try:
        stock[modelo][0] = int(nuevo_precio)
        return True
    except:
        return False
    
def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock Marca.")
        print("2. Busqueda De Precios.")
        print("3. Actualizar Precios.")
        print("4.  Salir")

        opc = input("Seleccione una opcion: ")

        if opc == "1":
            marca = input("ingrese la marca: ")
            stock_marca(marca)
        
        elif opc == "2":
            p_min = input("ingrese su precio minimo: ")
            p_max = input("ingrese el precio maximo: ")
            busqueda_de_precio(p_min, p_max)

        elif opc == "3":
            modelo = input("ingrese modelo: ")
            precio = input ("ingrese nuevo precio: ")
            actualizado = actualizar_precio(modelo, precio)
            if actualizado:
                print ("¡Precio Actualizado!")
            else:
                print("El modelo no existe o el precio es invalido.")
            
            seguir = input("Desea Actualizar otro precio (Si/No): ")
            if seguir == "Si":
                continue
        
        elif opc == "4":
            print("Programa De Compra Finalizado.")
            break
        
        else:
            print("Bebes selecionar una opcion valida para continuar.")
menu()
