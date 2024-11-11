import unittest
from models.boa_constrictor import BoaConstrictor

class TestBoaConstrictor(unittest.TestCase):
    # Método para probar que el sonido de la boa es el esperado
    def test_make_sound_successed(self):
        boa = BoaConstrictor('Helena', 19.0, 9, 'Brazil', 3500.3)
        self.assertEqual(boa.make_sound(),'¡Tsss!')

    # Método para probar un fallo esperado en el sonido de la boa
    @unittest.expectedFailure
    def test_make_sound_failed(self):
        boa = BoaConstrictor('Helena', 19.0, 9, 'Brazil', 3500.3)
        self.assertEqual(boa.make_sound(),'¡Tsss Tssss!')

    # Método para probar que el cálculo de los costos de transporte es el esperado
    def test_calculate_freight_successed(self):
        boa = BoaConstrictor('Helena', 19.0, 9, 'Brazil', 3500.3)
        self.assertEqual(boa.calculate_freight(), 66505.70)

    # Método para probar un fallo esperado en el cálculo de los costos de transporte
    @unittest.expectedFailure
    def test_calculate_freight_failed(self):
        boa = BoaConstrictor('Helena', 19.0, 9, 'Brazil', 3500.3)
        self.assertEqual(boa.calculate_freight(), 100000)
    
    # Método para probar que alimentar a la boa funciona correctamente y cuenta el número de ratones comidos
    def test_feed_boa_successed(self):
        boa = BoaConstrictor('Helena', 19.0, 9, 'Brazil', 3500.3)
        for _ in range(10):
            self.assertEqual(boa.feed_boa(), 'Éxito')
            self.assertEqual(boa.get_eatenMice(), _ + 1)

    # Método para probar un fallo esperado cuando la boa ha comido demasiados ratones
    @unittest.expectedFailure
    def test_feed_boa_too_much_mice(self):
        boa = BoaConstrictor('Helena', 19.0, 9, 'Brazil', 3500.3)
        for _ in range(20):
            print(f'feed boa: {_}')
            boa.feed_boa()
        with self.assertRaises(ValueError) as context:
            boa.feed_boa()

        self.assertEqual(str(context.exception), 'Demasiados Ratones!')

if __name__ == '__main__':
    unittest.main()
