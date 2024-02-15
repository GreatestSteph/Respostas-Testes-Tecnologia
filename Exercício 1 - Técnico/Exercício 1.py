import time

Indice = 13
Soma = 0
K = 0

while K < Indice:
# Enquanto K for menor que Indice
    K = K + 1
# O valor de K receberá o seu próprio valor, somado a +1
    Soma = Soma + K
# O valor de Soma receberá o seu próprio valor, somado ao valor atual de K

print("Ao final do processamento, o valor da variável Soma será igual a: '", Soma, "'")
# Imprime uma mensagem que mostra o que acontece no final do processamento que será 91

time.sleep(5)