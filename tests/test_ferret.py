import unittest
from models.ferret import Ferret

class TestFerret(unittest.TestCase):
    # Método para probar que el sonido del hurón es el esperado
    def test_make_sound_successed(self):
        ferret = Ferret('Thiago', 2.0, 9, 'Brazil', 1500.5)
        self.assertEqual(ferret.make_sound(), '¡Eek Eek!')

    # Método para probar un fallo esperado en el sonido del hurón
    @unittest.expectedFailure
    def test_make_sound_failed(self):
        ferret = Ferret('Thiago', 2.0, 9, 'Brazil', 1500.5)
        self.assertEqual(ferret.make_sound(), '¡Eeek Eeek!')

    # Método para probar que el cálculo de los costos de transporte es el esperado
    def test_calculate_freight_successed(self):
        ferret = Ferret('Helena', 19.0, 9, 'Brazil', 3500.3)
        self.assertEqual(ferret.calculate_freight(), 66505.70)

    # Método para probar un fallo esperado en el cálculo de los costos de transporte
    @unittest.expectedFailure
    def test_calculate_freight_failed(self):
        ferret = Ferret('Thiago', 2.0, 9, 'Brazil', 1500.5)
        self.assertEqual(ferret.calculate_freight(), 100000)

if __name__ == '__main__':
    unittest.main()
