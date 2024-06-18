##https://github.com/papablik24/Prueba-3-pablo-novoa

import csv
lista=[]
efectividad=0
categoria=False


def menu():
    print("")
    print("1.- Agregar plan")
    print("2.- Listar planes")
    print("3.- Eliminar plan por ID")
    print("4.- Generar bbdd")
    print("5.- Cargar bbdd")
    print("6.- Estadísticas")
    print("0.- Salir.")
    
def validar():
    efectividad==False
    
    if efectividad <0 and efectividad >101:
        print("error")
    elif efectividad>= 0 and efectividad <=100:
        efectividad==True
def validarplan():
    pregunta=input("Desea eliminar el plan? (si/no) : ").lower()
    if pregunta=="si" or pregunta=="s":
        lista.remove(x)
        print("Plan ELIMINADO!")
    else:
        print("No se eliminó el plan :)")
            
def agregar():
    
    print(".-.-.-.- Agregar plan .-.-.-.-.")
    Identificacion=int(input("Ingrese numero de ID :"))
    nombre=input("Ingrese nombre : ")
    efectividad=int(input("Ingrese porcentaje de efectividad : "))
    validar()
    plan=[Identificacion,nombre,efectividad,categoria]
    lista.append(plan)  
    efectividad=0
    
    
    
def categoria():
    categoria=False
    if efectividad >= 0 and efectividad <25:
        categoria = True
        return categoria
            
    elif efectividad >= 26 and efectividad <50:
        categoria = True
        return categoria
    elif efectividad >=51 and efectividad <75:
        categoria = True
        return categoria
    elif efectividad >=76 and efectividad >99:
        categoria = True
        return categoria
    elif efectividad == 100:
        categoria = True
        return categoria
        
def listar():
    for x in lista:
        print(f"ID : ",x[0],"Nombre : ", x[1], "efectividad : ", x[2], "Categoria : ", x[3])
        
        
def generar_archivo():
    with open('planes.csv','r',newline='')as archivo:
        escribircsv=csv.writer(archivo)
        escribircsv.writerow(["ID","Nombre","Efectividad","Categoria"])
        escribircsv.writerows(lista)
        print("Archivo generado....")
        
def cargar_archivo():
    lista.clear()
    with open('planes.csv','r',newline='')as archivo:
        leercsv=csv.reader(archivo)
        for x in leercsv:
            lista.append(x)
    lista.pop(0)
    for x in lista:
        print("ID : ",x[0],"Nombre : ", x[1], "efectividad : ", x[2], "Categoria : ", x[3])
    
def estadisticas1():
    total=0
    cantidad=len(lista)
    promedio=total/cantidad
    print(f"Promedio de efectividad : {promedio}")
    
    
def estadisticas2():
    total2=0
    efectividadmasalta=0
    for x in lista:
        efectividad=int(x[2])
        total2=total2+efectividad
        if efectividad>efectividadmasalta:
            efectividadmasalta=efectividad
    print(f"Porcentaje de efectividad mas alto : {efectividadmasalta}")        


while True:
    menu()
    op=int(input("Seleccione una opcion :"))
    if op==1:
        agregar()
    
        
    elif op==2:
        print(".-.-.-. Listar Planes  .-.-.-.-.-")
        listar()
    elif op==3:
        print(".-.-.-. Eliminar Plan por ID .-.-.-.")
        encontrado=False
        Identificacion=int(input("Ingrese numero de ID"))
        for x in lista:
            num_id=int(x[0])
            if Identificacion==num_id:
                print("plan encontrado")
                print("ID : ",x[0],"Nombre : ", x[1], "efectividad : ", x[2], "Categoria : ", x[3])
                encontrado=True
                validarplan()
    elif op==4:
        print(".-.-.- Generar Archivo .-.-.-.-")
        generar_archivo()
    elif op==5:
        print(".-.-.-. Cargar archivo .-.-.-.-.-.")
        cargar_archivo()
    elif op==6:
        print(".-.-.-. Estadisticas .-.-.-.-.-.-.")
        estadisticas1()
        estadisticas2()
    elif op==0:
        print("Adiooooooooooooooooos")
        break
    
    else:
        print("errooooooooooooooooooooooor, ingrese una opcion valida")