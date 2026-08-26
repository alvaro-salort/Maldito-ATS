import unittest
from pathlib import Path
from herramientas.guardas_seguridad import verificar_gitignore, ERRORES, RAIZ


class TestGuardasSeguridad(unittest.TestCase):
    def setUp(self):
        ERRORES.clear()

    def test_gitignore_contiene_todas_las_reglas_obligatorias(self):
        verificar_gitignore()
        self.assertEqual(len(ERRORES), 0, f"Se encontraron fallos de seguridad: {ERRORES}")

    def test_archivos_sensibles_no_estan_en_el_arbol(self):
        # Asegurar que no se hayan commiteado datos personales reales
        self.assertFalse((RAIZ / "registro_postulaciones.csv").exists())
        self.assertFalse((RAIZ / "job_search_tracker.csv").exists())


if __name__ == "__main__":
    unittest.main()
