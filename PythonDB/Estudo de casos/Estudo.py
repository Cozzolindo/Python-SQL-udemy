#Estudo do crescimento da população brasileira
#Data Sus

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

print("Valores colhido para X:\n")
print(x)
print("\nValores colhido para Y:\n")
print(y)

plt.bar(x, y, color = 'pink')
plt.plot(x, y, color = "g")
plt.title("Crescimento da população brasileira de 1980 - 2016")
plt.xlabel("Ano")
plt.ylabel("População x 100.000.000")
plt.savefig("popbr.png", dpi = 300)
plt.show()

