from models.animal import Animal

#Clase ExoticAnimal hija de Animal
class ExoticAnimal(Animal):

    #Constructor de la clase que define sus propiedades e inicializa las propiedades de su padre (Animal)
    def __init__(self, name:str, weight:float, age:int, originCountry:str, taxes:float) -> None:
        super().__init__(name, weight,age)
        self._originCountry = originCountry
        self._taxes = taxes

    #Getters y Setters
    def get_originCountry(self) ->str:
        return self._originCountry
    
    def get_taxes(self) -> float:
        return self._taxes
    
    def set_originCountry(self, originCountry:str) -> None:
        self._originCountry  = originCountry
    
    def set_taxes(self, taxes:float) -> float:
        self._taxes = taxes
    
    #Método específico de la clase, que calcula la rentabilidad de importación (rentabilidad = peso * impuestos)
    def calculate_freight(self) -> float:
        freight = round(self._weight * self._taxes, 2)
        return freight
    


