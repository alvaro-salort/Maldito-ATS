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

> **El framework de búsqueda laboral con Inteligencia Artificial diseñado para Argentina y Latinoamérica.**
> 
> *Multi-agente, 100% en español, compatible con OpenCode, Antigravity, Cursor, Claude Code y modelos libres/locales (DeepSeek, Gemini, Ollama).*

---

## 🌟 ¿Qué es Maldito ATS?

**Maldito ATS** es una plataforma de código abierto que convierte a tu asistente de IA en tu propio mentor de carrera y equipo de reclutamiento personal. 

Diseñado específicamente para las particularidades del mercado laboral de **Latinoamérica y Argentina** (esquema bimonetario ARS/USD, inflación, modalidades de contratación, filtros ATS estrictos y competencia alta), te ayuda a:

1. 🔍 **Prospectar ofertas reales**: Búsqueda en **LinkedIn**, **Bumeran / Zonajobs**, **Computrabajo**, **Get on Board** y portales de trabajo remoto en USD.
2. 🎯 **Evaluar la compatibilidad**: Puntuación automática de ofertas según tus habilidades, expectativas salariales y modalidad de trabajo.
3. 📄 **Generar CVs de alto impacto**: Confección en LaTeX/ATS utilizando la **Fórmula Google XYZ** (*"Logré X medido por Y haciendo Z"*).
4. ✉️ **Redactar cartas de presentación y mensajes**: Cartas personalizadas y plantillas de *cold outreach* para conectar con Recruiters en LinkedIn.
5. 💬 **Optimizar tu LinkedIn**: Mejora de titulares, biografía y palabras clave para posicionarte en búsquedas de RRHH.
6. 🤝 **Preparar entrevistas y negociar**: Simulador de entrevistas STAR y análisis de compensación total (bruto, neto, Ganancias, prepagas, bonos, paritarias y pagos en USD).

---

## 🚀 Comandos del Asistente

Puedes interactuar con el asistente a través de los siguientes comandos en tu chat (**OpenCode**, **Antigravity**, **Cursor**, **Claude**):

| Comando | Acción |
|---|---|
| `/configuracion` | Configura tu perfil profesional leyendo tus CVs/diplomas o respondiendo preguntas guiadas. |
| `/postular` | Pega el enlace o texto de una oferta para evaluarla, redactar el CV a medida y la carta. |
| `/evaluar` | Clasifica y prioriza automáticamente todas las ofertas encontradas. |
| `/entrevista` | Simula una entrevista para el puesto y prepara respuestas para preguntas difíciles. |
| `/linkedin` | Audita y genera mejoras para tu perfil, titular y resumen de LinkedIn. |
| `/mensajes` | Genera mensajes de contacto para reclutadores y notas de agradecimiento post-entrevista. |
| `/comparar-ofertas` | Compara múltiples propuestas laborales analizando sueldo, moneda, beneficios y proyección. |
| `/resultado` | Registra el avance de tus postulaciones en tu planilla de seguimiento (`registro_postulaciones.csv`). |
| `/reporte` | Genera un reporte interactivo en HTML con el progreso de tu búsqueda. |

---

## 📁 Estructura del Repositorio

```
MalditoATS/
├── .agents/skills/          # Skills portables de búsqueda y optimización (LinkedIn, Bumeran, GetOnBrd, XYZ)
├── .opencode/commands/      # Definición de comandos para OpenCode
├── .claude/commands/        # Definición de comandos para Claude Code
├── cv/                      # CV maestro y plantillas LaTeX optimizadas para ATS
├── cartas_presentacion/     # Plantilla y cartas de presentación personalizadas
├── plantillas/              # Plantillas de cold outreach, mensajes de LinkedIn y follow-ups
├── documentos/              # Carpeta para colocar tus CVs, certificados y notas
├── buscador_empleos/        # Estado de ofertas recopiladas y deduplicadas
├── investigacion_empresas/  # Fichas técnicas de empresas evaluadas
├── capacitacion/            # Planes para cubrir brechas técnicas de cara a entrevistas
├── herramientas/            # Scripts en Python (consulta de salarios Sysarmy/ARS/USD, ATS, seguridad)
└── pruebas/                 # Suite automatizada de tests
```

---

## ⚡ Guía de Inicio Rápido

Consulta nuestra guía completa en [INICIO_RAPIDO.md](INICIO_RAPIDO.md).

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/MalditoATS.git
   cd MalditoATS
   ```
2. Agrega tus documentos existentes (CV actual, diplomas o export de LinkedIn) en la carpeta `documentos/`.
3. Inicia tu asistente favorito (**OpenCode**, **Antigravity**, **Cursor** o **Claude Code**) y ejecuta:
   ```text
   /configuracion
   ```
4. ¡Listo! Ya puedes empezar a buscar empleo y postularte de forma personalizada con `/postular`.

---

## 🔒 Privacidad y Seguridad

- Tus datos personales, CVs generados, registros de postulaciones y datos de sueldo están preconfigurados en `.gitignore` para que **nunca se suban a un repositorio público**.
- El proyecto incluye un script de protección en `herramientas/guardas_seguridad.py` para prevenir fugas accidentales de información personal.

---

## 📄 Licencia

Distribuido bajo la Licencia MIT. Consulta [LICENSE](LICENSE) para más detalles.
