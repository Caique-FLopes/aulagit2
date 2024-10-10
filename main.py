notas = []
mediaFinal = 0

while len(notas) < 3:
    notas.append(float(input("Adicione uma nota: ")))

for nota in notas:
    mediaFinal += nota

mediaFinal = mediaFinal / len(notas)

print("A média final é: ", mediaFinal)