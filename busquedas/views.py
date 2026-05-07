from django.shortcuts import render

from algorithms.bfs import buscar_solucion_BFS
from algorithms.dfs import buscar_solucion_DFS
from algorithms.ucs import buscar_solucion_UCS


def index(request):

    resultado = None
    algoritmo_usado = None
    costo = 0

    if request.method == 'POST':

        inicial = request.POST['inicial']
        objetivo = request.POST['objetivo']
        algoritmo = request.POST['algoritmo']

        algoritmo_usado = algoritmo.upper()

        estado_inicial = list(
            map(int, inicial.split(','))
        )

        solucion = list(
            map(int, objetivo.split(','))
        )

        # BFS
        if algoritmo == 'bfs':

            nodo = buscar_solucion_BFS(
                estado_inicial,
                solucion
            )

        # DFS
        elif algoritmo == 'dfs':

            nodo = buscar_solucion_DFS(
                estado_inicial,
                solucion
            )

        # UCS
        elif algoritmo == 'ucs':

            nodo = buscar_solucion_UCS(
                estado_inicial,
                solucion
            )

        camino = []

        while nodo.get_padre() is not None:

            camino.append(nodo.get_datos())

            nodo = nodo.get_padre()

            costo += 1

        camino.append(estado_inicial)

        camino.reverse()

        resultado = camino

    return render(request, 'index.html', {

        'resultado': resultado,
        'algoritmo': algoritmo_usado,
        'costo': costo

    })