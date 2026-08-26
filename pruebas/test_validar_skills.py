import unittest
from pathlib import Path
from herramientas.validar_skills import validar_skill_md, ERRORES, RAIZ


class TestValidarSkills(unittest.TestCase):
    def setUp(self):
        ERRORES.clear()

    def test_todas_las_skills_tienen_frontmatter_valido(self):
        archivos_skill = list(RAIZ.glob(".agents/skills/**/SKILL.md")) + list(RAIZ.glob(".claude/skills/**/SKILL.md"))
        self.assertGreater(len(archivos_skill), 0, "No se encontraron skills para validar")
        for skill in archivos_skill:
            validar_skill_md(skill)
        self.assertEqual(len(ERRORES), 0, f"Errores en validación de skills: {ERRORES}")


if __name__ == "__main__":
    unittest.main()
