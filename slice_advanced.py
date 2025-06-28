def slice_advanced():
    texto = "Awesome"  # Aseguramos todo en minúsculas

    primeras_tres = texto[:3]
    medio = texto[2:5]  # Posiciones 2, 3 y 4 (centrales)
    primera_a_cuarta = texto[:4]
    antepenultima_a_ultima = texto[-3:]

    print(primeras_tres.lower())
    print(medio.lower())
    print(primera_a_cuarta.lower() + antepenultima_a_ultima.lower())
