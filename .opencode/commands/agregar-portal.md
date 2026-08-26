# /agregar-portal - Scaffolding para Nuevos Portales de Empleo

Permite agregar una nueva habilidad de búsqueda y scraping de un portal de empleo (ej. Workana, Torre, HiringCafe, WeWorkRemotely, bolsas de empleo universitarias) al directorio `.agents/skills/`.

---

## Parámetros
- `nombre`: Nombre corto del portal (ej. `workana`, `torre`, `empleos-uba`).
- `url`: URL base del portal de empleo.

---

## Pasos de Ejecución

### 1. Crear el Directorio de la Skill
Crear el directorio `.agents/skills/busqueda-<nombre>/`.

### 2. Generar el Archivo `SKILL.md`
Generar `.agents/skills/busqueda-<nombre>/SKILL.md` con:
- Frontmatter YAML:
  ```yaml
  ---
  name: busqueda-<nombre>
  description: >
    Búsqueda de ofertas de trabajo en <nombre> (<url>).
    Palabras clave: <nombre>, empleos <nombre>, vacantes.
  ---
  ```
- Documentación de parámetros de búsqueda (puesto, ubicación, modalidad).
- Formato de salida estandarizado (título, empresa, ubicación, modalidad, sueldo, enlace).

### 3. Actualizar Consultas de Búsqueda
Agregar ejemplos de búsqueda específicos en `.claude/skills/buscador-empleos/consultas-busqueda.md`.

### 4. Notificación
Informar al usuario que el portal fue configurado exitosamente y ya puede ser utilizado por el buscador de empleos.
