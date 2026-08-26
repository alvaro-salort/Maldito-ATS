#!/usr/bin/env python3
"""
Conversor de Datasets Salariales (Excel/CSV a JSON) - Maldito ATS

Convierte planillas de sueldos (ej. export de la Encuesta Sysarmy / Openqube)
en el formato `datos_salarios.json` utilizado por `consulta_salarios.py`.

Uso:
    python herramientas/convertir_excel_salarios.py archivo_sueldos.xlsx --salida herramientas/datos_salarios.json
"""

import json
import sys
import argparse
from pathlib import Path


def procesar_csv_o_excel(ruta_archivo: Path) -> dict:
    """Lee y estructura los datos salariales desde un archivo."""
    datos_resultado = {
        "fuente": ruta_archivo.name,
        "empresas": {}
    }
    
    # Procesar archivo CSV
    if ruta_archivo.suffix.lower() == ".csv":
        import csv
        with open(ruta_archivo, mode="r", encoding="utf-8", errors="ignore") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                empresa = fila.get("empresa") or fila.get("Company") or fila.get("Empresa") or "General"
                rol = fila.get("puesto") or fila.get("Role") or fila.get("Puesto") or fila.get("Seniority") or "General"
                salario = fila.get("salario") or fila.get("sueldo_neto") or fila.get("Salary") or "0"
                
                if empresa not in datos_resultado["empresas"]:
                    datos_resultado["empresas"][empresa] = {"roles": {}}
                datos_resultado["empresas"][empresa]["roles"][rol] = salario

    return datos_resultado


def main():
    parser = argparse.ArgumentParser(description="Conversor de datos salariales a JSON - Maldito ATS")
    parser.add_argument("entrada", type=Path, help="Archivo CSV o Excel de origen")
    parser.add_argument("--salida", type=Path, default=Path(__file__).parent / "datos_salarios.json", help="Ruta de salida JSON")

    args = parser.parse_args()
    if not args.entrada.exists():
        print(f"Error: El archivo {args.entrada} no existe.", file=sys.stderr)
        sys.exit(1)

    resultado = procesar_csv_o_excel(args.entrada)
    with open(args.salida, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    print(f"✅ Datos salariales convertidos exitosamente en: {args.salida}")


if __name__ == "__main__":
    main()
