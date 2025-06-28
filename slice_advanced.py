def slice_advanced():  # Aseguramos todo en minúsculas
    texto = input("Ingrese un texto: ")
    resultado = texto[4::2]  # Desde el 5º carácter (índice 4) en adelante, saltando de a 2
    print(resultado)
