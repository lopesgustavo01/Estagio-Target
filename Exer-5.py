string = 'Was it a car or a cat I saw'

def inverter(string):
    string_invertida = ''
    for i in string:
        string_invertida = i + string_invertida
    return string_invertida
print(inverter(string))