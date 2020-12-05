#!/usr/bin/python3

# Importando Librerias Telnet
import getpass
import telnetlib

# Variables para Gestionar la Data de la Conexion
equipo = "192.168.122.x"
usuario = input("Ingresa tu nombre de usuario Telnet: ")
clave = getpass.getpass()

# Conexion al dispositivo con Libreria Telnet de Python
conexion = telnetlib.Telnet(equipo)

conexion.read_until(b"Username: ")
conexion.write(usuario.encode('ascii') + b"\n")
if clave:
    conexion.read_until(b"Password: ")
    conexion.write(clave.encode('ascii') + b"\n")

# Comandos Cisco para configurar el equipo via Telnet
conexion.write(b"enable\n")
conexion.write(b"thor\n")
conexion.write(b"config term\n")
conexion.write(b"int lo0\n")
conexion.write(b"ip add 1.1.1.1 255.255.255.255\n")
conexion.write(b"end\n")
conexion.write(b"exit\n")

#Lee la infromacion de la conexion Telnet y la imprime en el Network Automation
print(conexion.read_all().decode('ascii'))

