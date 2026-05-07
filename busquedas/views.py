from django.shortcuts import render

from algorithms.bfs import buscar_solucion_BFS
from algorithms.dfs import buscar_solucion_DFS
from algorithms.ucs import buscar_solucion_UCS


def obtener_camino(nodo, estado_inicial):

    camino = []

    while nodo.get_padre() is not None:

        camino.append(nodo.get_datos())

        nodo = nodo.get_padre()

    camino.append(estado_inicial)

    camino.reverse()

    return camino


def index(request):

    resultados = {}

    if request.method == 'POST':

        inicial = request.POST['inicial']

        objetivo = request.POST['objetivo']

        algoritmo = request.POST['algoritmo']

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

            resultados['BFS'] = obtener_camino(
                nodo,
                estado_inicial
            )

        # DFS
        elif algoritmo == 'dfs':

            nodo = buscar_solucion_DFS(
                estado_inicial,
                solucion
            )

            resultados['DFS'] = obtener_camino(
                nodo,
                estado_inicial
            )

        # UCS
        elif algoritmo == 'ucs':

            nodo = buscar_solucion_UCS(
                estado_inicial,
                solucion
            )

            resultados['UCS'] = obtener_camino(
                nodo,
                estado_inicial
            )

        # TODOS
        elif algoritmo == 'todos':

            nodo_bfs = buscar_solucion_BFS(
                estado_inicial,
                solucion
            )

            nodo_dfs = buscar_solucion_DFS(
                estado_inicial,
                solucion
            )

            nodo_ucs = buscar_solucion_UCS(
                estado_inicial,
                solucion
            )

            resultados['BFS'] = obtener_camino(
                nodo_bfs,
                estado_inicial
            )

            resultados['DFS'] = obtener_camino(
                nodo_dfs,
                estado_inicial
            )

            resultados['UCS'] = obtener_camino(
                nodo_ucs,
                estado_inicial
            )

    return render(request, 'index.html', {

        'resultados': resultados

    })