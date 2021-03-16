from math import log10
from matplotlib import pyplot as plt
import time
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')


def l_free_space(d: 'km', f: 'MHz'):
    return 32.44 + 20 * log10(d) + 20 * log10(f)


def atenuacaoEspacoLivre(freq):
    lista_d = []
    lista_free_space = []
    for d in range(1, 1000+1):
        lista_d.append(d)
        lista_free_space.append(l_free_space(d/1000, freq))
    plt.plot(lista_d, lista_free_space)
    plt.title(f"{freq} MHz")
    plt.xlabel('Distância [m]')
    plt.ylabel('Atenuacao em Espaço livre [dB]')
    plt.grid()
    # criar nome para o novo gráfico
    nome_grafico = f"plot_atenuacao_{freq}MHz_" + str(time.time()) + ".jpg"
    # apagar o gráfico antigo
    for filename in os.listdir('app/static/'):
        if filename.startswith(f'plot_atenuacao_{freq}MHz_'):
            os.remove('app/static/' + filename)
    plt.savefig('app/static/' + nome_grafico)
    plt.close()
    return nome_grafico


def propagacaoEspacoLivre(freq):
    Pe = 100  # mW
    Ge = 0  # dBi
    Gr = 0  # dBi
    lista_d = []
    lista_pr = []
    lista_prx_min = []
    pe = 10 * log10(Pe)  # dBm
    for d in range(1, 500+1):
        lista_d.append(d)
        lista_prx_min.append(-70)
        pr = pe + Ge - l_free_space(d/1000, freq) + Gr
        lista_pr.append(pr)
    plt.plot(lista_d, lista_pr, label="Prx")
    plt.title(f"{freq} MHz")
    plt.legend()
    plt.xlabel('Distância [m]')
    plt.ylabel('Potência recebida [dBm]')
    plt.grid()
    plt.show()
    # criar nome para o novo gráfico
    nome_grafico = f"plot_propagacao_{freq}MHz_" + str(time.time()) + ".jpg"
    # apagar o gráfico antigo
    for filename in os.listdir('app/static/'):
        if filename.startswith('plot_propagacao_{freq}MHz_'):
            os.remove('app/static/' + filename)
    plt.savefig('app/static/' + nome_grafico)
    plt.close()
    return nome_grafico
