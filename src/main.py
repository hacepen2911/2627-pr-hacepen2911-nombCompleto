def formatear_nombre(nombre: str, apellido1: str, apellido2: str) -> str:
    """
    Formateo de las cadenas y union de las mismas

    :param nombre: El nombre del usuario
    :param apellido1: El primer apellido del usuario
    :param apellido2: El segundo apellido del usuario

    :return Una cadena de texto con el nombre completo en en formato requerido: 
    """
    nombre_formateado = f"{nombre.title().strip()} {apellido1.title().strip()} {apellido2.title().strip()}"
    return nombre_formateado

def main():
    """Función principal"""
    nombre:str = input("Introduce tu nombre: ")
    apellido1:str = input("Introduce tu primer apellido: ")
    apellido2:str = input("Introduce tu segundo apellido: ")

    nombre_formateado:str = formatear_nombre(nombre, apellido1, apellido2)

    print(nombre_formateado)
    
if __name__ == "__main__":
    main()