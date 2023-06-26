# Método Iterativo de Geração de Curvas de George Chaikin (Método de Subdivisão ou Recorte de Cantos)
# A cada iteração são gerados 2n-2 pontos ou arestas

import matplotlib.pyplot

x = [1, 2, 3, 4, 5]
y = [2, 3, 1, 4, 3]

matplotlib.pyplot.scatter(x, y)
matplotlib.pyplot.plot(x, y, 'b-')
matplotlib.pyplot.show()

for i in range(1, 6):

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

    x = list(vector_arestas_x)
    y = list(vector_arestas_y)

    matplotlib.pyplot.scatter(x, y)
    matplotlib.pyplot.plot(x, y, 'y-')
    matplotlib.pyplot.show()
