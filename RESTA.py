def resta (lista, lista1, n):
    if type (lista) == list and type (lista1) == list:
        return resta_aux (lista, 0, lista1, n)
    else: return 'Error'

def resta_aux (lista, prestado, lista1, base):
    if lista == []:
        return []
    if  (lista[0] - prestado) > lista1 [0]:
        return [(lista [0] - prestado) - lista1 [0]] + resta_aux (lista[1:], prestado, lista1[1:], base)
    if (lista [0]- prestado)== lista1[0]:
        return [0] +  resta_aux (lista[1:], prestado, lista1[1:], base)
    if (lista[0] - prestado) < lista1[0]:
        return [((lista [0] - prestado) + base) - lista1[0]] + resta_aux (lista[1:], prestado+1, lista1[1:], base)

