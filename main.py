nombreArchivo = "la voz de los 80.txt" 
archivo = open(nombreArchivo, 'r')

#print(archivo.read())

lineas = archivo.readlines()
#print(lineas) 
print(lineas.count("Ya se siente la atmósfera"))

archivo.close()