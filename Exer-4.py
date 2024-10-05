faturamento_estados = [
    {"estado": "SP", "valor": 67836.43},
    {"estado": "RJ", "valor": 36678.66},
    {"estado": "MG", "valor": 29229.88},
    {"estado": "ES", "valor": 27165.48},
    {"estado": "Outros", "valor": 19849.53}
]
faturamento_estados_porcentagem = []
total = 0

for estado in faturamento_estados:
    total += estado['valor'] 

for estado in faturamento_estados:
    porcentagem = round(estado["valor"] * 100 / total, 2)
    print(f'estado {estado['estado']} = {porcentagem} %')
    faturamento_estados_porcentagem.append({'estado': estado["estado"], 'valor': porcentagem})
