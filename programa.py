import funcoes

cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
jogada = 0 

while jogada<12:
    lista_dados = funcoes.rolar_dados(5)
    lista_guardados = []
    jogando = True
    rolar_novamente = 0
    funcoes.imprime_cartela(cartela_de_pontos)
    while jogando:
        print("Dados rolados: {}".format(lista_dados))
        print("Dados guardados: {}".format(lista_guardados))
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acao = int(input(">"))
        if acao == 0:
            print("Digite a combinação desejada:")
            combinacao = input(">")
            if combinacao == "1" or combinacao == "2" or combinacao == "3" or combinacao == "4" or combinacao == "5" or combinacao == "6": 
                combinacao = int(combinacao)
                if cartela_de_pontos["regra_simples"][combinacao] != -1: 
                    print("Essa combinação já foi utilizada.")
                    combinacao = input(">")
                else:
                     cartela_de_pontos = funcoes.faz_jogada(lista_dados,combinacao,cartela_de_pontos)
            elif combinacao in cartela_de_pontos["regra_avancada"]: 
                if cartela_de_pontos["regra_avancada"][combinacao] != -1: 
                    print("Essa combinação já foi utilizada.")
                else: 
                    cartela_de_pontos = funcoes.faz_jogada(lista_dados,combinacao,cartela_de_pontos)
                    combinacao = input(">")
            else: 
                print("Essa combinação não existe.")
                combinacao = input(">")

        elif acao == 1: 
            print("Digite o índice do dado a ser guardado (0 a 4):")
            guardado = int(input(">"))
            lista = funcoes.guardar_dado(lista_dados,lista_guardados,guardado)
            lista_dados = lista[0]
            lista_guardados=lista[1]
        
        elif acao == 2: 
            print("Digite o índice do dado a ser guardado (0 a 4):")
            removido = int(input(">"))
            lista = funcoes.remover_dado(lista_dados,lista_guardados,removido)
            lista_dados = lista[0]
            lista_guardados = lista[1]
        
        elif acao ==3: 
            if rolar_novamente>2: 
                print("Você já usou todas as rerrolagens.")
            else: 
                lista_dados = funcoes.rolar_dados(len(lista_dados))
       
        elif acao == 4:
            funcoes.imprime_cartela(cartela_de_pontos)
       
        else:
            print("Opção inválida. Tente novamente.")
        
        if cartela_de_pontos["regra_simples"][1] != 0 and cartela_de_pontos["regra_simples"][2] != 0 and cartela_de_pontos["regra_simples"][3] != 0 and cartela_de_pontos["regra_simples"][4] != 0 and cartela_de_pontos["regra_simples"][5] != 0 and cartela_de_pontos["regra_simples"][6] != 0 and cartela_de_pontos["regra_avancada"]["sem_combinacao"] != 0 and cartela_de_pontos["regra_avancada"]["quadra"] != 0 and cartela_de_pontos["regra_avancada"]["full_house"] != 0 and cartela_de_pontos["regra_avancada"]["sequencia_baixa"] != 0 and cartela_de_pontos["regra_avancada"]["sequencia_alta"] != 0 and cartela_de_pontos["regra_avancada"]["cinco_iguais"] != 0:
            pontuacao_final = cartela_de_pontos["regra_simples"][1] + cartela_de_pontos["regra_simples"][2] + cartela_de_pontos["regra_simples"][3] + cartela_de_pontos["regra_simples"][4] + cartela_de_pontos["regra_simples"][5] + cartela_de_pontos["regra_simples"][6] + cartela_de_pontos["regra_avancada"]["sem_combinacao"] + cartela_de_pontos["regra_avancada"]["quadra"] + cartela_de_pontos["regra_avancada"]["full_house"] + cartela_de_pontos["regra_avancada"]["sequencia_baixa"] + cartela_de_pontos["regra_avancada"]["sequencia_alta"] + cartela_de_pontos["regra_avancada"]["cinco_iguais"]
            simples = cartela_de_pontos["regra_simples"][1] + cartela_de_pontos["regra_simples"][2] + cartela_de_pontos["regra_simples"][3] + cartela_de_pontos["regra_simples"][4] + cartela_de_pontos["regra_simples"][5] + cartela_de_pontos["regra_simples"][6]
            if simples>63: 
                 pontuacao_final = pontuacao_final + 35
            funcoes.imprime_cartela(cartela_de_pontos)
            print("Pontuação final: {}".format(pontuacao_final))
            jogando = False

    jogada = jogada + 1 

