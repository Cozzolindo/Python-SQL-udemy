#Boxplot - diagrama de caixa

import matplotlib.pyplot as plt
import random

vetor = []
for i in range(1000):
    num = random.uniform(0,100)
    vetor.append(num)



plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()
