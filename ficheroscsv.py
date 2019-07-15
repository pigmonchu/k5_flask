import csv

fMedias = open('data/medias.txt', 'w')
fAlumnos = open('data/alumnos.txt', 'r')
csvreader = csv.reader(fAlumnos,delimiter=',', quotechar='"')

for campos in csvreader:
    print(campos)
    notas_alumno = campos[2:]
    suma = 0
    for nota in notas_alumno:
        suma += float(nota)
    media = suma / len(notas_alumno)
    fMedias.write('"{}","{}",{}\n'.format(campos[0], campos[1], media))

fAlumnos.close()
fMedias.close()