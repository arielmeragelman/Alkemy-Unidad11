import os
import sys
import unittest
sys.path.append("")
import functions.functions as f

from pathlib import Path
from docs_from_tests.instrument_call_hierarchy import (
    instrument_and_import_package,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)

instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(),"..","functions"),"functions")

class Test1(unittest.TestCase):
    
    def test_suma_positivos(self):
        self.assertEqual(f.sumar(1, 2, 3, 4, 5), 15)

        initialise_call_hierarchy("start")

        root_call = finalise_call_hierarchy()
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__),"..","docs","diagramadesecuencia.md")
        print(sequence_diagram_filename)
        Path(sequence_diagram_filename).write_text(sequence_diagram)



if __name__ == '__main__':
    unittest.main()









'''
import sys
import os
from typing import Type
import unittest

class Pruebasf(unittest.TestCase):


    def test_suma_negativos(self):
        self.assertEqual(f.sumar(-1, -2, -3, -4, -5), -15)
        self.assertEqual(f.sumar(1, 2, 3, -4, -5), -3)

    def test_resta_positivos(self):
        self.assertEqual(f.restar(100, 1, 2, 3, 4, 5), 85)

    def test_resta_negativos(self):
        self.assertEqual(f.restar(100, -1, -2, -3, -4, -5), 115)
        self.assertEqual(f.restar(100, -100, -2, -3, -4, -5), -14)

    def test_producto_positivos(self):
        self.assertEqual(f.multiplicar(2, 3, 4), 24)

    def test_producto_negativos(self):
        self.assertEqual(f.multiplicar(-2, -3, -4), -24)
        self.assertEqual(f.multiplicar(-1, -2, -3, -4), 24)

    def test_division_positivos(self):
        self.assertEqual(f.dividir(100, 2, 2), 25)
        self.assertEqual(f.dividir(2, 2, 2), 0.5)

    def test_division_negativos(self):
        self.assertEqual(f.dividir(100, -2, 2), -25)
        self.assertEqual(f.dividir(-2, 2), -1)
        self.assertEqual(f.dividir(-2, 4), -0.5)
        self.assertEqual(f.dividir(-2, -4), 0.5)

    def test_division_cero(self):
        with self.assertRaises(ZeroDivisionError):
            f.dividir(100, 2, 0, 3)

    def test_valores_no_numericos(self):
        with self.assertRaises(TypeError):
            f.sumar(1, 2, "3")
        with self.assertRaises(TypeError):
            f.restar(1, 2, "3")
        with self.assertRaises(TypeError):
            f.multiplicar(1, 2, "3")
        with self.assertRaises(TypeError):
            f.dividir(1, 2, "3")


if __name__ == '__main__':
    unittest.main()



'''



