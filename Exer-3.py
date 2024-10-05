import json

def InfoBasicaFaturamento(arquivo):
    media = 0
    diasValidos = 0
    maior = []
    menor = []

    for dia in arquivo:
        if dia['valor'] != 0.0:
            media += dia['valor']
            diasValidos += 1
            if not maior:
                maior = dia
                menor = dia
            else:
                if dia['valor'] > maior['valor']:
                    maior = dia
                if dia['valor'] < menor['valor']:
                    menor = dia
    return media/diasValidos, menor, maior 

def AcimaMedia(arquivo, media):
    lista = []
    dias = ''
    for dia in arquivo:
        if dia['valor'] > media:
            lista.append(dia)
            dias = dias +' '+ str(dia['dia'])
    return lista, dias
with open('ExemploFaturamento.json', 'r') as file:
    dados = json.load(file)

faturamento = dados['faturamento_diario']

media, menor, maior = InfoBasicaFaturamento(faturamento)
diasMaisProdutivos, dias = AcimaMedia(faturamento, media)
print(f'Media de faturamento no mês: {media},\nO pior de de Faturamento: {menor['dia']} com o faturamento de R${menor['valor']},\nO maior de de Faturamento: {maior['dia']} com o faturamento de R${maior['valor']},') 
print(f'Dias acima da media: {len(diasMaisProdutivos)}\nOs dias foram: {dias}')   
            
    