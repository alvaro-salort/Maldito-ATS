import unittest
from herramientas.verificar_pdf import validar_capa_texto


class TestVerificarPdf(unittest.TestCase):
    def test_validacion_capa_texto_limpia(self):
        texto_limpio = "Martín González\nDesarrollador Backend Senior\nBuenos Aires, Argentina\n" + ("Experiencia laboral destacada\n" * 10)
        alertas = validar_capa_texto(texto_limpio)
        self.assertEqual(len(alertas), 0)

    def test_deteccion_texto_vacio(self):
        alertas = validar_capa_texto("")
        self.assertGreater(len(alertas), 0)
        self.assertIn("FALLO CRÍTICO", alertas[0])

    def test_deteccion_caracteres_cid_rotos(self):
        texto_roto = "Martín González (cid:123) Desarrollador" + ("\nlinea" * 15)
        alertas = validar_capa_texto(texto_roto)
        self.assertTrue(any("cid:" in a for a in alertas))


if __name__ == "__main__":
    unittest.main()
