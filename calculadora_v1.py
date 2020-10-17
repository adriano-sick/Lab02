# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

#Desenvolvido por Adriano Siqueira em 17/10/20

print("\n******************* Python Calculator *******************")
print("******* :::::::: ::::::::::: ::::::::  :::    ::: *******")
print("*******:+:    :+:    :+:    :+:    :+: :+:   :+:  *******")  
print("*******+:+           +:+    +:+        +:+  +:+   *******")
print("*******+#++:++#++    +#+    +#+        +#++:++    *******")
print("*******       +#+    +#+    +#+        +#+  +#+   *******")
print("*******#+#    #+#    #+#    #+#    #+# #+#   #+#  *******")
print("******* ######## ########### ########  ###    ### *******")
print("*********************************************************")

#metodos:

def comeco():

    #esse metodo apresenta as opções, recebe o input do user, e chama o metodo de operações
    
    print("Qual operação deseja realizar?\n")
    print("1 - Soma\n")
    print("2 - Subtração\n")
    print("3 - Multiplicação\n")
    print("4 - Divisão\n")
    operacao = input("Escolha as opções de 1 a 4 e pressione enter: ")
    operacoes(operacao)

def operacoes(operacao):

    #Aqui estão todas as operações possiveis
    #os 'try' realizam a operação, os except tratam caso a entrada não seja um numero

    #soma
    if(operacao == "1"):
        print("\nSoma")
        try:
            num1 = float(input("Insira o primeiro valor: "))
            num2 = float(input("Insira o segundo valor: "))
            print(str(num1) + " + " + str(num2) + " = " + str(float(num1 + num2)))        
            fim()
        except ValueError:
            print("Apenas numeros!!!\n")
            operacoes(operacao)

    #subtração    
    elif(operacao == "2"):
        try:
            print("\nSubtração")
            num1 = float(input("Insira o primeiro valor: "))
            num2 = float(input("Insira o segundo valor: "))
            print(str(num1) + " - " + str(num2) + " = " + str(float(num1 - num2)))
            fim()
        except ValueError:
            print("Apenas numeros!!!\n")
            operacoes(operacao)

    #multiplicação    
    elif(operacao == "3"):
        try:
            print("\nMultiplicação")
            num1 = float(input("Insira o primeiro valor: "))
            num2 = float(input("Insira o segundo valor: "))
            print(str(num1) + " * " + str(num2) + " = " + str(float(num1 * num2)))
            fim()
        except ValueError:
            print("Apenas numeros!!!\n")
            operacoes(operacao)

    #divisão
    elif(operacao == "4"):
        try:
            print("\nDivisão")
            num1 = float(input("Insira o primeiro valor: "))
            num2 = float(input("Insira o segundo valor: "))
            print(str(num1) + " / " + str(num2) + " = " + str(float(num1 / num2)))
            fim()
        except ValueError:
            print("Apenas numeros!!!\n")
            operacoes(operacao)

    #caso o user entre uma opção de operação errada, aparece  mensagem, e chama o metodo "começo" novamente    
    else:
        print("\nOpcao invalida, escolha a operação digitando:\n 1 para soma\n 2 para subtração\n 3 para multiplicação\n 4 para divisão\n")
        comeco()


def fim():

    #apresenta opção de reiniciar ou finalizar o programa

    print("\nS - Sim")
    print("N - Não")
    novamente = input("Você deseja realizar uma nova operação??? \n")    

    #verifica entrada do usuario e chama metodo correspondente, o else repete o metodo fim, caso o input nao exista
    if(novamente == "s"):
        comeco()
    elif(novamente == "n"):
        exit()
    else:
        fim()


#loop do programa:
comeco()
