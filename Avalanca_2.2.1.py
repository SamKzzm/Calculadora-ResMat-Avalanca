#importar biblioteca para cálculos
import math

#definição dos materiais e suas respectivas propriedades
class Material:
    def __init__ (self, nomeID, nome, lim_esc, rup_trac):
        self.nomeID = nomeID
        self.nome = nome
        self.lim_esc = lim_esc
        self.rup_trac = rup_trac

#transferência dos dados dos materiais para uma lista para facilidade de acesso posterior
mat_esc = []
nome_mats = []
nomeID_mats = []

#lista de funções disponíveis para consulta do usuário
funcs = [
        '1 - Decomposição de Forças',
        '2 - Cálculo de Força Resultante',
        '3 - Tensão de Cisalhamento', 
        '4 - Diâmetro do Rebite (Critério Resistência)',
        '5 - Máxima Tensão de Flexão (Indisponível)'
         ]

#definição das propriedades de cada material disponível, e inclusão das mesmas 
#nas listas criadas anteriormente
mat0 = Material("N/A", "N/A", 0, 0)

mat1 = Material("1 - Aço Inox AISI 304", "Aço Inox AISI 304", 190, 550)
nomeID_mats.append(mat1.nomeID)
nome_mats.append(mat1.nome)
mat_esc.append(mat1.lim_esc)

mat2 = Material("2 - Titânio ASTM F136", "Titânio ASTM F136", 790, 860)
nomeID_mats.append(mat2.nomeID)
nome_mats.append(mat2.nome)
mat_esc.append(mat2.lim_esc)

mat3 = Material("3 - Aço Estrutural ASTM A36", "Aço Estrutural ASTM A36", 250, 450)
nomeID_mats.append(mat3.nomeID)
nome_mats.append(mat3.nome)
mat_esc.append(mat3.lim_esc)


#apresentação do projeto e instruções para a utilização do software
print(f"Projeto Semestral - ResMat - Team Avalanca\n")
print(f"LEIA ATENTAMENTE ÀS INFORMAÇÕES ABAIXO")
print(f"\nAlgumas observações importantes:\n -Para utilização de casas decimais, utilize ponto (.) ao invés de vírgula (,);")
print(f" -Atente-se às unidades de medida para cada variável para garantir o resultado correto;")
print(f" -Para visualizar a lista de materiais disponíveis e seu respectivo ID, digite 'materiais';")
print(f" -Para visualizar a lista de funções disponíveis e seus respectivos IDs, digite 'funções';")
print(f" -Para sair do programa, digite 'sair'.\n")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#seleção da função do software a ser executada (qual cálculo será realizado)
while True:
    select = input(str(f"\nSelecione o parâmetro que deseja calcular ou digite 'sair' para finalizar: "))
    print('')
  
    #'materiais' equivale à lista de materiais disponíveis
    if select in ['materiais', 'Materiais', 'MATERIAIS']:
      while True:
        print('\n\n'.join(str(x) for x in nomeID_mats))
        break

    #'funções' equivale à lista de funções disponíveis
    if select in ['funcoes', 'funções', 'Funções', 'Funcoes', 'FUNÇÕES', 'FUNCOES']:
      while True:
        print('\n\n'.join(str(x) for x in funcs))
        break

    #'sair' finaliza o programa
    if select in ['sair', 'Sair', 'SAIR']:
      break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #1 equivale à função de decomposição de forças
    if select == str(1):
        while True:
          #coleta os valores de força e seu ângulo a partir de input do usuário
          F = float(input("Digite o valor da Força [N]: "))
          angulo = float(input("Digite o valor do ângulo entre o vetor e seu plano horizontal [°]: "))

          #converte os valores de ângulo em graus para radianos
          ang_rad_x = math.radians(angulo)
          ang_rad_y = math.radians(90-angulo)

          #calcula os valores de força em x e y
          Fx = F * math.cos(ang_rad_x)
          Fy = F * math.cos(ang_rad_y)

          #exibe os resultados calculados acima
          print(f"A força no eixo x é de {round(Fx, 2)}N")
          print(f"A força no eixo y é de {round(Fy, 2)}N")
          break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #2 equivale à função de cálculo de força resultante
    if select == str(2):
        while True:
            #definição da função para coleta dos dados e cálculo
            def calcular_resultante():
                vetores_x = []
                vetores_y = []
                while True:
                    #enquanto o valor do input do usuário for diferente de 'q'
                    #continua a coletar força e ângulo das forças
                    vetor = input(f"\nDigite a intensidade da força [N], ou ""'q'"" para finalizar: ")
                    if vetor == 'q':
                        break
                    else:
                        #coleta e armazena os valores dos ângulos das forças
                        vetor_ang = input(f"Digite o ângulo [°] entre o vetor e o eixo X(anti-horário): ")
                        valor_x = float(vetor)*math.cos(math.radians(float(vetor_ang)))
                        vetores_x.append(valor_x)
                        valor_y = float(vetor)*math.sin(math.radians(float(vetor_ang)))
                        vetores_y.append(valor_y)
                
                #realiza a soma dos vetores em x e y
                total_x = sum(vetores_x)
                total_y = sum(vetores_y)

                #utiliza pitágoras para calcular a força resultante, utilizando
                #a soma dos vetores em x e y calculados acima
                forca_result = round(math.sqrt(total_x**2+total_y**2), 2)
                
                #calcula o ângulo formado entre o eixo x e o vetor resultante
                angulo = round(math.degrees(math.atan(total_y/total_x)))

                #exibe o resultado final
                print(f"\nA força resultante é de {forca_result}N com um ângulo de {angulo}° em relação ao eixo X")
            
            #executa a função definida acima
            calcular_resultante()
            break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #3 equivale ao cálculo de Tensão de cisalhamento
    if select == str(3):
        while True:

          #confirmar ao usuário a função escolhida, e em seguida, definição das
          #variáveis a serem utilizadas para a execução da função
          print("Parâmetro selecionado: Tensão de cisalhamento sobre o(s) rebite(s).\n")
          Q = float(input(f"Carga cortante exercida sobre a peça [N]: "))
          n = float(input(f"Número de rebites: "))
          N = float(input(f"Quantidade de pontos onde o rebite sofrerá cisalhamento: "))
          d = float(input(f"Diâmetro do(s) rebite(s) [mm]: "))

          #calculo da tensão de cisalhamento sobre o(s) rebite(s)
          result_cis = round(Q/(n*N*(math.pi/4)*math.pow(d, 2)))

          #exibe o resultado do cálculo em MPa
          print(f"\nTensão de cisalhamento sobre os rebites: {result_cis}MPa")

          #compara o resultado do cálculo com os valores da biblioteca de materiais,
          #retornando o valor mais próximo disponível
          close = min(mat_esc, key=lambda x: abs(x - result_cis))

          #encontra o material que possui o a propriedade 
          #com o valor encontrado na comparação acima
          pos = mat_esc.index(close)

          #exibe o nome do material indicado e seu valor máximo de tensão admissível
          print(f"O material mais indicado para sua aplicação, considerando o critério da resistência, é o {nome_mats[pos]}, com uma tensão limite de {mat_esc[pos]}MPa.")
          break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #4 equivale ao cálculo do diâmetro mínimo do rebite, considerando o fator de
    #segurança e limite de escoamento/ruptura a partir da biblioteca de materiais
    if select == str(4):
        while True:
          
          #confirma ao usuário a função escolhida, e em seguida, define as variáveis
          #necessárias para executar a função
          print("\nParâmetro selecionado: Diâmetro mínimo do(s) rebite(s).")
          
          #input do usuário selecionando o ID do material desejado
          mat_sel = int(input("Insira o ID do material do rebite:"))
          
          #a partir do input, encontra na lista de propriedades o material desejado, e
          #armazena seu valor para uso no cálculo
          selec_prop = float(mat_esc[mat_sel])

          #a partir do input, encontra na lista de nomes o material desejado, e
          #armazena seu valor para retornar ao usuário o material escolhido junto ao resultado
          selec_name = str(nome_mats[mat_sel])
          
          Q = float(input(f"Carga cortante exercida sobre a peça [N]: "))
          n = float(input(f"Número de rebites: "))
          N = float(input(f"Quantidade de pontos onde o rebite sofrerá cisalhamento: "))
          s = float(input(f"Fator de segurança dos rebites: "))

          #definindo a equação em formato de função para uso posterior
          def diam_reb(Q, n, N, s):
              return round((math.sqrt((Q*s*4)/(n*N*math.pi*selec_prop))),2)

          #exibe ao usuário o resultado do cálculo com base no material escolhido
          print(f"\nDiâmetro do(s) rebite(s) em {selec_name}: {diam_reb}mm")
          break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#