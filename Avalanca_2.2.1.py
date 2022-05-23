import math
import time

################################################################## FUNÇÕES ##############################################################################

class funcs: #Classe definindo as funções disponíveis
  def __init__(self):
    pass

################################################################## FUNÇÃO 1 #############################################################################

  @classmethod #Decomposição de forças
  def decomposicao(cls):
    print(f"Função selecionada: Decomposição de forças.\n")
    F = float(input("Digite o valor da Força [N]: "))
    angulo = float(input("Digite o valor do ângulo entre o vetor e seu plano horizontal [°]: "))
    ang_rad_x = math.radians(angulo)
    ang_rad_y = math.radians(90-angulo)
    Fx = F * math.cos(ang_rad_x)
    Fy = F * math.cos(ang_rad_y)
    return print(f"A força no eixo x é de {round(Fx, 2)}N" , f"\nA força no eixo y é de {round(Fy, 2)}N\n")

################################################################## FUNÇÃO 2 #############################################################################

  @classmethod #Cálculo de força resultante
  def calcular_resultante(cls):
    print(f"Função selecionada: Cálculo de força resultante.\n")
    vetores_x = []
    vetores_y = []
    while True:              
      vetor = input(f"\nDigite a intensidade da força [N], ou ""'q'"" para finalizar: ")
      if vetor == 'q':
        break
      else:                
        vetor_ang = input(f"Digite o ângulo [°] entre o vetor e o eixo X(anti-horário): ")
        valor_x = float(vetor)*math.cos(math.radians(float(vetor_ang)))
        vetores_x.append(valor_x)
        valor_y = float(vetor)*math.sin(math.radians(float(vetor_ang)))
        vetores_y.append(valor_y)
                
    total_x = sum(vetores_x)
    total_y = sum(vetores_y)
    forca_result = round(math.sqrt(total_x**2+total_y**2), 2)
    angulo = round(math.degrees(math.atan(total_y/total_x)))
    return print(f"\nA força resultante é de {forca_result}N com um ângulo de {angulo}° em relação ao eixo X")

################################################################## FUNÇÃO 3 #############################################################################

  @classmethod #Cálculo de tensão de cisalhamento sobre o rebite
  def tensaoCis(cls):
    print(f"Função selecionada: Tensão de cisalhamento sobre o(s) rebite(s).\n")
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
    close = min(mat_esc, key = lambda x: abs(x - result_cis))

    #encontra o material que possui o a propriedade 
    #com o valor encontrado na comparação acima
    pos = mat_esc.index(close)

    #exibe o nome do material indicado e seu valor máximo de tensão admissível
    return print(f"""O material mais indicado para sua aplicação, considerando o critério da resistência, é o {nome_mats[pos]}, 
com uma tensão limite de {mat_esc[pos]}MPa.\n""")

################################################################## FUNÇÃO 4 #############################################################################

  @classmethod #Cálculo de diâmetro dos rebites utilizando a propriedade do mat
  def diamRebite(cls):
    print("\nParâmetro selecionado: Diâmetro mínimo do(s) rebite(s).")
          
    mat_sel = int(input("Insira o ID do material do rebite:"))
          
    selec_prop = float(mat_esc[mat_sel])
    selec_name = str(nome_mats[mat_sel])
       
    Q = float(input(f"Carga cortante exercida sobre a peça [N]: "))
    n = float(input(f"Número de rebites: "))
    N = float(input(f"Quantidade de pontos onde o rebite sofrerá cisalhamento: "))
    s = float(input(f"Fator de segurança dos rebites: "))

    def diam_reb(Q, n, N, s):
      return round((math.sqrt((Q*s*4)/(n*N*math.pi*selec_prop))),2)

    return print(f"\nDiâmetro do(s) rebite(s) em {selec_name}: {diam_reb(Q, n, N, s)}mm")

################################################################## FUNÇÃO 5 #############################################################################

  @classmethod #Tensão de máxima flexão
  def tensFlex(cls):
    pass

################################################################## FUNÇÃO 6 #############################################################################

  @classmethod #Momento Fletor
  def momFletor(cls):
    pass

################################################################## FUNÇÃO 6 #############################################################################

  @classmethod #Momento Torsor
  def momTorsor(cls):
    pass

########################################################################################################################################################

def nomesIDs(): #Função com os nomes e IDs dos materiais
  print("")
  while True:
    return print('\n\n'.join(str(x) for x in nomeID_mats[1:]))
    break

def listaFuncoes(): #Função com a lista de funções disponíveis
  print("")
  while True:
    return print('\n\n'.join(str(x) for x in listFuncs))
    break

listFuncs = [
        '1 - Decomposição de Forças',
        '2 - Cálculo de Força Resultante',
        '3 - Tensão de Cisalhamento', 
        '4 - Diâmetro do Rebite (Critério Resistência)',
        '5 - Máxima Tensão de Flexão (Indisponível)'
         ]

################################################################## MATERIAIS ###########################################################################

class Material: #Classe para definição dos materiais
  def __init__(self, nomeID, nome, lim_esc, rup_trac):
    self.nomeID = nomeID
    self.nome = nome
    self.lim_esc = lim_esc
    self.rup_trac = rup_trac

mat_esc = []
nome_mats = []
nomeID_mats = []

mat0 = Material("N/A", "N/A", 9999, 9999)
nomeID_mats.append(mat0.nomeID)
nome_mats.append(mat0.nome)
mat_esc.append(mat0.lim_esc)

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

################################################################## FUNCTION REFS #######################################################################

exec_funcao1 = funcs.decomposicao

exec_funcao2 = funcs.calcular_resultante

exec_funcao3 = funcs.tensaoCis

exec_funcao4 = funcs.diamRebite

################################################################## EXECUÇÃO #############################################################################

funcoes = {
           "materiais": nomesIDs,
           "funcoes": listaFuncoes,
           "1": exec_funcao1,
           "2": exec_funcao2,
           "3": exec_funcao3,
           "4": exec_funcao4
           }

while True:
  try:
    select_func = str(input("Selecione a função que deseja executar, ou ""'sair'"" para sair: "))
    if select_func == "sair":
      print(f"\nObrigado!")
      break
    else:
      pass
    exe_func = funcoes.get(select_func)()

    end = input(f"Deseja executar uma nova função? ")
    if end in ["sim", "s"]:
      pass
    elif end in ["não", "nao", "n"]:
      print(f"\nObrigado!")
      break
    else:
      print("ERRO!")
      time.sleep(5)
      break

  except:
    print("Valor inserido inválido. Tente novamente.")

#########################################################################################################################################################
