import json


def dias_faturamento():
    try:
        # Lê os dados do json
        with open('dados.json', 'r') as file:
            dados = json.load(file)

        # Verifica quais dias tem valores maiores que 0 e os adiciona na lista
        dias_com_faturamento = []
        for dia in dados:
            if dia["valor"] > 0:
                dias_com_faturamento.append(dia["valor"])

        if dias_com_faturamento:
            # Guarda o menor valor dos dias com faturamento
            menor = min(dias_com_faturamento)
            # Guarda o maior valor dos dias com faturamento
            maior = max(dias_com_faturamento)
            # Faz a média dos valores
            media = sum(dias_com_faturamento) / len(dias_com_faturamento)
            # Conte 1 a cada valor de dias_com_faturamento, que tiver seu valor maior que a media
            acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media)

            # Imprime as mensagens de qual é o maior, menor, a média e os dias com faturamento acima da média
            print("Menor valor de faturamento:", menor)
            print("Maior valor de faturamento:", maior)
            print("A média é:", media)
            print("Dias com faturamento acima da média:", acima_da_media)

    # Verifica se há algum erro na leitura do arquivo
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Erro ao ler o arquivo:", {e})


dias_faturamento()
# Dá início à função
