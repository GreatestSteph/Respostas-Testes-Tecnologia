import time
#importa tempo

#Faturamento mensal por estado
distribuidora_sp = 67836.43
distribuidora_rj = 36678.66
distribuidora_mg = 29229.88
distribuidora_es = 27165.48
distribuidora_outros = 19849.53

#Valor total mensal
total = distribuidora_sp + distribuidora_rj + distribuidora_mg + distribuidora_es + distribuidora_outros

#Percentual de faturamento de cada Estado
percentual_sp = (distribuidora_sp / total) * 100
percentual_rj = (distribuidora_rj / total) * 100
percentual_mg = (distribuidora_mg / total) * 100
percentual_es = (distribuidora_es / total) * 100
percentual_outros = (distribuidora_outros / total) * 100

#Mensagem com os valores percentuais
print("Percentual de faturamento que cada Estado teve na distribuidora:")
time.sleep(1)
#Pequena pausa
print("SP:", round(percentual_sp, 2), "%")
time.sleep(1)
#Pequena pausa
print("RJ:", round(percentual_rj, 2), "%")
time.sleep(1)
#Pequena pausa
print("MG:", round(percentual_mg, 2), "%")
time.sleep(1)
#Pequena pausa
print("ES:", round(percentual_es, 2), "%")
time.sleep(1)
#Pequena pausa
print("Outros:", round(percentual_outros, 2), "%")

time.sleep(10)
#Pausa 10 segundos antes do programa fechar