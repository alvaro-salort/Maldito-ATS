import unittest
from herramientas.verificar_robots import verificar_acceso


class TestVerificarRobotsSeguridad(unittest.TestCase):
    def test_esquemas_inseguros_rechazados(self):
        """Verifica que esquemas de URL distintos a http/https sean rechazados por seguridad."""
        urls_inseguras = [
            "file:///etc/passwd",
            "ftp://servidor.com/archivo",
            "gopher://sitio.com",
            "javascript:alert(1)",
            "data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==",
            "///etc/passwd",
            "relative/path/file.txt",
        ]
        for url in urls_inseguras:
            with self.subTest(url=url):
                self.assertFalse(verificar_acceso(url), f"La URL insegura {url} debería ser rechazada")


if __name__ == "__main__":
    unittest.main()
