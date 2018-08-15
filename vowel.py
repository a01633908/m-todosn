def count_vowels(txt):
   vowels = ['a','e','i','o','u']
   v = 0
   for p in txt:
      if p in vowels:
         v += 1
   return v
