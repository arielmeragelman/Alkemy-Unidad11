import os
import sys
import unittest
sys.path.append("..")
import functions.functions as f

from pathlib import Path
from docs_from_tests.instrument_call_hierarchy import (
    instrument_and_import_package,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)

instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), "..", "functions"),"functions")


class Test1(unittest.TestCase):
    
    def test_suma_positivos(self):
        initialise_call_hierarchy("start")
        self.assertEqual(f.sumar(1, 2, 3, 4, 5), 15)
        self.assertEqual(f.sumar(1, 2, 3, 4, 5), 15)
        

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
