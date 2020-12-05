#!/usr/bin/python3

# Importando Librerias Telnet
import getpass
import telnetlib

# Variables para Gestionar la Data de la Conexion a Switch
equipo = "192.168.122.100"
usuario = input("Ingresa tu nombre de usuario Telnet: ")
clave = getpass.getpass()

# Conexion al dispositivo con Libreria Telnet de Python
conexion = telnetlib.Telnet(equipo)

conexion.read_until(b"Username: ")
conexion.write(usuario.encode('ascii') + b"\n")
if clave:
    conexion.read_until(b"Password: ")
    conexion.write(clave.encode('ascii') + b"\n")

# Comandos Cisco para entrar al modo de configuracion del Switch
conexion.write(b"enable\n")
conexion.write(b"thor\n")
conexion.write(b"config term\n")

#Loop para crear multiples VLAN en un solo comando
for vlan in range (2,11):
    conexion.write(b"vlan " + str(vlan).encode('ascii') + b"\n")
    conexion.write(b"name VLAN-PY-" + str(vlan).encode('ascii') + b"\n")
conexion.write(b"end\n")
conexion.write(b"exit\n")

#Lee la infromacion de la conexion Telnet y la imprime en el Network Automation
print(conexion.read_all().decode('ascii'))