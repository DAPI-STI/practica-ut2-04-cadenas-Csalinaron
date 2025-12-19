"""
Ejercicio 6: pedir una frase y una vocal y mostrar la frase con la vocal en mayúsculas.

La función debe:

Recibir una frase y una vocal (a, e, i, o, u) en cualquier caso.

Devolver la frase sustituyendo esa vocal (mayúscula/minúscula) por su versión en mayúscula.

Si la vocal no es válida, lanzar ValueError.
"""

def emphasize_vowel(phrase: str, vowel: str) -> str:
    """
    Convierte a mayúscula todas las apariciones de vowel en la frase.
    Sugerencia:
    - Comprueba que vowel es un solo carácter y está en "aeiou" (en minúscula).
    - Recorre la frase carácter a carácter y construye una nueva cadena.
    """
    # TODO: validar y transformar
    vocal = vocal.lower()
    if len(vocal) != 1 or vocal not in "aeiou":
        raise ValueError("La vocal no es válida")

    resultado = ""
    for caracter in frase:
        if caracter.lower() == vocal:
            resultado += caracter.upper()
        else:
            resultado += caracter
    return resultado
    raise NotImplementedError("Implementa emphasize_vowel(phrase, vowel)")