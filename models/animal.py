from models.ianimal import IAnimal
from abc import abstractmethod


#Clase padre Animal que implementa la interfaz IAnimal
class Animal(IAnimal):
    #Constructor de la clase
    def __init__(self, name:str, weight:float, age:int) -> None:
        self._name = name
        self._weight = weight
        self._age = age
        self._kilos_eaten = 0
    
    #Getters y Setters para las propiedades de la clase
    def get_name(self) -> str:
        return self._name
    
    def get_weight(self) -> float:
        return self._weight
    
    def get_age(self) -> int:
        return self._age
    
    def set_name(self, name:str) -> None:
        if isinstance(name, str):
            self._name = name
    
    def set_weight(self, weigth:float) -> None:
        if isinstance(weigth, float):
            self._weigth = weigth

    def set_age(self, age:int) -> None:
        if isinstance(age, int):
            self._age = age

    #Método definido pero sin implementación para ser definida en cada una de las clases hijas  
    @abstractmethod
    def make_sound(self) -> str:
        pass