datoa = int(input("ingresa un numero: "))
datob = int(input("ingresa otro numero: "))

if datoa > datob:
    print("el mayor es ", datoa)
else:
    print("el mayor es ", datob)

#CIClo while
x = 50
while x > 0:
    print(x)
    x = x-1
#Ciclo FOR

for x in range(1, 50):
    print(x)

palabra = "Jose"

for letra in palabra:
    print(letra)

for i in range(-100, 0, 2):
    print(i)


def saludo():
    print("Hola mundo")


saludo()

