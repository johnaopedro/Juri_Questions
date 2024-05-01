N=[]
for i in range(20):
    N.append(int(input()))
for i in range(10): #Metade porque vai trocando até a metade, nesse caso 10.
    N[i], N[19 - i] = N[19 - i], N[i] #Começa no 19-0
for _ in range(20):
    print("N[%d] = %d"%(_,N[_]))

# Original
##print("Original array:")
##for i in range(20):
##    print("N[%d] = %d" % (i, vetor[i]))

# Troca
##for i in range(10):
    # Swap elements at position i and position 19 - i
##    vetor[i], vetor[19 - i] = vetor[19 - i], vetor[i]

# Print da troca
##print("\nModified array:")
##for i in range(20):
##    print("N[%d] = %d" % (i, vetor[i]))

