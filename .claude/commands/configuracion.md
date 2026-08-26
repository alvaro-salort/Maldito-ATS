# /configuracion - Asistente de Configuración de Perfil (Onboarding)

Este comando guía al usuario en la configuración inicial de su perfil profesional.

## Flujo de Configuración

El asistente ofrece 3 caminos de inicio:

### Camino A: Carga desde la carpeta `documentos/` (Recomendado)
1. Escanea las subcarpetas `documentos/cv/`, `documentos/linkedin/`, `documentos/titulos/`, `documentos/referencias/`.
2. Lee y extrae información sobre educación, experiencia, stack técnico y certificaciones.
3. Genera automáticamente `CLAUDE.md`, `01-perfil-candidato.md` y `cv/cv_maestro.md`.

### Camino B: Importación de un CV individual
1. El usuario pega o adjunta su CV actual.
2. El asistente extrae los datos y formula preguntas breves sobre expectativas salariales y modalidades de contratación deseadas.

### Camino C: Entrevista guiada paso a paso
1. El asistente hace preguntas estructuradas sección por sección:
   - Datos personales y ubicación.
   - Puestos deseados y nivel de seniority.
   - Modalidad de trabajo (Relación de Dependencia / Contractor USD / Monotributo).
   - Pretensión salarial en ARS y/o USD.
   - Historial de empresas y logros más relevantes.
   - Stack tecnológico y herramientas.
   - Idiomas y nivel de fluidez.
