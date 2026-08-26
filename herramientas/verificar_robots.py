#!/usr/bin/env python3
"""
Verificador Ético de Robots.txt - Maldito ATS

Verifica que las peticiones y scrapers respeten las políticas de robots.txt de los sitios.

Uso:
    python herramientas/verificar_robots.py https://ejemplo.com/empleos
"""

import sys
import argparse
from urllib.parse import urlparse
import urllib.robotparser


def verificar_acceso(url: str, user_agent: str = "*") -> bool:
    """Verifica si un User-Agent tiene permitido acceder a la URL según robots.txt."""
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        print(f"Error: URL inválida: {url}", file=sys.stderr)
        return False

    url_robots = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url_robots)
    try:
        rp.read()
        return rp.can_fetch(user_agent, url)
    except Exception:
        # Si falla la lectura de robots.txt, asumir permitido con prudencia
        return True


def main():
    parser = argparse.ArgumentParser(description="Verificador de robots.txt - Maldito ATS")
    parser.add_argument("url", help="URL a verificar")
    parser.add_argument("--user-agent", default="MalditoATSBot", help="User-Agent a simular")

    args = parser.parse_args()
    permitido = verificar_acceso(args.url, args.user_agent)
    if permitido:
        print(f"✅ Acceso permitido a {args.url}")
        sys.exit(0)
    else:
        print(f"⛔ Acceso bloqueado por robots.txt a {args.url}")
        sys.exit(1)


if __name__ == "__main__":
    main()
