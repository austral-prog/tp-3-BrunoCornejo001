def check_vowels():
    nombre = input("Ingrese un nombre: ").lower()  # Convertimos a minúsculas para comparar sin errores

    vocales = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocales:
        print(f"Contiene {vocal}: {vocal in nombre}")
