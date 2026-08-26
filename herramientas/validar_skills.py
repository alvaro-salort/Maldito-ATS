#!/usr/bin/env python3
"""
Validador de Skills y Comandos (Linter) - Maldito ATS

Verifica que todos los archivos SKILL.md y comandos .md contengan
frontmatter YAML válido y sigan el estándar portable de Agent Skills.

Uso:
    python herramientas/validar_skills.py
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ERRORES: list[str] = []


def validar_skill_md(ruta_archivo: Path):
    """Valida la estructura y frontmatter de un SKILL.md."""
    contenido = ruta_archivo.read_text(encoding="utf-8")
    if not contenido.startswith("---"):
        ERRORES.append(f"{ruta_archivo.relative_to(RAIZ)}: No comienza con frontmatter YAML (---)")
        return
    partes = contenido.split("---", 2)
    if len(partes) < 3:
        ERRORES.append(f"{ruta_archivo.relative_to(RAIZ)}: Frontmatter YAML incompleto o mal cerrado")
        return
    frontmatter = partes[1]
    if "name:" not in frontmatter:
        ERRORES.append(f"{ruta_archivo.relative_to(RAIZ)}: Falta el campo obligatorio 'name:' en frontmatter")
    if "description:" not in frontmatter:
        ERRORES.append(f"{ruta_archivo.relative_to(RAIZ)}: Falta el campo obligatorio 'description:' en frontmatter")


def main():
    archivos_skill = list(RAIZ.glob(".agents/skills/**/SKILL.md")) + list(RAIZ.glob(".claude/skills/**/SKILL.md"))
    if not archivos_skill:
        print("Advertencia: No se encontraron archivos SKILL.md")
        sys.exit(0)

    for skill in archivos_skill:
        validar_skill_md(skill)

    if ERRORES:
        print("❌ Errores detectados en la validación de Skills:", file=sys.stderr)
        for err in ERRORES:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"✅ Se validaron {len(archivos_skill)} archivos SKILL.md exitosamente.")


if __name__ == "__main__":
    main()
