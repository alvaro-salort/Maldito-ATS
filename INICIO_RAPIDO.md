# 🚀 Guía de Inicio Rápido: Maldito ATS

Esta guía te ayudará a poner en marcha **Maldito ATS** en cuestión de minutos utilizando tu entorno preferido (**OpenCode**, **Antigravity**, **Cursor**, **Claude Code** o mediante terminal).

---

## 1. Requisitos Previos

### Obligatorio
- **Python 3.10 o superior**: Para las herramientas de análisis salarial, validación de PDFs y seguridad.
- **Git**: Para clonar y versionar tu repositorio personal.

### Opcional (Recomendado)
- **Compilador de LaTeX** (para generar los PDFs finales de CV y carta):
  - **Windows**: Instala [MiKTeX](https://miktex.org/) o [TeX Live](https://tug.org/texlive/).
  - **Linux (Ubuntu/Debian)**: `sudo apt update && sudo apt install texlive-xetex texlive-luatex texlive-fonts-extra`
  - **macOS**: `brew install --cask mactex-no-gui`
  - *Nota*: Si no deseas instalar LaTeX localmente, puedes compilar los archivos `.tex` generados en [Overleaf](https://www.overleaf.com/) sin costo.
- **Bun / Node.js**: Si deseas ejecutar los scrapers CLI directos de búsqueda de empleo.

---

## 2. Instalación y Puesta en Marcha

1. **Clonar y entrar al directorio:**
   ```bash
   git clone https://github.com/tu-usuario/MalditoATS.git
   cd MalditoATS
   ```

2. **Crear entorno virtual de Python e instalar dependencias auxiliares:**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Linux / macOS:
   source venv/bin/activate

   pip install -r requirements.txt
   ```

---

## 3. Configuración de tu Perfil

Elige la forma más cómoda para cargar tus datos:

### Opción A: Carga automática desde documentos (Recomendado)
1. Coloca tu CV actual en `documentos/cv/` (en formato PDF o Word).
2. Si tienes certificados o cartas de recomendación, colócalos en `documentos/titulos/` y `documentos/referencias/`.
3. Inicia tu asistente (OpenCode / Antigravity / Cursor / Claude) y escribe:
   ```text
   /configuracion
   ```
4. El asistente leerá tus documentos y estructurará tu perfil en `CLAUDE.md` / `cv/cv_maestro.md`.

### Opción B: Entrevista guiada
Ejecuta `/configuracion` y el asistente te hará preguntas paso a paso sobre tu experiencia, tecnologías, pretensión salarial y expectativas laborales.

---

## 4. Flujo de Trabajo Habitual

### Buscar ofertas de empleo
Dile al asistente:
> *"Buscá ofertas de empleo de Backend Developer en Argentina y en remoto"*

### Postularte a una vacante específica
Pega el enlace o la descripción de la oferta y ejecuta:
```text
/postular https://www.linkedin.com/jobs/view/1112223344
```
El asistente:
1. Evaluará si cumples los requisitos clave.
2. Adaptará tu CV destacando logros con la fórmula XYZ.
3. Redactará una carta de presentación concisa y personalizada.
4. Te dará recomendaciones para la entrevista técnica.

### Optimizar tu LinkedIn
```text
/linkedin
```
Generará sugerencias de titulares con palabras clave y una biografía atractiva para reclutadores de LATAM.

### Redactar mensajes para Recruiters
```text
/mensajes
```
Te dará mensajes personalizados listos para copiar y pegar en LinkedIn o enviar por email.

### Comparar ofertas laborales
```text
/comparar-ofertas
```
Compara sueldos brutos/netos en pesos argentinos vs dólares contractor, prepagas, bonos y revisiones por inflación.
