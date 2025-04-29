import random

def rolar_dados(n):
    i = 0 
    lista = []
    while i<n: 
        dado = random.randint(1,6)
        lista.append(dado)
        i += 1 
    return lista



def guardar_dado(dados, guardados, i):
    guardados.append(dados[i])
    del dados[i]
    return [dados, guardados]

def remover_dado(dados, guardados, i):
    dados.append(guardados[i])
    del guardados[i]
    return [dados, guardados]



def calcula_pontos_regra_simples(dados):
    dicionario={}
    soma1=0
    soma2=0
    soma3=0
    soma4=0
    soma5=0
    soma6=0
    for i in range(len(dados)):
        if dados[i]==1:
            soma1+=1
        elif dados[i]==2:
            soma2+=2
        elif dados[i]==3:
            soma3+=3
        elif dados[i]==4:
            soma4+=4
        elif dados[i]==5:
            soma5+=5
        elif dados[i]==6:
            soma6+=6
    dicionario[1]=soma1
    dicionario[2]=soma2
    dicionario[3]=soma3
    dicionario[4]=soma4
    dicionario[5]=soma5
    dicionario[6]=soma6
    return dicionario


def calcula_pontos_soma (dados):
    i = 0 
    soma = 0
    while i<len(dados):
        soma = soma + dados[i]
        i = i + 1 
    return soma 


def calcula_pontos_sequencia_baixa(dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados:
        return 15
    elif  2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 15
    elif 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 15
    else:
        return 0


def calcula_pontos_sequencia_alta(dados): 
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados and 5 in dados: 
        return 30 
    elif 2 in dados and 3 in dados and 4 in dados and 5 in dados and 6 in dados: 
        return 30 
    else: 
        return 0
    

def calcula_pontos_full_house(dados):
    contador=0
    ocorrencias=[]
    soma=0
    for i in range(len(dados)):
        if dados[i] in ocorrencias:
            contador = contador
        else:
            contador+=1 
            ocorrencias.append(dados[i])
        soma+=dados[i]
    if contador>2:
        return 0
    if dados[0]==dados[1]==dados[2]==dados[3]==dados[4] or dados[0]==dados[1]==dados[2]==dados[3] or dados[0]==dados[1]==dados[2]==dados[4] or dados[0]==dados[1]==dados[3]==dados[4] or dados[0]==dados[2]==dados[3]==dados[4] or dados[1]==dados[2]==dados[3]==dados[4]:
        return 0
    else:
        return soma


def calcula_pontos_quadra(dados):
    i = 0 
    quantidade = 0
    while i<len(dados):
        o = 0
        iguais = 0
        while o<len(dados):
            if dados[i] == dados[o]:
                iguais = iguais + 1 
            o = o + 1
        if iguais >= 4:
            quantidade = iguais 
        i = i + 1 
    if quantidade >= 4: 
        soma = 0
        for i in range(len(dados)):
            soma = soma + dados[i]
        return soma 
    else: 
        return 0



def calcula_pontos_quina(dados):
    i = 0 
    quantidade = 0
    while i<len(dados):
        o = 0
        iguais = 0
        while o<len(dados):
            if dados[i] == dados[o]:
                iguais = iguais + 1 
            o = o + 1
        if iguais >= 5:
            quantidade = iguais 
        i = i + 1 
    if quantidade >= 5:
        return 50 
    else: 
        return 0


def calcula_pontos_regra_avancada(dados):
    dic = {}
    dic["cinco_iguais"] = calcula_pontos_quina(dados)
    dic["full_house"] = calcula_pontos_full_house(dados)
    dic["quadra"] = calcula_pontos_quadra(dados)
    dic["sem_combinacao"] = calcula_pontos_soma(dados)
    dic["sequencia_alta"] = calcula_pontos_sequencia_alta(dados)
    dic["sequencia_baixa"] = calcula_pontos_sequencia_baixa(dados)
    return dic 