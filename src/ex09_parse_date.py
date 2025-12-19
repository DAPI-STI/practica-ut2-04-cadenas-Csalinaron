"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    # TODO: usa split("/"), convierte a int y valida rangos sencillos
    partes = date_str.split("/")

    if len(partes) != 3:
        raise ValueError("Formato incorrecto")

    dia_str, mes_str, año_str = partes

    if not (dia_str.isdigit() and mes_str.isdigit() and año_str.isdigit()):
        raise ValueError("Solo se permiten números")

    dia = int(dia_str)
    mes = int(mes_str)
    año = int(año_str)

    if not (1 <= dia <= 31):
        raise ValueError("Día fuera de rango")
    if not (1 <= mes <= 12):
        raise ValueError("Mes fuera de rango")
    if año <= 0:
        raise ValueError("Año fuera de rango")

    return dia, mes, año
    raise NotImplementedError("Implementa parse_date(date_str)")