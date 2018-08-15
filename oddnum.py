def noOdds(lst):
	b = []
	for n in lst:
		if n % 2 == 0:	
			b.append(n)
	return b
