"""
Lab 2 — Implementación de principio FIFO
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Isaac Cubilla
Grupo: INF 222 — Estructura de Datos (2026-2)
Fecha: 10/6/2026

"""

if __name__ == "__main__":

    cola_clientes = []
    ingresando = True

    print("=== REGISTRO DE CLIENTES (ENTRADA DE DATOS) ===")
    
    # 1. CICLO PARA CAPTURAR DATOS POR TECLADO
    
    while ingresando: # si ingresando  es false se termien el while
        
        nombre = input("\nIngrese nombre del cliente (o escriba 'salir' para terminar): ")
        
        if nombre.lower() == "salir":# si se escribe salir se termina el ciclo
            ingresando = False
        else:
            pedido = input("Ingrese el pedido del cliente: ")
                        
            paquete = (nombre, pedido)# se crea la tupla con nombre y apellido

            cola_clientes.append(paquete) # se agrega la tupla a la pila

            print(f"-> ¡{nombre} agregado a la cola!")

    
    print(f"TOTAL DE CLIENTES EN ESPERA: {len(cola_clientes)}")  

    # 3. PROCESAR Y VACIAR LA COLA EN ORDEN FIFO (Dequeue)
    print("\n=== ATENDIENDO CLIENTES (FIFO) ===")
    
    while len(cola_clientes) > 0: #mientras cola_clientes sea mayor que 0 se ejecuta el ciclo

        pedido = None
        
        cliente, pedido = cola_clientes.pop(0) # Extrae el primer paquete de la cola
        
        print(f" -> Atendiendo a: {cliente}")
        print(f"    Pedido entregado: {pedido}")
        print(f"    (Quedan {len(cola_clientes)} personas en la cola)\n")

    print("¡Todos los clientes han sido atendidos exitosamente!")


"""
    
DECLARACION DE IA

IA utilizada                        : geminis 3.1 PRO y vs code

Para que                            : para investigar los principios de FIFO

que hice yo                         : le di prompts a la IA para que me explique el código y me ayude a entenderlo, 
pense la logica y funcionamiento del codigo y la IA autocompletaba el codigo repetitivo

prompts que le di a la IA           : Que hace este codigo?
                                      

puedo explicar todo el codigo sin IA: Sí

"""
