#!/usr/bin/env python3
"""
Validador de PDF y Capa de Texto ATS - Maldito ATS

Verifica que el PDF del CV o Carta de Presentación generado por LaTeX contenga
una capa de texto limpia, legible por sistemas ATS (Workday, Greenhouse, Lever, etc.).

Uso:
    python herramientas/verificar_pdf.py cv/cv_ejemplo.pdf
    python herramientas/verificar_pdf.py cv/cv_ejemplo.pdf --volcar-texto cv/cv_ejemplo.txt
"""

import sys
import argparse
from pathlib import Path


def extraer_texto_pdf(ruta_pdf: Path) -> str:
    """Extrae texto del PDF utilizando pypdf o pdftotext."""
    if not ruta_pdf.exists():
        print(f"Error: El archivo PDF {ruta_pdf} no existe.", file=sys.stderr)
        sys.exit(1)

    texto = ""
    # Intentar con pypdf primero
    try:
        from pypdf import PdfReader
        lector = PdfReader(str(ruta_pdf))
        for pagina in lector.pages:
            t = pagina.extract_text()
            if t:
                texto += t + "\n"
    except ImportError:
        pass

    # Si pypdf no está o dio vacío, intentar comando pdftotext
    if not texto.strip():
        import subprocess
        try:
            res = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(ruta_pdf), "-"], capture_output=True, text=True, check=True)
            texto = res.stdout
        except Exception:
            pass

    return texto


def validar_capa_texto(texto: str) -> list[str]:
    """Valida la calidad del texto extraído para ATS."""
    alertas = []
    if not texto.strip():
        alertas.append("FALLO CRÍTICO: No se pudo extraer texto del PDF (el archivo podría ser una imagen escaneada o no tener capa de texto).")
        return alertas

    if "(cid:" in texto:
        alertas.append("ADVERTENCIA: Se detectaron caracteres no mapeados (cid:*), posibles fuentes LaTeX incompatibles.")
    if "" in texto:
        alertas.append("ADVERTENCIA: Se detectaron caracteres de reemplazo unicode ().")
    
    lineas = [l.strip() for l in texto.splitlines() if l.strip()]
    if len(lineas) < 10:
        alertas.append("ADVERTENCIA: El texto extraído tiene muy pocas líneas (< 10). Verifique el contenido del documento.")

    return alertas


def main():
    parser = argparse.ArgumentParser(description="Verificador de PDF para ATS - Maldito ATS")
    parser.add_argument("pdf", type=Path, help="Ruta al archivo PDF a verificar")
    parser.add_argument("--volcar-texto", type=Path, help="Guardar el texto extraído en un archivo de texto plano")

    args = parser.parse_args()
    texto = extraer_texto_pdf(args.pdf)
    alertas = validar_capa_texto(texto)

    if args.volcar-texto:
        with open(args.volcar_texto, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"Texto extraído guardado en: {args.volcar_texto}")

    print(f"=== Reporte de Verificación ATS para '{args.pdf.name}' ===")
    if alertas:
        for a in alertas:
            print(f"⚠️ {a}")
        sys.exit(1)
    else:
        print("✅ La capa de texto del PDF es limpia y totalmente legible por sistemas ATS.")
        print(f"Total de caracteres extraídos: {len(texto)}")


if __name__ == "__main__":
    main()
