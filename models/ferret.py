from models.exotic_animal import ExoticAnimal

#Clase Ferret hija de la clase ExoticAnimal
class Ferret(ExoticAnimal):

    #Constructor de la clase que define sus propiedades e inicializa las propiedades de sus padres (ExoticAnimal y Animal)
    def __init__(self, name: str, weight: float, age: int, originCountry: str, taxes: float) -> None:
        super().__init__(name, weight, age, originCountry, taxes)

     #Implementación del método make_sound de la clase padre Animal
    def make_sound(self) -> str:
        return '¡Eek Eek!'
    
    #Implementación de los métodos propios de la clase interfaz IAnimal    
    def get_kilos_eaten(self) -> float:
        return self._kilos_eaten
    
    def eat(self, kilos:float) -> None:
        self._kilos_eaten += kilos