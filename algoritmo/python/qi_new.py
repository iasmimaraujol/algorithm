i1 = [1, 10, 2, 2, 10, 3, 3, 3, 4, 5, 5]
i2 = ["G", "e", "e", "k", "s"]

def valor(ar):
	aux = len(ar)
	for i in range(0,aux):
		try:
			a = 0
			while a < i:				
				if ar[i] == ar[a]:
					print(ar[a], ar[i])
					ar.remove(ar[i])
				a = a + 1
			a = 0
		except IndexError:
			continue
	return ar
			
i1 = valor(i1)
i2 = valor(i2)			
print(i1)
print(i2)
