inventario_marca = []

vehiculos = {
    'TOY8475': ['Toyota', 2019, '65000km', 'Gasolina', 'Automática', '1.8L 4cil', 'Blanco'],
    'FOR2175': ['Ford', 2017, '85000km', 'Gasolina', 'Manual', '1.6L 4cil', 'Azul'],
    'CHE9834': ['Chevrolet', 2020, '25000km', 'Gasolina', 'Automática', '2.0L 4cil', 'Negro'],
    'NIS7654': ['Nissan', 2016, '95000km', 'Gasolina', 'Manual', '1.6L 4cil', 'Rojo'],
    'HYU4521': ['Hyundai', 2021, '15000km', 'Híbrido', 'Automática', '1.6L 4cil', 'Gris'],
    'KIA3456': ['Kia', 2018, '75000km', 'Diesel', 'Manual', '2.0L 4cil', 'Blanco'],
    'MAZ8901': ['Mazda', 2019, '55000km', 'Gasolina', 'Automática', '2.5L 4cil', 'Rojo'],
    'SUB2468': ['Subaru', 2020, '30000km', 'Gasolina', 'Manual', '2.0L 4cil', 'Verde'],
    # ... más vehículos
}

inventario = {
    'TOY8475': [8500000, 1], 
    'FOR2175': [6200000, 1], 
    'CHE9834': [12750000, 1],
    'NIS7654': [5400000, 2], 
    'HYU4521': [15200000, 1], 
    'KIA3456': [7800000, 1],
    'MAZ8901': [9200000, 1], 
    'SUB2468': [11500000, 0], 
    'HON1357': [6800000, 0],
    # ... más vehículos
}

precio_max = 500000
precio_min = 2000000

while True:
    print("====Menu concesionario autos usados====")
    print("1.consultar inventario por marca")
    print("2.buscar por un rango de precios")
    print("3.Modificar precio de vehiculo")
    print("4.salir del programa")

    opcion = input("Ingrese su opcion aqui: ")

    if opcion == "1":
        input("ingrese la marca a consultar: ")
        print(vehiculos)
    
    elif opcion == "2":
        precio_ingresado = int(input("Ingrese el precio: "))
        if precio_ingresado <= precio_max or precio_ingresado <= precio_min:
            print("no hay vehiculos en ese rango de precio")
        elif precio_ingresado == precio_max or precio_ingresado == precio_min:
            print("si hay vehiculos en ese rango de precios")

    elif opcion == "3":
        codigo_vehiculo = input("ingrese codigo del vehiculo a actualizar: ")
        precio_nuevo = int(input("Ingrese el precio nuevo: "))

    elif opcion == "4":
        print("Sistema finalizado correctamente")

    else:
        print("opcion no valida ingrese una opcion entre 1 y 4")