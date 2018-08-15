" " "Create a function that takes a list of numbers and returns the mean value." " " 
def mean(lst):
  result = 0
  for a in lst:
    result += a
  result = result/len(lst)
  return round(result, 2)
