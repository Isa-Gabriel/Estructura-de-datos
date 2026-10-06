"""
Lab 2 — Implementación de principio FIFO
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Isaac Cubilla
Grupo: INF 222 — Estructura de Datos (2026-2)
Fecha: 10/6/2026

"""

if __name__ == "__main__":

    print("=== VERIFICADOR DE PARÉNTESIS BALANCEADOS ===")
    
    cadena = input("\nIngrese una expresión (ejemplo: [{()}]): ")

    # El tope de nuestra pila empieza en None (vacía)
    tope = None
    
    # Diccionario con las parejas correctas: cierre -> apertura
    parejas = {')': '(', ']': '[', '}': '{'}
    aperturas = "([{"
    
    balanceado = True

    # Recorremos la cadena letra por letra
    for caracter in cadena:

        # 1. SI ES APERTURA: HACEMOS PUSH (Apilamos)
        if caracter in aperturas:
            # Creamos el nuevo nodo: [el caracter, la conexión al tope anterior]
            nuevo_nodo = [caracter, tope]
            # Movemos el tope al nuevo nodo
            tope = nuevo_nodo

        # 2. SI ES CIERRE: HACEMOS POP Y COMPARAMOS
        elif caracter in parejas:
            
            # Si viene un cierre pero la pila está vacía (no hay apertura con qué comparar)
            if tope is None:
                balanceado = False
                break

            # Extraemos el nodo de arriba
            nodo_extraido = tope
            
            # Movemos el tope hacia la caja de abajo
            tope = nodo_extraido[1]
            
            # Sacamos el caracter que estaba guardado
            simbolo_guardado = nodo_extraido[0]

            # Verificamos si la apertura guardada coincide con la de cierre que leímos
            if simbolo_guardado != parejas[caracter]:
                balanceado = False
                break

    # 3. VERIFICACIÓN FINAL
    # Si terminamos el ciclo y todavía quedaron símbolos sin cerrar en la pila
    if tope is not None:
        balanceado = False

    # RESULTADO
    print("\n" + "=" * 40)
    if balanceado:
        print(f"¡ÉXITO! La expresión '{cadena}' está BALANCEADA.")
    else:
        print(f"¡ERROR! La expresión '{cadena}' NO está balanceada.")
    print("=" * 40)

    
"""
    
DECLARACION DE IA

IA utilizada                        : geminis 3.1 PRO y vs code

Para que                            : para investigar los parentesis balanceados 
que hice yo                         : le di prompts a la IA para que me explique el código y me ayude a entenderlo, 
pense la logica y funcionamiento del codigo y la IA autocompletaba el codigo repetitivo
                                 
puedo explicar todo el codigo sin IA: Sí

"""
