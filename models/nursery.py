from models.boa_constrictor import BoaConstrictor
from models.ferret import Ferret

class Nursery:
    def __init__(self) -> None:
        # Inicialización de las listas para almacenar boas constrictoras y hurones
        self.__lstBoasConstrictor = []
        self.__lstFerrets = []

    # Método para obtener la lista de boas constrictoras
    def get_lstBoasConstrictor(self) -> list:
        return self.__lstBoasConstrictor

    # Método para añadir una boa constrictora a la lista
    def add_boa_constrictor(self, boa_constrictor: BoaConstrictor) -> None:
        self.__lstBoasConstrictor.append(boa_constrictor)

    # Método para obtener la lista de hurones
    def get_lstFerrets(self) -> list:
        return self.__lstFerrets

    # Método para añadir un hurón a la lista
    def add_ferret(self, ferret: Ferret) -> None:
        self.__lstFerrets.append(ferret)

    # Método para alimentar una boa constrictora
    def feed_boa(self, boa: BoaConstrictor = None) -> str:
        result = ''  # Inicializamos la variable result
        
        # Verificamos si la boa proporcionada es None
        if boa is None:
            raise ValueError('Esta Boa no existe')
        
        # Buscamos la boa en la lista de boas constrictoras
        temp_boa = next((b for b in self.__lstBoasConstrictor if b == boa), None)
        
        # Verificamos si la boa se encontró en la lista y es una instancia de BoaConstrictor
        if temp_boa is None or not isinstance(temp_boa, BoaConstrictor):
            raise ValueError('Esta Boa no existe')
        
        try:
            # Intentamos alimentar a la boa y asignamos el resultado
            result = temp_boa.feed_boa()
        except ValueError as exc:
            # Capturamos y mostramos cualquier excepción de tipo ValueError
            print('Error: ' + str(exc))
            raise
        
        # Imprimimos el resultado de la operación
        print('Result: ' + str(result))
        
        return result
