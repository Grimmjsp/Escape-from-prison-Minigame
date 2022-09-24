import random

# Mini Game based on simple decisions

print("Escapa de la prisión\n"
      "--------------------\n"
      "Has sido encarcelado por robar en un banco nacional.\nDelante de la puerta está el guardia con las llaves de la celda y debajo de la cama hay un clip.\nPuedes usar el clip cuando el guarda se marche para tratar de abrir la celda o\npuedes crear una distracción para que el guardia entre y noquearlo para coger las llaves.")

decision = input("¿Qué vas a hacer, opción [1] u opción [2]?\n")

# Si decides opción 1
if decision == "1" or decision == "opción 1" or decision == "opcion 1":
    print("\nHas usado el clip para tratar de abrir la cerradura cuando el guardia no estaba.\nSe escucha un 'click' y la cerradura se abre.\n"
          "Avanzas por el pasillo hasta llegar a una habitación.\n"
          "En ella encuentras una porra.\n"
          "¿Deseas recoger la porra?")
    decision = input("[Si] o [No]")
    
    # Si decides no coger la porra
    if decision == "No" or decision == "NO" or decision == "nO" or decision == "no":
      print("Sigues avanzando y sales a una especie de patio de recreo.\n"
            "Hay un guardia en el muro de la derecha mirando hacia la salida del patio.\n"
            "A la izquierda hay un guardia apostado en una torre vigilando alrrededor de la misma.\n"
            "Puedes esperar a que el guardia apostado se de la vuelta e intentar noquear al guardia del muro para pasar o\n"
            "puedes tratar de escabullirte sin que te vean para llegar a la salida.\n")
      decision = input("¿Qué vas a hacer, opción [1] u opción [2]?\n")
      
      # Si decides esperar y forcejear
      if decision == "1" or decision == "opción 1" or decision == "opcion 1":
            print("Consigues llegar hasta el guardia del muro y al forcejear se dispara su arma alertando al guardia apostado. Tratas de correr hacia la salida\n"
                  "pero la puerta se bloquea debido a la alarma. El guardia de la torre te dispara y mueres.\n"
                  "GAME OVER\n"
                  "---------\n")
      # Si decides escabullirte de forma sigilosa            
      elif decision == "2" or decision == "opción 2" or decision == "opcion 2":
            chance = random.randint(0, 100)
            print("Probabilidades de éxito {}%".format(chance))

            if chance >= 50 <= 100:
                  print("Has conseguido sortear a los guardias y te encuentras en la entrada de la prisión.\n"
                        "Resulta que no hay ningún guardia en el recibidor por lo que procedes a buscar la llave que te hará libre.\n"
                        "Mientras rebuscabas los cajones del recibidor escuchas pasos acercándose. Es un guardia que va directo hacia ti.\n"
                        "Puedes tratar de neutralizar al guardia con el material de oficina a tu alcance (lápices, bolígrafos, grapadoras, etc.) o\n"
                        "puedes tratar de rodear el recibidor para que el guardia no te vea, ver donde guarda la llave y tratar de cogerla sigilosamente.\n")
                  decision = input("¿Qué vas a hacer, opción [1] u opción [2]?")
                  
                  # Si decides neutralizar al guardia
                  if decision == "1" or decision == "opcion 1" or decision == "opción 1":
                        print("Tratas de neutralizar al guardia atacándolo con un bolígrafo, por desgracia no consigues atravesar su chaleco pero durante el forcejeo\n"
                              "se le cae la pistola. La recoges y le disparas. Coges la llave y sales fuera de la prisión pero los demás guardias dieron la voz de alarma.\n"
                              "Tratas de correr para escabullirte de ellos pero disponen de muchos efectivos por lo que tratas de defenderte con la pistola.\n"
                              "Los guardias te disparan y te dan. Llegas hasta un coche pero ya has perdido mucha sangre por lo que una vez dentro del coche\n"
                              "comienzan a cerrarse tus ojos y mueres.\n"
                              "GAME OVER\n"
                              "---------\n")

                  # Si decides jugar sigilosamente            
                  elif decision == "2" or decision == "opcion 2" or decision == "opción 2":
                        print("Consigues rodear al guardia y observas que la llave está atada a su cinturón. Lanzas un papel hacia un lado y en el descuido\n"
                              "consigues hacerte con la llave del guardia y escapar. Más adelante te encuentras con un coche. Sacas a su conductor, te montas\n"
                              "y te marchas a vivir una nueva vida.\n"
                              "!FELICIDADES¡\n"
                              "Has completado el juego.\n"
                              "------------------------\n")
            
            elif chance < 50 >= 0:
                  print("El guardia de la torre te ve tratando de escapar y da la voz de alarma. Las puertas de la prisión se cierran y los guardias te atrapan.\n"
                        "Vuelves a la celda pero esta vez estás en aislamiento sin posibilidad de escapar.\n"
                        "GAME OVER\n"
                        "---------\n")

    # Si decides coger la porra
    elif decision == "Si" or decision == "si" or decision == "sI" or decision == "SI":
        print("Sigues avanzando y sales a una especie de patio de recreo.\n"
              "Hay un guardia en el muro de la derecha mirando hacia la salida del patio.\n"
              "A la izquierda hay un guardia apostado en una torre vigilando alrrededor de la misma.\n"
              "\n"
              "Puedes esperar a que el guardia de la torre se de la vuelta y noquear al otro guardia con la porra o\n"
              "puedes esperar a que el guardia de la torre se de la vuelta y lanzar la porra a un lado para distraer al otro guardia y salir del patio.\n")
        decision = input("¿Que vas a hacer, opción [1] u opción [2]?\n")
        
        # Decides esperar a que el guardia de la torre se de la vuelta y noquear al otro
        if decision == "1" or decision == "opción 1" or decision == "opcion 1":
            chance = random.randint(0, 100)
            print("Probabilidades de éxito {}%".format(chance))

            if chance >= 50 <= 100:
                print("Noqueas al guardia con éxito pero haces mucho ruido y el guardia apostado te mira escabullirte por la salida y da la alarma.\n"
                      "Sigues adelante y terminas en la entrada de la prisión.\n"
                      "Hay dos guardias alerta por la alarma y lo único que tienes a mano es material de oficina (lápices, papeles, papeleras, grapadoras, etc.)\n"
                      "Puedes tratar de noquear a los guardias en un intento desesperado de salir usando todos los recursos disponibles a tu alcance o\n"
                      "puedes crear una distración para desviar su antención de la salida y escabullirte lo más rápido que puedas.\n")
                decision = input("Solo se vive una vez [opción 1] o Sneaky like a panthera [opción 2]\n")
                
                # Decides hacer un YOLO
                if decision == "1" or decision == "opción 1" or decision == "opcion 1":
                    print("Te lanzas desesperada mente contra los guardas, le clavas un bolígrafo en el cuello a uno y forcejeas con el otro.\n"
                          "Por desgracia el guardia con el bolígrafo clavado no muere y te dispara.\n"
                          "Te da varios disparos y mueres desangrado no sin antes acabar en el otro guardia.\n"
                          "GAME OVER\n"
                          "---------\n")

                # Tratas de hacerlo en sigilo
                elif decision == "2" or decision == "opción 2" or decision == "opcion 2":
                    print("Llamas la atención de uno de los guardias y consigues abatirlo con un lápiz en el cuello.\n"
                          "Registras al guardia y encuentras la llave que te lleva hacia la libertad.\n"
                          "Para poder usar la llave tienes que deshacerte del segundo guardia y abrir las puertas de la prisión.\n"
                          "Puedes coger el arma del guardia abatido y disparar al otro guardia, lo cual alertará a la prisión o\n"
                          "Puedes usar el walkietalkie del guardia abatido para dar información falsa y hacer que el guardia salga de ahí.\n")
                    decision = input("¿Qué vas a hacer, opción [1] o opción [2]?\n")
                    
                    # Decides armarte y abatir al guardia
                    if decision == "1" or decision == "opción 1" or decision == "opcion 1":
                        chance = random.randint(0, 100)
                        print("Probabilidades de éxito {}%".format(chance))

                        if chance >= 50 <= 100:
                              print("Recoges el arma del suelo y disparas al guardia, el cual muere al instante. Suena la alarma pero consigues abrir las puertas y salir.\n"
                                    "Fuera de la prisión robas un coche y te marchas a rehacer tu vida sabiendo que serás siempre perseguido por la justicia.\n"
                                    "!FELICIDADES¡\n"
                                    "Has compleado el juego.\n"
                                    "-----------------------\n")

                        if chance < 50 >= 0:
                              print("Recoges el arma del suelo y disparas, fallando el primer tiro. El guarda responde pero por desgracia para tí, él no falla.\n"
                                    "Recibes un disparo en el pecho y mueres desangrado.\n"
                                    "GAME OVER\n"
                                    "---------\n")

            elif chance < 50 >= 0:
                print("No has tenido suerte, forcejeas con el guarda pero la porra se rompe.\n"
                      "Recibes un disparo mortal en el pecho, te desangras y mueres.\n"
                      "GAME OVER\n"
                      "---------\n")
        # Decides esperar y distraer al guardia
        elif decision == "2" or decision == "opción 2" or decision == "opcion 2":
            chance = random.randint(0, 100)
            print("Probabilidades de éxito {}%".format(chance))

            if chance >= 50 < 100:
                print("Consigues distraer al guarda, lo que te permite colarte sin problemas por la salida.\n"
                      "Sigues avanzando y terminas en la entrada de la prisión.\n"
                      "Hay un guardia detrás de un mostrador mirando papeles y con una llave sobre el mostrador que abre la puerta que da a la salida.\n"
                      "Puedes tratar de robar la llave de forma sigilosa o puedes distraer al guardia usando lo que tienes al alcance y robar la llave.\n")
                decision = input("Modo sigiloso [opción 1] o Distracción [opción 2]\n")

                # Tratas de robar la llave de forma sigilosa
                if decision == "1" or decision == "opción 1" or decision == "opcion 1":
                  chance = random.randint(0, 100)
                  print("Probabilidades de éxito {}%".format(chance))

                  if chance >= 50 <= 100:
                        print("Consigues robar la llave sin que se de cuenta. Distraes al guardia con éxito y abres la puerta sin que te vea.\n"
                              "Sales a la calle, robas un coche y te marchas a comenzar una nueva vida.\n"
                              "!FELICIDADES¡\n"
                              "Has completado el juego.\n"
                              "------------------------\n")

                  elif chance < 50 >= 0:
                        print("Tratas de coger la llave pero por desgracia para ti el guarda te ve.\n"
                              "Intentas escapar corriendo pero te dispara y mueres desangrado.\n"
                              "GAME OVER\n"
                              "---------\n")
                
                # Tratas de distraer al guardia y robar la llave.
                elif decision == "2" or decision == "opcion 2" or decision == "opción 2":
                  print("Usas unos lápices para distraer al guarda, pero por desgracia, el guardia sale del mostrador por el lado donde tu te encuentras y te ve.\n"
                        "Forcejeas con el, pero el guardia es más fuerte que tu y te reduce. Vuelves a prisión pero esta vez en aislamiento e incomunicado.\n"
                        "GAME OVER\n"
                        "---------\n")

            elif chance < 50 >= 0:
                print("No ha habido suerte, el guardia te mira lanzar el palo y comienza a dispararte.\n"
                      "Te dan en el hombro, te desangras y mueres.\n"
                      "GAME OVER\n"
                      "---------\n")

elif decision == "2" or decision == "opción 2" or decision == "opcion 2":
    print("Llamas la atención del guardia y entra en tu celda.\n"
          "Forcejeas con el guarda y en un segundo saca la pistola y dispara.\n"
          "Has muerto de un disparo en el pecho.\n"
          "GAME OVER\n"
          "---------\n")


