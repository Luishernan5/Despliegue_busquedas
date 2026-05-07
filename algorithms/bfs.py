from .nodo import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):

    visitados = []
    frontera = []

    nodo_inicial = Nodo(estado_inicial)
    frontera.append(nodo_inicial)

    while frontera:

        nodo = frontera.pop(0)
        visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo

        dato = nodo.get_datos()

        hijos_datos = [
            [dato[1], dato[0], dato[2], dato[3]],
            [dato[0], dato[2], dato[1], dato[3]],
            [dato[0], dato[1], dato[3], dato[2]]
        ]

        hijos = []

        for h in hijos_datos:

            hijo = Nodo(h)
            hijo.set_padre(nodo)

            if not hijo.en_lista(visitados) and not hijo.en_lista(frontera):
                frontera.append(hijo)

            hijos.append(hijo)

        nodo.set_hijos(hijos)

    return None