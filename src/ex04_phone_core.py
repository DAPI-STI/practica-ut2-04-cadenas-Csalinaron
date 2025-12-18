"""
Ejercicio 4: a partir de un teléfono con el formato "+34-<numero>-<extension>"
obtener solamente la parte central (el número), sin prefijo ni extensión.

Ejemplo: "+34-913724710-56" -> "913724710"
"""

def phone_core(s: str) -> str:
    """
    Recibe el teléfono como cadena y devuelve solo la parte central.
    Requisitos mínimos (si no se cumplen, lanza ValueError):
    - Debe haber exactamente 3 partes separadas por "-".
    - La primera parte debe comenzar por "+" (prefijo).
    - La parte central debe ser numérica.
    """
    # TODO: usa .strip(), .split("-") y validaciones con .isdigit() y startswith("+")
    s = s.strip()
    partes = s.split("-")

    if len(partes) != 3:
        raise ValueError("Formato incorrecto")

    prefijo = partes[0]
    numero = partes[1]

    if not prefijo.startswith("+"):
        raise ValueError("Prefijo incorrecto")

    if not numero.isdigit():
        raise ValueError("Número central no numérico")

    return numero
   
    raise NotImplementedError("Implementa phone_core(s)")