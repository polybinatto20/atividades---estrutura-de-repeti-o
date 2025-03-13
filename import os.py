import os

#Limpando a tela 
os.system('cls')

print("TABUADA")
print("========")


numerador=int(input("Digite o  valor que desejar: "))

contador =  0

while(contador <=10):
    mutiplicacao = numerador * contador
    print(numerador, "x",contador,"=", mutiplicacao )
    contador = contador + 1



