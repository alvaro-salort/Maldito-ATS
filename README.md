<div align="center">

<pre>
   *                                            (     
 (  `        (  (          )        (      *   ))\ )  
 )\))(     ) )\ )\ ) (  ( /(        )\   ` )  /(()/(  
((_)()\ ( /(((_|()/( )\ )\())(   ((((_)(  ( )(_))(_)) 
(_()((_))(_))_  ((_)|(_|_))/ )\   )\ _ )\(_(_()|_))   
|  \/  ((_)_| | _| | (_) |_ ((_)  (_)_\(_)_   _/ __|  
| |\/| / _` | / _` | | |  _/ _ \   / _ \   | | \__ \  
|_|  |_\__,_|_\__,_| |_|\__\___/  /_/ \_\  |_| |___/  
                                                      
</pre>

### El framework de búsqueda laboral con Inteligencia Artificial para Argentina y Latinoamérica

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-brightgreen.svg)](https://www.python.org/)
[![OpenCode Ready](https://img.shields.io/badge/OpenCode-Compatible-orange.svg)](OPENCODE.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](https://github.com/alvaro-salort/Maldito-ATS/pulls)

*Multi-agente, 100% en español, compatible con OpenCode, Antigravity, Cursor, Claude Code y modelos abiertos (DeepSeek, Gemini, Ollama).*

</div>

---

## ¿Qué es Maldito ATS?

**Maldito ATS** es una plataforma de código abierto que convierte a tu asistente de IA en tu propio mentor de carrera y equipo de reclutamiento personal.

Diseñado específicamente para las particularidades del mercado laboral de **Latinoamérica y Argentina** (esquema bimonetario ARS/USD, inflación, modalidades de contratación, filtros ATS estrictos y alta competencia):

- **Prospección de ofertas reales**: Búsqueda estructurada en LinkedIn Jobs, Bumeran, Zonajobs, Computrabajo, Get on Board y agregadores de empleo remoto en USD.
- **Evaluación de compatibilidad (Fit Scoring)**: Análisis objetivo de tus habilidades y expectativas contra los requisitos excluyentes de la vacante.
- **Confección de CVs ATS (Fórmula Google XYZ)**: Transformación de listas pasivas de tareas en viñetas de alto impacto (*"Logré [X], medido por [Y], haciendo [Z]"*).
- **Cartas de presentación y mensajes directos**: Redacción a medida y plantillas de *cold outreach* para conectar con reclutadores y líderes de equipo.
- **Optimización de perfil de LinkedIn**: Mejora de titulares con palabras clave y sección *Acerca de* orientada a búsquedas de RRHH en LATAM.
- **Preparación de entrevistas y negociación**: Simulador con método STAR y análisis de compensación total (bruto, neto, Ganancias, prepagas, paritarias y pagos en USD).

---

## Comandos del Asistente

Puedes interactuar con el asistente escribiendo los siguientes comandos en tu chat (**OpenCode**, **Antigravity**, **Cursor**, **Claude**):

| Comando | Acción |
|---|---|
| `/configuracion` | Configura tu perfil profesional leyendo tus documentos o respondiendo preguntas guiadas. |
| `/postular` | Analiza una oferta, calcula compatibilidad, redacta tu CV en LaTeX y la carta de presentación. |
| `/evaluar` | Clasifica y prioriza automáticamente las ofertas encontradas. |
| `/entrevista` | Simula una entrevista técnica/conductual y prepara respuestas sobre negociación salarial. |
| `/linkedin` | Audita y genera mejoras de palabras clave para tu perfil de LinkedIn. |
| `/mensajes` | Genera mensajes de contacto para reclutadores y correos de seguimiento post-entrevista. |
| `/comparar-ofertas` | Compara múltiples propuestas analizando sueldo, moneda, beneficios e inflación. |
| `/resultado` | Registra el avance de tus postulaciones en tu planilla local (`registro_postulaciones.csv`). |
| `/reporte` | Genera un reporte interactivo en HTML con el progreso de tu búsqueda. |

> [!TIP]
> Los comandos funcionan de forma idéntica en entornos locales y gratuitos con OpenCode o modelos servidos por Ollama/DeepSeek. Consulta [OPENCODE.md](OPENCODE.md) para más detalles.

---

## Estructura del Repositorio

```
MalditoATS/
├── .agents/skills/          # Herramientas portables de búsqueda y optimización (LinkedIn, Bumeran, GetOnBrd, XYZ)
├── .opencode/commands/      # Comandos para OpenCode
├── .claude/commands/        # Comandos para Claude Code
├── cv/                      # CV maestro y plantillas LaTeX optimizadas para ATS
├── cartas_presentacion/     # Clase y plantillas de cartas de presentación
├── plantillas/              # Modelos de cold outreach, mensajes de LinkedIn y follow-ups
├── documentos/              # Carpeta personal para colocar CVs, títulos y notas
├── buscador_empleos/        # Base de datos local de ofertas encontradas y vistas
├── investigacion_empresas/  # Fichas técnicas y análisis de empresas
├── capacitacion/            # Planes de estudio intensivos para cubrir brechas técnicas
├── herramientas/            # Scripts en Python (salarios Sysarmy/ARS/USD, validación ATS, seguridad)
└── pruebas/                 # Suite de pruebas automatizadas
```

---

## Guía de Inicio Rápido

Consulta la guía detallada paso a paso en [INICIO_RAPIDO.md](INICIO_RAPIDO.md).

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/alvaro-salort/Maldito-ATS.git
   cd Maldito-ATS
   ```

2. **Instalar dependencias auxiliares:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Cargar tus documentos:**
   Coloca tu CV actual o export de LinkedIn en `documentos/cv/`.

4. **Iniciar la configuración:**
   En tu asistente de IA escribe:
   ```text
   /configuracion
   ```

> [!IMPORTANT]
> No necesitas tener compiladores de LaTeX instalados para utilizar el framework; el asistente puede generar el código `.tex` o `.md` listo para compilar en Overleaf sin costo.

---

## Privacidad y Seguridad

> [!WARNING]
> Nunca subas datos personales reales (teléfono, dirección, DNI o CVs generados) a un repositorio público en GitHub.

- Tus datos personales, registros de postulaciones (`registro_postulaciones.csv`) y CVs generados están preconfigurados en `.gitignore` para no ser rastreados por Git.
- Puedes verificar la integridad de las reglas de seguridad en cualquier momento ejecutando:
  ```bash
  python herramientas/guardas_seguridad.py
  ```

> [!NOTE]
> Todos los datos procesados durante las postulaciones se mantienen estrictamente locales en tu máquina.

---

## 💖 Agradecimientos y Créditos

Este proyecto se inspiró y apoya en el trabajo de la comunidad open source:

- **[Mads Lorentzen / ai-job-search](https://github.com/MadsLorentzen/ai-job-search)**: Por la idea original y la arquitectura base de flujos de postulación asistidos por IA.
- **[Param Choudhary / ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)**: Por las metodologías de redacción de viñetas con la fórmula Google XYZ, optimización de CVs técnicos y estrategias de networking.

---

## Licencia

Distribuido bajo la Licencia MIT. Consulta [LICENSE](LICENSE) para más detalles.
