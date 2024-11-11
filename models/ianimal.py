from abc import ABC, abstractmethod


#Clase interfaz para definir métodos para la clase animal
class IAnimal(ABC):

    #Métodos abstractos sin implementación para la interfaz
    @abstractmethod
    def eat(self, kilos:float) ->None:
        pass

    @abstractmethod
    def get_kilos_eaten(self) -> float:
        pass