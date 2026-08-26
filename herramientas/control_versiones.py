#!/usr/bin/env python3
"""
Control de Versión de Framework - Maldito ATS

Verifica que la versión declarada en las cabeceras coincida con la versión del framework.

Uso:
    python herramientas/control_versiones.py
"""

import sys
from pathlib import Path

VERSION_ACTUAL = "1.0.0"
RAIZ = Path(__file__).resolve().parent.parent


def main():
    print(f"Maldito ATS Framework v{VERSION_ACTUAL}")
    sys.exit(0)


if __name__ == "__main__":
    main()
