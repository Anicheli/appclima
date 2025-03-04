import requests
from datetime import datetime
import json

import pytz
import pycountry_convert as pc


chave = '1f7a59765d700e6f584e2f56d7f4e0c8'
cidade = 'Lisboa'
api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade, chave)


#chamada da API usando request
r = requests.get(api_link)

#convertendo os dados da variavel r em dicionario
dados = r.json()
print(dados)
print('*'*45)

# obtendo zona, pais e horas
pais_codigo = dados['sys']['country']

#zona
zona_fuso = pytz.country_timezones[pais_codigo]

#pais
pais = pytz.country_names[pais_codigo]

#data
zona = pytz.timezone(zona_fuso[0])
zona_horas = datetime.now(zona)
zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")

#tempo
tempo = dados['main']['temp']
pressao = dados['main']['pressure']
humidade = dados['main']['humidity']
velocidade = dados['wind']['speed']
descricao = dados['weather'][0]['description']



#mudando informacoes

def pais_para_continente(i):
    pais_alpha = pc.country_name_to_country_alpha2(i)
    pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
    pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)
    
    return pais_continente_nome

continente = pais_para_continente(pais)
    















