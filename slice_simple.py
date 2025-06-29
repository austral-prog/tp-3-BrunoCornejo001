def slice_simple():
  texto = input()
  primeras_3 = texto[:3]
  tres_del_medio = texto[2:5]  # asumiendo que siempre será el mismo texto "awesome"
  primera_a_cuarta = texto[:4]
  antepenultima_a_ultima = texto[-3:]
  print(primeras_3)
  print(tres_del_medio)
  print(primera_a_cuarta + antepenultima_a_ultima)
