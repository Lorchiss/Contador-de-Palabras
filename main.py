import operator

nombreArchivo = "la voz de los 80.txt" 
archivo = open(nombreArchivo, 'r')

lineas = archivo.readlines()

cancion = {}

for iter in lineas:
    iter = iter.lower()
    palabras = iter.split()
    for palabra in palabras:
        if palabra in cancion:
            cancion[palabra] += 1
        else:
            cancion[palabra] = 1
     

cancionOrdenado = sorted(cancion.items(),key=operator.itemgetter(1), reverse=True)
for palabra in cancionOrdenado:
    print(palabra)

archivo.close()