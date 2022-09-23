import random

# Mini Game based on simple decisions

print("Escapa de la prisión\n"
      "--------------------\n"
      "Has sido encarcelado por robar en un banco nacional.\nDelante de la puerta está el guardia con las llaves de la celda y debajo de la cama hay un clip.\nPuedes usar el clip cuando el guarda se marche para tratar de abrir la celda o\npuedes crear una distracción para que el guardia entre y noquearlo para coger las llaves.")

decision = input("¿Qué vas a hacer, opción [1] u opción [2]?\n")

if decision == "1" or decision == "opción 1" or decision == "opcion 1":
    print("\nHas usado el clip para tratar de abrir la cerradura cuando el guardia no estaba.\nSe escucha un 'click' y la cerradura se abre.\n"
          "Avanzas por el pasillo hasta llegar a una habitación.\n"
          "En ella encuentras una porra.\n"
          "¿Deseas recoger la porra?")
    decision = input("[Si] o [No]")
    if decision == "Si" or decision == "si" or decision == "sI" or decision == "SI":
        print("Sigues avanzando y sales a una especie de patio de recreo.\n"
              "Hay un guardia en el muro de la derecha mirando hacia la salida del patio.\n"
              "A la izquierda hay un guardia apostado en una torre vigilando alrrededor de la misma.\n"
              "\n"
              "Puedes esperar a que el guardia de la torre se de la vuelta y noquear al otro guardia con el palo o\n"
              "puedes esperar a que el guardia de la torre se de la vuelta y lanzar el palo a un lado para distraer al otro guardia y salir del patio.\n")
        decision = input("¿Que vas a hacer, opción [1] u opción [2]?\n")
        if decision == "1" or decision == "opción 1" or decision == "opcion 1":
            chance = random.randint(0, 100)
            print("Probabilidades de éxito {}%".format(chance))
            if chance >= 50 < 100:
                print("Noqueas al guardia con éxito pero haces mucho ruido y el guardia apostado te mira escabullirte por la salida y da la alarma.\n"
                      "Sigues adelante y terminas en la entrada de la prisión.\n"
                      "Hay dos guardias alerta por la alarma y lo único que tienes a mano es material de oficina (lápices, papeles, papeleras, grapadoras, etc.)\n"
                      "Puedes tratar de noquear a los guardias en un intento desesperado de salir usando todos los recursos disponibles a tu alcance o\n"
                      "puedes crear una distración para desviar su antención de la salida y escabullirte lo más rápido que puedas.\n")
                decision = input("Solo se vive una vez [opción 1] o Sneaky like a panthera [opción 2]\n")
                if decision == "1" or decision == "opción 1" or decision == "opcion 1":
                    print("Te lanzas desesperada mente contra los guardas, le clavas un bolígrafo en el cuello a uno y forcejeas con el otro.\n"
                          "Por desgracia el guardia con el bolígrafo clavado no muere y te dispara.\n"
                          "Te da varios disparos y mueres desangrado no sin antes acabar en el otro guardia.\n"
                          "GAME OVER\n"
                          "---------\n")
                elif decision == "2" or decision == "opción 2" or decision == "opcion 2":
                    print("Llamas la atención de uno de los guardias y consigues abatirlo con un lápiz en el cuello.\n"
                    )
            elif chance < 50 >= 0:
                print("No has tenido suerte, forcejeas con el guarda pero el palo se rompe.\n"
                      "Recibes un disparo mortal en el pecho, te desangras y mueres.\n"
                      "GAME OVER\n"
                      "---------\n")
        elif decision == "2" or decision == "opción 2" or decision == "opcion 2":
            chance = random.randint(0, 100)
            print("Probabilidades de éxito {}%".format(chance))
            if chance >= 50 < 100:
                print("Consigues distraer al guarda, lo que te permite colarte sin problemas por la salida.\n"
                      "Sigues avanzando y terminas en la entrada de la prisión.\n"
                      "Hay un guardia detrás de un mostrador mirando papeles y con una llave sobre el mostrador que abre la puerta que da a la salida.\n"
                      "Puedes tratar de robar la llave de forma sigilosa o puedes distraer al guardia usando lo que tienes al alcance y robar la llave.\n")
                decision = input("Modo sigiloso [opción 1] o Distracción [opción 2]\n")
            elif chance < 50 >= 0:
                print("No ha habido suerte, el guardia te mira lanzar el palo y comienza a dispararte.\n"
                      "Te dan en el hombro, te desangras y mueres.\n"
                      "GAME OVER\n"
                      "---------\n")

    elif decision == "No" or decision == "nO" or decision == "no" or decision == "NO":
        print("Sigues avanzando y sales a una especie de patio de recreo.\n"
              "Hay un guardia en el muro de la derecha mirando hacia la salida del patio.\n"
              "A la izquierda hay un guarda apostado en una torre vigilando alrrededor de la misma.\n"
              "\n"
              "Tratas de escabullirte de forma sigilosa, pero el guardia de la torre te mira mientras sorteas al guarda del muro.\n"
              "Comienzan a disparar y te dan en el hombro, te desangras y mueres.\n"
              "GAME OVER\n"
              "---------\n")
elif decision == "2" or decision == "opción 2" or decision == "opcion 2":
    print("Llamas la atención del guardia y entra en tu celda.\n"
          "Forcejeas con el guarda y en un segundo saca la pistola y dispara.\n"
          "Has muerto de un disparo en el pecho.\n"
          "GAME OVER\n"
          "---------\n")


