import random
turno="heroe"
heroe_hp = 100
enemigo_hp = 100
heroe_pociones = 3

def generar_daño(min, max):
    if turno=="heroe":
        heroe=random.randint(10, 25)
        return heroe
    elif turno== "enemigo":
        enemigo=random.randint(15, 20)
        return enemigo
    else:
        h_especial=random.randint(30, 50)
        return h_especial

def turno_jugador():
    accion_valida = False
    while not accion_valida:
        print("Es tu turno, elige una acción:")
        print("1. Atacar")
        print("2. Usar poción")
        print("3. Usar habilidad especial")
        accion = input("Ingresa el número de la acción que deseas realizar: ")
        
        if accion == "1":
                daño = generar_daño(10, 25)
                enemigo_hp -= daño
                print(f" El Héroe golpea por {daño} de daño.")        
                accion_valida = True
        elif accion == "2":
                if heroe_pociones <= 0:
                    print("No tienes pociones. Elige otra acción.")
    
                heroe_hp = min(heroe_hp + 20, 100)
                heroe_pociones -= 1
                print(f" Usaste una poción. ({heroe_pociones} restantes)")  
                accion_valida = True
        elif accion == "3":
                daño_especial = generar_daño(30, 50)
                enemigo_hp -= daño_especial
                print(f" Usaste tu habilidad especial y golpeas por {daño_especial} de daño.")         
                accion_valida = True
        else:
         print(" Acción no válida. Intenta de nuevo.")

def turno_enemigo():
    print("Es el turno del enemigo, está atacando...")
    daño_enemigo = generar_daño(15, 20)
    print(f"El enemigo inflige {daño_enemigo} puntos de daño.")
    return daño_enemigo
def verificar_ganador(hp_h, hp_e):
    if hp_h <= 0:
        print("¡El enemigo ha ganado!")
        return True
    elif hp_e <= 0:
        print("¡Has ganado!")
        return True
    return False
