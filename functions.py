import math

def calculaM(valores_de_m):
    m = 1
    for i in valores_de_m:
        m *= i
    return m


def calculaMzao(valores_de_m, m):
    lista_Mzao = []
    for i in valores_de_m:
        mzao = m / i
        lista_Mzao.append(mzao)
    return lista_Mzao


def calculaMbarra(tam_lista, lista_mzao, lista_mzin):
    lista_m_barra = []
    for i in range(0, tam_lista):
        m_barra = lista_mzao[i] % lista_mzin[i]
        lista_m_barra.append(m_barra)
    return lista_m_barra


def calculaInversos(tamanho, lista_m_barra, lista__mzin):
    inversos = []
    for i in range(0, tamanho):
        n = 1
        while True:
            inverso  = (n * lista_m_barra[i]) % lista__mzin[i]
            if inverso == 1:
                inversos.append(n)
                break
            n += 1
    return inversos


def calculaSomatorio_aMy(tamanho, lista_a, lista_mzao, inversos):
    soma = 0
    for i in range(0, tamanho):
        aMy = lista_a[i] * lista_mzao[i] * inversos[i]
        soma += aMy
    return soma


def saoPrimosRelativos(valores_m):
    tamanho_lista = len(valores_m)
    for i in range(0, tamanho_lista):
        for k in range(i + 1, tamanho_lista):
            nao_sao = math.gcd(valores_m[i], valores_m[k]) != 1
            if nao_sao:
                return False
        return True