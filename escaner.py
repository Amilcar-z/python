#!/usr/bin/python

#importamos la libreria socket 
import socket
from socket import *
#creamos una funcion principal
if __name__ == '__main__':
	#definimos una variable en la cual se almacenara la ip o nombre de dominio que se quiera escanear
   equipo = raw_input('ingresa el domino o ip que deseas escanear: ')
   #gethostbyname nos permitira traducir ya sea el dominio o direccion ip ingresada para poder realizar el escaneo en la ip
   ipequipo = gethostbyname(equipo)
   #iniciando el escaneo
   print 'comenzando el escaneo en la ip ', ipequipo;
  #creamos un ciclo con el rango de puestos que desehamos escanear
   for puertos in range(10,500):
    #creamos un socket af_inet para indicar que seran direcciones ipv4 y sock_stream para indicar que sera tcp
    cliente = socket(AF_INET, SOCK_STREAM)
    #guardamos todo en la variable resultado del chekeo al puerto del equipo
    resultado = cliente.connect_ex((ipequipo, puertos))
    #si el resultado es igual a 0 imprimimos en pantalla el numero de puerto con su respectivo estado  
    if (resultado == 0):
      print 'puerto %d: Abierto' %(puertos) 
      #por ultimo cerramos la conexion para que se analice el siguiente puerto
      cliente.close()
