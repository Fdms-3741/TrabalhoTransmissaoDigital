import numpy as np
import matplotlib.pyplot as plt

def PlotConstelacao(data):
    """
    PlotConstelacao(data)
    Descrição:
        Faz um plot de constelação dos dados
    Parâmetros:
        - data: Símbolos em quaisquer dimensões para fazer a constelação.
    """
    plt.scatter(np.real(data.ravel()),np.imag(data.ravel()))
