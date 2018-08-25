def cumulative_sum(lst):
  t = 0
  lista2 = []
  for number in lst:
    t += number
    lista2.append(t) 
  return lista2
