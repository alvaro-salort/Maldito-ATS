---
framework_version: 1.0.0
---

# Guía de Agentes: Maldito ATS (Búsqueda Laboral con IA)

Este repositorio está estructurado para gestionar de punta a punta la búsqueda laboral: prospección y scraping de vacantes en portales de Argentina y Latinoamérica, evaluación de compatibilidad, adaptación de CVs de alto impacto (fórmula XYZ), redacción de cartas de presentación personalizadas, optimización de perfiles de LinkedIn, preparación para entrevistas y análisis salarial bimonetario (ARS/USD).

## Diseño de Fuente Única de Verdad (Single Source of Truth)

Para evitar duplicación y discrepancias entre diferentes entornos de agentes de IA (**OpenCode**, **Antigravity**, **Cursor**, **Codex**, **Aider**, **Claude Code**, **Gemini CLI**, **Ollama/DeepSeek**), este espacio de trabajo utiliza un diseño unificado y agnóstico:

1. **Perfil del Candidato:**
   - El perfil profesional, datos de contacto, educación, stack tecnológico, expectativas salariales (ARS/USD) y preferencias de modalidad (Relación de Dependencia / Contractor / Monotributo / Remoto) se definen en [CLAUDE.md](CLAUDE.md) / [OPENCODE.md](OPENCODE.md) y en los módulos de [.claude/skills/asistente-postulaciones/](.claude/skills/asistente-postulaciones/) (especialmente `01-perfil-candidato.md`).
2. **Especificaciones de Flujo y Comandos:**
   - Los comandos y flujos (`/configuracion`, `/postular`, `/evaluar`, `/entrevista`, `/linkedin`, `/mensajes`, `/comparar-ofertas`, `/resultado`, `/reporte`) están definidos en [.opencode/commands/](.opencode/commands/) y [.claude/commands/](.claude/commands/).
3. **Skills de Búsqueda y Optimización:**
   - Las herramientas de búsqueda de empleo y optimización residen en [.agents/skills/](.agents/skills/) bajo el estándar portable de Agent Skills (`SKILL.md` por herramienta):
     - `busqueda-linkedin`: Búsqueda en LinkedIn Jobs para Argentina, LATAM y remoto.
     - `busqueda-bumeran`: Búsqueda en Bumeran y Zonajobs (Argentina).
     - `busqueda-computrabajo`: Búsqueda en Computrabajo Argentina.
     - `busqueda-getonbrd`: Búsqueda en Get on Board (Tech LATAM).
     - `busqueda-remota`: Agregadores de empleo remoto global con pago en USD.
     - `redactor-vinietas`: Transformación de bullets con la fórmula Google XYZ (Logro + Métrica + Acción).
     - `optimizador-linkedin`: Optimización de titulares y sección Acerca de.
     - `mensajes-networking`: Plantillas de cold outreach y seguimiento.
     - `comparador-ofertas`: Análisis multidimensional de ofertas laborales.
