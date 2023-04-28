from functions import *

'''
O código implementa o Teorema Chinês do Resto.
O usuário é solicitado a inserir o número de equações, e para cada equação, os valores de 'a' e 'm' são inseridos.
Se todos os valores de 'm' forem inteiros positivos e primos entre si, o programa prossegue para calcular a solução usando o Teorema Chinês do Resto.
Caso contrário, o programa exibe uma mensagem de erro.
Os passos do algoritmo incluem calcular o valor de 'm' como o produto de todos os valores 'm' inseridos e, em seguida, encontrar os valores de 'Mn' e 'Mbarra'.
A seguir, os inversos 'Yn' são calculados e usados para obter o somatório de 'a * M * Y', a partir do qual a solução é calculada.
O resultado é exibido na forma 'N = resultado + m * n'.
'''

# main
print('-' * 50)
qntd_equacoes = input('Qual a quantidade de equações? ')
qntd_equacoes_int = int(qntd_equacoes)

valores_de_m = []
valores_de_a = []
sao_positivos = True

# Inserindo os valores de 'a' e 'm'
for i in range(qntd_equacoes_int):
    print('-' * 50)
    print('\nSeja a equação do tipo x ≡ a (mod m)')
    print(f'Para a equação {i + 1}')
    a = int(input('Digite o valor de a: '))
    valores_de_a.append(a)
    m = int(input('Digite o valor de m: '))
    if m <= 1:
        sao_positivos = False
        break
    valores_de_m.append(m)

# Função para ver se são primos relativos
sao_primos_relativos = saoPrimosRelativos(valores_de_m) 

if sao_primos_relativos and sao_positivos:  
    # Calculando o valor de m = m1 * m2 * ... * mn
    m = calculaM(valores_de_m)
    # Listando os valores de Mn = m/mn
    lista_mzao = calculaMzao(valores_de_m, m)
    # Listando os valores de Mbarra = Mn / mn
    lista_m_barra = calculaMbarra(qntd_equacoes_int, lista_mzao, valores_de_m)
    # Calculado os inversos: Yn
    inversos = calculaInversos(qntd_equacoes_int, lista_m_barra, valores_de_m)
    # Somatório dos inversos
    somatorio_aMy = calculaSomatorio_aMy(qntd_equacoes_int, valores_de_a, lista_mzao, inversos)
    # Resultado do menor número
    resultado = somatorio_aMy % m

    print('-' * 50)
    print(f'\nLogo, {somatorio_aMy} ≡ {resultado} (mod {m})')
    print(f'N = {resultado} + {m} * n')
else:
    print('O Teorema se aplica apenas onde m1, m2 ... mn sejam inteiros positivos primos relativos maiores que 1.')