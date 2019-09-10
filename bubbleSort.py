#Bubble sort

def bubbleSort(vetor):
	tamanhoVetor = len(vetor) - 1
	for i in range(tamanhoVetor, 0, -1):
		trocouLugar = False
		for j in range(i):
			if vetor[j] > vetor[j + 1]:
				vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
				trocouLugar = True
		if not trocouLugar:
			break

vetor = [9,3,6,0,1,2,5,8,7,4]

bubbleSort(vetor)

print(vetor)
