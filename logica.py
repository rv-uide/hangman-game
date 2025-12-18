import random

def obtener_palabra_random(lista_palabras):
    """
    Elige una palabra al azar.
    """
    return random.choice(lista_palabras).upper()

def formatear_palabra_secreta(palabra_secreta, letras_adivinadas):
    """
    Mapea la palabra secreta a una cadena visible.
    Si la letra está en 'letras_adivinadas', la muestra. Si no, pone '_'.
    """
    letras_visibles = [letra if letra in letras_adivinadas else '_' for letra in palabra_secreta]
    return ' '.join(letras_visibles)

def obtener_estado_juego(palabra_secreta, letras_adivinadas, vidas):
    """
    Analiza si el juego ha terminado.
    Retorna: 'GANO', 'PERDIO', o 'JUGANDO'
    """
    # Usamos conjuntos (sets) para verificar matemáticamente si
    # todas las letras de la palabra están dentro de las adivinadas.
    if set(palabra_secreta).issubset(letras_adivinadas):
        return 'GANO'
    
    if vidas <= 0:
        return 'PERDIO'
        
    return 'JUGANDO'