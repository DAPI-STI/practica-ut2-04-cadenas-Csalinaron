"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:

Recibe una cadena como "123.45" o "123,45".

Devuelve una tupla (euros, centimos) como enteros.

Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    # TODO: sustituye coma por punto, separa, valida y convierte a enteros
    cadena_precio = cadena_precio.replace(",", ".")
    
    if "." not in cadena_precio:
        raise ValueError("Debe haber parte decimal separada por punto o coma")
    
    partes = cadena_precio.split(".")
    
    if len(partes) != 2:
        raise ValueError("Debe haber exactamente una parte decimal")
    
    parte_entera = partes[0]
    parte_decimal = partes[1]
    
    if len(parte_decimal) != 2:
        raise ValueError("La parte decimal debe tener exactamente dos dígitos")
    
    if not parte_entera.isdigit() or not parte_decimal.isdigit():
        raise ValueError("Ambas partes deben ser números enteros")
    
    euros = int(parte_entera)
    centimos = int(parte_decimal)
    
    return euros, centimos
    raise NotImplementedError("Implementa euros_cents(price_str)")