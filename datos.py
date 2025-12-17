# Lista de palabras para el juego.
PALABRAS = ['PYTHON', 'FUNCIONAL', 'RECURSIVIDAD', 'LAMBDA', 'INMUTABLE']

# Diccionario que mapea el número de vidas restantes al arte ASCII.
# Clave (int): Vidas | Valor (str): Dibujo
AHORCADO_DIBUJOS = {
    6: "",
    5: "O",
    4: "O\n|",
    3: "O\n/|",
    2: "O\n/|\\",
    1: "O\n/|\\\n/",
    0: "O\n/|\\\n/ \\"
}