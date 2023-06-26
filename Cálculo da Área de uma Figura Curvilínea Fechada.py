# Método Iterativo de Geração de Curvas de George Chaikin (Método de Subdivisão ou Recorte de Cantos)
# A cada iteração são gerados 2n-2 pontos ou arestas

import numpy
import matplotlib.pyplot
from scipy.integrate import simps
#from scipy.interpolate import interp1d
#from scipy.integrate import quad
#from scipy.interpolate import CubicSpline

x = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2]
y = [2, 3, 1, 4, 3, 5, 7, 6, 6.5, 4.5, 2, 3]

matplotlib.pyplot.scatter(x, y)
matplotlib.pyplot.plot(x, y, 'b-')
matplotlib.pyplot.show()

for iteracao in range(1, 6):

    vector_arestas_x =[]
    vector_arestas_y =[]
    
    for j in range(len(x)-1):

        x1 = (3/4)*x[j]+(1/4)*x[j+1]
        y1 = (3/4)*y[j]+(1/4)*y[j+1]
        vector_arestas_x.append(x1)
        vector_arestas_y.append(y1)

        x1 = (1/4)*x[j]+(3/4)*x[j+1]
        y1 = (1/4)*y[j]+(3/4)*y[j+1]
        vector_arestas_x.append(x1)
        vector_arestas_y.append(y1)

    x = numpy.array(vector_arestas_x)
    y = numpy.array(vector_arestas_y)

    matplotlib.pyplot.scatter(x, y)
    matplotlib.pyplot.plot(x, y, 'y-')
    matplotlib.pyplot.show()

# Preparar os dados para processamento

x = x[:-2]
y = y[:-2]

indices = numpy.argsort(x)

''' Ordenar x e aplicar a mesma ordem a y. Isto é, manter a correspondência
entre os valores dos vectores x e y, após ordenar o vector x.
'''
x_sorted = x[indices]
y_matching = y[indices]

# Criar uma cópia do vector y_matching.
y_sorted = y_matching.copy()

# Ciclo para percorrer o vector e ordenar os valores em cada par de posições.
''' Nota que: A expressão vector[0:2] seleciona os elementos do vector nas
posições de índice de 0 a 2, excluindo o elemento no índice 2.'''
for i in range(0, len(y_matching), 2):
    y_sorted[i:i+2] = numpy.sort(y_matching[i:i+2])

''' Calcular a área da figura curvilínea fechada pelo método de integração
numérica regra dos trapézios composta com n sub-intervalos, cuja fórmula geral
é: (h/2)*(y(1)+2y(2)+2y(3)+...+2y(n-1)+2y(n)+y(n+1)).'''

# n é o número de sub-intervalos
n = 159

# Calcular a área para a curva cujos valores das ordenadas são os mais baixos.
'''
# Calcular o somatório 2y(2)+...+2y(n), para a curva cujos valores das ordenadas
# são os mais baixos.
'''
resultado = y_sorted[2:-2:2]

'''
lower_2y2_2yn = 0
for i in range(len(resultado)):
    lower_2y2_2yn += 2*resultado[i]

# calcular o somatório y(1)+y(n+1), para a curva cujos valores das ordenadas são
# os mais baixos.
lower_y1_ynplus1 = y_sorted[0] + y_sorted[len(y_sorted)-2]

# Calcular a área, para a curva cujos valores das ordenadas são os mais baixos
h = x_sorted[len(x_sorted)-1]-x_sorted[0]
lower_curve_area = (h/2)*(lower_y1_ynplus1+lower_2y2_2yn)
'''

h = (x_sorted[len(x_sorted)-1]-x_sorted[0])/n
lower_curve_area = h*(numpy.sum(resultado)-0.5*(resultado[0]+resultado[-1]))

# Calcular a área para a curva cujos valores das ordenadas são os mais altos.
'''
# Calcular o somatório 2y(2)+...+2y(n), para a curva cujos valores das ordenadas
# são os mais altos.
'''
resultado = y_sorted[3:-2:2]

'''
higher_2y2_2yn = 0
for i in range(len(resultado)):
    higher_2y2_2yn += 2*resultado[i]

# calcular o somatório y(1)+y(n+1), para a curva cujos valores das ordenadas são
# os mais altos.
higher_y1_ynplus1 = y_sorted[1] + y_sorted[len(y_sorted)-1]

# Calcular a área, para a curva cujos valores das ordenadas são os mais altos
higher_curve_area = (h/2)*(higher_y1_ynplus1+higher_2y2_2yn)
'''

higher_curve_area = h*(numpy.sum(resultado)-0.5*(resultado[0]+resultado[-1]))

# Calcular a área da figura curvilínea fechada
closed_curvy_figure_area = higher_curve_area-lower_curve_area

print("A área da figura curvilínea fechada é aproximadamente = ", round(closed_curvy_figure_area, 2), " units of length²")

area = simps(y_sorted, x_sorted)
print("Área: ", area)

'''
interpolation_function = interp1d(x_sorted, y_sorted)

def function(x_sorted):
    return interpolation_function(x_sorted)

area, error = quad(function, min(x_sorted), max(x_sorted), limit=100000)
print("Área: ", area)
'''
'''
x1 = x_sorted[::2]
x2 = x_sorted[1::2]
y1 = y_sorted[::2]
y2 = y_sorted[1::2]

spline1 = CubicSpline(x1, y1)
spline2 = CubicSpline(x2, y2)

def funcao1(x1):
    return spline1(x1)

def funcao2(x2):
    return spline2(x2)
'''
'''
for i in range (len(x)):
    print(x[i])
    matplotlib.pyplot.scatter(x[i], y[i])
    matplotlib.pyplot.draw()
    matplotlib.pyplot.pause(0.1)
matplotlib.pyplot.show()
'''
