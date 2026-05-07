from .nodo import Nodo


def buscar_solucion_UCS(estado_inicial, solucion):

    nodos_visitados = []
    nodos_frontera = []

    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)

    nodos_frontera.append(nodo_inicial)

    while len(nodos_frontera) != 0:

        # Ordenar por costo
        nodos_frontera = sorted(
            nodos_frontera,
            key=lambda x: x.get_costo()
        )

        nodo = nodos_frontera.pop(0)

        nodos_visitados.append(nodo)

        # Verificar solución
        if nodo.get_datos() == solucion:
            return nodo

        dato = nodo.get_datos()

        # Operadores
        hijos_datos = [

            # I
            [dato[1], dato[0], dato[2], dato[3]],

            # C
            [dato[0], dato[2], dato[1], dato[3]],

            # D
            [dato[0], dato[1], dato[3], dato[2]]

        ]

        hijos = []

        for h in hijos_datos:

            hijo = Nodo(h)

            hijo.set_padre(nodo)

            # costo acumulado
            hijo.set_costo(nodo.get_costo() + 1)

            hijos.append(hijo)

            if not hijo.en_lista(nodos_visitados):

                if hijo.en_lista(nodos_frontera):

                    for n in nodos_frontera:

                        if (
                            n.get_datos() == hijo.get_datos()
                            and n.get_costo() > hijo.get_costo()
                        ):

                            nodos_frontera.remove(n)
                            nodos_frontera.append(hijo)
                            break

                else:

                    nodos_frontera.append(hijo)

        nodo.set_hijos(hijos)

    return None