from datos import PALABRAS, AHORCADO_DIBUJOS
from logica import obtener_palabra_random, formatear_palabra_secreta, obtener_estado_juego

def iniciar_juego():
    # --- CONFIGURACIÓN INICIAL DEL ESTADO ---
    palabra_secreta = obtener_palabra_random(PALABRAS)
    vidas = 6
    letras_adivinadas = set() # Conjunto vacío para guardar letras
    
    print("--- BIENVENIDO AL JUEGO DEL AHORCADO ---")

    # --- BUCLE PRINCIPAL DEL JUEGO ---
    while True:
        
        # 1. MOSTRAR LA "VISTA" AL USUARIO
        # Usamos las funciones de logica.py para transformar los datos a texto
        print("\n" + "="*30)
        print(f"Vidas restantes: {vidas}")
        print(AHORCADO_DIBUJOS.get(vidas, "X"))
        print("Palabra: " + formatear_palabra_secreta(palabra_secreta, letras_adivinadas))

        # 2. VERIFICAR EL ESTADO DEL JUEGO
        # Le preguntamos a nuestra función pura cómo está el juego
        estado = obtener_estado_juego(palabra_secreta, letras_adivinadas, vidas)

        if estado == 'GANO':
            print(f"\n¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
            break # Rompemos el ciclo while para terminar
        
        if estado == 'PERDIO':
            print(f"\n¡Game Over! La palabra era: {palabra_secreta}")
            break # Rompemos el ciclo while para terminar

        # 3. ENTRADA DE DATOS (INPUT)
        intento = input("Adivina una letra: ").upper().strip()

        # 4. VALIDACIÓN
        if not intento or len(intento) > 1 or not intento.isalpha():
            print("Entrada inválida. Debe ser una sola letra.")
            continue # Saltamos al inicio del while sin cambiar vidas ni letras

        if intento in letras_adivinadas:
            print(f"Ya habías intentado con '{intento}'.")
            continue # Saltamos al inicio del while

        # 5. ACTUALIZACIÓN DEL ESTADO
        # Agregamos la letra al conjunto
        letras_adivinadas.add(intento)

        if intento not in palabra_secreta:
            print(f"¡Mala suerte! '{intento}' no está en la palabra.")
            vidas -= 1 # Reducimos la vida (Mutación de estado, común en while)
        else:
            print(f"¡Bien hecho! '{intento}' es correcta.")

if __name__ == "__main__":
    iniciar_juego()