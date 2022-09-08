import math
import time
from decimal import Decimal

################################################################## FUNÇÕES ##############################################################################

class funcs: #Classe definindo as funções disponíveis
  def __init__(self):
    pass

################################################################## FUNÇÃO 1 #############################################################################

  @classmethod #Decomposição de forças
  def decomposicao(cls):
    separator()
    print('')
    print(f"Função selecionada: Decomposição de forças.\n")
    F = float(input("Digite o valor da Força [N]: "))
    angulo = float(input("Digite o valor do ângulo entre o vetor e seu plano horizontal [°]: "))
    ang_rad_x = math.radians(angulo)
    ang_rad_y = math.radians(90-angulo)
    Fx = F * math.cos(ang_rad_x)
    Fy = F * math.cos(ang_rad_y)
    return print(f"A força no eixo x é de {round(Fx, 2)}N" , f"\nA força no eixo y é de {round(Fy, 2)}N\n"), separator()

################################################################## FUNÇÃO 2 #############################################################################

  @classmethod #Cálculo de força resultante
  def calcular_resultante(cls):
    separator()
    print('')
    print(f"Função selecionada: Cálculo de força resultante.")
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
    return print(f"\nA força resultante é de {forca_result}N com um ângulo de {angulo}° em relação ao eixo X\n"), separator()

################################################################## FUNÇÃO 3 #############################################################################

  @classmethod #Pressão de Contato (rebite)
  def pressaoCont(cls):
    separator()
    print('')
    print(f"Função selecionada: Pressão de Contato sobre o(s) rebite(s).\n")
    Q = float(input(f"Carga cortante exercida sobre a peça [N]: "))
    n = float(input(f"Número de rebites: "))
    d = float(input(f"Diâmetro do(s) rebite(s) [mm]: "))
    t = float(input(f"Espessura da(s) chapa(s) [mm]: "))

    resultCont = round(Q/(n*d*t), 2)

    return print(f"Pressão de contato sobre cada rebite: {resultCont}MPa\n"), separator()

################################################################## FUNÇÃO 4 #############################################################################

  @classmethod #Cálculo de tensão de cisalhamento sobre o rebite
  def tensaoCis(cls):
    separator()
    print('')
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
    result = [mat_esc - result_cis for mat_esc in mat_esc]
    resultIndex = min([result for result in result if result > 0])
    posIndex = result.index(resultIndex)

    #encontra o material que possui a propriedade 
    #com o valor encontrado na comparação acima
    posNome = nome_mats[posIndex]
    posCis = mat_esc[posIndex]

    if posIndex == 0:
      return print("""Nenhum dos materiais da base de materiais possui resistência suficiente para a aplicação.
Tente aumentar a quantidade de rebites ou seu diâmetro.\n"""), separator()

    else:
      return print(f"""O material mais indicado para sua aplicação, considerando a resistência do material, é o {posNome}, 
com uma tensão limite de {posCis}MPa.\n"""), separator()

################################################################## FUNÇÃO 5 #############################################################################

  @classmethod #Cálculo de diâmetro dos rebites utilizando a propriedade do mat
  def diamRebite(cls):
    separator()
    print(f"\nFunção selecionada: Diâmetro mínimo do(s) rebite(s).")
          
    mat_sel = int(input("Insira o ID do material do rebite:"))

    selec_prop = float(mat_esc[mat_sel])
    selec_name = str(nome_mats[mat_sel])
       
    Q = float(input(f"Carga cortante exercida sobre a peça [N]: "))
    n = float(input(f"Número de rebites: "))
    N = float(input(f"Quantidade de pontos onde o rebite sofrerá cisalhamento: "))
    s = float(input(f"Fator de segurança dos rebites: "))

    diam_reb = round((math.sqrt((Q*s*4)/(n*N*math.pi*selec_prop))),2)

    return print(f"\nDiâmetro do(s) rebite(s) em {selec_name}: {diam_reb}mm\n"), separator()

################################################################## FUNÇÃO 6 #############################################################################

  @classmethod #Momento de Inércia (Rebite)
  def inercia(cls):
    separator()
    print(f"\nFunção selecionada: Momento de Inércia.")

    d = float(input(f"Diâmetro do rebite [m]: "))
    r = d/2

    momentIn = (math.pi*r**4)/4

    return print(f"\nMomento de Inércia sobre a peça: {Decimal(momentIn):.3E}m⁴\n"), separator()

################################################################## FUNÇÃO 7 #############################################################################

  @classmethod #Momento Fletor
  def momFletor(cls):
    separator()
    print(f"\nFunção selecionada: Cálculo de Momento Fletor.")

    F = float(input(f"Intensidade da força que origina o Momento Fletor [N]: "))
    l = float(input(f"Distância entre o ponto de referência e o ponto onde a força é aplicada[m]: "))

    resMomento = F*l

    return print(f"\nO valor do momento fletor é de {round(resMomento, 2)}Nm\n"), separator()

################################################################## FUNÇÃO 8 #############################################################################

  @classmethod #Tensão máxima de flexão
  def maxFlexao(cls):
    separator()
    print(f"\nFunção selecionada: Tensão Máxima de Flexão.")

    M = float(input(f"Momento fletor sobre a peça [Nm]: "))
    y = float(input(f"Raio do rebite [m]: "))
    I = float(input(f"Momento de inércia da geometria [m⁴]: "))

    flexao = M*y/I*(1e-6)

    return print(f"""
A tensão máxima de flexão para o rebite é de {round(flexao, 2)}MPa
"""), separator()

########################################################################################################################################################
'--------------------------------------------------------------------------------------------------------------------------------------------------------'
def separator(): 
  return print(113*'-')
'--------------------------------------------------------------------------------------------------------------------------------------------------------'
def nomesIDs(): #Função com os nomes e IDs dos materiais
  separator()
  print('')
  while True:
    return print('\n\n'.join(str(x) for x in nomeID_mats[1:]), '\n'), separator()
    break
'--------------------------------------------------------------------------------------------------------------------------------------------------------'
def listaFuncoes(): #Função com a lista de funções disponíveis
  separator()
  print('')
  while True:
    return print('\n\n'.join(str(x) for x in listFuncs), '\n'), separator()
    break
'--------------------------------------------------------------------------------------------------------------------------------------------------------'
def properties():
  nome_mats.pop(0)
  mat_esc.pop(0)
  
  separator()
  
  for x in range(len(nome_mats)):
    print(f"""
Material: {nome_mats[x]}
Tensão de Escoamento: {mat_esc[x]}MPa
Tensão de Ruptura: {tens_ult[x]}MPa
Módulo de Elasticidade (Young): {elast_mats[x]}GPa""")
  print('')
  separator()

  nome_mats.insert(0, "N/A")
  mat_esc.insert(0, 9999)
'--------------------------------------------------------------------------------------------------------------------------------------------------------'
listFuncs = [
        '1 - Decomposição de Forças',
        '2 - Cálculo de Força Resultante',
        '3 - Pressão de Contato (rebites)',
        '4 - Tensão de Cisalhamento',
        '5 - Diâmetro do Rebite (Critério Resistência)',
        '6 - Momento de Inércia',
        '7 - Momento Fletor',
        '8 - Tensão Máxima de Flexão'
         ]

################################################################## MATERIAIS ###########################################################################

class Material: #Classe para definição dos materiais
  def __init__(self, nomeID, nome, lim_esc, ultim_tens, elast):
    self.nomeID = nomeID
    self.nome = nome
    self.lim_esc = lim_esc
    self.ultim_tens = ultim_tens
    self.elast = elast

mat_esc = []
nome_mats = []
nomeID_mats = []
tens_ult = []
elast_mats = []

mat0 = Material("N/A", "N/A", 9999, 9999, 9999)
nomeID_mats.append(mat0.nomeID)
nome_mats.append(mat0.nome)
mat_esc.append(mat0.lim_esc)

mat1 = Material("1 - Aço Inox AISI 304", "Aço Inox AISI 304", 190, 550, 193)
nomeID_mats.append(mat1.nomeID)
nome_mats.append(mat1.nome)
mat_esc.append(mat1.lim_esc)
tens_ult.append(mat1.ultim_tens)
elast_mats.append(mat1.elast)

mat2 = Material("2 - Titânio ASTM F136", "Titânio ASTM F136", 790, 860, 122)
nomeID_mats.append(mat2.nomeID)
nome_mats.append(mat2.nome)
mat_esc.append(mat2.lim_esc)
tens_ult.append(mat2.ultim_tens)
elast_mats.append(mat2.elast)

mat3 = Material("3 - Aço Estrutural ASTM A36", "Aço Estrutural ASTM A36", 250, 450, 200)
nomeID_mats.append(mat3.nomeID)
nome_mats.append(mat3.nome)
mat_esc.append(mat3.lim_esc)
tens_ult.append(mat3.ultim_tens)
elast_mats.append(mat3.elast)

mat4 = Material("4 - Alumínio-6061 T6", "Alumínio 6061-T6", 241, 290, 68)
nomeID_mats.append(mat4.nomeID)
nome_mats.append(mat4.nome)
mat_esc.append(mat4.lim_esc)
tens_ult.append(mat4.ultim_tens)
elast_mats.append(mat4.elast)

mat5 = Material("5 - Aço Carbono SAE 1020", "Aço Carbono AISI 1020", 350, 420, 186)
nomeID_mats.append(mat5.nomeID)
nome_mats.append(mat5.nome)
mat_esc.append(mat5.lim_esc)
tens_ult.append(mat5.ultim_tens)
elast_mats.append(mat5.elast)

mat6 = Material("6 - Aço Inox AISI 420", "Aço Inox AISI 420", 345, 655, 200)
nomeID_mats.append(mat6.nomeID)
nome_mats.append(mat6.nome)
mat_esc.append(mat6.lim_esc)
tens_ult.append(mat6.ultim_tens)
elast_mats.append(mat6.elast)

mat7 = Material("7 - Titânio Grau 2 (98% Ti)", "Titânio Grau 2 (98% Ti)", 275, 345, 102)
nomeID_mats.append(mat7.nomeID)
nome_mats.append(mat7.nome)
mat_esc.append(mat7.lim_esc)
tens_ult.append(mat7.ultim_tens)
elast_mats.append(mat7.elast)

mat8 = Material("8 - Alumínio 2014-T6", "Alumínio 2014-T6", 365, 413, 72)
nomeID_mats.append(mat8.nomeID)
nome_mats.append(mat8.nome)
mat_esc.append(mat8.lim_esc)
tens_ult.append(mat8.ultim_tens)
elast_mats.append(mat8.elast)

mat9 = Material("9 - Aço Inox AISI 316L", "Aço Inox AISI 316L", 172, 482, 193)
nomeID_mats.append(mat9.nomeID)
nome_mats.append(mat9.nome)
mat_esc.append(mat9.lim_esc)
tens_ult.append(mat9.ultim_tens)
elast_mats.append(mat9.elast)

mat10 = Material("10 - Ferro Fundido ASTM A536", "Ferro Fundido ASTM A536", 275, 413, 168)
nomeID_mats.append(mat10.nomeID)
nome_mats.append(mat10.nome)
mat_esc.append(mat10.lim_esc)
tens_ult.append(mat10.ultim_tens)
elast_mats.append(mat10.elast)

################################################################## FUNCTION REFS #######################################################################

exec_funcao1 = funcs.decomposicao

exec_funcao2 = funcs.calcular_resultante

exec_funcao3 = funcs.pressaoCont

exec_funcao4 = funcs.tensaoCis

exec_funcao5 = funcs.diamRebite

exec_funcao6 = funcs.inercia

exec_funcao7 = funcs.momFletor

exec_funcao8 = funcs.maxFlexao

################################################################## EXECUÇÃO #############################################################################

#apresentação do projeto e instruções para a utilização do software
print(f"""
                      Projeto Semestral - ResMat - Team Avalanca

                        LEIA ATENTAMENTE ÀS INFORMAÇÕES ABAIXO

 -Para utilização de casas decimais, utilize ponto (.) ao invés de vírgula (,);
 -Atente-se às unidades de medida para cada variável para garantir o resultado correto;
 -Para visualizar a lista de materiais disponíveis e seu respectivo ID, digite 'materiais';
 -Para visualizar a lista de funções disponíveis e seus respectivos IDs, digite 'funcoes';
 -Para visualizar a lista com as propriedades mecânicas dos materiais disponíveis, digite 'propriedades';
 -Para inserir valores com exponenciais, utilize o exemplo a seguir: 3.2e-3
 """) 
separator()
print('')

funcoes = {
           "propriedades": properties,
           "materiais": nomesIDs,
           "funcoes": listaFuncoes,
           "1": exec_funcao1,
           "2": exec_funcao2,
           "3": exec_funcao3,
           "4": exec_funcao4,
           "5": exec_funcao5,
           "6": exec_funcao6,
           "7": exec_funcao7,
           "8": exec_funcao8
           }

while True:
  try:
    select_func = str(input("Selecione a função que deseja executar, ou ""'sair'"" para sair: "))
    print("")
    if select_func == "sair":
      print(f"Obrigado!")
      break
    else:
      pass
    exe_func = funcoes.get(select_func)()

    end = input(f"\nDeseja executar uma nova função?(S/N) ")
    print("")
    if end in ["sim", "s", "S", "SIM"]:
      pass
    elif end in ["não", "nao", "n", "N", "Nao", "Não", "NÃO"]:
      print(f"Obrigado!")
      break
    else:
      print("ERRO!")
      time.sleep(5)
      break

  except:
    print("Valor inserido inválido. Tente novamente.")

#########################################################################################################################################################
