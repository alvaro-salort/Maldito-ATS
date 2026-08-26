import unittest
from herramientas.comparar_ofertas import calcular_compensacion_anual


class TestCompararOfertas(unittest.TestCase):
    def test_calculo_relacion_dependencia_con_aguinaldo(self):
        oferta = {
            "empresa": "Banco Local",
            "modalidad": "relacion_dependencia",
            "sueldo_mensual": 2000000,
            "moneda": "ARS",
            "bono_anual": 2000000,
            "prepaga_estimada_mensual": 150000
        }
        res = calcular_compensacion_anual(oferta, tipo_cambio_usd=1000.0)
        # 13 sueldos * 2M = 26M + 2M bono + 1.8M prepaga = 29.8M ARS
        self.assertEqual(res["total_anual_ars"], 29800000.0)
        self.assertEqual(res["total_anual_usd"], 29800.0)

    def test_calculo_contractor_usd(self):
        oferta = {
            "empresa": "Tech US",
            "modalidad": "contractor_usd",
            "sueldo_mensual": 4000,
            "moneda": "USD",
            "bono_anual": 0,
            "prepaga_estimada_mensual": 0
        }
        res = calcular_compensacion_anual(oferta, tipo_cambio_usd=1200.0)
        # 12 meses * $4000 = $48000 USD
        self.assertEqual(res["total_anual_usd"], 48000.0)
        self.assertEqual(res["total_anual_ars"], 48000.0 * 1200.0)


if __name__ == "__main__":
    unittest.main()
