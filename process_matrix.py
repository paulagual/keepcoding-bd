from functools import reduce

def process_matrix(matrix):
    """ 
    Recibe como parámetro una matriz (lista de listas)
    y si los valores son todos numéricos la pasa a _process_matrix
    """
    #Si alguno de los elementos no es numerico
    if not is_numerical_matrix(matrix):
        #lanzo una excepción
        raise ValueError('The elements of the matrix must be numeric')
    else:
        #si no proceso la matriz
        return _process_matrix(matrix)

def is_numerical_matrix(matrix):
    """ 
    Recibe una matriz y devuelve True si todos sus elementos son números
    False si no es así
    """
    #obtengo una lista con todos los elementos
    all_elements = [element for row in matrix for element in row]

    #selecciono los elementos numéricos
    numerical_elements = filter(is_numerical, all_elements)

    #si las dos listas tienen los mismos items, es toda numérica
    return all_elements == list(numerical_elements)

def is_numerical(element):
    """ 
    Recibe un elemento y devuelve True si es numérico int o float
    False si no es así
    """
    return type(element) in (int, float)

def _process_matrix(matrix):
    """ 
    Recibe como parámetro una matriz (lista de listas) de números 
    y devuelve otra, con el mismo tamaño y número de elementos,
    con el promedio de sus vecinos.
    Interior: 4 vecinos.
    Borde: 3 vecins.
    Esquina: 2 vecinos.
    """
    #devuelvo la matriz procesada
    return [[process_element((i, j), matrix) for j in range(len(matrix[0]))] for i in range(len(matrix))]


def process_element(index,matrix):
    """ 
    Recibe un indice (i,j) y una matrix, encuentra sus vecinos,
    calcula el promedio con sus vecinos y devuelve dicho promedio.
    """
    #obtengo la lista de indices de los vecinos
    neighbours_indexes = get_neighbours_indexes(index, matrix)

    #obtengo la lista de los valores de los vecinos
    neighbours_values = get_neighbours_values(neighbours_indexes, matrix)

    #Calcula el promedio de los elementos
    average = get_average(neighbours_values)
    
    #Devuelve la media
    return average

def get_neighbours_indexes(index,matrix):
    """ 
    Obtenemos la lista de indices (i,j) de vecinos que incluye
    el indice (i,j) del propio elemento y el de sus vecinos.
    Sólo los posibles.
    """

    #Obtengo una lista con los vecinos genéricos
    neighbours_indexes = get_all_neighbours_indexes(index,matrix)

    #Filtro solo los indices POSIBLES 
    #(todos los valores de la tupla mayores que cero o menor que la longitud de columna o fila)
    return filter(lambda index: 
                    index[0]>=0 and 
                    index[0]<len(matrix) and 
                    index[1]>=0 and 
                    index[1]<len(matrix[0]), 
                    neighbours_indexes)

def get_all_neighbours_indexes(index,matrix):
    """ 
    Obtiene la lista de todos los vecinos de un punto (posibles e imposibles)
    """
    i = index[0]
    j = index[1]

    #Hago una lista con los vecinos genéricos
    all_neighbours_indexes = [(i,j-1),(i,j+1),(i,j),(i-1,j),(i+1,j)]

    return all_neighbours_indexes

def get_neighbours_values(indexes, matrix):
    """ 
    Obtenemos los valores de una lista, dados sus indices (i,j) de una matriz.
    """
    #Hago una lista de los valores de los vecinos
    return [get_value(index, matrix) for index in indexes]

def get_value(index, matrix):
    """
    Obtiene el valor de un elemento de una matriz, dado su índice
    """
    return matrix[index[0]][index[1]]
    
def get_average(values):
    """ 
    Recibe una lista de numeros y devuelve el promedio de sus valores.
    """
    #Calculo el promedio de los valores de una lista
    return reduce(lambda accum , value: accum + value, values, 0) / len(values)