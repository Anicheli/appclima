import tkinter
from tkinter import *
from tkinter import ttk

#importanto pillow
from PIL import Image, ImageTk


#importacoes
import requests
from datetime import datetime
import json

import pytz
import pycountry_convert as pc


# cores #
co0 = "#444466"  #preto
co1 = "#feffff"  #branco  
co2 = "#6f9fbd"  #azul  

fundo_dia="#6cc4cc"
fundo_noite="#484f60"
fundo_tarde="#bfb86d"

fundo = fundo_dia


janela = Tk()
janela.title('')
janela.geometry('350x320')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

#criando frames
frame_top = Frame(janela, width=355, height=50, bg=co1, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

global imagem

def informacao():
    
    chave = '1f7a59765d700e6f584e2f56d7f4e0c8'
    cidade = e_local.get()
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
    
    #passando info nas labels
    
    l_cidade['text'] = cidade + " - " + pais + " / " + continente
    l_data['text'] = zona_horas
    l_humidade['text'] = humidade
    l_h_simbol['text'] = '%'
    l_h_nome['text'] = 'Humidity'
    l_pressao['text'] = "Pressure : "+str(pressao)
    l_velocidade['text'] = "Wind speed : "+str(velocidade)
    l_descricao['text'] = descricao
    
    
    #trocar fundo
    
    zona_periodo = datetime.now(zona)
    zona_periodo = zona_periodo.strftime("%H")
    
    global imagem
    
    zona_periodo = int(zona_periodo)
    
    if zona_periodo <= 5:
        imagem = Image.open('imagens proj/lua.png')
        fundo = fundo_noite
    elif zona_periodo <= 11:
        imagem = Image.open('imagens proj/sol_dia.png')
        fundo = fundo_dia
    elif zona_periodo <= 17:
        imagem = Image.open('imagens proj/sol_tarde.png')
        fundo = fundo_tarde
    elif zona_periodo <= 23:
        imagem = Image.open('imagens proj/lua.png')
        fundo = fundo_noite
    else:
        pass
    
        
        
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_icon = Label(frame_corpo,image=imagem, bg=fundo)
    l_icon.place(x=190, y=50)
    
    #passando info nas labels
    janela.configure(bg=fundo)
    frame_top.configure(bg=fundo)
    frame_corpo.configure(bg=fundo)
    
    
    l_cidade['bg'] = fundo
    l_data['bg'] = fundo
    l_humidade['bg'] = fundo
    l_h_simbol['bg'] = fundo
    l_h_nome['bg'] = fundo
    l_pressao['bg'] = fundo
    l_velocidade['bg'] = fundo
    l_descricao['bg'] = fundo
            
        

    #configurando frame top

e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)
b_ver = Button(frame_top, command=informacao, text='See weather', bg=co1, fg=co2, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE)
b_ver.place(x=253, y=10)

    #configurando frame corpo
l_cidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 14"))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_data.place(x=10, y=54)

l_humidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 45"))
l_humidade.place(x=10, y=100)

l_h_simbol = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 10 bold"))
l_h_simbol.place(x=85, y=110)

l_h_nome = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 8"))
l_h_nome.place(x=85, y=140)

l_pressao = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_velocidade.place(x=10, y=212)

l_descricao = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))    
l_descricao.place(x=200, y=190)



janela.mainloop()