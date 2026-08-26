---
name: buscador-empleos
description: >
  Busca ofertas de empleo activas en LinkedIn Jobs, Bumeran, Zonajobs, Computrabajo,
  Get on Board y portales remotos en USD. Deduplica vacantes y genera reportes de compatibilidad.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(bun run .agents/skills/*/cli/src/cli.ts *), WebFetch, WebSearch, AskUserQuestion
---

# Buscador de Empleos (Job Scraper LATAM & Argentina)

Esta habilidad coordina la búsqueda de ofertas en portales de empleo mediante herramientas CLI instaladas en `.agents/skills/` y búsqueda web alternativa.

## Pasos de Ejecución

### Paso 0: Carga de Estado
1. Leer `buscador_empleos/empleos_vistos.json` (crear si no existe con `{"vistos": {}}`).
2. Leer `registro_postulaciones.csv` para ignorar empresas y roles a los que ya te postulaste.
3. Leer `consultas-busqueda.md` para aplicar la estrategia de búsqueda por rol y prioridad.

### Paso 1: Búsqueda en Portales Habilitados
Ejecutar las skills de portales en `.agents/skills/`:
- `busqueda-linkedin`
- `busqueda-bumeran` (Bumeran y Zonajobs)
- `busqueda-computrabajo`
- `busqueda-getonbrd`
- `busqueda-remota`

### Paso 2: Deduplicación y Evaluación de Fit
1. Filtrar ofertas ya vistas o descartadas previamente.
2. Evaluar requisitos excluyentes (idioma, ubicación, modalidad).
3. Calcular puntuación estimada de compatibilidad (Fit Score 0-100).

### Paso 3: Presentación de Resultados
Presentar al usuario una tabla clara con:
- Puesto y Empresa.
- Ubicación y Modalidad (Remoto / Híbrido / Presencial).
- Rango salarial (si está publicado).
- Puntuación de Fit y Brechas detectadas.
- Enlace directo a la vacante.
