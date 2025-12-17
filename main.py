from datos import PALABRAS, AHORCADO_DIBUJOS
from logica import obtener_palabra_random, formatear_palabra_secreta, obtener_estado_juego

def jugar_turno(palabra_secreta, letras_adivinadas, vidas):
    """
    Bucle principal del juego usando RECURSIVIDAD.
    En lugar de modificar variables (vidas -= 1), pasamos
    los NUEVOS valores a la siguiente llamada de la función.
    """
    
    # --- 1. MOSTRAR ESTADO ACTUAL (Efecto secundario necesario: Print) ---
    print("\n" + "="*30)
    print(f"Vidas restantes: {vidas}")
    print(AHORCADO_DIBUJOS.get(vidas, "X"))
    print("Palabra: " + formatear_palabra_secreta(palabra_secreta, letras_adivinadas))
    
    # --- 2. CASOS BASE (Condición de parada de la recursión) ---
    estado = obtener_estado_juego(palabra_secreta, letras_adivinadas, vidas)
    
    if estado == 'GANO':
        print(f"\n¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
        return # Fin de la recursión
    
    if estado == 'PERDIO':
        print(f"\n¡Game Over! La palabra era: {palabra_secreta}")
        return # Fin de la recursión

    # --- 3. INPUT DEL USUARIO ---
    intento = input("Adivina una letra: ").upper().strip()

    # Validación simple
    if not intento or len(intento) > 1 or not intento.isalpha():
        print("Entrada inválida. Intenta de nuevo.")
        # Llamada recursiva con el MISMO estado (nada cambia)
        return jugar_turno(palabra_secreta, letras_adivinadas, vidas)

    if intento in letras_adivinadas:
        print(f"Ya habías intentado con '{intento}'.")
        # Llamada recursiva con el MISMO estado
        return jugar_turno(palabra_secreta, letras_adivinadas, vidas)

    # --- 4. CALCULAR NUEVO ESTADO (Inmutabilidad) ---
    # Creamos un NUEVO conjunto agregando la letra (unión de conjuntos)
    nuevas_letras_adivinadas = letras_adivinadas | {intento}
    
    # Calculamos las nuevas vidas sin modificar la variable original
    # Operador ternario: (valor_si_verdadero) if (condicion) else (valor_si_falso)
    nuevas_vidas = vidas if intento in palabra_secreta else vidas - 1

    if intento not in palabra_secreta:
        print(f"¡Mala suerte! '{intento}' no está en la palabra.")

    # --- 5. PASO RECURSIVO ---
    # Llamamos a la función a sí misma con los NUEVOS datos
    return jugar_turno(palabra_secreta, nuevas_letras_adivinadas, nuevas_vidas)

def iniciar_juego():
    # Configuración inicial
    palabra = obtener_palabra_random(PALABRAS)
    vidas_iniciales = 6
    letras_iniciales = set() # Conjunto vacío
    
    print("--- BIENVENIDO AL AHORCADO FUNCIONAL ---")
    jugar_turno(palabra, letras_iniciales, vidas_iniciales)

if __name__ == "__main__":
    iniciar_juego()