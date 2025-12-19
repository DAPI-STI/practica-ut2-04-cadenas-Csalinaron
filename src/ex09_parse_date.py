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
    partes = fecha_str.split("/")
    
    if len(partes) != 3:
        raise ValueError("Formato incorrecto")
    
    dia_str = partes[0]
    mes_str = partes[1]
    año_str = partes[2]
    
    try:
        dia = int(dia_str)
        mes = int(mes_str)
        año = int(año_str)
    except ValueError:
        raise ValueError("Formato incorrecto")
    
    if año < 1:
        raise ValueError("Formato incorrecto")
    
    if mes < 1 or mes > 12:
        raise ValueError("Formato incorrecto")
    
    if dia < 1 or dia > 31:
        raise ValueError("Formato incorrecto")
    
    if mes in [4, 6, 9, 11] and dia > 30:
        raise ValueError("Formato incorrecto")
    
    if mes == 2 and dia > 29:
        raise ValueError("Formato incorrecto")
    
    return dia, mes, año
    raise NotImplementedError("Implementa parse_date(date_str)")