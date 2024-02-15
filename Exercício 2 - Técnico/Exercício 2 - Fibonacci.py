import time
#Importa tempo


#Funçao que verifica se o numero pertence a Fibonacci
def VerificaFibonacci(NumeroEscolhido):
    pri_fibonnaci = 0
    #Primeiro numero de Fibonacci
    seg_fibonnaci = 1
    #Segundo numero de Fibonacci
    while seg_fibonnaci < NumeroEscolhido:
    #Enquanto o Numero escolhido for menor que 1
        pri_fibonnaci, seg_fibonnaci = seg_fibonnaci, pri_fibonnaci + seg_fibonnaci
    return seg_fibonnaci == NumeroEscolhido



print("Quer verificar se um número pertence a Fibonnaci?")
NumeroEscolhido = int(input("Digite aqui um número:"))

if VerificaFibonacci(NumeroEscolhido):
    print(NumeroEscolhido, "pertence à sequência de Fibonacci.")
    #Retorna a mensagem que o número pertence a sequência de Fibonacci
else:
    print(NumeroEscolhido, "não pertence à sequência de Fibonacci.")
    #Retorna a mensagem que o número não pertence a sequência de Fibonacci

time.sleep(8)
#faz o programa esperar um pouco antes de fechar.