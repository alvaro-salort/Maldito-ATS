import unittest
from herramientas.consulta_salarios import normalizar_texto, buscar_empresa


class TestConsultaSalarios(unittest.TestCase):
    def test_normalizacion_sufijos_societarios_argentinos(self):
        self.assertEqual(normalizar_texto("MercadoLibre S.R.L."), "mercadolibre")
        self.assertEqual(normalizar_texto("Globant S.A."), "globant")
        self.assertEqual(normalizar_texto("Ualá (Tech Argentina)"), "uala")
        self.assertEqual(normalizar_texto("Despegar.com S.A.S."), "despegar.com")

    def test_busqueda_empresa(self):
        datos_mock = {
            "empresas": {
                "MercadoLibre S.R.L.": {
                    "roles": {
                        "Senior Software Engineer": "ARS 4.500.000 Bruto",
                        "Tech Lead": "ARS 6.200.000 Bruto"
                    }
                },
                "Globant S.A.": {
                    "roles": {
                        "Backend Developer SSr": "ARS 3.200.000 Bruto"
                    }
                }
            }
        }
        
        resultados = buscar_empresa("MercadoLibre", datos_mock)
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]["empresa"], "MercadoLibre S.R.L.")
        self.assertIn("Senior Software Engineer", resultados[0]["datos"]["roles"])


if __name__ == "__main__":
    unittest.main()
