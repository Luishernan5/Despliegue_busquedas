class Nodo:

    def __init__(self, datos, padre=None):
        self.datos = datos
        self.padre = padre
        self.hijos = []
        self.costo = 0

    def set_hijos(self, hijos):
        self.hijos = hijos

    def get_hijos(self):
        return self.hijos

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def get_datos(self):
        return self.datos

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def en_lista(self, lista_nodos):
        for n in lista_nodos:
            if self.datos == n.datos:
                return True
        return False