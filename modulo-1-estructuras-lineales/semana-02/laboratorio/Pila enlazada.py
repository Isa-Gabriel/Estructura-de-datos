"""
Lab 2 — Implementación de la clase Pila Enlazada (Stack)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Isaac Cubilla
Grupo: INF 222 — Estructura de Datos (2026-2)
Fecha: 10/6/2026

"""
if __name__ == "__main__":

    # El tope de la pila inicia en None (vacío)
    tope = None
    ingresando = True

    print("=== REGISTRO EN PILA ENLAZADA  ===")

    # 1. CAPTURA Y CONEXIÓN DE NODOS (PUSH)
    while ingresando:
        nombre = input("\nIngrese nombre (o 'salir' para terminar): ")

        if nombre.lower() == "salir":
            ingresando = False
        else:
            pedido = input("Ingrese el pedido: ")
            paquete = (nombre, pedido)

            # UN NODO ES SOLO UNA LISTA DE 2 POSICIONES: [DATO, SIGUIENTE]
            # Posición 0: El paquete (datos del cliente)
            # Posición 1: La conexión al nodo anterior (el tope actual)
            nuevo_nodo = [paquete, tope]

            # El tope ahora pasa a ser este nuevo nodo
            tope = nuevo_nodo

            print(f"-> ¡{nombre} apilado con éxito!")


    # 2. PROCESAMIENTO Y VACIADO DE LA PILA (POP)
    print("\n" + "=" * 40)
    print("=== PROCESANDO PILA ENLAZADA (LIFO) ===")
    print("=" * 40)

    
    while tope is not None:# Mientras el tope no sea None

        # Extraemos el nodo del tope
        nodo_extraido = tope
        
        # Desconectamos: el tope ahora es el nodo que estaba de segundo en la lista (índice 1)
        tope = nodo_extraido[1]

        # Extraemos los datos del cliente que estaban de primero en la lista (índice 0)
        cliente, pedido = nodo_extraido[0]

        print(f" -> Atendiendo a: {cliente}")
        print(f"    Entregando: {pedido}\n")

    print("¡Pila totalmente vacía!")
