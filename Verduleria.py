''' 
carga de producto
bucle de carga\compra
    -mostrar opciones 
    -seleccion y carga de  productos y validar
        -condicion de salida
    -mostrar compra parcial
mostrar ticket

'''

from locale import locale_encoding_alias
from optparse import Values

#----------------------------------------------------------------------------------------------#
#Varibles

list_actualizada = ["limon",100,"papa",250,"cebolla",223,"tomate",455,"lechuga",250]

list_articulos = {}
list_precios = {}
dic_par = {}
dic_kg = {}

precio_par = 0

#cerrar = True


#----------------------------------------------------------------------------------------------#
#Funciones

def menu(art,prec):
    print("------MENU------")
    #print("----------------")
    for i in range(len(art)):
        print(i + 1, art[i + 1], "$",prec[i + 1] )
    return

def validar_pedido(num):
    if num >= 1 and num <= len(articulos):
        kg = float(input("Ingrese cantidad de kilos: "))
        dic_kg[num] = kg

        precio_par= kg * precios[num]
        dic_par[num] = precio_par

        print(" ")
        print("-------------Detalle de Compra---------------")
        print(" ")
        for value in dic_par:
            
            print(f"{dic_kg[value]}kg de {articulos[value]} son ${dic_par[value]}")
        
        print("---------------------------------------------")
        print(" ")
    else:
        print("fruta no disponible")

def total_compra():
    total = 0
    print(" ")
    print("-------------Verduleria Adrian---------------")
    print(" ")

    for value in dic_par:
        
        print(f"{dic_kg[value]}kg de {articulos[value]} son ${dic_par[value]}")
        total = total + dic_par[value]
    print("---------------------------------------------")
    print("El total de su compra es: ", total)

def datos_fijos():
    j = 0
    for i in range(0,len(list_actualizada), 2):
        j += 1
        agr_art = {j:list_actualizada[i]}
        agr_pre = {j:list_actualizada[i+1]}
        list_articulos.update(agr_art)
        list_precios.update(agr_pre)
    return [ list_articulos, list_precios ]

#----------------------------------------------------------------------------------------------#
#Ejecucion del Programa

resultado = datos_fijos()
articulos = resultado[0]
precios = resultado[1]



while True:
    try:
        menu(articulos,precios)
        pedido = int(input("Ingrese el cod de Fruta a llevar o x para salir: "))
        validar_pedido(pedido)
    except:
        total_compra()
        break

print(" ")
print("---------------------")
print("gracias por su compra")
print("---------------------")