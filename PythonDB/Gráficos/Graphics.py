import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,7,5,4]

x1 = [0,2,4,6,8]
x2 = [1,3,5,7,9]
y1 = [9,7,5,3,1]
y2 = [16,12,8,4,0]
#titulo = "Gráfico de barras"
titulo = "Grafico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
#plt.bar(x1,y1, label = "Grupo 1")
#plt.bar(x2,y2, label = "Grupo 2")
#plt.legend()
plt.plot(x, y, color = "violet", linestyle = ":")
plt.scatter(x, y, label = "Meus pontos", color = "Blue", marker = "*", s = 200)
plt.legend()
plt.savefig("figura1.pdf")
plt.show()

#plt.title("Meu primeiro e mais gostoso gráfico")
#plt.xlabel("Eixo X")
#plt.ylabel("Eixo Y")
#plt.plot(x, y)
#plt.show()
#plt.bar(x,y)
#plt.show()
