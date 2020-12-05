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

# Comandos Cisco para configurar Switch y VLAN via Telnet
conexion.write(b"enable\n")
conexion.write(b"thor\n")
conexion.write(b"confi term\n")
conexion.write(b"vlan 2\n")
conexion.write(b"name VLAN-PY-2\n")
conexion.write(b"vlan 3\n")
conexion.write(b"name VLAN-PY-3\n")
conexion.write(b"vlan 4\n")
conexion.write(b"name VLAN-PY-4\n")
conexion.write(b"vlan \n")
conexion.write(b"name VLAN-PY-5\n")
conexion.write(b"vlan 6\n")
conexion.write(b"name VLAN-PY-6\n")
conexion.write(b"vlan 7\n")
conexion.write(b"name VLAN-PY-7\n")
conexion.write(b"end\n")
conexion.write(b"exit\n")

#Lee la infromacion de la conexion Telnet y la imprime en el Network Automation
print(conexion.read_all().decode('ascii'))