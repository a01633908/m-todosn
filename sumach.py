def sum_two_smallest_nums(lista):
  lista = sorted(x for x in lista if x >= 0)
  return sum(lista[:2])
