import random
import cursos

cicle = "not"
x = random.randint(100000, 150000)
lista = []

if cicle == "sim":
    for i in range(x):
        y = random.randint(0,x-1)
        z = random.randint(0,x-1)
        if z!=y:
            lista.append([y,z])


else:
    near = [[]]*x
    for i in range(x):
        y = random.randint(0,x-1)
        z = random.randint(0,x-1)
        if z!=y and [y,z] not in lista and [z,y] not in lista and z not in near[y] and y not in near[z]:
            lista.append([y,z])
            near[y].append(z)
            near[z].append(y)


final = cursos.canFinish(x, lista)

if final == True:
    f = open("out6.txt", "w")
    f.write("True")
    f.close()
else:
    f = open("out6.txt", "w")
    f.write("False")
    f.close()

with open('inp6.txt', 'w') as f:
    f.write(str(x)+"\n")
    for i in lista[0:-1]:
        a = str(i[0])
        b = str(i[1])
        f.write(a+","+b+"\n")

    last = lista[-1]
    a = str(last[0])
    b = str(last[1])
    f.write(a+","+b)

