"""Lista enlazada y tabla hash para consultar guias de envio."""


class Nodo:
    """Nodo de una lista enlazada que guarda una guia y su estado."""

    def __init__(self, guia: int, estado: str) -> None:
        """Crea un nodo sin siguiente."""
        self.guia = guia
        self.estado = estado
        self.siguiente: "Nodo | None" = None


class ListaEnlazada:
    """Lista simplemente enlazada de guias, con insercion al inicio."""

    def __init__(self) -> None:
        """Crea una lista vacia."""
        self.cabeza: "Nodo | None" = None
        self.tamano = 0

    def insertar(self, guia: int, estado: str) -> None:
        """Agrega una guia al inicio de la lista."""
        nodo_nuevo = Nodo(guia, estado)
        nodo_nuevo.siguiente = self.cabeza
        self.cabeza = nodo_nuevo
        self.tamano += 1

    def buscar(self, guia: int) -> "str | None":
        """Busca una guia recorriendo la lista."""
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.guia == guia:
                return nodo_actual.estado
            nodo_actual = nodo_actual.siguiente
        return None


class TablaHash:
    """Tabla hash con encadenamiento y funcion hash por division."""

    def __init__(self, m: int) -> None:
        """Crea una tabla con m casillas vacias."""
        self.m = m
        self.casillas: list[ListaEnlazada] = [ListaEnlazada() for _ in range(m)]
        self.tamano = 0

    def hash(self, guia: int) -> int:
        """Calcula la casilla de una guia."""
        return guia % self.m

    def insertar(self, guia: int, estado: str) -> None:
        """Inserta una guia en la lista de su casilla."""
        indice = self.hash(guia)
        self.casillas[indice].insertar(guia, estado)
        self.tamano += 1

    def buscar(self, guia: int) -> "str | None":
        """Busca una guia recorriendo solo la lista de su casilla."""
        indice = self.hash(guia)
        return self.casillas[indice].buscar(guia)

    def factor_carga(self) -> float:
        """Calcula el factor de carga de la tabla (n / m)."""
        return self.tamano / self.m