#!/usr/bin/env python3
"""
Comparador Multidimensional de Ofertas Laborales - Maldito ATS

Compara propuestas laborales calculando compensación anualizada en ARS y USD,
beneficios (prepaga, bonos, SAC), impacto de inflación y modalidad contractual.

Uso:
    python herramientas/comparar_ofertas.py --oferta1 oferta_a.json --oferta2 oferta_b.json
"""

import json
import sys
import argparse
from pathlib import Path


def calcular_compensacion_anual(oferta: dict, tipo_cambio_usd: float = 1250.0) -> dict:
    """Calcula el paquete anualizado estimado de una oferta."""
    modalidad = oferta.get("modalidad", "relacion_dependencia")  # relacion_dependencia / contractor_usd / monotributo
    sueldo_mensual = float(oferta.get("sueldo_mensual", 0))
    moneda = oferta.get("moneda", "ARS").upper()
    bono_anual = float(oferta.get("bono_anual", 0))
    prepaga_valor_mensual = float(oferta.get("prepaga_estimada_mensual", 150000 if moneda == "ARS" else 120))
    
    # Cálculos según modalidad
    if modalidad == "relacion_dependencia":
        # En Argentina: 13 sueldos (12 meses + 1 SAC aguinaldo)
        meses_sueldo = 13.0
        sueldo_anual = sueldo_mensual * meses_sueldo
    else:
        # Contractor o Monotributo: habitualmente 12 facturas salvo acuerdo de vacaciones/bono
        meses_sueldo = float(oferta.get("meses_al_ano", 12))
        sueldo_anual = sueldo_mensual * meses_sueldo

    total_beneficios_anual = prepaga_valor_mensual * 12 + bono_anual
    total_anual_moneda_original = sueldo_anual + total_beneficios_anual

    # Conversión a ambas monedas para comparación directa
    if moneda == "USD":
        total_anual_usd = total_anual_moneda_original
        total_anual_ars = total_anual_usd * tipo_cambio_usd
    else:
        total_anual_ars = total_anual_moneda_original
        total_anual_usd = total_anual_ars / tipo_cambio_usd if tipo_cambio_usd > 0 else 0

    return {
        "empresa": oferta.get("empresa", "Empresa"),
        "modalidad": modalidad,
        "moneda_original": moneda,
        "sueldo_mensual": sueldo_mensual,
        "total_anual_ars": round(total_anual_ars, 2),
        "total_anual_usd": round(total_anual_usd, 2),
        "vacaciones_dias": oferta.get("vacaciones_dias", 14),
        "ajuste_inflacion": oferta.get("ajuste_inflacion", "No especificado"),
        "prepaga": oferta.get("prepaga", "Incluida"),
    }


def imprimir_comparativa(res1: dict, res2: dict):
    """Imprime una tabla comparativa clara en consola."""
    print("=" * 65)
    print(f"📊 COMPARATIVA DE OFERTAS: {res1['empresa']} vs {res2['empresa']}")
    print("=" * 65)
    print(f"{'Concepto':<25} | {res1['empresa']:<18} | {res2['empresa']:<18}")
    print("-" * 65)
    print(f"{'Modalidad':<25} | {res1['modalidad']:<18} | {res2['modalidad']:<18}")
    print(f"{'Sueldo Mensual':<25} | {res1['moneda_original']} {res1['sueldo_mensual']:<14} | {res2['moneda_original']} {res2['sueldo_mensual']:<14}")
    print(f"{'Total Anual (ARS est.)':<25} | ARS {res1['total_anual_ars']:<14,.0f} | ARS {res2['total_anual_ars']:<14,.0f}")
    print(f"{'Total Anual (USD est.)':<25} | USD {res1['total_anual_usd']:<14,.0f} | USD {res2['total_anual_usd']:<14,.0f}")
    print(f"{'Días de Vacaciones':<25} | {str(res1['vacaciones_dias']) + ' días':<18} | {str(res2['vacaciones_dias']) + ' días':<18}")
    print(f"{'Ajustes Inflación':<25} | {str(res1['ajuste_inflacion']):<18} | {str(res2['ajuste_inflacion']):<18}")
    print(f"{'Prepaga':<25} | {str(res1['prepaga']):<18} | {str(res2['prepaga']):<18}")
    print("=" * 65)


def main():
    parser = argparse.ArgumentParser(description="Comparador de Ofertas Laborales - Maldito ATS")
    parser.add_argument("--tipo-cambio", type=float, default=1250.0, help="Tipo de cambio USD/ARS orientativo")
    parser.add_argument("--json", action="store_true", help="Salida en JSON")

    # Ejemplo de demostración si se ejecuta sin argumentos
    ejemplo1 = {
        "empresa": "Fintech Local (Arg)",
        "modalidad": "relacion_dependencia",
        "sueldo_mensual": 3500000,
        "moneda": "ARS",
        "bono_anual": 3500000,
        "vacaciones_dias": 15,
        "ajuste_inflacion": "Trimestral IPC",
        "prepaga": "OSDE 310"
    }
    ejemplo2 = {
        "empresa": "Startup USA (Remote)",
        "modalidad": "contractor_usd",
        "sueldo_mensual": 4500,
        "moneda": "USD",
        "bono_anual": 2000,
        "vacaciones_dias": 20,
        "ajuste_inflacion": "Anual en USD",
        "prepaga": "Reintegro $150 USD"
    }

    r1 = calcular_compensacion_anual(ejemplo1)
    r2 = calcular_compensacion_anual(ejemplo2)

    imprimir_comparativa(r1, r2)


if __name__ == "__main__":
    main()
