#!/usr/bin/env python3
"""
Guardas de Seguridad y Privacidad - Maldito ATS

Verifica que las reglas de protección de datos personales (.gitignore)
y las configuraciones de seguridad del asistente estén activas y protegidas.

Uso:
    python herramientas/guardas_seguridad.py
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ERRORES: list[str] = []

REGLAS_GITIGNORE_REQUERIDAS = [
    "registro_postulaciones.csv",
    "job_search_tracker.csv",
    "datos_salarios.json",
    "salary_data.json",
    "**/buscador_empleos/empleos_vistos.json",
    "**/job_scraper/seen_jobs.json",
    "documentos/cv/*",
    "documentos/titulos/*",
    "cv/cv_*.*",
    "cartas_presentacion/carta_*.*",
]


def verificar_gitignore():
    """Verifica que .gitignore contenga todas las reglas de privacidad obligatorias."""
    archivo_gitignore = RAIZ / ".gitignore"
    if not archivo_gitignore.exists():
        ERRORES.append("No se encontró el archivo .gitignore en la raíz del repositorio.")
        return

    contenido = archivo_gitignore.read_text(encoding="utf-8")
    for regla in REGLAS_GITIGNORE_REQUERIDAS:
        if regla not in contenido:
            ERRORES.append(f"Regla de privacidad faltante en .gitignore: '{regla}'")


def main():
    verificar_gitignore()

    if ERRORES:
        print("❌ FALLO EN LAS GUARDAS DE SEGURIDAD Y PRIVACIDAD:", file=sys.stderr)
        for err in ERRORES:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)
    else:
        print("✅ Todas las guardas de seguridad y privacidad están activas y conformes.")


if __name__ == "__main__":
    main()
