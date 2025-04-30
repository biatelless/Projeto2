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
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
jogada = 0 

funcoes.imprime_cartela(cartela_de_pontos)
while jogada<12:
    dados = funcoes.rolar_dados(5)
    guardados = []
    jogando = True
    rolar_novamente = 0
    while jogando:
        print("Dados rolados: {}".format(dados))
        print("Dados guardados: {}".format(guardados))
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acao = (input(">"))

        while acao != "0" and acao != "1" and acao != "2" and acao != "3" and acao != "4": 
            print("Opção inválida.Tente novamente.")
            acao = (input(">"))

        if acao == "0":
            print("Digite a combinação desejada:")
            combinacao = input(">")
            if combinacao == "1" or combinacao == "2" or combinacao == "3" or combinacao == "4" or combinacao == "5"or combinacao == "6": 
                if cartela_de_pontos["regra_simples"][int(combinacao)] != -1: 
                    print("Essa combinação já foi utilizada.")
                    combinacao = input(">")
                else:
                    cartela_de_pontos = funcoes.faz_jogada(guardados,combinacao,cartela_de_pontos)
                    jogando = False
            elif combinacao == "sem_combinacao" or combinacao == "quadra" or combinacao == "full_house" or combinacao == "sequencia_baixa" or combinacao == "sequencia_alta" or combinacao == "cinco_iguais":
                if cartela_de_pontos["regra_avancada"][combinacao] != -1: 
                    print("Essa combinação já foi utilizada.")
                    combinacao = input(">")
                else: 
                    cartela_de_pontos = funcoes.faz_jogada(guardados,combinacao,cartela_de_pontos)
                    jogando = False
            else:
                print("Combinação inválida.Tente novamente.")
                combinacao = (input(">"))

        elif acao == "1": 
            print("Digite o índice do dado a ser guardado (0 a 4):")
            g = int(input(">"))
            lista = funcoes.guardar_dado(dados,guardados,g)
            dados = lista[0]
            guardados = lista[1]
            
        elif acao == "2": 
            print("Digite o índice do dado a ser removido (0 a 4):")
            r = int(input(">"))
            lista = funcoes.remover_dado(dados,guardados,r)
            dados = lista[0]
            guardados = lista[1]
            
        elif acao == "3": 
            if rolar_novamente>=2: 
                print("Você já usou todas as rerrolagens.")
            else: 
                dados = funcoes.rolar_dados(len(dados))
            rolar_novamente += 1 
        
        elif acao == "4":
            funcoes.imprime_cartela(cartela_de_pontos)
            
        if cartela_de_pontos["regra_simples"][1] != -1 and cartela_de_pontos["regra_simples"][2] != -1 and cartela_de_pontos["regra_simples"][3] != -1 and cartela_de_pontos["regra_simples"][4] != -1 and cartela_de_pontos["regra_simples"][5] != -1 and cartela_de_pontos["regra_simples"][6] != -1 and cartela_de_pontos["regra_avancada"]["sem_combinacao"] != -1 and cartela_de_pontos["regra_avancada"]["quadra"] != -1 and cartela_de_pontos["regra_avancada"]["full_house"] != -1 and cartela_de_pontos["regra_avancada"]["sequencia_baixa"] != -1 and cartela_de_pontos["regra_avancada"]["sequencia_alta"] != -1 and cartela_de_pontos["regra_avancada"]["cinco_iguais"] != -1:
            jogando = False
            jogada = 12  

    jogada = jogada + 1 

pontuacao_final = cartela_de_pontos["regra_simples"][1] + cartela_de_pontos["regra_simples"][2] + cartela_de_pontos["regra_simples"][3] + cartela_de_pontos["regra_simples"][4] + cartela_de_pontos["regra_simples"][5] + cartela_de_pontos["regra_simples"][6] + cartela_de_pontos["regra_avancada"]["sem_combinacao"] + cartela_de_pontos["regra_avancada"]["quadra"] + cartela_de_pontos["regra_avancada"]["full_house"] + cartela_de_pontos["regra_avancada"]["sequencia_baixa"] + cartela_de_pontos["regra_avancada"]["sequencia_alta"] + cartela_de_pontos["regra_avancada"]["cinco_iguais"]
simples = cartela_de_pontos["regra_simples"][1] + cartela_de_pontos["regra_simples"][2] + cartela_de_pontos["regra_simples"][3] + cartela_de_pontos["regra_simples"][4] + cartela_de_pontos["regra_simples"][5] + cartela_de_pontos["regra_simples"][6]
if simples>63: 
    pontuacao_final = pontuacao_final + 35
funcoes.imprime_cartela(cartela_de_pontos)
print("Pontuação total: {}".format(pontuacao_final))