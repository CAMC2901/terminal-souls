import random
## RETO JUEGO: Terminal Souls
## Héroe: 100 HP, 3 pociones de curación. 
## Enemigo: 120 HP.

## ------ BARRA DE SALUD ---##

def mostrar_estado(nombre_h, heroe_hp, nombre_e, enemigo_hp):
    barras_h = int(( max (0,heroe_hp) / 100) * 30) 
    barra_h = "[" + "#" * barras_h + "-" * (30 - barras_h) + "]"
    
    barras_e = int((max(0,enemigo_hp) / 120) * 30)  
    barra_e = "[" + "#" * barras_e + "-" * (30 - barras_e) + "]"
    
    print(f"\n{nombre_h}: {max(0,heroe_hp)} HP {barra_h}")
    print(f"{nombre_e}: {max(0,enemigo_hp)} HP {barra_e}")


## FUNCIONES DEL JUEGO

heroe_hp = 100
enemigo_hp = 120
heroe_pociones = 3

def generar_daño(min, max):
    return random.randint(min, max)


def turno_jugador(heroe_hp, enemigo_hp, heroe_pociones):
    accion_valida = False
    while not accion_valida:
        print("Es tu turno, elige una acción:")
        print("1. Atacar🥊")
        print("2. Usar poción💊", "(", heroe_pociones, ")"    )
        print("3. Usar habilidad especial🪄")
        accion = input("Ingresa el número de la acción que deseas realizar: ")
        
        if accion == "1":
                daño = generar_daño(10, 25)
                enemigo_hp -= daño
                print(f" El Héroe golpea por {daño} de daño.💥")        
                accion_valida = True
        elif accion == "2":
                if heroe_pociones <= 0:
                    print(" No tienes pociones. Elige otra acción.❌")
                    continue  
                heroe_hp = min(heroe_hp + 20, 100)
                heroe_pociones -= 1
                print(f" Usaste una poción. ({heroe_pociones} restantes)💊")  
                accion_valida = True
        elif accion == "3":
            if random.random() < 0.5:
                daño_especial = generar_daño(30, 50)
                enemigo_hp -= daño_especial
                print(f"¡Habilidad especial! Golpeas por {daño_especial} de daño. 🪄")
            else:
                print("¡La habilidad especial falló!😵")
            accion_valida = True
        else:
            print(" Acción no válida. Intenta de nuevo.")
    return heroe_hp, enemigo_hp, heroe_pociones


def turno_enemigo(heroe_hp):
    print("Es el turno del enemigo, está atacando...")
    daño_enemigo = generar_daño(15, 20)
    print(f"El enemigo inflige {daño_enemigo} puntos de daño.💥")
    heroe_hp -= daño_enemigo
    return heroe_hp


def verificar_ganador(heroe_hp, enemigo_hp):
    if heroe_hp <= 0:
        print ("\n ❇︎❇︎❇︎❇︎❇︎❇︎❇︎ FIN DEL JUEGO ❇︎❇︎❇︎❇︎❇︎❇︎❇︎")
        print("¡El enemigo ha ganado!☠️")
        return True
    elif enemigo_hp <= 0:
        print ("\n ❇︎❇︎❇︎❇︎❇︎❇︎❇︎ FIN DEL JUEGO ❇︎❇︎❇︎❇︎❇︎❇︎❇︎")
        print("¡Has ganado!🏅")
        return True
    return False

## ### ------ EJECUCION DEL JUEGO ----- #### 
print ("TERMINAL SOULS")
nombre_h = input("Nombre Heroe🦸: ")
nombre_e = input("Nombre Enemigo🦹: ")

while enemigo_hp > 0 and heroe_hp > 0:

    mostrar_estado(nombre_h, heroe_hp, nombre_e, enemigo_hp)

    heroe_hp, enemigo_hp, heroe_pociones = turno_jugador(heroe_hp, enemigo_hp, heroe_pociones)

    if enemigo_hp > 0 and heroe_hp > 0:
        heroe_hp = turno_enemigo(heroe_hp)

mostrar_estado(nombre_h, heroe_hp, nombre_e, enemigo_hp)
verificar_ganador(heroe_hp, enemigo_hp)
   

        
     
    
         