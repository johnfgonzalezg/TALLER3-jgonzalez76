from models.nursery import Nursery
from models.boa_constrictor import BoaConstrictor
from models.ferret import Ferret
import unittest

class TestNursery(unittest.TestCase):
   
    # Método para probar que alimentar a una boa funciona correctamente
    def test_feed_boa_successed(self) -> None:
        boa1 = BoaConstrictor('Helena', 19.0, 9, 'Brasil', 3500.3)
        boa2 = BoaConstrictor('Albert', 24.0, 5, 'Colombia', 4500.2)
        ferret1 = Ferret('Hugo', 5.56, 4, 'Venezuela', 2345.2)
        ferret2 = Ferret('Victor', 3.34, 2, 'Mexico', 3200.23)
        nursery = Nursery()
        nursery.add_boa_constrictor(boa1)
        nursery.add_boa_constrictor(boa2)
        nursery.add_ferret(ferret1)
        nursery.add_ferret(ferret2)

        # Alimentar a la boa 10 veces y comprobar que cada vez se retorna 'Éxito'
        for _ in range(10):
            self.assertEqual(nursery.feed_boa(boa1), 'Éxito')

    # Método para probar que alimentar a una boa con demasiados ratones lanza una excepción
    @unittest.expectedFailure
    def test_feed_boa_too_much_mice(self) -> None:
        boa1 = BoaConstrictor('Helena', 19.0, 9, 'Brasil', 3500.3)
        boa2 = BoaConstrictor('Albert', 24.0, 5, 'Colombia', 4500.2)
        ferret1 = Ferret('Hugo', 5.56, 4, 'Venezuela', 2345.2)
        ferret2 = Ferret('Victor', 3.34, 2, 'Mexico', 3200.23)
        nursery = Nursery()
        nursery.add_boa_constrictor(boa1)
        nursery.add_boa_constrictor(boa2)
        nursery.add_ferret(ferret1)
        nursery.add_ferret(ferret2)

        # Alimentar a la boa hasta que haya comido demasiados ratones y comprobar que lanza una excepción
        for _ in range(10):
            nursery.feed_boa(boa2)
        with self.assertRaises(ValueError) as context:
            nursery.feed_boa(boa2)
        self.assertEqual(str(context.exception), 'Demasiados Ratones!')

    # Método para probar que alimentar a una boa que no existe lanza una excepción
    @unittest.expectedFailure
    def test_feed_boa_dont_exist(self) -> None:
        boa1 = BoaConstrictor('Helena', 19.0, 9, 'Brasil', 3500.3) 
        boa2 = BoaConstrictor('Albert', 24.0, 5, 'Colombia', 4500.2) 
        boa3 = BoaConstrictor('Miriam', 12.34, 10, 'Venezuela', 3300.98) 
        ferret1 = Ferret('Hugo', 5.56, 4, 'Venezuela', 2345.2) 
        ferret2 = Ferret('Victor', 3.34, 2, 'Mexico', 3200.23) 
        nursery = Nursery()
        nursery.add_boa_constrictor(boa1) 
        nursery.add_boa_constrictor(boa2) 
        nursery.add_ferret(ferret1) 
        nursery.add_ferret(ferret2) 

        # Intentar alimentar a una boa que no ha sido añadida y comprobar que lanza una excepción
        with self.assertRaises(ValueError) as context: 
            nursery.feed_boa(boa3) 
        self.assertEqual(str(context.exception), 'Esta Boa no existe')

if __name__ == '__main__':
    unittest.main()
