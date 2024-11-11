
from models.exotic_animal import ExoticAnimal


#Clase BoaConstrictor hija de la clase ExoticAnimal
class BoaConstrictor(ExoticAnimal):

    #Constructor de la clase que define sus propiedades e inicializa las propiedades de sus padres (ExoticAnimal y Animal)
    def __init__(self, name: str, weight: float, age: int, originCountry: str, taxes: float) -> None:
        super().__init__(name, weight, age, originCountry, taxes)
        self.__eatenMice = 0
    
    #Getters de la propiedad eatenMice
    def get_eatenMice(self) -> int:
        return self.__eatenMice

    #Implementación del método make_sound de la clase padre Animal
    def make_sound(self) -> str:
        return '¡Tsss!'
    
    #Método propio de la clase BoaCosntrictor
    def feed_boa(self) -> str:
        if self.get_eatenMice() >= 20:
            raise ValueError('Demasiados Ratones!')
        self.__eatenMice += 1
        return 'Éxito'

    #Implementación de los métodos propios de la clase interfaz IAnimal    
    def get_kilos_eaten(self) -> float:
        return self._kilos_eaten
    
    def eat(self, kilos:float) -> None:
        self._kilos_eaten += kilos