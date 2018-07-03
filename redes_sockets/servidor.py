#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1) #Establece cuantas conexiones puede encolar

conn, addr = s.accept()
print 'Se ha establecido enlace con:', addr

mensaje = ""
while mensaje != "salir":
  mensaje = conn.recv(BUFFER_SIZE)
  print "Mensaje recibido:", mensaje
conn.close()