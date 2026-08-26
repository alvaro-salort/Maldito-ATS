import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


class TestEstructuraArchivos(unittest.TestCase):
    def test_archivos_raiz_principales(self):
        archivos_esperados = [
            "README.md",
            "INICIO_RAPIDO.md",
            "HISTORIAL_CAMBIOS.md",
            "OPENCODE.md",
            "AGENTS.md",
            "CLAUDE.md",
            ".gitignore",
        ]
        for archivo in archivos_esperados:
            self.assertTrue((RAIZ / archivo).exists(), f"Falta el archivo principal {archivo}")

    def test_directorios_en_espanol(self):
        directorios_esperados = [
            "cv",
            "cartas_presentacion",
            "plantillas",
            "herramientas",
            "documentos",
            "buscador_empleos",
            "investigacion_empresas",
            "capacitacion",
            "pruebas",
            ".agents/skills",
            ".opencode/commands",
            ".claude/commands",
            ".claude/skills",
        ]
        for directorio in directorios_esperados:
            self.assertTrue((RAIZ / directorio).is_dir(), f"Falta el directorio {directorio}")

    def test_skills_regionales_existen(self):
        skills_esperadas = [
            "busqueda-linkedin",
            "busqueda-bumeran",
            "busqueda-computrabajo",
            "busqueda-getonbrd",
            "busqueda-remota",
            "redactor-vinietas",
            "optimizador-linkedin",
            "mensajes-networking",
            "comparador-ofertas",
        ]
        for skill in skills_esperadas:
            ruta_skill = RAIZ / ".agents" / "skills" / skill / "SKILL.md"
            self.assertTrue(ruta_skill.exists(), f"Falta la skill {skill}")


if __name__ == "__main__":
    unittest.main()
