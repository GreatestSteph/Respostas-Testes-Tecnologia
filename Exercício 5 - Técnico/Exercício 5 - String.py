import time
#importa tempo

def Inverte_String(string):
    return string[::-1]
#inverte a string

string = input("Digite qualquer coisa: ")
#input para enviar qualquer string
resultado = Inverte_String(string)
#a variavel resultado guarda o valor final
print("O que você digitou foi invertido para:", resultado)
#mostra uma mensagem com o valor final

time.sleep(5)
#espera 5 segundos
