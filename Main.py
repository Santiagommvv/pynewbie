logout = False

#viene a ser un crud a mano, en la carpeta /datos irían en texto plano los players
#va a ser difícil mejorar algo tan abarcativo, pero la idea es ir complejizándolo

while(not logout) :
    #esto lo quiero meter en un switch case pero todavía no lo encuentro
    print('''Choose
          1) See players
          2) Find player : bool
          3) Add player
          4) Modify player
          5) Delete player
          6) Exit\n''')
    
    logout = True

#tratando de meterlos uno a uno y que salte una linea
jugadores = ['Ascii-man', 'Alvarez', 'FILIP']

#asumo que abrir y cerrar el archivo dos veces no tiene sentido, pero...
#además que no estoy interesado en reventar los contenidos cada vez que escribo
fileEsc = open('./datos/players.txt', 'w')
for j in jugadores : 
    fileEsc.writelines(j)
fileEsc.close()

fileRead = open('./datos/players.txt', 'r')
lines = fileRead.readlines()
for line in lines:
    print(line, end='')
fileRead.close()

print('\n')
print('exit')