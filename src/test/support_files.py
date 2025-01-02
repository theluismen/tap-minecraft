def lines_of_file( filename ):
    try:
        lines = 0
        with open(filename, 'r') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        print(f"El archivo {filename} no fue encontrado.")
        return 0
    except Exception:
        print(f"Hubo un error al leer el archivo: {e}")
        return 0
