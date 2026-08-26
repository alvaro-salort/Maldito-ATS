# Historial de Cambios - Maldito ATS

Todos los cambios notables de este proyecto se documentan en este archivo.

El formato sigue los lineamientos de [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [1.0.0] - 2026-08-26

###  Lanzamiento Inicial de Maldito ATS
Framework integral de búsqueda laboral asistida por IA diseñado específicamente para el mercado de **Argentina y Latinoamérica**.

####  Compatibilidad Multi-Agente Libre y Agnóstica
- Soporte nativo para **OpenCode** (`OPENCODE.md`), **Antigravity**, **Cursor**, **Claude Code** (`AGENTS.md`, `CLAUDE.md`) y modelos de lenguaje locales/económicos (**DeepSeek-V3 / R1**, **Gemini Flash**, **Ollama**).
- Cero dependencia obligatoria de APIs o suscripciones de pago.

####  Metodologías de ResumeSkills Integradas
- **Redactor de Viñetas (Fórmula Google XYZ)**: Transformación de tareas pasivas en declaraciones de impacto cuantitativo (*"Logré [X], medido por [Y], haciendo [Z]"*).
- **Optimizador de LinkedIn**: Generación de titulares estratégicos con palabras clave y sección *Acerca de* para reclutadores de LATAM.
- **Plantillas de Networking y Cold Outreach**: Mensajes directos para LinkedIn, notas post-postulación y correos de agradecimiento/seguimiento (*follow-up*).
- **Comparador Multidimensional de Ofertas**: Análisis comparativo de compensación bimonetaria (ARS vs USD), aguinaldo (SAC), prepaga (OSDE, Swiss Medical), paritarias y días de vacaciones.
- **Gestión de Versiones de CV**: Estructura de CV Maestro (`cv/cv_maestro.md`) para compilar versiones adaptadas a cada vacante.

####  Portales de Empleo de Argentina y LATAM
- **`busqueda-bumeran`**: Scraper y buscador para Bumeran y Zonajobs (Grupo Jobint / Navent).
- **`busqueda-computrabajo`**: Búsqueda por provincia y categoría en Computrabajo Argentina.
- **`busqueda-getonbrd`**: Integración con Get on Board para empleos tech en LATAM con salarios transparentes.
- **`busqueda-linkedin`**: Búsqueda en LinkedIn Jobs con filtros para Argentina, LATAM y remoto.
- **`busqueda-remota`**: Agregadores de empleo internacional con pago en USD (Contractor / Monotributo Tech).

####  Comandos del Asistente (en `.opencode/commands/` y `.claude/commands/`)
- `/configuracion`: Asistente de onboarding y lectura de documentos.
- `/postular`: Evaluación de vacante, cálculo de match, generación de CV y carta LaTeX.
- `/evaluar`: Clasificación y ranking automático de ofertas encontradas.
- `/entrevista`: Simulador de entrevistas con método STAR y negociación salarial.
- `/linkedin`: Auditoría y optimización del perfil de LinkedIn.
- `/mensajes`: Generador de mensajes directos para recruiters y líderes técnicos.
- `/comparar-ofertas`: Comparador de propuestas laborales y beneficios.
- `/resultado`: Registro y seguimiento en `registro_postulaciones.csv`.
- `/reporte`: Dashboard visual interactivo en HTML (`reporte-html.md`).
- `/agregar-portal`, `/agregar-plantilla`, `/sincronizar-gmail`, `/sincronizar-notion`, `/expandir`, `/reiniciar`.

####  Herramientas en Python (`herramientas/`)
- `consulta_salarios.py` y `convertir_excel_salarios.py`: Consulta salarial basada en la encuesta de **Sysarmy (Openqube)**, Glassdoor y normalización de sociedades argentinas (`S.A.`, `S.R.L.`, `S.A.S.`, `S.A.I.C.`).
- `comparar_ofertas.py`: Calculadora de paquete anualizado y beneficios.
- `verificar_pdf.py`: Validador de extracción de texto y compatibilidad con parsers ATS.
- `guardas_seguridad.py`: Protección y prevención de fugas de datos personales en `.gitignore`.
- `validar_skills.py`: Linter de sintaxis YAML para skills portables.
- `verificar_robots.py`: Verificación de políticas de robots.txt para scraping ético.
- `control_versiones.py`: Verificador de versiones del framework.

####  Plantillas LaTeX en Español
- `cv/cv_ejemplo.tex`: Plantilla de CV moderna de 1-2 páginas para ATS (compilable con LuaLaTeX/XeLaTeX).
- `cartas_presentacion/carta.cls` y `cartas_presentacion/carta_ejemplo.tex`: Clase LaTeX y modelo de carta de presentación persuasiva de 1 página.

####  Suite de Pruebas Automatizadas (`pruebas/`)
- Tests unitarios en Python para validar seguridad, motor salarial, comparador de ofertas, linter de skills, legibilidad de PDFs ATS y estructura de directorios.
