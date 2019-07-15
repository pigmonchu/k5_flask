fAlumnos = open('data/alumnos.txt', 'r')
fMedias = open('data/medias.txt', 'w')
alumnos = fAlumnos.readlines()

for alumno in alumnos:
    datos_alumno = alumno.split(',')
    notas_alumno = datos_alumno[2:]
    suma = 0
    for nota in notas_alumno:
        suma += float(nota)
    media = suma / len(notas_alumno)
    fMedias.write("{},{},{}\n".format(datos_alumno[0], datos_alumno[1], media))

fAlumnos.close()
fMedias.close()