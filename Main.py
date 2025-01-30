#dev-ería mergearme a main y no al revés.

logout = False

#viene a ser un crud a mano, en la carpeta /datos irían en texto plano los players
#va a ser difícil mejorar algo tan abarcativo, pero la idea es ir complejizándolo

while not logout: # los paréntesis no jodían, pero tampoco eran necesarios
    #esto lo quiero meter en un switch case pero todavía no lo encuentro
    # No existe el switch case, habría que usar if, elif, elif, elif, elif, else
    # me parece
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

# Un try para manejar errores (sería bueno que supiera bien cómo funca)
try: 
    # Abrir el archivo dentro de un with, que lo cierra automáticamente después
    with open('./datos/players.txt', 'w') as f:
        # Escribir mediante join(), que usa como separador a "\n", tomando los
        # strings a unir desde un iterable
        f.write("\n".join(jugadores) + "\n")
except Exception as e:
    print(f"Se produjo el error: {e}.")

try:
    with open('./datos/players.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
except Exception as e:
    print(f"Se produjo el error: {e}.")

for line in lines:
    print(line)
    
print('\n')
print('exit')

