
shopping_list = []
menu_option = ""

while menu_option != "4":
    
    print("Lista de compras")
    print("1. agregar")
    print("2. quitar")
    print("3. ver")
    print("4. salir")
    
    menu_option = input()

    if menu_option == "1":
      # Agregamos elementos a la lista
      shopping_list.append(input("ingresa lo que quieres agregar: "))
    elif menu_option == "2":
       element = input("ingresa el elemento a eliminar: ")
       shopping_list.remove(element)
    elif menu_option == "3":
       # Mostrar todo el contenido de shopping_list
       print("Tu listado de compras tiene lo siguiente")
       for item in shopping_list:
         print(item)
    elif menu_option == "4":
       print("Chao chao")
    else:
        print("Selecciona una opción válida")