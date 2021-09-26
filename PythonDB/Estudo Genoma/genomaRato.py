entrada = open("rat.txt").read()
saida = open("Rato.html", "w")

cont = {}

for i in ["A", "T", "C", "G"]:
    for j in ["A", "T", "C", "G"]:
        cont[i+j] = 0

entrada = entrada.replace("\n","")

for k in range(len(entrada)-1):
    cont[entrada[k]+entrada[k+1]] += 1


print(cont)


# html

i = 1

for k in cont:
    transp = cont[k]/max(cont.values())
    saida.write("<div style='width:100px; border:5px solid #111; color:black; height:100px; float:left; background-color:rgba(57,255,20,"+str(transp)+"')>"+k+"</div>")
    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")
    i+=1

saida.close()
