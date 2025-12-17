# 🐍 Juego del Ahorcado (Hangman)

Este es un proyecto educativo implementado en Python que simula el clásico juego del Ahorcado. 

## 📂 Estructura del Proyecto

El código está dividido en tres archivos para mantener el orden y la claridad:

### 1. `datos.py`
Contiene la información estática que no cambia durante la ejecución del código, pero que el juego necesita para funcionar.
* **Contiene:** La lista de palabras (`PALABRAS`) y los gráficos ASCII del ahorcado (`AHORCADO_DIBUJOS`).

### 2. `logica.py`
Contiene las **funciones asociadas al funcionamiento del juego**. Estas funciones realizan cálculos o transformaciones de datos, pero no interactúan con el usuario (no usan `input` ni `print`).
* **Funciones:**
    * `obtener_palabra_random()`: Selecciona la palabra.
    * `formatear_palabra_secreta()`: Convierte la palabra a adivinar en un su formato con espacios y letras adivinadas. Ejemplo: De "PYTHON" en "_ _ T H _ N".
    * `obtener_estado_juego()`: Decide si ganaste, perdiste o sigues jugando.

### 3. `main.py`
Es el punto de entrada. Une los datos y la lógica e interactúa con el usuario.
* **Contiene:** El ciclo `while` principal, la entrada de datos (`input`) y los mensajes en pantalla (`print`).

---

## 🎓 Conceptos de Programación Aplicados

Al estudiar este código, aprenderás sobre:

## 🚀 Cómo ejecutar el juego

Asegúrate de tener Python instalado en tu computadora.

1.  Descarga o clona este repositorio.
2.  Abre tu terminal (consola) en la carpeta del proyecto.
3.  Ejecuta el siguiente comando:

```bash
python main.py