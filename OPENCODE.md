# Configuración y Guía de Uso para OpenCode

Bienvenido a **Maldito ATS** ejecutado con **OpenCode** (el asistente y runner de código abierto).

## 🚀 Cómo usar Maldito ATS en OpenCode

OpenCode interpreta automáticamente las instrucciones de este repositorio y permite ejecutar comandos y flujos mediante cualquier modelo LLM libre, económico o local (como **DeepSeek-V3 / R1**, **Gemini 2.5/3.0 Flash**, **Claude**, **GPT-4o** o modelos locales servidos vía **Ollama / vLLM**).

### Comandos Disponibles

Puedes escribir directamente en el chat de OpenCode cualquiera de estos comandos:

| Comando | Descripción |
|---|---|
| `/configuracion` | Asistente de onboarding: lee tus CVs/diplomas o te entrevista para crear tu perfil profesional. |
| `/postular` | Pega una oferta (URL o texto) para evaluar el fit, generar CV en LaTeX y carta de presentación. |
| `/evaluar` | Clasifica y puntúa las ofertas encontradas por los scrapers según tu compatibilidad. |
| `/entrevista` | Simula entrevistas técnicas y conductuales (STAR) con preguntas de negociación salarial. |
| `/linkedin` | Audita y optimiza tu titular y la sección *Acerca de* de tu perfil de LinkedIn. |
| `/mensajes` | Genera mensajes de contacto directo (*cold outreach*) y emails de seguimiento a recruiters. |
| `/comparar-ofertas` | Compara ofertas laborales bimonetarias (ARS vs USD, bonos, prepaga, paritarias, vacaciones). |
| `/resultado` | Registra el estado de tus postulaciones (enviado, entrevista, oferta, rechazo) en CSV. |
| `/reporte` | Genera un reporte visual en HTML con el progreso y métricas de tu búsqueda. |

---

## 🛠 Requisitos de Entorno

1. **Python 3.10+**: Para las herramientas de salarios, validación de PDFs y seguridad.
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Compilador de LaTeX (Opcional pero recomendado para PDFs)**:
   - En Windows: [MiKTeX](https://miktex.org/) o [TeX Live](https://tug.org/texlive/).
   - En Linux: `sudo apt install texlive-xetex texlive-luatex texlive-fonts-extra`
   - Si no tienes LaTeX instalado, el asistente generará el código `.tex` o `.md` que puedes compilar en [Overleaf](https://www.overleaf.com/) gratuitamente.
3. **Bun / Node.js (Opcional para scrapers CLI)**:
   - Para ejecutar los scrapers CLI de portales de empleo. Si no está instalado, el asistente utilizará automáticamente búsqueda web alternativa.
