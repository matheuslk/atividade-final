import os
import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

coordenadas_x = np.arange(-7, 7, 0.1)

# FUNCAO DO SEGUNDO GRAU


def calcular_funcao_segundo_grau(coef_a, coef_b, coef_c, x):
  return ((coef_a*(x**2)) + (coef_b*x) + coef_c)


def calcular_delta_funcao_segundo_grau(coef_a, coef_b, coef_c):
  return ((coef_b**2) - (4*coef_a*coef_c))


def calcular_raizes_funcao_segundo_grau(coef_a, coef_b, coef_c):
  delta = calcular_delta_funcao_segundo_grau(coef_a, coef_b, coef_c)
  raiz_delta = 0
  if(delta > 0):
    raiz_delta = math.sqrt(delta)
  elif(delta < 0):
    raiz_delta = cmath.sqrt(delta)
  x1 = ((-coef_b + raiz_delta)/2*coef_a)
  x2 = ((-coef_b - raiz_delta)/2*coef_a)
  if(x1.imag == 0):
    x1 = x1.real
  if(x2.imag == 0):
    x2 = x2.real
  return [x1, x2]


def calcular_vertice_funcao_segundo_grau(coef_a, coef_b, coef_c):
  delta = calcular_delta_funcao_segundo_grau(coef_a, coef_b, coef_c)
  x_vertice = - (coef_b/2*coef_a)
  y_vertice = -(delta/4*coef_a)
  return [x_vertice, y_vertice]


def desenhar_grafico_funcao_segundo_grau(coef_a, coef_b, coef_c):
  coordenadas_y = []
  for x in coordenadas_x:
    coordenadas_y.append(
        calcular_funcao_segundo_grau(coef_a, coef_b, coef_c, x))
  # DESENHAR GRAFICO
  plt.figure(figsize=(5, 5), dpi=80)
  plt.plot(coordenadas_x, coordenadas_y, 'r')
  plt.title('f(x) = ax^2 + bx + c')
  plt.xlabel('Eixo X')
  plt.ylabel('Eixo Y')
  plt.legend()
  plt.grid(True, which='both')
  plt.axhline(y=0, color='k')
  plt.axvline(x=0, color='k')
  # MOSTRAR GRAFICO
  plt.show()

# FUNCAO EXPONENCIAL


def calcular_funcao_exponencial(base, expoente):
  return base**expoente


def desenhar_grafico_exponencial(base):
  coordenadas_y = []
  for expoente in coordenadas_x:
    coordenadas_y.append(
        calcular_funcao_exponencial(base, expoente))
  # DESENHAR GRAFICO
  plt.figure(figsize=(5, 5), dpi=80)
  plt.plot(coordenadas_x, coordenadas_y, 'r')
  plt.title('f(x) = ab^x')
  plt.xlabel('Eixo X')
  plt.ylabel('Eixo Y')
  plt.legend()
  plt.grid(True, which='both')
  plt.axhline(y=0, color='k')
  plt.axvline(x=0, color='k')
  # MOSTRAR GRAFICO
  plt.show()

# MATRIZES


def multiplicar_matrizes(matriz1):
  numero_linhas_2 = int(input("> Digite o numero de linhas para a matriz 2: "))
  numero_colunas_2 = int(
      input("> Digite o numero de colunas para a matriz 2: "))
  matriz2 = [0] * numero_linhas_2
  matriz_resultado = [0] * numero_linhas_1
  for linha in range(numero_linhas_1):
    matriz_resultado[linha] = [0] * numero_colunas_2
  for linha in range(numero_linhas_2):
    matriz2[linha] = [0] * numero_colunas_2
  if len(matriz1) == len(matriz2[0]):
    for linha in range(numero_linhas_2):
      for coluna in range(numero_colunas_2):
        matriz2[linha][coluna] = int(
            input(f"> Digite o conteudo da linha {linha} coluna {coluna} para a matriz 2: "))
    for cont in range(numero_linhas_1):
      for cont2 in range(numero_colunas_2):
        soma = 0
        for linha in range(numero_colunas_1):
          soma += matriz1[cont][linha] * matriz2[linha][cont2]
          matriz_resultado[cont][cont2] = soma
    print(f'> Matriz 1: {matriz1}')
    print(f'> Matriz 2: {matriz2}')
    print(f'> Matriz Resultado: {matriz_resultado}')
    return
  print('> Matriz invalida !')


def calcular_determinante(matriz1):
  diagonal_matriz_1 = matriz1[0][0] * matriz1[1][1] * matriz1[2][2] + \
      matriz1[0][1] * matriz1[1][2] * matriz1[2][0] + \
      matriz1[0][2] * matriz1[1][0] * matriz1[2][1]
  diagonal_matriz_2 = matriz1[2][0] * matriz1[1][1] * matriz1[0][2] + \
      matriz1[2][1] * matriz1[1][2] * matriz1[0][0] + \
      matriz1[2][2] * matriz1[1][0] * matriz1[0][1]
  determinante_matriz = diagonal_matriz_1 - diagonal_matriz_2
  print(f"> Determinante: {determinante_matriz}")


finalizar_calculadora = False
while not finalizar_calculadora:
  os.system('cls||clear')
  print('> (1) Funcao do Segundo Grau')
  print('> (2) Funcao Exponencial')
  print('> (3) Matriz')
  print('> (4) Sair')
  continuar = True
  tipo_funcao = input('> Escolha uma Funcao: ')
  os.system('cls||clear')
  if(tipo_funcao == '1' or tipo_funcao == '2' or tipo_funcao == '3'):
    if(tipo_funcao == '1'):
      # INÍCIO MENU FUNÇÃO DO SEGUNDO GRAU
      opcao_menu = input(
          '> Voce escolheu Funcao do Segundo Grau, digite "S" para continuar ou qualquer outra tecla para voltar: ')
      os.system('cls||clear')
      if(opcao_menu == 'S' or opcao_menu == 's'):
        coef_a = 0
        while(coef_a == 0):
          coef_a = int(input('> Digite o valor do coeficiente A: '))
          if(coef_a == 0):
            input('> O valor do coeficiente A deve ser diferente de 0, digite qualquer tecla para tentar novamente...')
            os.system('cls||clear')
        coef_b = int(input('> Digite o valor do coeficiente B: '))
        coef_c = int(input('> Digite o valor do coeficiente C: '))

        while(opcao_menu != '5'):
          # MENU FUNÇÃO DO SEGUNDO GRAU
          os.system('cls||clear')
          print('> (1) Calcular Raizes')
          print('> (2) Calcular Funcao em X')
          print('> (3) Calcular Vertice')
          print('> (4) Imprimir Grafico')
          print('> (5) Sair')
          opcao_menu = input('> Escolha uma Opcao: ')
          if(opcao_menu == '1' or opcao_menu == '2' or opcao_menu == '3' or opcao_menu == '4'):
            # CALCULAR RAIZES FUNCAO DO SEGUNDO GRAU
            if(opcao_menu == '1'):
              raizes_funcao_segundo_grau = calcular_raizes_funcao_segundo_grau(
                  coef_a, coef_b, coef_c)
              print(
                  f'> Raízes: {raizes_funcao_segundo_grau[0]} e {raizes_funcao_segundo_grau[1]}')
            # CALCULAR FUNCAO DO SEGUNDO GRAU EM X
            elif(opcao_menu == '2'):
              variavel_x = int(input('> Digite o valor da variável X: '))
              resultado_funcao_segundo_grau = calcular_funcao_segundo_grau(
                  coef_a, coef_b, coef_c, variavel_x)
              print(
                  f'> Resultado: {resultado_funcao_segundo_grau}')
            # CALCULAR VERTICE FUNCAO DO SEGUNDO GRAU
            elif(opcao_menu == '3'):
              vertice_funcao_segundo_grau = calcular_vertice_funcao_segundo_grau(
                  coef_a, coef_b, coef_c)
              print(
                  f'> Vertice: {vertice_funcao_segundo_grau[0]} , {vertice_funcao_segundo_grau[1]}')
            # DESENHAR GRÁFICO FUNCAO SEGUNDO GRAU
            elif(opcao_menu == '4'):
              desenhar_grafico_funcao_segundo_grau(coef_a, coef_b, coef_c)
            input('> Digite qualquer tecla para continuar...')
          # SAIR DO MENU DA FUNÇÃO DO SEGUNDO GRAU
          elif(opcao_menu != '5'):
            input('> Opcao invalida, digite qualquer tecla para tentar novamente...')
    elif(tipo_funcao == '2'):
      # INÍCIO MENU FUNÇÃO EXPONENCIAL
      opcao_menu = input(
          '> Voce escolheu Funcao Exponencial, digite "S" para continuar ou qualquer outra tecla para voltar: ')
      os.system('cls||clear')
      if(opcao_menu == 'S' or opcao_menu == 's'):
        base = 0
        while(base == 1 or base <= 0):
          coef_a = int(input('> Digite o valor do coeficiente A: '))
          coef_b = int(input('> Digite o valor do coeficiente B: '))
          base = coef_a * coef_b
          if(base == 1 or base <= 0):
            input('> O valor da base deve ser maior que 0 e diferente de 1, digite qualquer tecla para tentar novamente...')
            os.system('cls||clear')
        while(opcao_menu != '4'):
          # MENU FUNÇÃO EXPONENCIAL
          os.system('cls||clear')
          print('> (1) Verificar se a função é Crescente ou Decrescente')
          print('> (2) Calcular Funcao em X')
          print('> (3) Imprimir Grafico')
          print('> (4) Sair')
          opcao_menu = input('> Escolha uma Opcao: ')
          if(opcao_menu == '1' or opcao_menu == '2' or opcao_menu == '3'):
            # VERIFICAR EXPONENCIAL CRESCENTE / DECRESCENTE
            if(opcao_menu == '1'):
              if(base > 1):
                print(f'> Funcao Crescente')
              else:
                print(f'> Funcao Decrescente')
            # CALCULAR FUNCAO EXPONENCIAL EM X
            elif(opcao_menu == '2'):
              expoente = int(input('> Digite o valor do expoente: '))
              resultado_funcao_exponencial = calcular_funcao_exponencial(
                  base, expoente)
              print(
                  f'> Resultado: {resultado_funcao_exponencial}')
            # DESENHAR GRÁFICO FUNCAO EXPONENCIAL
            elif(opcao_menu == '3'):
              desenhar_grafico_exponencial(base)
            input('> Digite qualquer tecla para continuar...')
          # SAIR DO MENU DA FUNÇÃO EXPONENCIAL
          elif(opcao_menu != '4'):
            input('> Opcao invalida, digite qualquer tecla para tentar novamente...')
    elif(tipo_funcao == '3'):
      opcao_menu = input(
          '> Voce escolheu Matriz, digite "S" para continuar ou qualquer outra tecla para voltar: ')
      os.system('cls||clear')
      if(opcao_menu == 'S' or opcao_menu == 's'):
        numero_linhas_1 = int(
            input("\n> Digite o numero de linhas para a matriz 1: "))
        numero_colunas_1 = int(
            input("> Digite o numero de colunas para a matriz 1: "))
        matriz1 = [0] * numero_linhas_1
        for linha in range(numero_linhas_1):
          matriz1[linha] = [0] * numero_colunas_1
        for linha in range(numero_linhas_1):
          for coluna in range(numero_colunas_1):
            matriz1[linha][coluna] = int(
                input(f"> Digite o conteudo da linha {linha} coluna {coluna}: "))
        while(opcao_menu != '2'):
          # MENU MATRIZES
          os.system('cls||clear')
          print('> (1) Multiplicar Matrizes')
          print('> (2) Sair')
          opcao_menu = input('> Escolha uma Opcao: ')
          # CALCULAR MULTIPLICACAO DE MATRIZ
          if(opcao_menu == '1'):
            multiplicar_matrizes(matriz1)
            input('> Digite qualquer tecla para continuar...')
          elif(opcao_menu != '2'):
            input('> Opcao invalida, digite qualquer tecla para tentar novamente...')
  elif(tipo_funcao == '4'):
    finalizar_calculadora = True
    os.system('cls||clear')
    print('> Calculadora finalizada, ate a proxima !')
  else:
    input('> Opcao invalida, digite qualquer tecla para tentar novamente...')
