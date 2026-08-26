#!/usr/bin/env python3
"""
Herramienta de Consulta de Salarios (Maldito ATS - Edición Argentina y LATAM)

Consulta benchmarks y rangos salariales por empresa o puesto a partir de datasets locales
(como la Encuesta de Sueldos de Sysarmy / Openqube, reportes de Glassdoor, etc.).

Uso:
    python herramientas/consulta_salarios.py "Nombre de Empresa"
    python herramientas/consulta_salarios.py "Nombre de Empresa" --ciudad "Buenos Aires"
    python herramientas/consulta_salarios.py "Nombre de Empresa" --json
    python herramientas/consulta_salarios.py --listar-todas
"""

import json
import sys
import re
import argparse
import unicodedata
from pathlib import Path

ARCHIVO_DATOS = Path(__file__).parent / "datos_salarios.json"

# Sufijos societarios y términos corporativos frecuentes en Argentina y LATAM para normalizar búsquedas
PATRONES_LIMPIEZA = [
    r"\bs\.a\.?\b", r"\bs\.r\.l\.?\b", r"\bs\.a\.s\.?\b", r"\bs\.a\.i\.c\.?\b",
    r"\bs\.a\.u\.?\b", r"\bs\.c\.p\.a\.?\b", r"\bsrl\b", r"\bsa\b", r"\bsas\b",
    r"\bargentina\b", r"\blatam\b", r"\bsur\b", r"\bservicios\b",
    r"\bgroup\b", r"\bholding\b", r"\btechnologies\b", r"\btech\b",
    r"\(.*?\)",
    r",\s*.*$",
]


def normalizar_texto(texto: str) -> str:
    """Normaliza texto eliminando tildes y caracteres especiales."""
    if not texto:
        return ""
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFKD", texto).encode("ASCII", "ignore").decode("utf-8")
    for patron in PATRONES_LIMPIEZA:
        texto = re.sub(patron, " ", texto, flags=re.IGNORECASE)
    return " ".join(texto.split())


def cargar_datos(ruta_archivo: Path = ARCHIVO_DATOS):
    """Carga y valida el archivo de datos salariales JSON."""
    if not ruta_archivo.exists():
        # Retorna estructura vacía orientativa si no existe
        return {"empresas": {}, "fuente": "Sysarmy / Openqube / Glassdoor"}
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al leer {ruta_archivo}: {e}", file=sys.stderr)
        sys.exit(1)


def buscar_empresa(nombre_busqueda: str, datos: dict, ciudad: str = None):
    """Busca coincidencias de salarios para una empresa."""
    clave_busqueda = normalizar_texto(nombre_busqueda)
    resultados = []
    
    empresas = datos.get("empresas", {})
    for nombre_original, info in empresas.items():
        clave_empresa = normalizar_texto(nombre_original)
        if clave_busqueda in clave_empresa or clave_empresa in clave_busqueda:
            res = {"empresa": nombre_original, "datos": info}
            if ciudad:
                # Filtrar por ciudad si los datos contienen desglose geográfico
                if "ciudades" in info and ciudad.lower() in [c.lower() for c in info["ciudades"]]:
                    res["filtro_ciudad"] = ciudad
            resultados.append(res)
            
    return resultados


def main():
    parser = argparse.ArgumentParser(description="Consulta de Salarios y Benchmarks - Maldito ATS")
    parser.add_argument("empresa", nargs="?", help="Nombre de la empresa a consultar")
    parser.add_argument("--ciudad", help="Filtrar por ciudad o provincia (ej. Buenos Aires, Córdoba)")
    parser.add_argument("--json", action="store_true", help="Emitir salida en formato JSON")
    parser.add_argument("--listar-todas", action="store_true", help="Listar todas las empresas con datos disponibles")
    parser.add_argument("--archivo-datos", type=Path, default=ARCHIVO_DATOS, help="Ruta al archivo JSON de salarios")

    args = parser.parse_args()
    datos = cargar_datos(args.archivo_datos)

    if args.listar_todas:
        empresas = list(datos.get("empresas", {}).keys())
        if args.json:
            print(json.dumps({"empresas": empresas}, ensure_ascii=False, indent=2))
        else:
            print(f"Total de empresas registradas: {len(empresas)}")
            for emp in sorted(empresas):
                print(f"- {emp}")
        return

    if not args.empresa:
        parser.print_help()
        sys.exit(1)

    coincidencias = buscar_empresa(args.empresa, datos, args.ciudad)

    if args.json:
        print(json.dumps({"consulta": args.empresa, "resultados": coincidencias}, ensure_ascii=False, indent=2))
    else:
        if not coincidencias:
            print(f"No se encontraron datos salariales registrados para '{args.empresa}'.")
            print("Tip: Podés consultar la encuesta de Sysarmy o Glassdoor e importar los datos con convertir_excel_salarios.py.")
        else:
            print(f"=== Resultados de Salarios para '{args.empresa}' ===")
            for item in coincidencias:
                print(f"\nEmpresa: {item['empresa']}")
                detalles = item["datos"]
                for rol, info_rol in detalles.get("roles", {}).items():
                    print(f"  * Puesto: {rol}")
                    if isinstance(info_rol, dict):
                        for k, v in info_rol.items():
                            print(f"    - {k}: {v}")
                    else:
                        print(f"    - Salario estimado: {info_rol}")


if __name__ == "__main__":
    main()
