from contas import *

is_runing = True
menu = True
conta = True
while is_runing:
    while menu:
     print('Qual conta desejada?')
     print(
    '''
     1-Soma
     2-Subtrair
     3-multiplicar
     4-Dividir
     5-Potencia
     6-Converter decimal para outras bases[2 a 36]
    '''
        )
     # entry type handler
     try:
        entrada = int(input("entrada: "))
        if entrada < 1 or entrada > 7:
            print("opcao invalida")
        else:
           menu = False
     except ValueError:
        print("apenas numeros inteiros!")
     #==================
    while conta:
        try:
            if entrada == 1:
               num1 = float(input("primeiro valor: "))
               num2 = float(input("segundo valor: "))
               print("Resultado: ",soma(num1, num2))
               print("=============================")
               conta = False
               menu = True
            if entrada == 2:
               num1 = float(input("primeiro valor: "))
               num2 = float(input("segundo valor: "))
               print("Resultado: ",subtracao(num1, num2))
               print("=============================")
               conta = False
               menu = True
            if entrada == 3:
               num1 = float(input("primeiro valor: "))
               num2 = float(input("segundo valor: "))
               print("Resultado: ",multiplicacao(num1, num2))
               print("=============================")
               conta = False
               menu = True
            if entrada == 4:
               num1 = float(input("dividendo: "))
               num2 = float(input("divisor: "))
               print("Resultado: ",divisao(num1, num2))
               print("=============================")
               conta = False
               menu = True          
            if entrada == 5:
               num1 = float(input("base: "))
               num2 = float(input("expoente: "))
               print("Resultado: ",potencia(num1, num2))
               print("=============================")
               conta = False
               menu = True 
            if entrada == 6:
               num1 = float(input("numero: "))
               num2 = float(input("base destino[2 a 36]: "))
               print("Resultado: ",dec2any(num1, num2))
               print("=============================")
               conta = False
               menu = True  
        except ValueError:
            print("Valor invalido!!!")
            print("------------------")
            
        

