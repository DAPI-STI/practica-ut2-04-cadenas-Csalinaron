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
    def emphasize_vowel(frase: str, vocal: str) -> str:
    if len(vocal) != 1:
        raise ValueError("Debe ser un solo carácter")
    
    vocal_min = vocal.lower()
    if vocal_min not in "aeiou":
        raise ValueError("La vocal debe ser a, e, i, o, u")
    
    resultado = ""
    for caracter in frase:
        if caracter.lower() == vocal_min:
            resultado += caracter.upper()
        else:
            resultado += caracter
    
    return resultado
    raise NotImplementedError("Implementa emphasize_vowel(phrase, vowel)")